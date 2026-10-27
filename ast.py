
class Node:
    """Base class for all AST nodes."""
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"


class Variable(Node):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Variable({self.name})"


class BinaryOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinaryOp({self.left}, {self.op}, {self.right})"


class UnaryOp(Node):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

    def __repr__(self):
        return f"UnaryOp({self.op}, {self.operand})"


class Declaration(Node):
    def __init__(self, typ, name, value=None):
        self.typ = typ
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Declaration({self.typ}, {self.name}, {self.value})"


class Assignment(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Assignment({self.name}, {self.value})"
