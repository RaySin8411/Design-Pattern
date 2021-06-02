from slowing_down_revisited import countdown
from singleton import TheOne
from fibon import fibonacci1, fibonacci2
from unit import volume, average_speed

if __name__ == '__main__':
    countdown(3)
    first_one, another_one = TheOne(), TheOne()
    print('first_one id: ', id(first_one))
    print('another_one id: ', id(another_one))
    print(first_one is another_one)
    print(fibonacci1(10))
    print(fibonacci2(10))
    print(str(round(volume(3, 5), 4)) + ' ' + volume.unit)
    bolt = average_speed(100, 9.58)
    print(bolt)