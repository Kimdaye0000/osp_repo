import sys

a= sys.argv[1]
b= sys.argv[2]

file = open(a,'r')
content = file.read()

content1 = content.replace("?","")
content2 = content1.replace("!","")
content3 = content2.replace(".","")

content4=content3.split()

counts = dict()
for name in content4:
	if name not in counts:
		counts[name] = 1
	else:
		counts[name] += 1
pgm_lang_val_reverse = sorted(counts.items(),reverse=True, key=lambda item: item[1]) 

for key, value in pgm_lang_val_reverse[:int(b)]:
	print("{0:10}".format(key), value)
file.close() 
