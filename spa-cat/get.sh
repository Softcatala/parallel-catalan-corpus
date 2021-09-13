dogc() {
    cd raw
    wget -O dogc-ca-es.tmx.gz https://object.pouta.csc.fi/OPUS-DOGC/v2/tmx/ca-es.tmx.gz
    gzip -d dogc-ca-es.tmx.gz
    tmx-to-text convert -f dogc-ca-es.tmx -s es -t ca

    mv es-ca.es dogc-es-ca.es
    mv es-ca.ca dogc-es-ca.ca
    cd ..

    python3 ../data-processing-tools/clean-dogc.py
    xz -9 -k dogc-es-ca.es
    xz -9 -k dogc-es-ca.ca
}

europarl() {
    cd raw
    wget -O europarl-en-es.tmx.gz https://opus.nlpl.eu/download.php?f=Europarl/v8/tmx/en-es.tmx.gz
    gzip -d europarl-en-es.tmx.gz
    tmx-to-text convert -f europarl-en-es.tmx -s en -t es
    mv en-es.en europarl-en-es.en
    mv en-es.es europarl-en-es.es
    python3 ../../data-processing-tools/three-way-text-to-text.py -1 europarl-en-es.en -2 europarl-en-es.es -3 ../../eng-cat/europarl.en-ca.en  -4 ../../eng-cat/europarl.en-ca.ca
    mv src.txt ../europarl.es-ca.es
    mv tgt.txt ../europarl.es-ca.ca
    cd ..
    xz -9 -k europarl.es-ca.es
    xz -9 -k europarl.es-ca.ca
}

rm -r -f raw
mkdir raw
dogc
europarl
