import src.core as core
from dataclasses import dataclass
from operator import attrgetter

@dataclass
class NodeFlags:
    update : bool = True
    propagate : bool = True
    debug : bool = False

class Node:
    def __init__(self, context : core.Context):
        self.context = context 
        self.children = []
        self.order = 0
        self.flags = NodeFlags()

    def update(self):
        pass 

    def update_all(self):
        if self.flags.update:
            self.update()
        if self.flags.propagate:
            for child in sorted(self.children, key = attrgetter("order")):
                    child.update_all()

    def attach(self, node):
        self.children.append(node) 

