name = "Bhawya"
age = 20
sex = "Male"

print(name)
print(age)
print(sex)

# Method - 1
print("My name is", name)
print("My age is", age)
print("My sex is", sex)
print("My name is", name, "My age is", age, "My sex is", sex)


print("My name is", name + ".")
print("My age is", str(age) + ".")
print("My sex is", sex + ".")
print("My name is", name + ".", "My age is",
      str(age) + ".", "My sex is", sex + ".")

# Method-2 (F-Strings)
print(f"My name is {name}")
print(f"My age is {age}")
print(f"My sex is {sex}")
print(f"My name is {name} My age is {age} My sex is {sex}")

print(f"My name is {name}.")
print(f"My age is {age}.")
print(f"My sex is {sex}.")
print(f"My name is {name}.", "My age is {age}.", "My sex is {sex}.")
