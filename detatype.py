print("--------- tupleنوع داده -------")
# مثل لیست فقط در دیتا بیس از تاپل استفاده میشه وبه جای براکت از پرانتز استفاده میکنه
tuple1 = (1, 2, 5, "ali")
print(tuple1)
print(type(tuple1))
print(tuple1[1])


print("-----------نوع دادهset ----------------")
#ایندکسی نیست
set1 ={1, 2, 5, "ali", 15, "reza"}
set2 ={'hamed', 4, 5, 12}
print(set1)
print('ali' in set1)
print(set2 | set1)
print(set1 > set2)
print(set1 < set2)
print(set1 - set2)
print(set1 & set2)# هردو موجوده
print(len(set1))
set1.add('ahmad')
print(set1)


print("---------------نوع داده dictionary---------------")
capitals = {'iran':'tehran',
            'france':'paris',
            'italy':'rom'}
capitals2 ={'germany':'berlin',
            'uk':'london'}
print(capitals)
print(capitals['iran'])
capitals['spain'] = 'madrid'
print(capitals)
print('iran' in capitals)
capitals.update(capitals2)#add two dictionary
print(capitals)
'shiraz' in capitals.keys()
print(capitals.keys())