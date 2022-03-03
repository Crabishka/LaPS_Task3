import unittest

from main import choose_sweet


class Test(unittest.TestCase):

    def test_casual_case_1_func(self):
        test_dictionary = {'Ромашки': 350,
                           'Раф': 150,
                           'Чайные': 800,
                           'С ликером': 120,
                           'Антон': 10}
        money = 1080
        test_result = choose_sweet(test_dictionary, money)
        test_result.sort()
        test_answer = ['Раф', 'Антон', 'С ликером', 'Чайные']
        test_answer.sort()
        self.assertEqual(test_result, test_answer)

    def test_casual_case_2_func(self):
        test_dictionary = {'Ромашки': 350,
                           'Раф': 150}
        money = 0
        test_result = choose_sweet(test_dictionary, money)
        test_result.sort()
        test_answer = []
        test_answer.sort()
        self.assertEqual(test_result, test_answer)

    def test_casual_case_3_func(self):
        test_dictionary = {}
        money = 1000000000000
        test_result = choose_sweet(test_dictionary, money)
        test_result.sort()
        test_answer = []
        test_answer.sort()
        self.assertEqual(test_result, test_answer)

    def test_casual_case_4_func(self):
        test_dictionary = {'Ромашки': 350,
                           'Раф': 150,
                           'Чайные': 800,
                           'С ликером': 120,
                           'Антон': 10,
                           '3 Медведя': 350,
                           'Степ': 190,
                           'Крокант': 810,
                           'Нюша': 1200,
                           'АаАаА': 1000
                           }
        money = 1000000000000
        test_result = choose_sweet(test_dictionary, money)
        test_result.sort()
        test_answer = ['Ромашки', 'Раф', 'Чайные', 'С ликером',
                       'Антон', '3 Медведя', 'Степ', 'Крокант',
                       'Нюша', 'АаАаА']
        test_answer.sort()
        self.assertEqual(test_result, test_answer)

    def test_casual_case_5_func(self):
        test_dictionary = {'Ромашки': 350,
                           'Раф': 150,
                           'Чайные': 800,
                           'С ликером': 120,
                           'Антон': 10,
                           '3 Медведя': 360,
                           'Степ': 190,
                           'Крокант': 810,
                           'Нюша': 1200,
                           'АаАаА': 1000
                           }
        money = 1000
        test_result = choose_sweet(test_dictionary, money)
        test_result.sort()
        test_answer = ['3 Медведя', 'Антон', 'Раф', 'С ликером', 'Степ']
        test_answer.sort()
        self.assertEqual(test_result, test_answer)

    def test_casual_case_6_func(self):
        test_dictionary = {'Ромашки': 350,
                           'Раф': 150}
        money = 160
        test_result = choose_sweet(test_dictionary, money)
        test_result.sort()
        test_answer = ['Раф']
        test_answer.sort()
        self.assertEqual(test_result, test_answer)