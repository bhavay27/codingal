file=open('text.txt' ,'r')
print(file.read(5))
print(file.readline())
print(file.readline()) 
file.seek(0)
print(file.readlines()[2])