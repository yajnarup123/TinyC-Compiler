from lexer import lexer
from parser import parser
from semantic import analyze
from ir_generator import generate

def run(filename):
    print("\nFILE:", filename)

    with open(filename) as f:
        code = f.read()

    print("\nSOURCE CODE:")
    print(code)

    tokens = lexer(code)
    print("\nTOKENS:")
    print(tokens)

    program = parser(tokens)
    print("\nSYNTAX ANALYSIS: PASSED")

    try:
        analyze(program)
        print("SEMANTIC ANALYSIS: PASSED")
    except Exception as e:
        print("SEMANTIC ANALYSIS: FAILED")
        print("Error:", e)
        return

    print()
    generate(program)

run("test_cases/valid.c")