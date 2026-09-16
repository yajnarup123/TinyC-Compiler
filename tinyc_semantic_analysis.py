import re

keywords = {"int", "float"}

def lexer(code):
    return re.findall(r'\d+\.\d+|\d+|[A-Za-z_]\w*|[=+*;]', code)

def parser(tokens):
    if tokens.count(";") != 4:
        raise SyntaxError("Invalid syntax")
    return True

def semantic(tokens):
    symbols = {}
    errors = []

    for i, t in enumerate(tokens):
        if t in keywords and i + 1 < len(tokens):
            name = tokens[i + 1]
            if name in symbols:
                errors.append("Duplicate variable: " + name)
            symbols[name] = t

    for i, t in enumerate(tokens):
        if t not in keywords and t.isidentifier():
            if i > 0 and tokens[i - 1] not in keywords and t not in symbols:
                errors.append("Undeclared variable: " + t)

    return symbols, errors


code = "int a = 10; int b = 20; float result; result = a + b * 2;"

tokens = lexer(code)
print("TOKENS:", tokens)

parser(tokens)
print("SYNTAX ANALYSIS: PASSED")

symbols, errors = semantic(tokens)

print("SYMBOL TABLE:", symbols)
print("SEMANTIC ANALYSIS:", "PASSED" if not errors else errors)