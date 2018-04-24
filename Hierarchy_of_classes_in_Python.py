# Hierarchy of classes
# Subclasses of classes and multiple inheritance
# Checking to which class instance belongs
# Method resolution order
# Super methods

class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C): pass

issubclass(A, A)  # True
issubclass(C, D)  # False
issubclass(A, D)  # True
issubclass(C, object)  # True
issubclass(object, C)  # False

x = A()  # Creating an instance of class A
isinstance(x, A)  # True
isinstance(x, B)  # True
isinstance(x, object)  # True
isinstance(x, str)  # False

# Method resolution order
# Cjecking in which order the instance of class A will go through namespaces of inherited classes
print(A.mro())  # [<class '__main__.A'>, <class '__main__.B'>,
                # <class '__main__.D'>, <class '__main__.E'>, 
                # <class '__main__.C'>, <class 'object'>]

# Super methods
class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0

class MyList(list, EvenLengthMixin):
    def pop(self):
        # The method pop will be now searched upper in hierarchy except in class MyList 
        x = super(MyList, self).pop()
        print('Last value is', x)
        return x

ml = MyList([1, 2, 4, 17])
z = ml.pop()  # Last value is 17
print(z)  # 17
print(ml)  # [1, 2, 4]
        
