.PHONY: build-monolingual extract-corpus

SUBDIRS = $(find . -type d -name "*-cat*")

extract-corpus:
	find . -type f -name "*.xz" -execdir xz -k -f -d {} \;

build-monolingual: extract-corpus
	python3 data-processing-tools/monolingual-dataset.py


 
