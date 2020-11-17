# Программа выводит отдельно количество быков — символов,
# которые есть в обеих строках и стоят на одном и том же месте,
# и количество коров — символов, которые есть в обеих строках, но на разных местах.
word_1 = input()
word_2 = input()
bulls = 0
cows = 0
cow_pretendent_word1 = set()
cow_pretendent_word2 = set()
for i in range(len(word_1)):
    if word_1[i] == word_2[i]:
        bulls += 1
    else:
        cow_pretendent_word1.add(word_1[i])
        cow_pretendent_word2.add(word_2[i])
intersec = cow_pretendent_word1 & cow_pretendent_word2
cows = len(intersec)
print('Быки:', bulls,'Коровы:', cows)
