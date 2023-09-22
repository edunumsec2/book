.ONESHELL:

WEB_CHAPTERS = rep-info archi algo1 prog1 resx algo2 prog2 projets hist

PRINT_CHAPTERS = rep-info archi algo1 resx algo2

WEB_BUILD_DIR = build/appr

LATEX_BUILD_DIR = build/latex/appr

PDF_BUILD_DIR = build/pdf

MD_SOURCE_DIR = src/appr

EXT_DIR = src/exts

LATEX_FORMAT_DIR = src/static/latex

SOURCES = $(addsuffix /*.md, $(addprefix $(MD_SOURCE_DIR)/, $(CHAPTERS)))

SCRIPTS =  $(MD_SOURCE_DIR)/conf.py

LATEX_FORMAT = $(LATEX_FORMAT_DIR)/*.tex


# all: web print
# 	mkdir -p build/appr/media && cp build/latex/appr/rep_info.pdf build/appr/media/rep-info.pdf && cp build/latex/appr/archi.pdf build/appr/media/archi.pdf

# ext: $(wildcard $(EXT_DIR)*.py):
# 	echo "$^"

.PHONY: $(addsuffix .pdf, $(PRINT_CHAPTERS)) modulo.pdf web print sources latex scripts


sources: $(addsuffix /*.md, $(addprefix $(MD_SOURCE_DIR)/, $(CHAPTERS)))

scripts:  $(MD_SOURCE_DIR)/conf.py

latex: $(LATEX_FORMAT_DIR)/*.tex

web: sources scripts
	sphinx-build -aE -b html $(MD_SOURCE_DIR) $(WEB_BUILD_DIR)

print: sources scripts latex
	python -m playwright install chromium
	sphinx-build -aE -t latex_mode -b latex $(MD_SOURCE_DIR) $(LATEX_BUILD_DIR)
	cd $(LATEX_BUILD_DIR) && make

modulo.pdf: print
	cp $(LATEX_BUILD_DIR)/modulo.pdf $(PDF_BUILD_DIR)/

$(PDF_BUILD_DIR)/%.pdf:  $(MD_SOURCE_DIR)/$*/*.md scripts latex
	mkdir -p $(PDF_BUILD_DIR)
	python -m playwright install chromium
	sphinx-build -aE -t latex_mode -t $* -b latex $(MD_SOURCE_DIR) $(LATEX_BUILD_DIR)
	make -C $(LATEX_BUILD_DIR)
	mv $(LATEX_BUILD_DIR)/$*.pdf $(PDF_BUILD_DIR)/

%.pdf: 	$(PDF_BUILD_DIR)/%.pdf
	echo $@ is in $(PDF_BUILD_DIR) 

all: web modulo.pdf $(addsuffix .pdf, $(PRINT_CHAPTERS))
	mkdir -p  $(WEB_BUILD_DIR)/media && cp $(PDF_BUILD_DIR)/*.pdf $(WEB_BUILD_DIR)/media/

clean:
	rm -rf $(LATEX_BUILD_DIR)/* $(WEB_BUILD_DIR)/* $(PDF_BUILD_DIR)/*

