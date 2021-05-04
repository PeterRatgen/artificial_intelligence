# Questions on adversarial search

  - What is the branching factor at depth 0? At depth 1?
    - Depth 0 is topmost level. Here there is 9 empty fields, thus we have 9
      possible placments. At level 1 we have already placed 1, therefore there
      is 8 fields left (thus we have a branching factor of 8).
  - What is the maximal depth?
    - The maximal depth is 8. 
  - Will a MIN move attempt to minimize or maximize the utility?
    - For the MIN player, we want to minimize the utility function. 
  - Are states after a terminal stateexplored?
    - There are no states after a terminal state, so no.
  - Are all possible states explored to a terminal state?
    - This depends on if you are using alpha-beta pruning of the search tree. If
      using a naiive minimax algorithm exploring every node.
  - Is this a depth-first or breadth-first search? How do 
    you know? (see Python code)
    - The minimax algorithm is based on depth-first. For each move one decision
      is picked, going a level deeper.
