# DS5100_finalproject2 - ggd8hvd


# Metadata: 

### I'm Georgia Davidson, and my project is the Montecarlo Simulator (under the montecarlo-simulator folder). 


# Synopsis: 

### Clone repository:
##### git clone https://github.com/georgiagrace207/DS5100_finalproject2-ggd8hvd/tree/main/montecarlo-simulator.git
##### cd montecarlo-simulator

### Install and import code:
##### pip install (insert any packages necessary)

### Create dice:     
##### from montecarlo import Die
##### faces = [1, 2, 3, 4, 5, ,6 ]  <-- (insert your own list of numbers (int) or letters (str) inside the brackets) 
##### die = Die(faces)

### Play game: 
##### from montecarlo import Die, Game
##### faces = [1, 2, 3, 4, 5, 6]
##### dice = [Die(faces)]
##### game = Game(dice)
##### game.play(num_rolls=10)
##### results_wide = game.show_results(format='wide')
##### print("Results (wide format):")
##### print(results_wide)
##### results_narrow = game.show_results(format='narrow')
##### print("Results (narrow format):")
##### print(results_narrow)

### Analyze game:
##### from montecarlo import Die, Game, Analyzer
##### faces = [1, 2, 3, 4, 5, 6]
##### dice = [Die(faces)]
##### game = Game(dice)
##### analyzer = Analyzer(game)
##### game.play(num_rolls=10)
##### jackpot_count = analyzer.jackpot()
##### print("Jackpot count:", jackpot_count)
##### face_counts_df = analyzer.roll_face_counts()
##### print("Face counts:")
##### print(face_counts_df)






### API description: 

class Analyzer(builtins.object)
 |  Analyzer(game)
 |
 |  Analyzes the results of a game
 |
 |  Attributes:
 |      _game (Game): The Game object whose results are being analyzed
 |
 |  Methods:
 |      __init__(self, game): initializes an Analyzer object with a Game object
 |                                                                                                                          
 |      jackpot(self): counts # of times a jackpot occurred in the game                                                     
 |                                                                                                                          
 |      roll_face_counts(self): counts how many times each face value was rolled in each play of the game                   
 |                                                                                                                          
 |      combo_count(self): counts distinct combinations of faces rolled in the game                                         
 |                                                                                                                          
 |      permutation_count(self): counts distinct permutations of faces rolled in the game                                   
 |                                                                                                                          
 |  Methods defined here:                                                                                                   
 |                                                                                                                          
 |  __init__(self, game)                                                                                                    
 |      Initializes an Analyzer object with a Game object                                                                   
 |                                                                                                                          
 |      Args:                                                                                                               
 |          game (Game): Game object whose results are being analyzed                                                       
 |                                                                                                                          
 |      Raises:                                                                                                             
 |          ValueError: Not a valid Game object                                                                             
 |                                                                                                                          
 |  combo_count(self)                                                                                                       
 |      Counts distinct combinations of faces rolled in the game                                                            
 |                                                                                                                          
 |      Returns:                                                                                                            
 |          DataFrame: a DataFrame with counts of the distinct combinations                                                 
 |                                                                                                                          
 |  jackpot(self)                                                                                                           
 |      Counts # of times a jackpot occurred in the game                                                                    
 |                                                                                                                          
 |      Returns:                                                                                                            
 |          int: # of jackpots                                                                                              
 |                                                                                                                          
 |  permutation_count(self)                                                                                                 
 |      Counts distinct permutations of faces rolled in the game                                                            
 |                                                                                                                          
 |      Returns:                                                                                                            
 |          DataFrame: a DataFrame with counts of the distinct permutations                                                 
 |                                                                                                                          
 |  roll_face_counts(self)                                                                                                  
 |      Counts # of times each face value was rolled in each play of the game                                               
 |                                                                                                                          
 |      Returns:                                                                                                            
 |      DataFrame: a DataFrame showing the face counts for each roll                                                        
 |                                                                                                                          
 |  ----------------------------------------------------------------------                                                  
 |  Data descriptors defined here:                                                                                          
 |                                                                                                                          
 |  __dict__                                                                                                                
 |      dictionary for instance variables                                                                                   
 |                                                                                                                          
 |  __weakref__                                                                                                             
 |      list of weak references to the object                                                                               

--------------------------------------------------

