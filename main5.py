count = 0
while count <10:
    print(count)
    count += 1
print('--------------------------')
lst = ['ali', 'reza', 'hamed']
for name in lst:
    print(lst)# kole list
    print(name)# index list
    print(name[0:])
    print(len(lst))
print('=======================')
var ="ali"
for ch in var[::-1]:
    print(ch)

lst2 = ["ali", "reza", "farhad"]
lst2.append("mamad")
lst2.remove("reza")
lst2.extend(["bahman", "saman","danial"])
for name in lst2:
    print(lst2)
    print(len(lst2))
    print(lst2[1])

print("=======================")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [5, 21, 37, 40, 5, 16, 7, 8, 9, 1]
for aa in range(0, 10):
    jam = list1[aa] + list2[aa]
    print(jam)
print("******************")
for i in range(len(list1)):
    jam2 = list1[i] + list2[i]
    print(jam2)

print("-------------break----------")
counter = 0
while True:
    print(counter)
    counter +=1
    if counter >=10:
        break
        print("loop finish")
    else:
        print("in loop")
print("out loop")

print("------------countinue-----------")
for i in range(10):
    if i == 5:
        continue
    print(i)