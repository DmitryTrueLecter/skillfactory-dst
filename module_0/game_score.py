import numpy as np


# Функция принимает загаданное число и возвращает число попыток
def game_core_bisection(number):
    """
    Используем метод половинного деления
    Для этого берем минимальное и максимальное возможное число.
    Делим этот отрезок пополам (берем округленное среднее арифетическое)
    Если данная точка - это загаданное число, то выходим из функции
    Иначе повторяем поиск в той половине отрезка,
    в которой находится загаданное число
    """
    count = 1
    min_possible = 1
    max_possible = 100
    predict = 50

    while number != predict:
        count += 1

        """
        Если мы попали в ситуацию, когда возможные числа различаются
        на единицу, то среднеарифметическое считать нельзя,
        так как округляя его до целого мы будем всегда получать
        одно и тоже число (то есть попадем в бесконечный цикл).
        При этом только что проверенный predict - это одно из двух этих чисел
        И поскольку мы используем деление без остатка, то это меньшее число
        следовательно загаднное число - это максимальное из этих двух
        """
        if max_possible - min_possible == 1:
            predict = max_possible
        else:
            if number > predict:
                min_possible = predict
            elif number < predict:
                max_possible = predict

            predict = (min_possible + max_possible) // 2

    return count  # выход из цикла, если угадали


# Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
def score_game(game_core):
    count_ls = []

    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# запускаем
score_game(game_core_bisection)
