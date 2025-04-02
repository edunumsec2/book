.ONESHELL:

WEB_CHAPTERS = rep-info archi algo1 prog1 resx algo2 prog2 projets hist

PRINT_CHAPTERS = rep-info archi algo1 resx algo2

BUILD_DIR = build

HELPER_DIR = deployment

ADDITIONAL_FILES_DIR = $(HELPER_DIR)/additionalfiles

WEB_BUILD_DIR = $(BUILD_DIR)/appr

LATEX_BUILD_DIR = $(BUILD_DIR)/latex/appr

PDF_BUILD_DIR = $(BUILD_DIR)/pdf

MD_SOURCE_DIR = src/appr

EXT_DIR = src/exts

LATEX_FORMAT_DIR = src/static/latex

SOURCES = $(addsuffix /*.md, $(addprefix $(MD_SOURCE_DIR)/, $(CHAPTERS)))

SCRIPTS =  $(MD_SOURCE_DIR)/conf.py

LATEX_FORMAT = $(LATEX_FORMAT_DIR)/*.tex

SERVER = 31826.ftp.infomaniak.com

SSH_USER = 31826_hep



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
	mkdir -p $(PDF_BUILD_DIR)
	cp $(LATEX_BUILD_DIR)/modulo.pdf $(PDF_BUILD_DIR)/

$(PDF_BUILD_DIR)/%.pdf:  $(MD_SOURCE_DIR)/$*/*.md scripts latex
	mkdir -p $(PDF_BUILD_DIR)
	python -m playwright install chromium
	sphinx-build -aE -t latex_mode -t $* -b latex $(MD_SOURCE_DIR) $(LATEX_BUILD_DIR)
	make -C $(LATEX_BUILD_DIR) $*.pdf
	mv $(LATEX_BUILD_DIR)/$*.pdf $(PDF_BUILD_DIR)/

%.pdf: 	$(PDF_BUILD_DIR)/%.pdf
	echo $@ is in $(PDF_BUILD_DIR) 

pdf: $(addprefix $(PDF_BUILD_DIR)/, $(addsuffix .pdf, $(PRINT_CHAPTERS))) modulo.pdf
	mkdir -p  $(WEB_BUILD_DIR)/media && cp $(PDF_BUILD_DIR)/*.pdf $(WEB_BUILD_DIR)/media/

all: web pdf

clean:
	rm -rf $(LATEX_BUILD_DIR)/* $(PDF_BUILD_DIR)/* $(WEB_BUILD_DIR)/* $(BUILD_DIR)/ens/* 

upload:
	rsync -avz --progress --delete $(WEB_BUILD_DIR)/             $(SSH_USER)@$(SERVER):sites/apprendre.modulo-info.ch/
	rsync -avz --progress          $(ADDITIONAL_FILES_DIR)/appr/ $(SSH_USER)@$(SERVER):sites/apprendre.modulo-info.ch/

