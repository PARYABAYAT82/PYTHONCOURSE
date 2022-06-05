"""
13. What happens when an executing program attempts to retrieve a value using a key that is not present
in the dictionary?
"""
d = {"Fred": 20, "parya": 19}
x = d.get("John")
print(x)
"""
14. What happens when an executing program attempts to associate a value with a key that is not present
in the dictionary?
"""
d = {"Fred": 20, "parya": 19}
d["John"] = 35
print(d)
"""
15. Are dictionaries mutable or immutable?
Mutable
"""

