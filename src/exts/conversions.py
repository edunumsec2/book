from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

def convert_svgs_to_pdfs(app):
    import os

    # Check if building LaTeX
    if app.builder.format != 'latex':
        return

    # Get the path to the build directory
    build_dir = app.outdir

    for root, dirs, files in os.walk(app.srcdir):
        for file in files:
            if file.endswith('.svg'):
                svg_path = os.path.join(root, file)
                pdf_path = os.path.join(build_dir, file[:-4] + '.pdf')

                # Check if pdf exists and is newer than svg
                if os.path.exists(pdf_path):
                    if os.path.getmtime(pdf_path) > os.path.getmtime(svg_path):
                        continue
                
                # Convert svg to pdf
                drawing = svg2rlg(svg_path)
                renderPDF.drawToFile(drawing, pdf_path)

def setup(app):
    app.connect('builder-inited', convert_svgs_to_pdfs)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }