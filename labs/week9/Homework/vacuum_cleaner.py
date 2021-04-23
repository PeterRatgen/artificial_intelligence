
class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, heuristic=0, path_cost=0,parent=None, depth=0):
        self.STATE = state
        self.HEURISTIC = heuristic
        self.PATH_COST = path_cost
        self.PARENT_NODE = parent
        self.DEPTH = depth

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH) + ' - Heuristic: ' + str(self.HEURISTIC) + ' - Path cost ' + str(self.PATH_COST)

'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE, STATE_MAP[INITIAL_STATE].get("heuristic"))
    expanded_nodes = 0
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_FIRST(fringe)
        if node.STATE in GOAL_STATES:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))
        expanded_nodes += 1
        print("Expanded notes:" + str(expanded_nodes))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''

def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.HEURISTIC = STATE_MAP[child]["heuristic"]
        s.PATH_COST = node.PATH_COST + 1
        s.PARENT_NODE = node
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
   queue.append(node)
   return queue
    


'''
    Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for item in list:
        queue.append(item)
    return queue


'''
Removes and returns the best element from fringe
'''
def REMOVE_FIRST(queue):
    lowest_element = queue[0]
    for item in queue:
        if evaluation_function(item) < evaluation_function(lowest_element):
            lowest_element = item
    queue.remove(lowest_element)
    return lowest_element

def evaluation_function (node):
    return node.HEURISTIC + node.PATH_COST


'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state[0]]

# 0 = left, 1 = right
# STATE are represented with: 
# [placement, [l_state, r_state], cost]
INITIAL_STATE = "A"
GOAL_STATES = ["D", "H"]

STATE_SPACE = {
    "A" : ["A", "B", "E"],
    "B" : ["B", "C"],
    "C" : ["B", "C", "D"],
    "D" : ["D", "H"], 
    "E" : ["A", "E", "F"],
    "F" : ["F", "G"],
    "G" : ["F", "G", "H"],
    "H" : ["H" "D"]
}

STATE_MAP = {
    "A" : {
            "placement_state" : 0,
            "clean_state" :["dirty", "dirty"],
            "heuristic" : 3
        },
    "B" : {
            "placement_state" : 0,
            "clean_state" :["clean", "dirty"],
            "heuristic" : 2
        },
    "C" : {
            "placement_state" : 1,
            "clean_state" :["clean", "dirty"],
            "heuristic" : 1
        },
    "D" : {
            "placement_state" : 1,
            "clean_state" :["clean", "clean"],
            "heuristic" : 0
        },
    "E" : {
            "placement_state" : 1,
            "clean_state" :["dirty", "dirty"],
            "heuristic" : 3
        },
    "F" : {
            "placement_state" : 1,
            "clean_state" :["dirty", "clean"],
            "heuristic" : 2
        },

    "G" : {
            "placement_state" : 0,
            "clean_state" :["dirty", "clean"],
            "heuristic" : 1
        },
    "H" : {
            "placement_state" : 0,
            "clean_state" :["clean", "clean"],
            "heuristic" : 0
        }
}


'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
