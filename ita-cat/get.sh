

europarl() {

	# Europarl
	cd raw
	wget -O europarl-en-it.xml.gz  https://opus.nlpl.eu/download.php?f=Europarl/v8/tmx/en-it.tmx.gz
	gzip -d europarl-en-it.xml.gz
	tmx-to-text convert -f europarl-en-it.xml -s en -t it
	mv en-it.en europarl-en-it.en
	mv en-it.it europarl-en-it.it
	python3 ../../data-processing-tools/three-way-text-to-text.py -1 europarl-en-it.en -2 europarl-en-it.it -3 ../../eng-cat/europarl.en-ca.en  -4 ../../eng-cat/europarl.en-ca.ca
	mv src.txt ../europarl.it-ca.it
	mv tgt.txt ../europarl.it-ca.ca
	cd ..
	xz -9 -k europarl.it-ca.it
	xz -9 -k europarl.it-ca.ca
}

wikimatrix() {
	cd raw
	wget -O ca-it.tmx.gz  https://object.pouta.csc.fi/OPUS-WikiMatrix/v1/tmx/ca-it.tmx.gz
	gzip -d ca-it.tmx.gz 
	tmx-to-text convert -f ca-it.tmx -s it -t ca
	mv it-ca.it ../wikimatrix-it-ca.it
	mv it-ca.ca ../wikimatrix-it-ca.ca
    rm ca-it.tmx
	cd ..
}

ccmatrix() {
	cd raw
	wget -O ca-it.tmx.gz https://object.pouta.csc.fi/OPUS-CCMatrix/v1/tmx/ca-it.tmx.gz
	gzip -d ca-it.tmx.gz
	tmx-to-text convert -f ca-it.tmx -s it -t ca
	mv it-ca.it ../ccmatrix-it-ca.it
	mv it-ca.ca ../ccmatrix-it-ca.ca
	cd ..
}

rm -r -f raw 
mkdir raw

europarl
wikimatrix
ccmatrix

