# Python example to show the working of multiple
# inheritance

class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")
    def val(self):
        print("Base val 1")

class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")
    def val(self):
        print("Base val2")




class Derived(Base2, Base1):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")


ob = Derived()
ob.val()

