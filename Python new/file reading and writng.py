fw=open('sample.txt','w')
fw.write('Hi Rohan')
fw.write('Rohan is the best')
fw.close()
fr=open('sample.txt','r')
text=fr.read()
print(text)
fr.close()
