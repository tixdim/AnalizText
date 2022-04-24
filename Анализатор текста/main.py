def check_on_BadWord(text_analyz):
    words_1 = list(map(lambda x: x.lower(), open('BadWordsList.txt', encoding='utf-8').read().split()))
    words_2 = list(map(lambda x: x.lower(), open('filter.txt', encoding='utf-8').read().split()))
    Bad_words = words_1 + words_2

    fragments = []

    for word in Bad_words:
        for part in range(len(text_analyz)):
            fragment = text_analyz[part: part + len(word)]
            fragments.append(fragment)

    result = []

    for word in Bad_words:
        for fragment in fragments:
            if word == fragment or word in fragment or fragment in word:
               result.append(word)

    if len(result) == 0:
        return True

    with open("result.txt", "a") as file:
        file.writelines(result)

    return False


def main():
    text = input("Введите текст: ")
    w = check_on_BadWord(text)
    if w:
        print("В вашем тексте не найдено плохих слов. Поздраваляю, вы прошли проверку!")
    else:
        print("В вашем тексте найдены плохие слова. Увы, вы не прошли проверку!")


if __name__ == "__main__":
    main()
