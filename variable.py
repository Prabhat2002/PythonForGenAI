age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
    
    
name = input("Enter your name: ")
print("Hello, " + name + "!")
print(f"Hello, {name}!")
print("Hello, {}".format(name))
print("Hello, %s!" % name)
print(type(name) , name)