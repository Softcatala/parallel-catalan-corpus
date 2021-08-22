b = "en-ca.ca"	#File in language B
pivotb = "en-ca.en"	#Pivot file for language B
a = "en-de.de"	#File in language A
pivota = "en-de.en"	#Pivot file for language A

def ReadFile(file):
	print("Reading file ", file)
	readt = open(file,'r', encoding="utf-8")
	text = readt.read().splitlines()
	print("Successfully read file ", file)
	return text
    
texta = ReadFile(a)
textpivota = ReadFile(pivota)
textpivotb = ReadFile(pivotb)
textb = ReadFile(b)

def SearchLine(line):
	idl = -1
	for i in range(0,len(textpivota),1):

		if line == textpivota[i]:
			idl = i
			
			break
		
	return idl
newA = []
newB = []

print("Searching for identical segments")
   
for i in range (0,len(textpivotb),1):
	idl = SearchLine(textpivotb[i])
	if (i + 1) % 10 == 0:
		print(i+1)
	if idl != -1:
		newA.append(texta[idl])
		newB.append(textb[i])
print("Search ended")
 

print("Writing results")
writeA = open("langA.txt","a",encoding="utf-8")
writeB = open("langB.txt","a",encoding="utf-8")

for i in range (0,len(newA),1):
	writeA.write(newA[i])
	writeA.write("\n")
	writeB.write(newB[i])
	writeB.write("\n")
    
print("Process ended")
