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






### API description: A list of all classes with their public methods and attributes. Each item should show their docstrings. All parameters (with data types and defaults) should be described. All return values should be described. Do not describe private methods and attributes.
