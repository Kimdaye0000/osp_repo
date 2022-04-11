import sys

a= sys.argv[1]
b= sys.argv[2]
#print(sys.argv[0])
#print(a)
#print(int(b))

file = open(a,'r')
#content = '\nmy name is abc!'
content = file.read()
#file.write(content)
#lines = file.readlines()

content1 = content.replace("?","")
content2 = content1.replace("!","")
content3 = content2.replace(".","")

keys = []
values = []

#content4=content3.split()
#print(content1)
#print(content2)
#print(content3)
#print(content4)

for i in range(1,b):
	content4=data.split()
	keys.append(content4[i])
	values.append(content4[i])

print(keys)
print(values)

file.close() 
