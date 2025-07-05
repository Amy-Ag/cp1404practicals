"""
Word Occurrences
Estimate: 30-40 minutes
Actual: 16 minutes
"""
text=input("Text: ")
words=text.split()
words_to_count={}
for word in words:
    words_to_count[word]= words_to_count.get(word, 0) + 1
sorted_words=sorted(words_to_count.items())
maximum_word_length=max(len(word) for word, count in sorted_words)
for word,count in sorted_words:
    print(f"{word:{maximum_word_length}} : {count}")
