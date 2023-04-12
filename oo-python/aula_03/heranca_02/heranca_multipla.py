class A:
    def __init__(self, x, y, **kwargs):
        super().__init__(**kwargs)
        self._x = x
        self._y = y
        print(vars(self))

class B:
    def __init__(self, z, **kwargs):
        super().__init__(**kwargs)
        self._z = z
        print(vars(self))

class AB(A, B):
    def __init__(self, x, y, z):
        super().__init__(x=x, y=y, z=z)
        print(vars(self))

print('Classe A:')
a = A(0, 1)

print('Class B:')
b = B(2)

print('Classe AB:')
ab = AB(x=0, y=1, z=2)