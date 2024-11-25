def function (lst):
    result = {}
    for item in lst:
        result[item[0]]= item[1:]
    return result
list1=[[1,"bhavay","18"],[2,"aditya",17]]
print("\n",list1)
print(function(list1))
