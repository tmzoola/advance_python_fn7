
def outer():
    a = 25
    name = "Python"
    
    def inner():
        return name
    
    print("Salom Dunyo")
    return inner

my_func = outer()
name  = my_func()

print(name)