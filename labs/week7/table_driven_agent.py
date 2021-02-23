A = 'A'
B = 'B'
percepts = []
table = {
        ((A, 'Clean'),) : 'Right',
        ((A, 'Dirty'),) : 'Such',
        ((B, 'Clean'),) : 'Left',
        ((B, 'Dirty'),) : 'Suck',
        ((A, 'Clean'), (A, 'Clean')) : 'Right',
        ((A, 'Clean'), (A, 'Dirty')) : 'Suck',
        ((A, 'Dirty'), (A, 'Dirty')) : 'Suck',
        ((B, 'Clean'), (B, 'Clean')) : 'Left',
        ((B, 'Clean'), (B, 'Dirty')) : 'Suck',
        ((B, 'Dirty'), (B, 'Dirty')) : 'Suck',
        ((A, 'Clean'), (A, 'Clean'), (A, 'Clean')) : 'Right',
        ((A, 'Clean'), (A, 'Clean'), (A, 'Dirty')) : 'Suck',
        ((A, 'Clean'), (A, 'Clean'), (B, 'Clean')) : 'Left',
        ((B, 'Clean'), (B, 'Clean'), (B, 'Clean')) : 'Right',
        ((B, 'Clean'), (B, 'Clean'), (B, 'Dirty')) : 'Suck',
        ((B, 'Clean'), (B, 'Clean'), (A, 'Clean')) : 'Left',
        }

def LOOKUP(percepts, table):
    action = table.get(tuple(percepts))
    return action

def TABLE_DRIVEN_AGENT(percept):
    percepts.append(percept)
    action = LOOKUP(percepts, table)
    return action 

def run():
    print('Action\tPercepts')
    print(TABLE_DRIVEN_AGENT((A, 'Clean')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((A, 'Dirty')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((B, 'Clean')), '\t', percepts)

run()
