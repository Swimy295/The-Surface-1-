#Name: Swayem
#Start Date: December 7, 2022
#Program Name: The Surface
#Purpose: Opposite to the ASCII art game "The Cave", it will be a zelda type of game with abilities, save system, enemies, etc.

import start as s, time

s.main_menu()

while True:
  if s.intro == 0:
    time.sleep(1)
  else:
    print('s')
    break