# ✅ ==  (Equality Operator)
# 👉 Checks if the *values* of two variables are the same

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # ✅ True – because both lists have the same values!

# ✅ 'a' and 'b' contain the same data (equal values)
# ❗ BUT they are stored in different memory locations (different objects)

# ✅ is  (Identity Operator)
# 👉 Checks if two variables point to the *same object* in memory

print(a is b)  # ❌ False – because 'a' and 'b' are two different objects

# 🎯 Let’s understand with a more visual, friendly example:

x = 1000
y = 1000
print(id(x))
print(id(y))

print(x == y)  # ✅ True – same value
print(x is y)  # ❌ False – not the same memory location

# ✅ BUT for small integers, Python reuses objects (called interning)

p = 10
q = 10
print(id(p))
print(id(q))

print(p == q)  # ✅ True
print(p is q)  # ✅ True – Python optimizes memory for small numbers (like -5 to 256)

# 👶 Think of it like:
# == means both students wrote the *same answer* ✍️ (same content)
# is means both students are *literally the same person* 👤 (same memory identity)

# Another Fun Example 🎉:

name1 = "Anurag"
name2 = "Anurag"

print(id(name1))
print(id(name2))

print(name1 == name2)  # ✅ True – same characters
print(name1 is name2)  # ✅ True (usually) – Python reuses strings too!

# 🚨 But if we create objects dynamically:
list1 = list("data")
list2 = list("data")

print(list1 == list2)  # ✅ True
print(list1 is list2)  # ❌ False
