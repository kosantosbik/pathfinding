class Node():
    """
    Every instance represents a node in the grid.
    1 -> Obstacle | 0 -> Path
    """

    def __init__(self,
                 parent=None,
                 x=0,
                 y=0,
                 g=0,
                 h=0,
                 f=0):

        self.parent = parent
        self.x = x
        self.y = y

        self.g = g
        self.h = h
        self.f = f
