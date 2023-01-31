hesapA={
    "ad": "Sadık turan",
    "hesapno": "123123",
    "bakiye":3000,
    "ekhesap":2000
}

hesapB={
    "ad": "Ali turan",
    "hesap no": "123123",
    "bakiye":2000,
    "ekhesap":1000
}

def paracek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if hesap["bakiye"]>=miktar:
        hesap["bakiye"]-=miktar
    
        print("paranızı alabilirsinşz")
    else:
        toplam=hesap["bakiye"]+hesap["ekhesap"]
        if(toplam>=miktar):
            ekhesapkullanimi=input("ek hesap kullanılsın mı e/h")
            if ekhesapkullanimi=="e":
                ekhesapkullanimi=miktar-hesap["bakiye"]
                hesap["bakiye"]=0
                hesap["ekhesap"]-=ekhesapkullanimi
                print("paranızı alabilirsiniz")
            else:
                print(f"{hesap['hesapno']}nolu hesabınızda {hesap['bakiye']} bulunmaktadır")
        else:
            print("bakiye yetersiz")       
def bakiyesorgu(hesap):
    print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']} Tl bulunmaktadır ek hesap limitiniz ise {hesap['ekhesap']} tl bulunmaktadır")


paracek(hesapA,3000)
bakiyesorgu(hesapA)
print("*************")
paracek(hesapA,2000)
bakiyesorgu(hesapA)