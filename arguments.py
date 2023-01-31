# def changename(n):
#     n="ad"

# name="yiğit"
# changename(name)
# print(name)

# def change(n):
#     n[0]="istanbul"

# sehirler=["Ankara,","İzmir"]
# change(sehirler[:])
# print(sehirler)

# def add(*prams):
#     return sum((prams))

# print(add(10,20))
# print(add(10,20,30))

# def add(*prams):
#     sum=0
#     for n in prams:
#         sum=sum+n
#     return sum

# print(add(10,20))
# print(add(10,20,30,8,9,6,3,1,4,5))        
def displayuser(**args,):
    for key,value in args.items():
        print("{} is {}".format(key,value))
displayuser(name="çınar",age=2,city="istanbul")
displayuser(name="ada",age=12,city="kocaeli",phone="123123")
displayuser(name="adan",age=22,city="ankara",phone="12312322",gmail="email@gmail.com")

def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, 60, 70, key1 = 'value 1', key2 = 'value 2')