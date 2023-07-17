import sys
import os
# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPDF

if sys.platform != 'darwin':
    import cairosvg 



from PIL import Image

def svg2pdf(svg_file, pdf_file):
    #drawing = svg2rlg(svg_file)
    #renderPDF.drawToFile(drawing, pdf_file)
    ## version 3
    if sys.platform == 'darwin':
        os.system('/Applications/Inkscape.app/Contents/MacOS/inkscape ' +svg_file + ' --export-area-drawing --export-filename ' + pdf_file)
    elif sys.platform == 'linux':
        os.system('inkscape ' +svg_file + ' --export-area-drawing --export-filename ' + pdf_file)
    else:
        cairosvg.svg2pdf(url=svg_file,write_to=pdf_file) ## not tested  

def gif2pdf(gif_file, pdf_file):
    img = Image.open(gif_file)
    img.save(pdf_file, "PDF", resolution=100.0)

def webp2pdf(webp_file, pdf_file):
    img = Image.open(webp_file)
    img.save(pdf_file, "PDF", resolution=100.0)

def convert_images_to_pdfs(app):
    import os

    # Check if building LaTeX
    if app.builder.format != 'latex':
        return

    # Get the path to the build directory
    build_dir = app.outdir

    # Conversion functions
    conversions = {
        '.svg': svg2pdf,
        '.gif': gif2pdf,
        '.webp': webp2pdf,
    }

    # Walk the source directory

    for root, dirs, files in os.walk(app.srcdir):
        for file in files:
            file_ext = os.path.splitext(file)[1]

            if file_ext not in conversions.keys():
                continue
            
            src_path = os.path.join(root, file)
            pdf_path = os.path.join(build_dir, file[:-len(file_ext)] + '.pdf')

             # Check if the pdf exists and is newer than the source file
            if os.path.exists(pdf_path):
                if os.path.getmtime(pdf_path) > os.path.getmtime(src_path):
                    continue
            
            # Convert the image
            conversions[file_ext](src_path, pdf_path)

def setup(app):
    app.connect('builder-inited', convert_images_to_pdfs)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
