

from ast import Declaration, Assignment
from errors import ParserError


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def advance(self):
        token = self.current()
        self.pos += 1
        return token

    def expect(self, value):
        if self.current() != value:
            raise ParserError(
                f"Expected '{value}', got '{self.current()}'"
            )
        self.advance()

    def read_expression(self):
        expression = []
        depth = 0

        while self.current() is not None:
            token = self.current()

            if token == "(":
                depth += 1
            elif token == ")":
                if depth == 0:
                    break
                depth -= 1
            elif token == ";" and depth == 0:
                break

            expression.append(self.advance())

        if not expression or depth != 0:
            raise ParserError("Invalid or incomplete expression")

        return " ".join(expression)

    def parse(self):
        program = []

        while self.current() is not None:
            typ = self.current()

            if typ in ("int", "float"):
                self.advance()

                name = self.current()
                if name is None or not name.isidentifier():
                    raise ParserError("Expected a variable name")
                self.advance()

                value = None
                if self.current() == "=":
                    self.advance()
                    value = self.read_expression()

                self.expect(";")
                program.append(Declaration(typ, name, value))

            else:
                name = self.current()

                if name is None or not name.isidentifier():
                    raise ParserError(
                        f"Unexpected token: {name}"
                    )

                self.advance()
                self.expect("=")
                value = self.read_expression()
                self.expect(";")

                program.append(Assignment(name, value))

        return program


def parser(tokens):
    return Parser(tokens).parse()
