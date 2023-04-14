from playwright.sync_api import Page, sync_playwright


class PlaywrightWrapper:
    def __init__(self) -> None:
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.webkit.launch(headless=False)
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

    data_json = '{"v":5,"in":[{"pos":[100,55],"id":0}],"out":[{"pos":[300,110],"id":1}],"gates":[{"type":"NOT","pos":[200,85],"in":2,"out":3}],"wires":[[0,2],[3,1]]}'

    conversion_function = "toPNG"
    # conversion_function = "toSVG"

    result = page.evaluate(
        f"""async () => {{
        try {{
            const editor = window.Logic.singleton
            if (typeof editor === 'undefined') {{
                return "error: no editor"
            }}

            const dataJson = JSON.stringify({data_json})
            editor.loadCircuit(dataJson)
            editor.setModeFromString("tryout")
            const withMetadata = false
            const heightHint = undefined
            const blob = await editor.{conversion_function}(withMetadata, heightHint)
            const asBase64 = await editor.toBase64(blob)
            return asBase64
        }} catch (e) {{
            return "error: " + e
        }}
    }}"""
    )

    print(result)

    page.close()
    browser.close()


run()
