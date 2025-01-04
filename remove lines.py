file1=open('text1.txt','r')
file2=open('text2.txt','w')

for i in file1.readlines():
    if i.startswith('hi'):
     print (i) 
     file2.write(i)
file1.close()
file2.close()
