# По задаче:
# Сколько землекопов понадобится королю, чтобы за 2 дня вырыть яму длинной 1400 метров,
# при условии,что скорость одного землекопа - 3 метра/день?
import math
# time = int(input()
time = 2
# speed = int(input()
speed = 3
# length = int(input()
length = 1400
diggers = math.ceil(length / (time * speed))
print(diggers)
