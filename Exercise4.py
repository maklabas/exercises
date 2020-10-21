biggestword = 0

text = str(input("Введите текст: "))    # ввод текста в список в 1 элемент
text = text.split(' ')  # разбиваем список по словам, ориентир разделения - пробел
print(text)


def wordsInListsCounter(stringList):
    global biggestword  # в питоне можно использовать пременные по ссылке, а не по значению?
    elements = []   # пустой список, где мы "сортируем" слова по величине

    for element in stringList:
        if len(element) >= biggestword:     # проверяем самые большие слова
            biggestword = len(element)
            elements.append(element)    # записываем в список
    return elements


def mostCommonWord(stringList):
    most_common = None  # самое встречающееся слово
    qty_most_common = 0     # сколько раз оно встречалось

    for item in stringList:
        qty = stringList.count(item)    # берем элемент из списка, подсчитываем сколько раз он в списке встречается
        if qty > qty_most_common:   # если 1 э-т больше 0, значит он наиболее встречающийся
            qty_most_common = qty   # для сравнениея с другими э-тами
            most_common = item      # записываем значение в переменную

    return most_common


defpr = wordsInListsCounter(text)
print("Самое динное лово:", defpr[len(defpr) - 1])
defpr = mostCommonWord(text)
print("Наиболее встречающееся слово:", defpr)
