from collections import Counter
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']


word_count = Counter(words)
print("Word Count:", word_count)

most_common = word_count.most_common(2)
print("Most Common Words:", most_common)
