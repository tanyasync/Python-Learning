marks={
    "harry":100,
    "tanya":97,
    "jungkook":1000,
    0:"siya"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"tanya":99})
# print(marks)
# marks.update({"taehyung":1000})
# print(marks)

# print(marks.get("harry2")) #it will give None because harry2 is not present in the dictionary
# print(marks["harry2"]) #returns error because harry2 is not present in the dictionary

# marks.clear()
# print(marks)

# new_dict=marks.copy()
# print(new_dict)

# keys=marks.keys()
# new_dict= dict.fromkeys(keys,0)
# print(new_dict)

marks.pop("harry")
print(marks)