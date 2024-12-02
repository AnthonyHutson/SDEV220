# 13.2
file = open('today.txt', 'r')
today_string = file.read()
print(today_string)
# 13.3
with open('today.txt', 'r') as file:
    for i in file:
        i = i.split(' ')
        i = [word.strip(' ') for word in i]
        print(i)
file.close()