# Задача 12: Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


def FindNumber(comp, summ: int):
    for i in range(0,summ):
        for j in range(0,summ):
            if i * j == comp and i+j == summ:
                return f'Первое число {i}, второе число {j}'

comp = int(input('Введите произведение загаданных чисел: '))
summ = int(input('Введите сумму загаданных чисел: '))
print(FindNumber(comp,summ)) #Вводим произведение и сумму чисел