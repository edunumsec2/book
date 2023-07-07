.ONESHELL:

WEB_CHAPTERS = rep-info archi algo1 prog1 resx algo2 prog2 projets hist

PRINT_CHAPTERS = rep-info archi algo1 resx algo2

WEB_BUILD_DIR = build/appr/

LATEX_BUILD_DIR = build/latex/appr

MD_SOURCE_DIR = src/appr

EXT_DIR = src/exts

LATEX_FORMAT_DIR = src/static/latex

# all: web print
# 	mkdir -p build/appr/media && cp build/latex/appr/rep_info.pdf build/appr/media/rep-info.pdf && cp build/latex/appr/archi.pdf build/appr/media/archi.pdf

# ext: $(wildcard $(EXT_DIR)*.py):
# 	echo "$^"

sources: $(addsuffix /*.md, $(addprefix $(MD_SOURCE_DIR)/, $(CHAPTERS)))

scripts:  $(MD_SOURCE_DIR)/conf.py

latex: $(LATEX_FORMAT_DIR)/*.tex

web: sources scripts
	sphinx-build -aE -b html $(MD_SOURCE_DIR) $(WEB_BUILD_DIR)

print: sources scripts latex
	sphinx-build -aE -t latex_mode -b latex $(MD_SOURCE_DIR) $(LATEX_BUILD_DIR)
	cd $(LATEX_BUILD_DIR) && make && mv $(LATEX_BUILD_DIR)/modulo.pdf .

%.pdf: sources scripts latex
	sphinx-build -aE -t latex_mode -t $* -b latex $(MD_SOURCE_DIR) $(LATEX_BUILD_DIR)
	cd $(LATEX_BUILD_DIR) && rm -f $@ && make
	mv $(LATEX_BUILD_DIR)/$@ .

all: web print $(addsuffix .pdf, $(PRINT_CHAPTERS))

clean:
	rm -rf $(LATEX_BUILD_DIR)/* $(WEB_BUILD_DIR)*
# archi:
# 	sphinx-build  -E -b latex -t archi src/appr  build/latex/appr && \
# 	cd build/latex/appr && pdflatex archi.tex

# rep_info:
# 	sphinx-build  -E -b latex -t rep_info src/appr  build/latex/appr && \
# 	cd build/latex/appr && pdflatex rep_info.tex

# pdf:
# 	sphinx-build  -E -b latex  src/appr  build/latex/appr && \
# 	cd build/latex/appr && pdflatex modulo2.tex

# html:
# 	sphinx-build  -E -b html src/appr  build/appr
