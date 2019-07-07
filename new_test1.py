class A():
    def __init__(self):
        self.a = int(input('请输入第一个数：'))
        self.b = int(input('请输入第二个数：'))
        self.c = int(input("请输入第三个数："))
    def show(self):
        "显示结果"
        print(str(self.a)+"+"+str(self.b)+"is"+str(self.a+self.b)+"!")
    def add(self):
        print(self.a+self.b+self.c)
        return self.a+self.b+self.c
    def jian(self):
        print(self.a-self.b-self.c)
        return self.a-self.b-self.c
    def cheng(self):
        print(self.a*self.b*self.c)
        return self.a*self.b*self.c
class B(A):
    def __init__(self):
        super().__init__()
        self.d = int(input('请输入第四个数：'))
    def div(self):
        print(self.a/self.b/self.c/self.d)
        return self.a/self.b/self.c/self.d
class C(B):
    def __init__(self):
        super().__init__()
        self.e = "HUAWEI"
    def huawei(self):
        print('I can do it in %s !'%self.e)


test = C()
test.show()
test.add()
test.jian()
test.cheng()
test.div()
test.huawei()

