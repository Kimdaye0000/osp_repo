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

content4=content3.split()
#print(content1)
#print(content2)
#print(content3)
print(content4)
file.close() 
