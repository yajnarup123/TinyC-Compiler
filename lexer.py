import re
from errors import LexerError

KEYWORDS = {"int", "float", "return"}

def lexer(code):
    pattern = r'\d+(?:\.\d+)?|[A-Za-z_]\w*|[=+*;(){}]'
    tokens = re.findall(pattern, code)

    for token in tokens:
        if not re.match(r'\d+(?:\.\d+)?$|[A-Za-z_]\w*$', token) and token not in "=+*;(){}":
            raise LexerError(f"Invalid token: {token}")

    return tokens