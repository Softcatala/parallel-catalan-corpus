europarl() {

	cd raw
	wget -O europarl-en-pt.xml.gz  https://opus.nlpl.eu/download.php?f=Europarl/v8/tmx/en-pt.tmx.gz
	gzip -d europarl-en-pt.xml.gz
	tmx-to-text convert -f europarl-en-pt.xml -s en -t pt
	mv en-pt.en europarl-en-pt.en
	mv en-pt.pt europarl-en-pt.pt
	python3 ../../data-processing-tools/three-way-text-to-text.py -1 europarl-en-pt.en -2 europarl-en-pt.pt -3 ../../eng-cat/europarl.en-ca.en  -4 ../../eng-cat/europarl.en-ca.ca
	mv src.txt ../europarl.pt-ca.pt
	mv tgt.txt ../europarl.pt-ca.ca
	cd ..
	xz -9 -k europarl.pt-ca.pt
	xz -9 -k europarl.pt-ca.ca
}

wikimatrix() {
	cd raw
	wget -O ca-pt.tmx.gz  https://object.pouta.csc.fi/OPUS-WikiMatrix/v1/tmx/ca-pt.tmx.gz
	gzip -d ca-pt.tmx.gz 
	tmx-to-text convert -f ca-pt.tmx -s pt -t ca
	mv pt-ca.pt ../wikimatrix-pt-ca.pt
	mv pt-ca.ca ../wikimatrix-pt-ca.ca
    rm ca-pt.tmx
	cd ..
}

rm -r -f raw 
mkdir raw

europarl
wikimatrix

