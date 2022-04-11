import sys

a= sys.argv[1]
b= sys.argv[2]

file = open(a,'r')
content = file.read()
#file.write(content)
#lines = file.readlines()

content1 = content.replace("?","")
content2 = content1.replace("!","")
content3 = content2.replace(".","")

content4=content3.split()
print(content4)

counts = dict()
content4=content3.split()
for word in content4:
	counts[word] = counts.get(word,0)+1

bigcount = None
bigword = None
for word, count in counts.items():
	if bigcount is None or count>bigcount:
		bigword = word
		bigcount = count
print(bigword, bigcount)
file.close() 
