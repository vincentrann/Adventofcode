#part 1

Numbers = open('Day 1/Numbers.txt', 'r')

data = [int(i) for i in Numbers]
addition1 = 0
addition2 = 0


for x in data:
    for y in data:
        if x + y == 2020:
            addition1 = x
            addition2 = y

Answer = addition1*addition2

print('the two numbers that add up to 2020 are', addition1, 'and', addition2, 'when you multiply them together you get', Answer)

#part 2

add1 = 0
add2 = 0
add3 = 0


for a in data:
    for b in data:
        for c in data:
            if a + b + c == 2020:
                add1 = a
                add2 = b
                add3 = c

Answer2 = add1*add2*add3

print('the three numbers that add up to 2020 are', add1, add2, 'and', add3, 'when you multiply them all together you get', Answer2)

