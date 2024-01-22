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
    def __init__(self, data, _children=(), _op='', label=None):
        self.data = data
        self.grad = 0.0
        self._prev = set(_children)
        self._op = _op
        self.label = label
        
    def __repr__(self) -> str:
        return f"value(data={self.data})"
    
    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        output = Value(self.data + other.data, (self, other), "+")
        def _backward():
            self.grad += 1.0 * output.grad
            other.grad += 1.0 * output.grad
        output._backward = _backward
        return output
    
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        output = Value(self.data * other.data, (self, other), "*")
        def _backward():
            self.grad += other.data * output.grad
            other.grad += self.data * output.grad
        output._backward = _backward
        return output
    
    def tanh(self):
        x = self.data
        t = (math.exp(2*x) - 1)/(math.exp(2*x) + 1)
        output = Value(t, (self, ), 'tanh')
        def _backward():
            self.grad += (1 - t**2) * output.grad
        output._backward = _backward
        return output
    
    def backward(self):
        """
        implement a auto backpropagation function
        Parmas:
            self: the root of the backpropagation tree
            
        Return:
            a update of gradient of each variable in a chain rule
        """
        # set the root grad as 1.0
        self.grad = 1.0
        
        nodes_list = []
        visited = set()
        
        def collect(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    collect(child)
                nodes_list.append(v)
                
        collect(self)
        print(nodes_list)
        
        for node in reversed(nodes_list):
            if node._prev:
                node._backward()
    
                
    
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
    
    