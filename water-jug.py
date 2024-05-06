#Write a program to solve water jug problem.

jug_capacity_1, jug_capacity_2, target_aim = 4, 3, 2

visited_states = set()

def waterJugSolver(jug1_level, jug2_level):
 if (jug1_level == target_aim and jug2_level == 0) or (jug2_level ==
target_aim and jug1_level == 0):
   print(jug1_level, jug2_level)
   return True
 if (jug1_level, jug2_level) not in visited_states:
  print(jug1_level, jug2_level)
  visited_states.add((jug1_level, jug2_level))
  
  # List of all possible next states
  next_states = [
   (0, jug2_level), # Pour all water from jug 1
   (jug1_level, 0), # Pour all water from jug 2
   (jug_capacity_1, jug2_level), # Fill jug 1 to capacity
   (jug1_level, jug_capacity_2), # Fill jug 2 to capacity
   (jug1_level + min(jug2_level, jug_capacity_1 - jug1_level),
jug2_level - \
   min(jug2_level, jug_capacity_1 - jug1_level)), # Pour from jug 2 to
jug 1
   (jug1_level - min(jug1_level, jug_capacity_2 - jug2_level),
jug2_level + \
   min(jug1_level, jug_capacity_2 - jug2_level)) # Pour from jug 1 to
jug 2
 ]

  # Recursive call for each next state
  for state in next_states:
   if waterJugSolver(*state):
    return True

 return False

print("Steps: ")
waterJugSolver(0, 0)
