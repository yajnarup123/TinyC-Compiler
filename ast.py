class Node:
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


class Variable(Node):
    def __init__(self, name):
        self.name = name


class BinaryOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Declaration(Node):
    def __init__(self, typ, name, value=None):
        self.typ = typ
        self.name = name
        self.value = value


class Assignment(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value