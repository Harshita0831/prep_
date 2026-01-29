class A:
    def message(self):
        print("This is message from class")
class B(A):
    def message(self):
        print("this is mess")
class C(A):
    def message(self):
        print("this is me")
class D(B,C):
    pass
obj = D()
obj.message()
