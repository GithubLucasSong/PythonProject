class A():
    __name = 'songyu'
class B(A):
    pass

b = B()
print(b.__name)