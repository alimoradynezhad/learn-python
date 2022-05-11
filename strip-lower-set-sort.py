import os
with open("myfile.txt", "r") as f:
    deta =f.readlines()
    print(deta)
    print("-----------")
    word = deta[0]
    word.strip()#حذف چیزهای اضافه از استرینگ مثل \n
    word.lower()#کوچک کردن کاراکتر
    set(deta)#حذف تکراری ها
    print(deta)
    print(word)
    clean =[sorted(set(word.strip().lower())) for word in deta]#sort baray moratab kardan
    print(clean)