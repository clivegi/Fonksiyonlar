# Fonksiyonlar
#global scope
x="global x"
def fonksiyon():
    #local scope
    x="local x"
    print(x)
fonksiyon()
print(x)


##############

name="çınar"
def namem(new_name):
    name= new_name
    print(name)

namem("Ada")
print(name)
###################

name="global string"
def greeting():
    # name="Çınar"

    def hello():
        # name="Ada"
        print("hello "+ name)
    hello()
greeting()
print(name)

##########################
x=50
def test():
    global x
    print(f"x: {x}")

    x=100
    print(f"changed x to{x}")

test() 
print(x)
