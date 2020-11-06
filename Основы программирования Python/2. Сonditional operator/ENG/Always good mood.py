text = input('Hello, how is your mood?')
if ('?' not in text) or ('not' not in text):
    if ('fine' in text) or ('good' in text) or ('amazing' in text):
        print('Good! May you always have this mood!')
    elif ('bad' in text) or ('horrible' in text):
        print('Do not be upset! Everything will be alright!')
    else:
        print('Sorry, I do not understand you (Error 404!)')
else:
    print('Sorry, I do not understand you (Error 404!)')
