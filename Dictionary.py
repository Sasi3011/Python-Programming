#sample program using builtin

# dict1={'Name':'Zophie', 'Species':'cat', 'age':7}
# print("Length:%d"%len(dict1))

# x=dict('Name','Zophie', 'Species','cat', 'age',7)
# print(x)

# keys = {'a', 'e', 'i', 'o'}
# values = ["Vowel", "Letter", "Sound"]
# vowels = {key: values for key in keys}
# print(vowels)


x=dict(name="Zophie", species="cat", age=7)
y=x.copy()
print(y)
print(id(x))
print(id(y))