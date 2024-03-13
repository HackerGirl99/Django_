list1=["apple","banana","cherry","orange"]
print(list1)
print(type(list1))
for x in list1:
    print(x)

print()

list1[2]="watermelon"
print(list1)

print(len(list1))

print(list1.pop())
print(list1)
list1.insert(1,"Strawberry")
print(list1)

print()

tuple1=("car","van","bike")
print(tuple1)
print(type(tuple1))
list1.extend(tuple1)
print(list1)

print()
set1={'a','b','c','d'}
print(set1)
print(type(set1))

print()
set2={'a','b','c','d','a'}
print(set2)
set2.add('e')
print(set2)

di1={"number" : 2,"brand":"Sofa"}
print(di1)
print(type(di1))
print(di1["brand"])

"""
= RESTART: C:/Users/famly/Documents/Django-Workshop/Django-Day2-INTRO_TO_PYTHON/data.py
['apple', 'banana', 'cherry', 'orange']
<class 'list'>
apple
banana
cherry
orange

['apple', 'banana', 'watermelon', 'orange']
4
orange
['apple', 'banana', 'watermelon']
['apple', 'Strawberry', 'banana', 'watermelon']

('car', 'van', 'bike')
<class 'tuple'>
['apple', 'Strawberry', 'banana', 'watermelon', 'car', 'van', 'bike']

{'d', 'a', 'c', 'b'}
<class 'set'>

{'d', 'a', 'c', 'b'}
{'b', 'd', 'c', 'a', 'e'}
{'number': 2, 'brand': 'Sofa'}
<class 'dict'>
Sofa
"""
