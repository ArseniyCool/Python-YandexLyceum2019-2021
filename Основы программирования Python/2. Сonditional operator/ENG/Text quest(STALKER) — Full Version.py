print('"Hello, stalker! Where do you keep the path?"')
a = input('(1 - To Sidorovich, sell junk; 2 - To the Dump for artifacts; 3 - To the monolith):')
if a == '1':
    print('You were going to Sidorovich on Cordon. On the way, you again shot the military,')
    print('which forever sitting near the bridge and finally reached the beginner camp')
    print('When you was meeting with Sidorovich, he answered you:')
    print('"You would still pick up cans, Tagged!')
elif a == '2':
    print('You went to a landfill to look for gifts for scientists.')
    print("You have collected the artifacts in full,")
    print("it s time to get out - but the outburst didn't think to wait.")
    print('So your corpse is left to rest, hang on a tree afterwards in distress,which')
    print('showing stalkers,that there are noobs going to an abnormal scrapyard without armour...')
elif a == '3':
    print('You were going to the center of the Zone,')
    print('not a bit worried about going there with a single first-aid kit with Pmm gun...')
    print('Surprisingly, you got to the Monolith. What desire do you make?')
    d = input('(1 - I want a wealth!; 2 - I want go home!)')
    if d == '1':
        print('[Original ending STALKER: SCh]')
    elif d == '2':
        print('During these breathtakingly horrible years in the Zone that you spent,')
        print('hell really became your home ... Monolith fulfilled your desire!')
        print('Welcome!')
    else:
        print('Go your way,pseudo-stalker! (Error 404!)')
else:
    print('Go your way,pseudo-stalker! (Error 404!)')
