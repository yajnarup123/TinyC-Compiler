
from contextlib import redirect_stdout
from io import StringIO

import lexer
from parser import parser
from semantic import analyze
from ir_generator import generate
from assembly_generator import generate_assembly


# Find the lexer function
lexer_function = None

for name in ("tokenize", "lex", "lexer", "scan", "lexical_analysis"):
    if callable(getattr(lexer, name, None)):
        lexer_function = getattr(lexer, name)
        break

if lexer_function is None:
    raise ImportError(
        "Could not identify the lexer function in lexer.py"
    )


# Read source code
with open("test_cases/valid.c", "r") as file:
    source_code = file.read()


# LEXICAL ANALYSIS
print("\n========== LEXICAL ANALYSIS ==========")

tokens = lexer_function(source_code)

for token in tokens:
    print(token)


# SYNTAX ANALYSIS
print("\n========== SYNTAX ANALYSIS ==========")

program = parser(tokens)
print("SYNTAX ANALYSIS: PASSED")


# SEMANTIC ANALYSIS
print("\n========== SEMANTIC ANALYSIS ==========")

analyze(program)
print("SEMANTIC ANALYSIS: PASSED")


# INTERMEDIATE CODE GENERATION
print("\n========== THREE-ADDRESS CODE ==========")

tac_output = StringIO()

with redirect_stdout(tac_output):
    generate(program)

tac_code = tac_output.getvalue()
print(tac_code)


# ASSEMBLY CODE GENERATION
print("\n========== GENERATED ASSEMBLY CODE ==========")

assembly_code = generate_assembly(tac_code)
print(assembly_code)


print("\nCOMPILATION COMPLETED")
