# Dictionary from Two Lists

keys = ["name", "role", "experience"]
values = ["Aman", "SDET", 3]



con_dict = dict(zip(keys,values))
for keys,values in con_dict.items():
    print(keys,":",values)


#my_dict = dict(zip(keys, values))
#print(con_dict)


# Merge Two Dictionaries
#dict1 = {"a": 1, "b": 2}
#dict2 = {"c": 3, "d": 4}

dict_3 = { "a":1,"b":2}
dict_4 ={"c":"kum","d":"mar"}
merg_dic = dict_3 | dict_4
print(merg_dic)



#merged_dict = dict1 | dict2
#print(merged_dict)
#print(merged_dict.get("a"))