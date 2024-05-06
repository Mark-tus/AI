#1) Write a program to implement Hill Climbing Algorithm
import random

adj = [
[0, 10, 15, 20],
[10, 0, 35, 25],
[15, 35, 0, 30],
[20, 25, 30, 0]
]

def cal_dist(path):
total = 0
for i in range(len(path)-1):
total += adj[path[i]][path[i+1]]
total += adj[path[-1]][path[0]]
return total

def hill_climb(no):
curr_path = list(range(no))
curr_dist = cal_dist(curr_path)
for _ in range(10000):
new_path = curr_path.copy()
i, j = random.sample(range(no), 2)
new_path[i], new_path[j] = new_path[j], new_path[i]
new_dist = cal_dist(new_path)
if new_dist < curr_dist:
curr_path = new_path
curr_dist = new_dist
return curr_path

def main():
solution = hill_climb(4)
print("Best Path is ", solution)
print("Total Distance is ", cal_dist(solution))

if __name__ == "__main__":
main()
