import theano.tensor as T
from theano import function


class GPUMathKernel:

    def __init__(self):
        return

    def add(self, x_in, y_in):
        x = T.ivector('x')
        y = T.ivector('y')
        z = x + y
        f = function([x, y], z)
        return f(x_in, y_in)

    def sub(self, x_in, y_in):
        x = T.ivector('x')
        y = T.ivector('y')
        z = x - y
        f = function([x, y], z)
        return f(x_in, y_in)

    def mult(self, x_in, y_in):
        x = T.ivector('x')
        y = T.ivector('y')
        z = x * y
        f = function([x, y], z)
        return f(x_in, y_in)

    def div(self, x_in, y_in):
        x = T.ivector('x')
        y = T.ivector('y')
        z = x / y
        f = function([x, y], z)
        return f(x_in, y_in)

    def yaxb(self, x_in, y_in, b_in, a_in):
        x = T.ivector('x')
        y = T.ivector('y')
        b = T.ivector('b')
        a = T.ivector('a')
        z = (a * x * y) + b
        f = function([x, y, b, a], z)
        return f(x_in, y_in, b_in, a_in)
