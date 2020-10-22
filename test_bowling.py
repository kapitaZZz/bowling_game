# -*- coding: utf-8 -*-

import unittest

from lesson_014 import score


class MySortTest(unittest.TestCase):

    def test_space(self):
        self.assertRaises(score.SpaceError, score.get_score, '                ')

    def test_empty(self):
        self.assertRaises(score.EmptyDataError, score.get_score, '')

    def test_length(self):
        self.assertRaises(score.LengthError, score.get_score, '1234574844564213281231385854')

    def test_strike(self):
        self.assertRaises(score.SymbolError, score.get_score, 'FAF13521348')

    def test_symbol(self):
        self.assertRaises(score.SymbolError, score.get_score, '!@#{}[]()"?:^№$%^&*')

    def test_slash(self):
        self.assertRaises(score.WrongDataError, score.get_score, '/1/1/1/1/1/1/1/1/1/1')

    def test_frames(self):
        self.assertRaises(score.LengthError, score.get_score, '12345678')

    def test_wrong_strike(self):
        self.assertRaises(score.WrongDataError, score.get_score, '1X1X1X1X1X1X1X')

    def test_second_param(self):
        self.assertRaises(score.WrongDataError, score.get_score, '11' * 9 + '55')

    def test_throws(self):
        self.assertRaises(score.LimitFramesError, score.get_score, '--' * 9)

    def test_valid_1(self):
        incoming_data = 'X324/--234/X2-9-34'
        self.assertIs(score.get_score(incoming_data), 98)

    def test_valid_2(self):
        incoming_data = '11' * 9 + 'X'
        self.assertIs(score.get_score(incoming_data), 38)

    def test_valid_3(self):
        incoming_data = '11' * 9 + '-/'
        self.assertIs(score.get_score(incoming_data), 33)

    def test_valid_4(self):
        incoming_data = '--' * 9 + '-/'
        self.assertIs(score.get_score(incoming_data), 15)


if __name__ == '__main__':
    MySortTest()
