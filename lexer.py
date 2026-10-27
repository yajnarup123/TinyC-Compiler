
import re
from errors import LexerError

KEYWORDS = {
    # Data types
    "int", "float", "double", "char", "void",
    "short", "long", "signed", "unsigned",
    "_Bool",

    # Control statements
    "if", "else", "switch", "case", "default",
    "break", "continue", "goto",

    # Loops
    "for", "while", "do",

    # Functions and return
    "return", "sizeof",

    # Storage classes
    "auto", "static", "extern", "register",
    "typedef",

    # Type qualifiers
    "const", "volatile", "restrict",

    # User-defined types
    "struct", "union", "enum",

    # Other C keywords
    "inline", "_Alignas", "_Alignof",
    "_Atomic", "_Complex", "_Generic",
    "_Imaginary", "_Noreturn", "_Static_assert",
    "_Thread_local"
}

OPERATORS = {
    "+", "-", "*", "/", "%",
    "=", "==", "!=", "<", ">",
    "<=", ">=", "&&", "||", "!",
    "++", "--", "+=", "-=", "*=", "/=",
    "&", "|", "^", "~", "<<", ">>",
    "->", ".", "?"
}

PUNCTUATION = {
    "(", ")", "{", "}", "[", "]",
    ";", ",", ":"
}


def lexer(code):
    pattern = (
        r'"(?:\\.|[^"\\])*"'           # String literals
        r"|'(?:\\.|[^'\\])*'"          # Character literals
        r'|[A-Za-z_]\w*'                # Identifiers and keywords
        r'|\d+(?:\.\d+)?'               # Numbers
        r'|==|!=|<=|>=|&&|\|\||\+\+|--' # Multi-character operators
        r'|->|<<|>>|\+=|-=|\*=|/='
        r'|[+\-*/%=<>!&|^~.]'           # Single-character operators
        r'|[(){}\[\];,:?]'              # Punctuation
        r'|\S'                          # Any other non-whitespace character
    )

    tokens = re.findall(pattern, code)
    for token in tokens:
        if token not in KEYWORDS and not re.fullmatch(
            r'[A-Za-z_]\w*|\d+(?:\.\d+)?|'
            r'"(?:\\.|[^"\\])*"|'
            r"'(?:\\.|[^'\\])*'|"
            r'==|!=|<=|>=|&&|\|\||\+\+|--|'
            r'->|<<|>>|\+=|-=|\*=|/=|'
            r'[+\-*/%=<>!&|^~.]|[(){}\[\];,:?]',
            token
        ):
            raise LexerError(f"Invalid token: {token}")

    return tokens


def classify_token(token):
    if token in KEYWORDS:
        return "KEYWORD"
    elif re.fullmatch(r'[A-Za-z_]\w*', token):
        return "IDENTIFIER"
    elif re.fullmatch(r'\d+(\.\d+)?', token):
        return "NUMBER"
    elif token in OPERATORS:
        return "OPERATOR"
    elif token in PUNCTUATION:
        return "PUNCTUATION"
    elif token.startswith('"') and token.endswith('"'):
        return "STRING_LITERAL"
    elif token.startswith("'") and token.endswith("'"):
        return "CHAR_LITERAL"
    else:
        return "UNKNOWN"
