#fun little program

inputter = str(input('Please type whatever you would like to transcribe:\n'))

new = inputter.split(' ')

vowels = ['a' , 'e', 'i' , 'o', 'u']

for i in new:
    if i[0].lower() in vowels:
        word = 't' + i
    elif i[0:2].lower() == 'wh':
        word = 'tw' + i[2:]
    elif i[1].lower() == 't':
        word = 't' + i[2:]
    elif i[0:2].lower() == 'th':
        word = 't' + i[2:]
    elif i[0:2].lower() == 'kn':
        word = 't' + i[2:]
    else:
        word = 't' + i[1:]
    print(word, end = ' ')
