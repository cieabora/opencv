from cs1graphics import *
def f(n):
    return n ** 3 + n ** 2 + 2 * n


canvas = Canvas(300, 300)
x = Polygon()
y = Polygon()
z = Polygon()
canvas.add(x)
canvas.add(y)
canvas.add(z)
x.addPoint(Point(0, 150))
x.addPoint(Point(299, 150))

y.addPoint(Point(150, 0))
y.addPoint(Point(150, 299))

mid = 149
for i in range(300):
    xp = (i - 149) / 100
    z.addPoint(Point(i, f(xp) / 100 + 149))
