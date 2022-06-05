"""
5. Rewrite the last assignment statement in the following interactive sequence so that it behaves identically but uses tuple unpacking instead of tuple slicin
"""
a = (1, 2, 3, 4, 5, 6, 7, 8)
print(a)
s = _, _, *s, _, _ = a
print(s)
"""
6. Rewrite the last assignment statement in the following interactive sequence so that it behaves identically but uses tuple slicing instead of tuple unpackin
"""
a = (1, 2, 3, 4, 5, 6, 7, 8)
print(a)
s = a[3:7]
print(s)
"""
7. Consider the tuple tpl defined as
tpl = 7, 10, -3, 18, 6, 10
Provide one assignment statement that uses tuple unpacking to assign x to the first element and y to
the last element.
"""
tpl = (7, 10, -3, 18, 6, 10)
(x, _, _, _, _, y) = tpl
print(tpl)
print(x)
print(y)