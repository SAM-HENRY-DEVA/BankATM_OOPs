def sum_int(l):
    sum=0
    for i in l:
        if type(i)==int:
            sum+=i
        elif type(i) in [list,tuple,set]:
            sum+=sum_int(i)
    return sum

print(sum_int([10,20,(20,'hello',2.6,[23,8,'python'],100),200]))
print(sum_int([10,20,(20,'hello',2.6,[23,8,{10,5},'python'],100),200]))
print(sum_int([1,2,3]))
print(sum_int([1,2,3,[1,2],5]))
