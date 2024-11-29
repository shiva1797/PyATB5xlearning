my_list = [1, 2, 3]
for i in my_list:
    print(i)
my_list.append(5)

print(my_list)

my_list.extend([1,23,4,5,6])
for i in my_list:
    print(f"extented list -->",i)

print(len(my_list))
my_list.insert(9,"shiva")
print(my_list)

my_list.copy()
print(my_list)

my_list.pop(9)
print(my_list)

my_list.remove(6)
print(my_list)