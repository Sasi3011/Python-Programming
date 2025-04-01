#sample program using builtin

# dict1={'Name':'Zophie', 'Species':'cat', 'age':7}
# print("Length:%d"%len(dict1))

# x=dict('Name','Zophie', 'Species','cat', 'age',7)
# print(x)

# keys = {'a', 'e', 'i', 'o'}
# values = ["Vowel", "Letter", "Sound"]
# vowels = {key: values for key in keys}
# print(vowels)


# x=dict(name="Zophie", species="cat", age=7)
# y=x.copy()
# print(y)
# print(id(x))
# print(id(y))

tv={'size': 55, 'price': 1200}
keymax=min(tv,key=tv.get)
print(keymax)

tv={'size': 55, 'price': 1200}
keymax=max(tv,key=tv.get)
print(keymax)

dict1={'Name':547, 'Species':45, 'age':7}
y=sorted(dict1.items(),key=lambda x:x[1],reverse=True)
print(y)