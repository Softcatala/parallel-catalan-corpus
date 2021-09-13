

europarl() {

	cd raw
	wget -O europarl.en-fr.xml.gz  https://opus.nlpl.eu/download.php?f=Europarl/v8/tmx/en-fr.tmx.gz
	gzip -d europarl.en-fr.xml.gz
	python3 ../../data-processing-tools/tmx-to-text.py -f europarl.en-fr.xml -s en -t fr -p europarl
	python3 ../../data-processing-tools/three-way-text-to-text.py -1 europarl.en-fr.en -2 europarl.en-fr.fr -3 ../../eng-cat/europarl.en-ca.en  -4 ../../eng-cat/europarl.en-ca.ca
	mv src.txt ../europarl.fr-ca.fr
	mv tgt.txt ../europarl.fr-ca.ca
	cd ..
	xz -9 -k europarl.fr-ca.fr
	xz -9 -k europarl.fr-ca.ca
}

wikimatrix() {
	cd raw
	wget -O ca-fr.tmx.gz  https://object.pouta.csc.fi/OPUS-WikiMatrix/v1/tmx/ca-fr.tmx.gz
	gzip -d ca-fr.tmx.gz 
	python3 ../../data-processing-tools/tmx-to-text.py -f ca-fr.tmx -s fr -t ca -p wikimatrix
	mv wikimatrix.fr-ca.fr ../
	mv wikimatrix.fr-ca.ca ../
	cd ..
	xz -9 -k wikimatrix.fr-ca.fr
	xz -9 -k wikimatrix.fr-ca.ca
}

rm -r -f raw 
mkdir raw

#europarl
#wikimatrix

