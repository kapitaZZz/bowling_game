# -*- coding: utf-8 -*-

# Вас взяли на работу в молодой стартап. Идея стартапа - предоставлять сервис расчета результатов игр.
# Начать решили с боулинга, упрощенной версии.
#
# Правила такие.
#
# Всего 10 кеглей. Игра состоит из 10 фреймов. В одном фрейме до 2х бросков, цель - сбить все кегли.
# Результаты фрейма записываются символами:
#   «Х» – «strike», все 10 кеглей сбиты первым броском
#   «<число>/», например «4/» - «spare», в первый бросок сбиты 4 кегли, во второй – остальные
#   «<число><число>», например, «34» – в первый бросок сбито 3, во второй – 4 кегли.
#   вместо <число> может стоять прочерк «-», например «-4» - ни одной кегли не было сбито за первый бросок
# Результат игры – строка с записью результатов фреймов. Символов-разделителей между фреймами нет.
# Например, для игры из 3 фреймов запись результатов может выглядеть так:
#   «Х4/34-4»
# Предлагается упрощенный способ подсчета количества очков:
#   «Х» – 20 очков, «4/» - 15 очков, «34» – сумма 3+4=7, «-4» - сумма 0+4=4
# То есть для игры «Х4/34» сумма очков равна 20+15+7+4=46
#
# Надо написать python-модуль (назвать bowling), предоставляющий API расчета количества очков:
# функцию get_score, принимающую параметр game_result. Функция должна выбрасывать исключения,
# когда game_result содержит некорректные данные. Использовать стандартные исключения по максимуму,
# если не хватает - создать свои.
#
# Обязательно написать тесты на этот модуль. Расположить в папке tests.

# Из текущего файла сделать консольную утилиту для определения количества очков, с помощью пакета argparse
# Скрипт должен принимать параметр --result и печатать на консоль:
#   Количество очков для результатов ХХХ - УУУ.
import argparse


class BowlingException(Exception):
    def __str__(self):
        return 'Проверьте параметр ввода!'


class StrikeError(BowlingException):
    def __str__(self):
        return 'Неверный символ ввода'


class NumberError(BowlingException):
    def __str__(self):
        return 'Неверное число'


class SymbolError(BowlingException):
    def __str__(self):
        return 'Некорректный символ'


class LengthError(BowlingException):
    def __str__(self):
        return 'Недопустимый размер входных данных'


class SpaceError(BowlingException):
    def __str__(self):
        return 'Пробел недопустим для ввода'


class WrongDataError(BowlingException):
    def __str__(self):
        return 'Неверные данные для обработки'


class LimitFramesError(BowlingException):
    def __str__(self):
        return 'Ошибка количества бросков'


class EmptyDataError(BowlingException):
    def __str__(self):
        return 'Нет данных для обработки'


def get_score(game_result):
    score = 0
    a = 0
    throws = 0
    skittle = 10
    game_result = str(game_result)
    if game_result == '':
        raise EmptyDataError
    elif len(game_result) > 20 or len(game_result) < 10:
        raise LengthError
    elif ' ' in game_result:
        raise SpaceError
    for char in game_result:
        throws += 1
        if char == 'X' or char == 'Х' or char.isdigit() or char == '/' or char == '-':
            if char == 'X' or char == 'Х':
                if throws % 2 == 0:
                    raise WrongDataError
                score += 20
                throws += 1
            elif char.isdigit():
                if throws % 2 == 0:
                    if skittle - a < 0:
                        skittle = 0
                    else:
                        score += int(char)

                    if char != '/' and skittle == 0:
                        raise WrongDataError
                else:
                    score += int(char)
                    a = int(char)
                    skittle -= int(char)
            elif char == '/':
                if throws % 2 != 0:
                    raise WrongDataError
                score += (15 - a)
                skittle = 10
            elif char == '-':
                skittle = 10
                score += 0
                a = 0
        else:
            raise SymbolError

    if throws != 20:
        raise LimitFramesError

    return score


if __name__ == '__main__':
    game_result = '--'*9 + '7'
    print(get_score(game_result))
# зачет!
