print("---------loop | dictionary | enumrate -----------")
capitals = {'iran': 'tehran', 'spain': 'madrid', 'italy': 'rom'}
# استفاده از حلقه و نوع داده دیکشنری
for key in capitals:
    print(key)
    print(capitals)
    print(capitals.values())
# هر دو حلقه مشابه ولی این خوانایی بهتری دارد
for key in capitals.keys():
    print(key)
    print(capitals.values())
# مقدار ها رو نشون میده
for value in capitals.values():
    print(value)
#آیتم
print("-------------------------")
for item in capitals.items():
    print(item)
# آیتم به شکل جدا کردن unpack
for k, v in capitals.items():
    print(k, v)

#جابه جا کردی key , value
print("-------------------------")
revers_capital = dict()# ساخت دیکشنری جدید
for k, v in capitals.items():
    revers_capital[v] = k
print(revers_capital)


#enumrate
print("-------------------------")
# هم مقدار را میدهد هم ایندکس
lst = [1, 2, 'ali', 82]
for en, s in enumerate(lst):
    print(en, '>>>>>>', s)
# از یک ایندکس خاص شروع کند
for en, s in enumerate(lst, 2):
    print(en, s)
#زیپ
print("-------------------------")
lst1 = [1, 2, 3, 4]
lst2 = [4, 3, 2, 1]
lst3 =[]
for a, b in zip(lst1, lst2):
    lst3.append(a + b)
print(lst3)