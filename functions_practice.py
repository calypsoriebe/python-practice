def hello():
    print('Hello user')


hello()


def pack(x, y, z):
    packed = [x, y, z]
    print(packed)


pack('shoes', 'clothes', 'makeup')


def eat_lunch(food):
    if len(food) == 0:
        print('There is no food in your lunchbox')
    else:
        for i in range(len(food)):
            if i == 0:
                print(f'I eat my {food[0]} first')
            else:
                print(f'Im eating my {food[i]} next')


lunch_foods = ['apple', 'pear', 'salad', 'cookie']
empty_box = []
eat_lunch(empty_box)
eat_lunch(lunch_foods)
