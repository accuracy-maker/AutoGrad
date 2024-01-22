"""
We'll implement a data structure named "Value" to store our computation data.
class value():
    def __init__()
    def __repr__()
    def __add__()
    def __mul__()
"""
import math

class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0.0
        self._prev = set(_children)
        self._op = _op
        
    def __repr__(self) -> str:
        return f"value(data={self.data})"
    
    def __add__(self, other):
        output = Value(self.data + other.data, (self, other), "+")
        return output
    
    def __mul__(self, other):
        output = Value(self.data * other.data, (self, other), "*")
        return output
    
    def tanh(self):
        x = self.data
        t = (math.exp(2*x) - 1)/(math.exp(2*x) + 1)
        output = Value(t, (self, ), 'tanh')
        return output
    
    
if __name__ == '__main__':
    # Here is a test module
    a = Value(3.0)
    b = Value(-2.0)
    print(a) # value(data=3.0)
    c = a + b
    print(c) # value(data=1.0)
    d = a * b
    print(d) # value(data=-6.0)
    e = a * b + c
    print(e._prev)
    print(e._op)
    
    