class A:
    def __add__(self, b):
        return 4+b

c = A()
print(c + 5)
