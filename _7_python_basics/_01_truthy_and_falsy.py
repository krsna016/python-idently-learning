"""
In Python, the following values are considered as Truthy and Falsy:

Truthy values:
- Any non-zero number (e.g., 1, -1, 3.14)
- Any non-empty sequence or collection (e.g., "hello", [1, 2, 3], (1, 2), {1: 'a'}, {1, 2})

Falsy values:
- None
- False
- Zero of any numeric type (e.g., 0, 0.0, 0j)
- Empty sequences and collections (e.g., "", [], (), {}, set())
"""

print(bool([]))
print(bool([1, 12, 3]))
