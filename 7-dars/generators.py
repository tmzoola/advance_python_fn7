import random
import time

names = ["Asadbek", "Murodjon", "Hasanboy", "Ilyosbek", "Asrorbek", "Yaxyobek", "Abdulaziz", "Farruxbek"]
majors = ["IT", "Filologiya", "Tarix", "Jismoniy Tarbiya", "Iqtisod", "Meditsina", "Boshlang'ich"]

nums = (i for i in names[0])

for i in nums:
    if i.isupper():
        print(i)



# def people_list(people_num):
#     result = []
    
#     for i in range(people_num):
#         person = {
#             "id":i,
#             "name":random.choice(names),
#             "majors":random.choice(majors)
#         }
#         result.append(person)
#     return result

# def people_generator(people_num):
#     for i in range(people_num):
#         person = {
#             "id":i,
#             "name":random.choice(names),
#             "majors":random.choice(majors)
#         }
#         yield person

# time1 = time.time()
# people = people_generator(100000)
# time2 = time.time()

# print(f"Funksiya teligi {time2-time1} ga teng")



























# def square(num):
#     return num**2

# my_list = [1,2,3,4,5]


# res = map(square, my_list)
# print(res)

# for i in res:
#     print(i)




