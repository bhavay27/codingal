# opening the text file 
file1=open('bhavay.txt','r')
#initialiseing counter variable 
counter=0
# reading file 1 and storing in file2
file2=file1.read()
# spliting the file content into the list 
content=file2.split('\n')
# accessing the elements of list 
for file3 in content :
    # checking if list element is not empty
    if file3 :
        # increment counter variable when non empty list element is found.
        counter+=1 
print("no. of lines=",counter)
