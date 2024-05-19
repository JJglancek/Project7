my_list = ["apple", "orange", "mango", "currant", "haribo"]
print(my_list)
print(my_list[0])
print(my_list[4])
print(my_list[2:5])
my_list[2] = "mint"
print(my_list)
my_dict = {"Book": "Книга", "Table": "Стол", "Mouse": "Мышь", "Torch": "Факел", "Water": "Вода"}
print(my_dict)
print(my_dict.get("Loft", "такого ключа нет"))
print(my_dict.setdefault("Mouse"))
my_dict["Table"] = "Столик"
print(my_dict)
