# def sayHello(name="user"):
#     print("Hello "+ name)

# sayHello("Ramazan")
# sayHello("Yusuf")
# sayHello()

def sayHello(name="user"):
    return "Hello "+ name

msg=sayHello("Ramazan")
print(msg)

def total(num1,num2):
    return num1+num2

result=total(15,20)
print(result)

def yashesapla(dogumtarihi):
    return 2019-dogumtarihi

ageramazan=yashesapla(1999)
ageyusuf=yashesapla(1995)
ageelif=yashesapla(1979)
print(ageramazan,ageyusuf,ageelif)

def ememeklilikyılı(dogumtarihi,isim):
    """
    DOCSTRING: DOĞUM YILINIZA GÖRE EMEKLİLİĞİNİZE KAÇ YIL KALDI
    INPUT: DOĞUM YILI
    OUTPUT: HESAPLANAN YIL BİLGİSİ

    """
    yas=yashesapla(dogumtarihi)
    emeklilik=65-yas

    if emeklilik>0:
        print(f"Emekliliğinize {emeklilik} yaş kaldı")
    else:
        print("emekli oldunuz ztn .")
ememeklilikyılı(1983,"Ali")    
ememeklilikyılı(1923,"Ali")    
ememeklilikyılı(1953,"Ramazan")    
print(help(ememeklilikyılı))
list=[1,2,3]
print(help(list.append))