import json
from pprint import pprint
from time import sleep

from playwright.sync_api import Page, sync_playwright


class PlaywrightWrapper:
    def __init__(self) -> None:
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.context = self.browser.new_context()

    def close(self) -> None:
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    def new_page(self) -> Page:
        return self.context.new_page()


def run() -> None:
    browser = PlaywrightWrapper()
    page = browser.new_page()
    page.goto("https://logic.modulo-info.ch")

    data_json = """{ // JSON5
  v: 6,
  components: {
    in0: {type: 'in', pos: [100, 55], id: 0},
    out0: {type: 'out', pos: [300, 310], id: 1},
    not0: {type: 'not', pos: [200, 85], in: 2, out: 3},
  },
  wires: [[0, 2], [3, 1]]
}
"""

    # conversion_function, mime_type = "toPNG", "image/png"
    conversion_function, mime_type = "toSVG", "image/svg+xml"

    resultJSON = page.evaluate(
        f"""async () => {{
        try {{
            const editor = window.Logic.singleton
            if (typeof editor === 'undefined') {{
                return "error: no editor"
            }}

            const dataJson = JSON.stringify({data_json})
            editor.loadCircuitOrLibrary(dataJson)
            editor.setModeFromString("tryout")
            const withMetadata = false
            const heightHint = undefined
            const blob = await editor.{conversion_function}(withMetadata, heightHint)
            const imgData = await editor.toBase64(blob)
            const size = editor.guessAdequateCanvasSize()
            return JSON.stringify({{ imgData, size }})
        }} catch (e) {{
            return "error: " + e
        }}
    }}"""
    )

    result = json.loads(resultJSON)

    pprint(result)

    width, height = result["size"]
    img_data = result["imgData"]

    print(f"{img_data=}")
    print(f"{width=}, {height=}")

    page.set_content(
        f"""<html>
        <head>
            <style>
                @page {{
                    size: {width}px {height}px;
                    margin: {0}px;
                }}

                html, body {{
                    width: {width}px;
                    margin: 0;
                    background-color: transparent;
                }}

                img {{
                    background-color: transparent;
                }}
            </style>
        </head
        <body>
            <img style="width: 100%;" src="data:{mime_type};base64,{img_data}">
        </body>
    </html>"""
    )

    page.pdf(
        path="document.pdf",
        page_ranges="1",
        display_header_footer=False,
        margin=dict(top="0", left="0", right="0", bottom="0"),
        prefer_css_page_size=True,
        print_background=False,
    )

    page.close()
    browser.close()


run()
