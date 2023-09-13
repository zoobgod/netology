#task1
word = 'programming'
if len(word) % 2 == 0:
    print(word[int(len(word)/2)-1:int(len(word)/2)+1])
else:
    print(word[int(len(word)/2)])

#task2
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys.sort()
girls.sort()
# print(boys)
# print(girls)

if len(boys) == len(girls):
    for i in range(0, len(girls)):
        print(f"{boys[i]} and {girls[i]}")
else:
        print("Кто-то может остаться без пары!")




