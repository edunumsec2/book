from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PIL import Image

def convert_images_to_pdfs(app):
    import os

    # Check if building LaTeX
    if app.builder.format != 'latex':
        return

    # Get the path to the build directory
    build_dir = app.outdir

    for root, dirs, files in os.walk(app.srcdir):
        for file in files:
            exts = ['.svg', '.gif', '.webp']

            file_ext = os.path.splitext(file)[1]

            if file_ext not in exts:
                continue
            
            print(file_ext)

            src_path = os.path.join(root, file)
            pdf_path = os.path.join(build_dir, file[:-len(file_ext)] + '.pdf')

            print(pdf_path)

             # Check if pdf exists and is newer than svg
            if os.path.exists(pdf_path):
                if os.path.getmtime(pdf_path) > os.path.getmtime(src_path):
                    continue

            if file_ext == ".svg":
                # Convert svg to pdf
                drawing = svg2rlg(src_path)
                renderPDF.drawToFile(drawing, pdf_path)

            elif file_ext == ".gif":                
                # Convert gif to pdf
                img = Image.open(src_path)
                img.save(pdf_path, "PDF", resolution=100.0)

def setup(app):
    app.connect('builder-inited', convert_images_to_pdfs)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }