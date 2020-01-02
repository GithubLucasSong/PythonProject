class A():
    def f1(self):
        print('a f1')
        self.f2()


    def f2(self):
        print('a f2')


class B(A):
    def f2(self):
        print('b f2')


b= B()
b.f1()