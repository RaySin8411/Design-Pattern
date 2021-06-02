from circle import Circle
from time_waster import TimeWaster

if __name__ == '__main__':

    c = Circle(5)
    c1 = {'radius': c.radius, 'area': c.area}
    print(c1)
    print(Circle.pi())

    tw = TimeWaster(1000)
    tw.waste_time(999)