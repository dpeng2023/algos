"""

    ALGO - MAP-DICT:
    - Given directed connection node pairs
    - Create origin node list each with list of any connected nodes regardless of direction

    SAMPLE INPUT:
    - emp_input list of strings with names, departments, ids
    to create a master emp_ids list
    [1,2,3,4,5,6,7,8]
    - directed connection node pairs of real_friends
    [1,2]
    [2,1]
    [3,4]
    [3,6]
    [4,5]
    [5,4]
    [7,6]

    EXPECTED OUTPUT:  emp_friends
    1:[2]
    2:[1]
    3:[4,6]
    4:[3,5]
    5:[4]
    6:[3,7]
    7:[6]
    8:[]

"""


def load_emp_ids(empinput):
    master_emp = {}
    for empInfo in empinput:
        emp_id, name, dept = empInfo.split(",")
        # force type for later reference
        # BUGFIX change from List to Set type to remove duplicates
        # master_emp[int(emp_id)] = []
        master_emp[int(emp_id)] = set()
    return master_emp

def load_directed_friendships(master_emp, directed_friendships, isLtoR):
    for pair in directed_friendships:
        if isLtoR:
            fromNode, toNode = pair[0], pair[1]
        else:
            toNode, fromNode = pair[0], pair[1]
        # BUGFIX change from List to Set type to remove duplicates
        # master_emp[fromNode].append(toNode)
        master_emp[fromNode].add(toNode)
    return master_emp

# ********************* SHELL TESTING ************************

emp_input = [
    "1, Ray, Engr",
    "2, Emily, HR",
    "3, Alice, Engr",
    "4, Donald, Executive",
    "5, Ryan, Engr",
    "6, Rick, HR",
    "7, Angie, Executive",
    "8, Bozo, Marketing"
]

friends_input = [
    (1,2),
    (2,1),
    (3,4),
    (3,6),
    (4,5),
    (5,4),
    (7,6)
]

master_emp = load_emp_ids(emp_input)
print("***TEST1 Loaded master_emp is:  ")
print(master_emp)
print("First initialized emp_friends list and type is:  ")
print(master_emp[1])
print(type(master_emp[1]))

master_emp = load_directed_friendships(master_emp, friends_input, True)
print("\n***TEST2 AFTER loading From To relation, Loaded master_emp is:  ")
print(master_emp)

master_emp = load_directed_friendships(master_emp, friends_input, False)
print("\n***TEST3 AFTER loading fromTo toFrom relation, Loaded master_emp is:  ")
print(master_emp)

