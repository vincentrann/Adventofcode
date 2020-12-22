Passwords = open('Passwords.txt', 'r')
correct = 0
for x in Passwords:
    string = x.split(' ')
    min = string[0].split('-')[0]
    max = string[0].split('-')[1]
    count = 0
    for y in string[2]:
        if y == string[1][0]:
            count+=1
    if count >= int(min) and count <= int(max):
        correct+=1

print (correct)







