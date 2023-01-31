# def yazdir(kelime,adet):
#     print(kelime*adet)
# yazdir("merhaba\n",10)

# def listeyecevir(*args):
#     list=[]

#     for argss in args:
#         list.append(argss)

#     return list
# result= listeyecevir(10,20,30,"Merhaba")
# print(result)

# def  asalsayılarıbul(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi>1:
#             for i in range(2,sayi):
#                 if (sayi%i==0):
#                     break
#             else:
#                 print(sayi)
# sayi1=int(input("sayı1: "))
# sayi2=int(input("sayı2: "))
# asalsayılarıbul(sayi1,sayi2)

def tambolen(sayi):
    tambolenler=[]
    for i in range(2,sayi):
        if sayi%i==0:
            tambolenler.append(i)
    
    return tambolenler
print(tambolen(20))