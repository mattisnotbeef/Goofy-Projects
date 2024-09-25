#This script randomly chooses a movie from The Fast and the Furious franchise
fast_movies = ["the_fast_and_the_furious" , "2_fast_2_furious" , "fast_and_furious_tokyo_drift" , "fast_&_furious" , "fast_five" , "fast_six" , "fast_seven" , "f8_of_the_furious" , "hobbs_and_shaw" , "fast_nine" , "fast_X"]

import random

while True:
  x = int(input('Press 1 to roll the Fast dice or 0 to quit the program!\n'))
  if x == 1:
    print(random.choice(fast_movies))
  if x == 0:
    print('Goodbye!')
    break
