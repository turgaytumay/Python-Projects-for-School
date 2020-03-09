import random
import copy
parent = [[],[],[]]
numbers = [0,1,2,3,4,5,6,7,8]
path = [[["right" ,"down"],["left","right" ,"down"],["left" ,"down"]],[["up","right" ,"down"],["up","left","right" ,"down"],["up","left" ,"down"]],[["right" ,"up"],["left","right" ,"up"],["left" ,"up"]]]

# Generating random 3x3 puzzle

while numbers:
    if len(numbers) > 6:
        for i in range(3):
            cuka = random.choice(numbers)
            numbers.remove(cuka)
            parent[0].append(cuka)
        continue
    elif len(numbers) > 3:
        for i in range(3):
            cuka = random.choice(numbers)
            numbers.remove(cuka)
            parent[1].append(cuka)
        continue
    else:
        for i in range(3):
            cuka = random.choice(numbers)
            numbers.remove(cuka)
            parent[2].append(cuka)
        break

# rotating 0 to corners

while True:

    zero = []
    for i in range(3):
        for j in range(3):
            if parent[i][j] == 0:
                zero.append(i)
                zero.append(j)
    path_a = zero[0]
    path_b = zero[1]

    if parent[0][1] == parent[path_a][path_b] or parent[1][0] == parent[path_a][path_b] or parent[1][1] == parent[path_a][path_b] or parent[1][2] == parent[path_a][path_b] or parent[2][1] == parent[path_a][path_b]:
        placement = [[0,0],[0,2],[2,0],[2,2]]
        change = random.choice(placement)
        change_path_a = change[0]
        change_path_b = change[1]
        parent[path_a][path_b] = parent[change_path_a][change_path_b]
        parent[change_path_a][change_path_b] = 0
        break
    else:
        break

print("---------------")
print("--First State--")
for i in range(3):
    print (parent[i])
print("---------------")


def expand(parent):

    # catching to 0 form list

    zero = []
    for i in range(len(parent)):
        for j in range(3):
            if parent[i][j] == 0:
                zero.append(i)
                zero.append(j)

    path_a = zero[0]
    path_b = zero[1]

    list_for_left = copy.deepcopy(parent)
    list_for_right = copy.deepcopy(parent)
    list_for_up = copy.deepcopy(parent)
    list_for_down = copy.deepcopy(parent)

    successor = []

    # Creating path from parent list

    for i in path[path_a][path_b]:
        while True:
            if i == "right":
                list_for_right[path_a][path_b] = list_for_right[path_a][path_b + 1]
                list_for_right[path_a][path_b + 1] = 0
                successor.append(list_for_right)
                break
            elif i == "left":
                list_for_left[path_a][path_b] = list_for_left[path_a][path_b - 1]
                list_for_left[path_a][path_b - 1] = 0
                successor.append(list_for_left)
                break
            elif i == "up":
                list_for_up[path_a][path_b] = list_for_up[path_a - 1][path_b]
                list_for_up[path_a - 1][path_b] = 0
                successor.append(list_for_up)
                break
            elif i == "down":
                list_for_down[path_a][path_b] = list_for_down[path_a + 1][path_b]
                list_for_down[path_a + 1][path_b] = 0
                successor.append(list_for_down)
                break
    return successor

print("--------------")
print("Expanded State")
initial_state = expand(parent)
for i in range(len(initial_state)):
     for j in range(3):
         print(initial_state[i][j])
     print(" ")
print("--------------")

def graph_search(initial_state):

    # catching the goal state from successor list

    road_to_goal_a = expand(initial_state[0])
    road_to_goal_b = expand(initial_state[1])

    goal_path_a = []
    goal_path_b = []

    for i in range(3):
        if road_to_goal_a[i][1][1] == 0:
            goal_path_a.append(i)
        elif road_to_goal_b[i][1][1] == 0:
            goal_path_b.append(i)

    path_a = goal_path_a[0]
    path_b = goal_path_b[0]


    goal = [road_to_goal_a[path_a],road_to_goal_b[path_b]]

    return goal
goal = graph_search(initial_state)

print("--------------")
print("--Goal State--")
for i in range(2):
    for j in range(3):
        print(goal[i][j])
    print(" ")
print("--------------")
