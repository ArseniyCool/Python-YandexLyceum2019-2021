# The program checks the beauty of a three-digit number according to this principle:
#  If among the half-sum of the maximum and minimum by the value of the digits
#  is equal to the remaining digit of the number, then this number is beautiful
a = int(input('Enter three-digit number:'))
num_3 = a % 10
num_2 = (a // 10) % 10
num_1 = a // 100
if num_1 >= num_2 and num_1 >= num_3:
    if num_2 >= num_3:
        c = (num_1 + num_3) / 2
        if c == num_2:
            print('You enter the beautiful number!')
        else:
            print('It\'s a pity, you enter common number')
    else:
        c = (num_1 + num_2) / 2
        if c == num_3:
            print('You enter the beautiful number!')
        else:
            print('It\'s a pity, you enter common number')
elif num_2 >= num_1 and num_2 >= num_3:
    if num_1 >= num_3:
        c = (num_2 + num_3) / 2
        if c == num_1:
            print('You enter the beautiful number!')
        else:
            print('It\'s a pity, you enter common number')
    else:
        c = (num_2 + num_1) / 2
        if c == num_3:
            print('You enter the beautiful number!')
        else:
            print('It\'s a pity, you enter common number')
elif num_3 >= num_1 and num_3 >= num_2:
    if num_1 >= num_2:
        c = (num_3 + num_2) / 2
        if c == num_1:
            print('You enter the beautiful number!')
        else:
            print('It\'s a pity, you enter common number')
    else:
        c = (num_3 + num_1) / 2
        if c == num_2:
            print('You enter the beautiful number!')
        else:
            print('It\'s a pity, you enter common number')
