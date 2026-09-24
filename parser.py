from ast import Declaration, Assignment

def parser(tokens):
    program = []
    i = 0

    while i < len(tokens):
        if tokens[i] in ("int", "float"):
            typ = tokens[i]
            name = tokens[i + 1]

            if i + 2 < len(tokens) and tokens[i + 2] == "=":
                value = tokens[i + 3]
                program.append(Declaration(typ, name, value))
                i += 5
            else:
                program.append(Declaration(typ, name))
                i += 3

        elif tokens[i] == ";":
            i += 1

        else:
            name = tokens[i]
            i += 2
            value = []

            while i < len(tokens) and tokens[i] != ";":
                value.append(tokens[i])
                i += 1

            program.append(Assignment(name, " ".join(value)))
            i += 1

    return program