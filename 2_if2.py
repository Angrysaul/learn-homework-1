# ""

# Домашнее задание №1

# Условный оператор: Сравнение строк

# * Написать функцию, которая принимает на вход две строки
# * Проверить, является ли то, что передано функции, строками. 
#   Если нет - вернуть 0
# * Если строки одинаковые, вернуть 1
# * Если строки разные и первая длиннее, вернуть 2
# * Если строки разные и вторая строка 'learn', возвращает 3
# * Вызвать функцию несколько раз, передавая ей разные праметры 
#   и выводя на экран результаты

# """



def slovo(stroka_1, stroka_2):
  print(stroka_1, stroka_2)
  if ((type(stroka_1)!=str) or (type(stroka_2)!=str)):
    return "0"
  elif (len(stroka_1) == len(stroka_2)):
    return "1"
  elif (len(stroka_1) > len(stroka_2)):
    return "2"
  elif (len(stroka_1) < len(stroka_2)):
    return "3"
  else:
    return "4"

    
# stroka_1 = input("Введите несколько слов: ")
stroka_1 = 'text'
# stroka_2 = input("Еще раз введите несколько слов : ")
stroka_2 = 'text 2'
result = slovo(stroka_1, stroka_2)
print(result)

# if __name__ == "__main__":
#     main()
