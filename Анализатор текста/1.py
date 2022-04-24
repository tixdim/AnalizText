words_1 = list(map(lambda x: x.lower(), open('BadWordsList.txt', encoding='utf-8').read().split()))
words_2 = list(map(lambda x: x.lower(), open('filter.txt', encoding='utf-8').read().split()))
Bad_words = words_1 + words_2