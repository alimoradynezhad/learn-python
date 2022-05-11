# if تک خطی
val1 = 10
val2 = 20  if val1 == 1 else 10#اگر val1 مقدارش 1 بود که هیچ اگر نه val2 را با 10 مقدار دهی کن
print(val2)

val1 = 10
val2 = 20  if val1 == 1 else 5#اگر val1 مقدارش 1 بود که هیچ اگر نه val2 را با 5 مقدار دهی کن
print(val2)

sqr1 = [i**2 for i in range(10)]#از صفر تا 10 را به توان 2 برسان
print(sqr1)
sqr = [i**3 if i % 3 == 0 else 10 for i in range(10, 30)]#از 10 تا 30 را به توان 3 برسان اگر باقیمانده تقسیم بر سه اش 0 شد در غیر اینصورت 10 بزار
print(sqr)