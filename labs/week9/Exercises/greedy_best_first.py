class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, heuristic=0, parent=None, depth=0):
        self.STATE = state
        self.HEURISTIC = heuristic
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.PATH_COST = 0

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
    initial_node = Node(INITIAL_STATE)
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
        s.STATE = child[0][0]  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.HEURISTIC = child[0][1]
        s.PATH_COST = node.PATH_COST + child[1] 
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
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
        if item.HEURISTIC < lowest_element.HEURISTIC:
            lowest_element = item
    queue.remove(lowest_element)
    return lowest_element

'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]


INITIAL_STATE = 'A'  # STATE are represented with: (("STATE", heuristic), path cost) GOAL_STATES = ('K', 'L') 
GOAL_STATES = ['K', 'L']

STATE_SPACE = {
        'A': [[('B', 5), 1], [('C', 5), 2], [('D', 2), 4]],
        'B': [[('F', 5), 5], [('E', 4), 1]],
        'C': [[('E', 4), 1]],
        'D': [[('H', 1), 1], [('I', 2), 4], [('J', 1), 2]],
        'F': [[('G', 4), 1]],
        'E': [[('G', 4), 2], [('H', 1), 3]],
        'I': [[('L', 0), 3]],
        'J': [],
        'G': [[('K', 0), 6]],
        'H': [[('K',0), 6], [('L',0), 5]]
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
