class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, coords):
        return cls(*coords)

    @classmethod
    def from_point(cls, point):
        return cls(point.x, point.y)

def main():
    a = Point(1,2)
    print(a.x, a.y)

    p = Point.from_tuple((3,7))
    print(p.x, p.y)

    q = Point.from_point(p)
    print(q.x, q.y)

    r = Point.from_point(a)
    print(r.x, r.y)

if __name__ == '__main__':
    main()