class Die(builtins.object)
 |  Die(faces)
 |
 |  Represents a die with adjustable faces/weights
 |
 |  Attributes:
 |      _faces (numpy.ndarray): an array containing unique face values for the die
 |      _weights (numpy.ndarray): an array containing weights associated with each face
 |
 |   Methods:
 |      __init__(self, faces): initializes a Die object with given faces, and
 |      checks if input is valid.                                                                                           
 |                                                                                                                          
 |      alter_weight(self, face, new_weight): changes the weight of a particular                                            
 |      face on the die                                                                                                     
 |                                                                                                                          
 |      roll(self, times=1): rolls the die a specified number of times, returns                                             
 |      the outcomes                                                                                                        
 |                                                                                                                          
 |      display_state(self): returns the current state of the die, specifically the                                         
 |      faces and weights                                                                                                   
 |                                                                                                                          
 |  Methods defined here:                                                                                                   
 |                                                                                                                          
 |  __init__(self, faces)                                                                                                   
 |      Initializes the Die object with given faces.                                                                        
 |                                                                                                                          
 |      Args:                                                                                                               
 |              faces (numpy.ndarray): an array of face values for the die                                                  
 |                                                                                                                          
 |      Raises:                                                                                                             
 |              TypeError: Faces cannot be converted to a numpy array                                                       
 |              TypeError: Faces do not contain valid data type                                                             
 |              ValueError: Faces do not have distinct values                                                               
 |                                                                                                                          
 |  alter_weight(self, face, new_weight)                                                                                    
 |      Alters the weight of a specific face on the die.                                                                    
 |                                                                                                                          
 |      Args:                                                                                                               
 |          face: the face value whose weight needs to be changed                                                           
 |          new_weight: the new weight value for said face                                                                  
 |                                                                                                                          
 |      Raises:                                                                                                             
 |          IndexError: Specified face is not valid                                                                         
 |          TypeError: new_weight is not numeric                                                                            
 |                                                                                                                          
 |  display_state(self)                                                                                                     
 |      Returns the current state of the die                                                                                
 |                                                                                                                          
 |      Returns:                                                                                                            
 |          dict: a dictionary containing the faces/weights of the die                                                      
 |                                                                                                                          
 |  roll(self, times=1)                                                                                                     
 |       Rolls the die a specified number of times                                                                          
 |                                                                                                                          
 |      Args:                                                                                                               
 |          times (int): the number of times to roll the die (default is 1)                                                 
 |                                                                                                                          
 |      Returns:                                                                                                            
 |          list: a list of outcomes from rolling the die                                                                   
 |                                                                                                                          
 |  ----------------------------------------------------------------------                                                  
 |  Data descriptors defined here:                                                                                          
 |                                                                                                                          
 |  __dict__                                                                                                                
 |      dictionary for instance variables                                                                                   
 |                                                                                                                          
 |  __weakref__                                                                                                             
 |      list of weak references to the object                                                                               

--------------------------------------------------

class Game(builtins.object)
 |  Game(dice)
 |
 |  Represents a game that involves rolling multiple dice.
 |
 |  Attributes:
 |      _dice (list): a list of Die objects to be used in the game
 |      _results (dict): a dictionary storing results of game plays
 |
 |  Methods:
 |      __init__(self, dice): initializes a Game object with a list of Die objects
 |                                                                                                                          
 |      play(self, num_rolls): plays the game by rolling dice a specified                                                   
 |      number of times                                                                                                     
 |                                                                                                                          
 |      show_results(self, format='wide'): returns results of the most recent                                               
 |      play, in wide or narrow format                                                                                      
 |                                                                                                                          
 |  Methods defined here:                                                                                                   
 |                                                                                                                          
 |  __init__(self, dice)                                                                                                    
 |      Initializes Game object with a list of Die objects                                                                  
 |                                                                                                                          
 |      Args:                                                                                                               
 |          dice (list): a list of Die objects to be used in the game                                                       
 |                                                                                                                          
 |  play(self, num_rolls)                                                                                                   
 |      Plays the game by rolling dice a given number of times                                                              
 |                                                                                                                          
 |      Args:                                                                                                               
 |          num_rolls (int): # of times to roll all dice                                                                    
 |                                                                                                                          
 |  show_results(self, format='wide')                                                                                       
 |      Returns results of the most recent play, in wide or narrow format                                                   
 |                                                                                                                          
 |      Args:                                                                                                               
 |          format (str): format of the results                                                                             
 |                                                                                                                          
 |      Returns:                                                                                                            
 |          DataFrame or dict: results of most recent play                                                                  
 |                                                                                                                          
 |      Raises:                                                                                                             
 |          ValueError: Invalid format option is provided                                                                   
 |                                                                                                                          
 |  ----------------------------------------------------------------------                                                  
 |  Data descriptors defined here:                                                                                          
 |                                                                                                                          
 |  __dict__                                                                                                                
 |      dictionary for instance variables                                                                                   
 |                                                                                                                          
 |  __weakref__                                                                                                             
 |      list of weak references to the object                                                                               

--------------------------------------------------


