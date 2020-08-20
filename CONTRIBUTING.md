
# Introducció

Objectiu: generar corpus paral·lels anglès-català, amb llicència lliure (o tan lliure com sigui possible). 

Projecte actual: https://github.com/Softcatala/en-ca-corpus 

# Llicències

Un dels objectius és que els corpus siguin lliures per realment fer un salt endavant en tecnologies de la llengua. Considerem els següents requisits mínims:

* Que es pugui redistribuir sense massa restriccions
* Que es pugui modificar, i es pugui distribuir modificat (ens cal aplicar transformacions com ara neteges)
* Que es pugui usar en ús comercial

No considerem clau:
* Que es pugui combinar amb altres textos (compatibilitat de llicències)
* Que obligui a publicar les millores

Considerem acceptables:

- Totes les llicències considerades lliures per l'[Open Source Iniciative](https://opensource.org/licenses) o la [Free Software Foundation](https://www.gnu.org/licenses/licenses.en.html)
- Totes les llicències [Creative Commons](https://creativecommons.org/) que no restringeixin o limitin l'ús comercial (CC-0, CC-BY, CC-BY-SA)

# Millorar la qualitat dels corpus Wikimatrix i Europarl

Trobar o generar corpus d'aquest volum (un o dos milions de frases) i amb llicència lliure és molt complicat. Una de les tasques que es podria emprendre és millorar la qualitat d'aquests corpus. 
Possibles maneres:
* Descartar frases amb LanguageTool, de la mateixa manera que s'ha fet amb els texts de Common Voice. Es poden ajustar diferents paràmetres per a trobar el resultat desitjat. 
* En Wikimatrix s'utilitza la detecció d'idioma (cld2 o cld3). En Europarl això no cal. 

Un projecte relacionat és millorar l'Europarl eng-cat fins al punt de considerar-lo de prou qualitat per a consulta. Això es faria combinant la millora de la traducció spa-cat amb Apertium i postedició amb l'ajuda de LanguageTool. És un projecte que requeriria finançament, però seria molt més barat que una revisió només humana, que seria caríssima. Es millorarien diferents coses al mateix temps: Apertium, LanguageTool i el corpus en si. Considero que val molt la pena. Hauríem d'estar atents a oportunitats de trobar finançament. 

# Fer scraping de pàgines web amb traduccions ben estructurades i llicències lliures

He fet la prova amb la web de jw.org + scrapy (i abans amb TedTalks i Globalvoices). L'alineament es fa després amb youalign.com. Funciona molt bé. Però en jw.org, sense entrar en documents PDF i EPUB, hi ha menys volum del que em pensava en català (unes 45.000 paraules).

És una de les millors fórmules. Cal buscar webs que tinguin aquestes característiques. 

Per exemple: https://traduccionsinedites.wordpress.com/materials/ (Subtitulacions de documentals)
Web d'estudis de la Caixa: https://observatoriosociallacaixa.org/ca/ (Molta informació, i ben estructurada per llengües, una part és en PDF)

El volum en aquestes fonts és modest. Però es tracta d'anar sumant...

# Dades de webs no tan estructurades: Gencat / Bitextor

L'eina per a generar el corpus podria ser Bitextor. Un exemple d'aquestes webs: 
gencat.cat
No sabem realment quantes dades es podrien extraure. Podria ser que fos possible (i més fàcil) extraure dades de manera estructurada. Valdria la pena provar-ho 
https://www.barcelona.cat/ 
no totes les pàgines tenen traduccions
http://www.gnu.org
https://www.fsf.org/ 


Paracrawl ha estat finançat amb diners de la UE, i pensem que l'hauríem de poder fer servir. S'ha d'investigar/consultar amb la gent involucrada al projecte. A més, hauríem de poder contribuir-hi.

# Traducció inversa (back translation)

El procediment és el següent: 
Usar text original en català, de bona qualitat lingüística. Traduir-lo a l'anglès amb Apertium (o el que sigui: ¿Google, pagant?). La traducció en anglès serà de baixa qualitat. El corpus paral·lel eng-cat pot servir per a alimentar la traducció anglès>català (però no la traducció català>anglès). 

Es pot fer el mateix en el sentit invers per al català>anglès. 

El resultat serà llengua de qualitat, però la correspondència amb l'original és més dubtosa. 

El preu de traducció en Google Translate és de 20 $ / milió de caràcters. Traduir un volum com el de l'Europarl constaria uns 640 $. 

# Llibres

N'hi ha pocs amb llicència lliure. I molts llibres en català amb llicència lliure són en llengua antiga, per la normativa o per l'estil. (Antoni Oliver explica que ells ho han fet amb materials del projecte Gutenberg, amb les limitacions esmentades.)

Viquitexts té 25872 pàgines revisades (800 obres), algunes de les quals trobaríem també traduïts a l'anglès (en.wikisource.org). Les obres de Plató són correctes: https://ca.wikisource.org/wiki/Autor:Plat%C3%B3
https://ca.wikisource.org/wiki/P%C3%A0gina_principal
(Les traduccions de Joan Crexells sembla que serien de domini públic. Les de Carles Riba no, p. ex. Els deu mil, en el projecte Gutenberg.)

Segons Wikidata https://w.wiki/Nzi , els autors que passen a domini públic els pròxims 10 anys són Prudenci Bertrana (1941), Josep M. Folch i Torres (1945) i Pompeu Fabra (1948).

Idea: parlar amb editorials per a col·laborar en l'explotació de les traduccions que siguin de domini públic.

El procés de selecció i d'alineament pot ser laboriós.

Exemple català/anglès a wikisource (edicions diferents, articles no relacionats):
https://en.wikisource.org/wiki/Apology_(Plato)
https://ca.wikisource.org/wiki/Di%C3%A0legs_I_-_Defensa_de_S%C3%B2crates

En aquest cas, en anglès es podria trobar moltes traduccions de qualitat (es podria afegir diverses vegades):
http://socrates.clarke.edu/aplg0100.htm
https://www.bartleby.com/2/1/1.html
http://www.san.beck.org/Apology.html
http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0170%3Atext%3DApol.
etc.

Alguns autors podrien proporcionar alguns llibres. El corpus alineat podria estar desordenat (que no reprodueixi el llibre original de manera lineal). Si són pocs autors, no seria un volum gaire gran. 

Cada any es publiquen molts llibres en català (originals i traduccions). Podríem parlar amb el gremi d'editors, escriptors i traductors. Els autors podrien cedir un percentatge petit (1% o 5%) del seu material (desordenat?). No hauria de perjudicar el seu model de negoci. Això pot no ser viable per les traduccions (on també necessitaríem permís de l'original)

El volum de dades que caldria s'aniria obtenint a poc a poc. 

# Acords amb institucions

Es podria parlar amb diferents institucions perquè cedissin part de les seves dades amb llicències lliures. 

Exemples:
- Publicacions de la Generalitat de Catalunya (p. ex. publicacions en obert http://www.gencat.cat/drep/iea/pdfs/CF_Federalista.pdf)
- Guies de conversa universitària: http://www.ub.edu/guiaconversa/index.php [Però no és gaire. El traductor actual ja tradueix prou bé la majoria d'aquestes frases.]
- Subtítols de TV3...?

# Possibles tasques concretes

* Crear un corpus paral·lel de barcelona.cat. De manera semiautomàtica (amb una mica de supervisió manual) es podrien extraure moltes dades. 
    * Com: caldria preparar un crawler, usar eina d'alineació, i revisar manualment el resultat final.
* Crear un corpus paral·lel a partir de Viquitexts. Caldria seleccionar bé les obres per la qualitat dels textos
    * Com: baixar des de https://ca.wikisource.org les fonts, usar un OCR per convertir-ho a text, esmenar les errades de conversió, usar eina d'alineació, i revisar manualment el resultat final.
