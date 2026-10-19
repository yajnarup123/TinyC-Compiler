
from ast import Declaration, Assignment


def parser(tokens):
    program = []
    i = 0

    def error():
        raise SyntaxError(
            f"Invalid syntax near token: {tokens[i] if i < len(tokens) else 'end of input'}"
        )

    def read_expression():
        nonlocal i
        expr = []

        while i < len(tokens) and tokens[i] != ";":
            if tokens[i] == "=":
                error()
            expr.append(tokens[i])
            i += 1

        if not expr:
            error()

        return " ".join(expr)

    while i < len(tokens):
        if tokens[i] in ("int", "float"):
            typ = tokens[i]
            i += 1

            if i >= len(tokens):
                error()

            name = tokens[i]
            if not name.isidentifier():
                error()
            i += 1

            value = None

            if i < len(tokens) and tokens[i] == "=":
                i += 1
                value = read_expression()

            if i >= len(tokens) or tokens[i] != ";":
                error()

            i += 1
            program.append(Declaration(typ, name, value))

        else:
            name = tokens[i]

            if not name.isidentifier():
                error()
            i += 1

            if i >= len(tokens) or tokens[i] != "=":
                error()
            i += 1

            value = read_expression()

            if i >= len(tokens) or tokens[i] != ";":
                error()

            i += 1
            program.append(Assignment(name, value))

    return program
