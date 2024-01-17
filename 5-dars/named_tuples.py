from collections import namedtuple


Mentor = namedtuple('Mentor',['name', 'age', 'group'])
new_tuple = Mentor("Murodjon", 26, "FN7")

for i in new_tuple:
    print(i)




class Mentor:
    name = "Murodjon"
    age = 26
    group = "FN7"
    

new_class = Mentor()

for i in new_class:
    print(i)



