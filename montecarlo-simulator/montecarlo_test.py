# Testing the code:

import unittest
from montecarlo import Die, Game, Analyzer


class DieTest(unittest.TestCase):

    def test_die_creation(self):
        with open('english_letters.txt', 'r') as file:
            faces = file.read().strip().split()
        die = Die(faces)
        self.assertEqual(die._faces.tolist(), faces)

    def test_die_roll(self):
        with open('english_letters.txt', 'r') as file:
            faces = file.read().strip().split()
        die = Die(faces)
        outcome = die.roll()
        self.assertIn(outcome, faces)

class GameTest(unittest.TestCase):
    class GameTest(unittest.TestCase):

        def setUp(self):
            with open('english_letters.txt', 'r') as file:
                faces1 = file.read().strip().split()
            with open('scrabble_words.txt', 'r') as file:
                outcomes = file.read().strip().split()
            self.dice = [Die(faces1)]
            self.game = Game(self.dice, outcomes=outcomes)

        def test_game_play(self):
            self.game.play(num_rolls=10)
            results = self.game.show_results(format='wide')
            self.assertEqual(len(results), 10)

        def test_game_results_format_narrow(self):
            self.game.play(num_rolls=5)
            df = self.game.show_results(format='narrow')
            self.assertEqual(len(df), 5)


class AnalyzerTest(unittest.TestCase):

    def setUp(self):
        with open('english_letters.txt', 'r') as file:
            faces1 = file.read().strip().split()
        self.dice = [Die(faces1)]
        self.game = Game(self.dice)
        self.analyzer = Analyzer(self.game)

    def test_analyzer_jackpot(self):
        self.game.play(num_rolls=10)
        jackpot_count = self.analyzer.jackpot()
        self.assertGreaterEqual(jackpot_count, 0)

    def test_analyzer_roll_face_counts(self):
        self.game.play(num_rolls=10)
        face_counts_df = self.analyzer.roll_face_counts()
        self.assertEqual(len(face_counts_df.columns), 10)

if __name__ == '__main__':
    unittest.main()
