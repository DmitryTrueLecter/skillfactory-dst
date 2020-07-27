import numpy as np


# Функция принимает загаданное число и возвращает число попыток
def game_core_bisection(number):
    """
    Используем метод половинного деления
    Для этого берем минимальное и максимальное возможное число.
    Делим отрезок пополам (берем округленное среднее арифетическое)
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

        if number > predict:
            min_possible = predict
        else:
            max_possible = predict

        """
        Если возможные числа различаются на единицу,
        среденеарифметического - всегда одно и тоже число (бесконечный цикл)
        Потому проверяем напрямую
        """
        if max_possible - min_possible == 1:
            if min_possible == number:
                break
            elif max_possible == number:
                # не угадали с min_possible, потому увеличиваем число попыток
                count += 1
                break
            else:
                # если оба числа неверные, значит ошибка в алгоритме
                raise Exception(f"The algorithm can't guess '{number}'")

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
