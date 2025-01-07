with open ("bhavay1.txt",'w') as f:
    f.write("hello ")
f.close()

with open ("text.txt",'r')as f:
    data=f.readlines()
    for i in data :
        word=i.split()
        print(word)
f.close()
    
