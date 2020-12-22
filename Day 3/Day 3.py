#part 1
data = open("Map.txt", "r")
map = []

for i in data:
    map.append(i)

border = len(map[0])-1


def slope(xint,yint):
    posx = 0
    posy = 0
    trees = 0

    while posy < len(map):
        if map[posy][posx] == "#":
            trees+=1
        posx += xint
        posy +=yint
        if posx >= border:
            posx -=border
    return trees

print (slope(3,1))

#part 2
print (slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2))