list_d=[1,2,3,4,5,6,7]
#repeataion allowed
#mutable []
tuple_d=(1,2,3,4,5,6)
#repeataion allowed
#immutable ()
set_d={1,2,3,4,5,6,7}
#repeation not allowed
#immutable

dict_d= {"name":"shiva", "age":24,"place":"bang"}
print(dict_d)
print(dict_d["name"])
dict_d["name"] = "kumar"
print(dict_d)

#del dict_d["name"]
#print(dict_d)

print("value" in dict_d)


for i,j in dict_d.items():
    print(i,"is-->",j)





my_dict = { "name": "Aman", "age": 34,"role": "SDET", "experience": 3}
#print(my_dict)
#print(my_dict["age"])

my_dict["role"] = "Manual Tester"
#print(my_dict)

del my_dict["age"]
#print(my_dict)

#for key, value in my_dict.items():
    #print(key, " -> ", value)

#print("age" in my_dict)
#print("role" in my_dict)