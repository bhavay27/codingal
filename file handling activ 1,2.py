file1=open('bhavay.txt', 'r')
print(file1.read())
file1.close()

file2=open('bhavay.txt', 'w')
file2.write("hi my name is bhavay dhawan. ")
file2.close()

file3=open('bhavay.txt', 'a')
file3.write("my age is 18 yrs. ")
file3.close()

file5=open('bhavay.txt', 'r')
print("content of file after appending.")
print(file5.read())
file5.close()
