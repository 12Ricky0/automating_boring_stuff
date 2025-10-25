import random
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
spam = ['Ants', 'Cats', 'Dogs', 'Badgers', 'Elephants']

# for index, item in enumerate(supplies):
#     print(index)

r= random.choice(supplies)
k=random.shuffle(supplies)
spam.sort()
print(spam)


s = ['a', 'z', 'A', 'Z']
s.sort(key=str.lower)
print(s)