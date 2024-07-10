import pandas as pd
import numpy as np


class Die:
    """
    Represents a die with adjustable faces/weights

    Attributes:
        _faces (numpy.ndarray): an array containing unique face values for the die
        _weights (numpy.ndarray): an array containing weights associated with each face

     Methods:
        __init__(self, faces): initializes a Die object with given faces, and
        checks if input is valid.

        alter_weight(self, face, new_weight): changes the weight of a particular
        face on the die

        roll(self, times=1): rolls the die a specified number of times, returns
        the outcomes

        display_state(self): returns the current state of the die, specifically the
        faces and weights
    """
    def __init__(self, faces):
        """
        Initializes the Die object with given faces.

        Args:
                faces (numpy.ndarray): an array of face values for the die

        Raises:
                TypeError: Faces cannot be converted to a numpy array
                TypeError: Faces do not contain valid data type
                ValueError: Faces do not have distinct values
        """
        if not isinstance(faces, np.ndarray):
            try:
                faces = np.array(faces)
            except Exception as e:
                raise TypeError("Failed to convert faces to a numpy array") from e

        if faces.dtype.kind not in 'SUiu':
            raise TypeError("Invalid dtype for faces")

        if len(faces) != len(np.unique(faces)):
            raise ValueError("Faces must have distinct values")

        self._faces = faces
        self._weights = np.ones_like(faces, dtype=float)

    def alter_weight(self, face, new_weight):
        """
        Alters the weight of a specific face on the die.

        Args:
            face: the face value whose weight needs to be changed
            new_weight: the new weight value for said face

        Raises:
            IndexError: Specified face is not valid
            TypeError: new_weight is not numeric
        """
        if face not in self._faces:
            raise IndexError(f"Face {face} not valid")

        if not isinstance(new_weight, (int, float)):
            raise TypeError("Not a numeric value")

        index = np.where(self._faces == face)[0][0]
        self._weights[index] = new_weight

    def roll(self, times=1):
        """
         Rolls the die a specified number of times

        Args:
            times (int): the number of times to roll the die (default is 1)

        Returns:
            list: a list of outcomes from rolling the die
        """
        die_outcomes = np.random.choice(self._faces, size=times, p=self._weights / np.sum(self._weights))
        return die_outcomes

    def display_state(self):
        """
        Returns the current state of the die

        Returns:
            dict: a dictionary containing the faces/weights of the die
        """
        current_state = {
            'faces': self._faces.tolist(),
            'weights': self._weights.tolist()
        }
        return current_state


class Game:
    """
    Represents a game that involves rolling multiple dice.

    Attributes:
        _dice (list): a list of Die objects to be used in the game
        _results (dict): a dictionary storing results of game plays

    Methods:
        __init__(self, dice): initializes a Game object with a list of Die objects

        play(self, num_rolls): plays the game by rolling dice a specified
        number of times

        show_results(self, format='wide'): returns results of the most recent
        play, in wide or narrow format
    """
    def __init__(self, dice):
        """
        Initializes Game object with a list of Die objects

        Args:
            dice (list): a list of Die objects to be used in the game
        """
        self._dice = dice
        self._results = {}

    def play(self, num_rolls):
        """
        Plays the game by rolling dice a given number of times

        Args:
            num_rolls (int): # of times to roll all dice
        """
        cumulative_results = {}
        for i in range(num_rolls):
            roll_results = []
            for die in self._dice:
                roll_results.append(die.roll())
            cumulative_results[i + 1] = roll_results
        self._results = cumulative_results

    def show_results(self, format='wide'):
        """
        Returns results of the most recent play, in wide or narrow format

        Args:
            format (str): format of the results

        Returns:
            DataFrame or dict: results of most recent play

        Raises:
            ValueError: Invalid format option is provided
        """
        if format == 'wide':
            return self._results
        elif format == 'narrow':
            df = pd.DataFrame(self._results).stack().reset_index()
            df.columns = ['Roll No.', 'Die No.', 'Outcome']
            return df
        else:
            raise ValueError("Invalid format")


class Analyzer:
    """
      Analyzes the results of a game

      Attributes:
          _game (Game): The Game object whose results are being analyzed

      Methods:
          __init__(self, game): initializes an Analyzer object with a Game object

          jackpot(self): counts # of times a jackpot occurred in the game

          roll_face_counts(self): counts how many times each face value was rolled in each play of the game

          combo_count(self): counts distinct combinations of faces rolled in the game

          permutation_count(self): counts distinct permutations of faces rolled in the game
      """

    def __init__(self, game):
        """
        Initializes an Analyzer object with a Game object

        Args:
            game (Game): Game object whose results are being analyzed

        Raises:
            ValueError: Not a valid Game object
        """
        if not isinstance(game, Game):
            raise ValueError("Not a Game object")
        self._game = game

    def jackpot(self):
        """
        Counts # of times a jackpot occurred in the game

        Returns:
            int: # of jackpots
        """
        results = self._game.show_results(format='wide')
        jackpots = 0
        for roll in results.values():
            roll_list = [tuple(item) if isinstance(item, np.ndarray) else item for item in roll]
            if len(set(roll_list)) == 1:
                jackpots += 1
        return jackpots

    def roll_face_counts(self):
        """
        Counts # of times each face value was rolled in each play of the game

        Returns:
        DataFrame: a DataFrame showing the face counts for each roll
        """
        results = self._game.show_results(format='wide')
        face_counts = {}
        for roll_num, roll in results.items():
            roll_list = [tuple(item) if isinstance(item, np.ndarray) else item for item in roll]
            face_counts[roll_num] = {face: roll_list.count(face) for face in set(roll_list)}
        return pd.DataFrame(face_counts).fillna(0)

    def combo_count(self):
        """
        Counts distinct combinations of faces rolled in the game

        Returns:
            DataFrame: a DataFrame with counts of the distinct combinations
        """
        results = self._game.show_results(format='wide')
        combo_counts = {}
        for roll in results.values():
            combo = tuple(sorted(roll))
            if combo not in combo_counts:
                combo_counts[combo] = 0
            combo_counts[combo] += 1
        return pd.DataFrame.from_dict(combo_counts, orient='index', columns=['Count'])

    def permutation_count(self):
        """
        Counts distinct permutations of faces rolled in the game

        Returns:
            DataFrame: a DataFrame with counts of the distinct permutations
        """
        results = self._game.show_results(format='wide')
        perm_counts = {}
        for roll in results.values():
            perm = tuple(roll)
            if perm not in perm_counts:
                perm_counts[perm] = 0
            perm_counts[perm] += 1
        return pd.DataFrame.from_dict(perm_counts, orient='index', columns=['Count'])

