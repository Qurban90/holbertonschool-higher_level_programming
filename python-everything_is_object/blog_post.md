# Python3: Mutable, Immutable... Everything is Object!

## Introduction

In Python, everything is an object. Whether it is an integer, a string, a list, or even a function, Python treats all of them as objects. Each object has an identity, a type, and a value. Understanding how Python handles these objects, especially the difference between mutable and immutable types, is crucial for writing efficient and bug-free code. In this blog post, I will share what I learned about Python's object model through practical examples.

## id and type

Every object in Python has a unique identity and a type. The `id()` function returns the memory address of an object, while the `type()` function returns its type.
```python
a = 89
print(type(a))   # <class 'int'>
print(id(a))     # 140234866534752 (example address)

b = "Hello"
print(type(b))   # <class 'str'>
print(id(b))     # 140234866234208 (example address)
```

When you assign one variable to another, they point to the same object:
```python
a = 89
b = a
print(id(a) == id(b))  # True
print(a is b)           # True
```

CPython also caches small integers (-5 to 256) and some strings, so identical values may share the same object:
```python
a = 89
b = 89
print(a is b)  # True (cached integer)

s1 = "Best School"
s2 = "Best School"
print(s1 is s2)  # False (string with space, not interned)
```

## Mutable Objects

Mutable objects can be changed after creation. The main mutable types in Python are `list`, `dict`, and `set`. When you modify a mutable object, it keeps the same identity.
```python
l = [1, 2, 3]
print(id(l))     # 140234866234208
l.append(4)
print(l)         # [1, 2, 3, 4]
print(id(l))     # 140234866234208 (same id!)
```

Because mutable objects are modified in place, aliasing can lead to unexpected behavior:
```python
l1 = [1, 2, 3]
l2 = l1          # l2 is an alias, not a copy
l1.append(4)
print(l2)        # [1, 2, 3, 4] - l2 also changed!
print(l1 is l2)  # True
```

## Immutable Objects

Immutable objects cannot be changed after creation. The main immutable types are `int`, `float`, `str`, `tuple`, and `bool`. Any operation that seems to modify them actually creates a new object.
```python
a = 89
print(id(a))    # 140234866534752
a = a + 1
print(a)        # 90
print(id(a))    # 140234866534784 (different id, new object!)
```

Tuples are also immutable:
```python
t = (1, 2, 3)
# t[0] = 4  # TypeError: 'tuple' object does not support item assignment
```

Important tuple syntax to remember:
```python
a = ()     # empty tuple
a = (1, 2) # tuple with two elements
a = (1)    # NOT a tuple, just integer 1
a = (1,)   # tuple with one element (comma is required)
```

## Why Does It Matter?

Understanding mutability is essential because it affects how your program behaves. With mutable objects, multiple variables can reference the same object, so changing one affects all of them. With immutable objects, each modification creates a new object, so other references remain unchanged.
```python
# Mutable: += modifies in place
l = [1, 2, 3]
print(id(l))     # same id after +=
l += [4]
print(id(l))     # same id!

# Immutable: + creates new object
a = (1, 2, 3)
print(id(a))
a = a + (4,)
print(id(a))     # different id!
```

## How Arguments Are Passed to Functions

Python uses "pass by object reference". When you pass a variable to a function, you pass a reference to the object, not a copy. This means:

For **mutable objects**, modifications inside the function affect the original:
```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)  # [1, 2, 3, 4] - original list modified!
```

For **immutable objects**, the original remains unchanged because any modification creates a new local object:
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # 1 - original unchanged
```

Reassigning a variable inside a function only changes the local reference:
```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)  # [1, 2, 3] - unchanged
```

To safely work with mutable objects without affecting the original, always create a copy:
```python
def safe_modify(a_list):
    new_list = a_list[:]  # create a copy
    new_list.append(4)
    return new_list
```

## Conclusion

Everything in Python is an object with an identity, type, and value. Knowing whether you are working with mutable or immutable objects helps you predict how your code will behave, avoid hidden bugs from aliasing, and write cleaner, more efficient programs.
