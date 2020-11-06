a = input('Where do you live?')
if a == 'Kazan' or a == 'Moscow' or a == 'Home':
    b = input('Who can lift and move both a horse and an elephant?')
    if b == 'Strongman' or b == 'Nobody' or b == 'Chess player':
        c = input('What was “tomorrow” yesterday, and tomorrow will be “yesterday”?')
        if c == 'I do not know' or c == 'Today' or c == 'Something':
            if b == 'Strongman' and c == 'Something':
                print('Result: You are an urban commoner! (Your IQ = 35.)')
            elif a == 'Kazan' and c == 'I do not know':
                print('Result: You Kazan know-nothing man! (Your IQ = 27.)')
            elif a == 'Moscow' and c == 'I do not know':
                print('Result: You Moscow know-nothing man! (Your IQ = 20.)')
            elif a == 'Home' and b == 'Chess player' and c == 'Today':
                print('Result: You are a tricky expert! (Your IQ = 100!)')
            elif a == 'Kazan' or a == 'Moscow' or a == 'Home':
                print('Result: You are not an easy urban commoner! (Your IQ = 56.)')
        else:
            print('Error!')
    else:
        print('Error!')
else:
    print('Error!')
