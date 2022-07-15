#Exercise 1
import collections
user_integer_input = int(input().strip())
lst1 = []
for i in range(user_integer_input):
    lst1.append(input().strip(""))

word_counts = collections.Counter(lst1)

print(len(word_counts))

for word, count in word_counts.items():
    print(count, end=" ")