symbols = input()
mid_symbol = len(symbols) // 2
if len(symbols) % 2 == 0:
    print(symbols[mid_symbol - 1] + symbols[mid_symbol])
else:
    print(symbols[mid_symbol])
