import sys

sys.stdin = open('input.txt', "r")

n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(n)]

# print(words)

word_length = [[] for _ in range(51)]
set_words = set(words)

for i in set_words:
    word_length[len(i)].append(i)

for word in word_length:
    word = sorted(word)
    if word:
        for j in range(len(word)):
            print(word[j])

