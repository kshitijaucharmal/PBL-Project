def split_and_join(line):
    a = ("this is a string")
    a = a.split(" ")
    
    a = "-".join(a)
    print(a)
split_and_join(line=" ")

l1 = [2,2,2,3]
for x in l1:
    if l1.count(x)>1:
        l1.remove(x)
print(l1)

l2=(set(l1)) 
print(list(l2))
    
    



