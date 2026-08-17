# main.py

# Import the complete module
import mymodule

mymodule.say_hello("Madhav")
mymodule.say_bye("Rishabh")


# Import a specific item from the module
from mymodule import person1

print(person1["age"])


# Import a specific function
from mymodule import say_hello

say_hello("Ansh")