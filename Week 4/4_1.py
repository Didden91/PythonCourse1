import random

c = [1, 2, 3, 4, 5, 9, 1231, 9378478]

for i in range(10):
    x = random.random()
    y = random.randint(1, 10)
    choice = random.choice(c)
    print(x)
    print(y)
    print(choice)
