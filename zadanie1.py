import numpy as np
import matplotlib as plt

class Polynomial:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def solving_eq(self):
        delta = self.b ** 2 - 4 * self.a *self.c
        if delta < 0:
            return None
        else:
            x1 = -(self.b - np.sqrt(delta))/( 2 * self.a)
            x2 = -(self.b + np.sqrt(delta))/( 2 * self.a)
            solutions = x1, x2
            return solutions

    def value(self,x):
        return self.a*x**2 + self.b *x +self.c

    def plot(self,zakresargumentu):
        plt.plot(zakresargumentu, self.value(zakresargumentu))
        plt.title('graph of the function')
        plt.grid(True)
        plt.show()


poli1 = Polynomial(2,5,3)
print(poli1.solving_eq())
