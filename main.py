
from lexer import lexer
from parser import parser
from semantic import analyze
from ir_generator import generate

filename = input("Enter test file (valid/invalid): ")
source_path = f"test_cases/{filename}.c"

with open(source_path, "r") as file:
    source_code = file.read()

tokens = lexer(source_code)

print("\n========== SOURCE CODE ==========")
print(source_code)

print("\n========== TOKENS ==========")
print(f"{'TOKEN':<20} {'TOKEN TYPE':<20}")
print("-" * 40)

KEYWORDS = {
    "int", "float", "return", "if", "else",
    "while", "for", "void"
}

for token in tokens:
    if token in KEYWORDS:
        token_type = "KEYWORD"
    elif token.isidentifier():
        token_type = "IDENTIFIER"
    elif token.replace(".", "", 1).isdigit():
        token_type = "NUMBER"
    elif token in {"+", "-", "*", "/", "%", "="}:
        token_type = "OPERATOR"
    else:
        token_type = "SYMBOL"

    print(f"{token:<20} {token_type:<20}")

print("-" * 40)

print("\n========== SYNTAX ANALYSIS ==========")
program = parser(tokens)
print("SYNTAX ANALYSIS: PASSED")

print("\n========== SEMANTIC ANALYSIS ==========")
analyze(program)

print("\n========== INTERMEDIATE CODE ==========")
generate(program)

print("\nCOMPILATION COMPLETED")
