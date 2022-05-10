lst = [1, 1, 2, 5, 2, 2, 'reza', 'reza', 'reza', 'reza', 'reza']
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in lst:
    if i == 1:
        count1 +=1
    elif i == 2:
        count2 +=1
    elif i == 5:
        count3 +=1
    elif i == 'reza':
        count4 +=1

print(f"1  >>>>>>>>>>>>  {count1}")
print(f"2  >>>>>>>>>>>>  {count2}")
print(f"5  >>>>>>>>>>>>>  {count3}")
print(f"rezs >>>>>>>>>>> {count4}")

print("----------Exercise 2-------------")

list = ['11', 'pooya', '10', '15.5']

for y in list:


    if y=='11':
        print(y)
    elif y=='10':
        print(y)
    elif y == 'pooya' or '15.5':
        continue



