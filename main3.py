var = 'hello world'
print(var)
print(var * 2)
print(var + "  " +"python")
print(len(var))
print(var[2])
print(var[2:5])#index 234
print(var[2:])#index 2->
print(var[:3])#index 012
print(var[-2])#of end 2
print(var[::-1])#revers
slice1 = var[0:5]
slice2 = var[6:11]
print(slice1 +"_" +slice2)
age = 12
print(f'age is {age}')
name = "reza"
print(f'name student is  {name}')
print(f' name is {name} and age is {age}')
listname = ["ali", "reza", "hamed"]
print(listname)
print(len(listname))
print(listname[2])
listname.index('ali')
listmix = [1, 2, [5, 6], 'ali']
print(listmix)
print(len(listmix))
listmix.append('saman')
print(listmix)
listmix.extend(['ashkan', 'farhad'])
print(listmix)
listmix.insert(0, 'bahman')
print(listmix)
listmix.remove('farhad')
print(listmix)
listmix.pop(0)
print(listmix)