import sys

a= sys.argv[1]
b= sys.argv[2]
print(sys.argv[0])
print(a)
print(int(b))

file = open(a,'r')
#content = '\nmy name is abc!'
content = file.read()
#file.write(content)
#lines = file.readlines()
print(content)
file.close() 
