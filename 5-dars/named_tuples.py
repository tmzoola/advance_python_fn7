from collections import namedtuple


Mentor = namedtuple('Mentor',['name', 'age', 'group'])
new_tuple = Mentor("Murodjon", 26, "FN7")

# print(new_tuple.__getnewargs__())



# class Mentor:
#     name = "Murodjon"
#     age = 26
#     group = "FN7"
    

# new_class = Mentor()

# for i in new_class:
#     print(i)



