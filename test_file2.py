# Authors: John Hoffman, Rodrigo Chavez, Anahi Barron
# Date: 09/19/2019
# Demonstration of Random

import random
die1 = random.randint(1,6)
print("die:" + str(die1))
die2 = random.randint(1,6)
print("die:" + str(die1))
roll = die1 + die2
print("You rolled:" + str(roll))

print("We are done")