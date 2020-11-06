a = input('Do you like an ice cream?')
b = input('Do like programming?')
if a == 'yes' and (b == 'yes' or b == 'no'):
    print('You are true programmer!Even if you are not programming...')
elif a == 'no' and (b == 'yes' or b == 'no'):
    print('You are not true programmer!')
