
from lexer import lexer
from parser import parser
from semantic import analyze
from ir_generator import generate


def run(filename):
    try:
        with open(filename, "r") as f:
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

        print("\n")
        generate(program)

    except Exception as e:
        print("\nCOMPILATION FAILED")
        print("Error:", e)


if __name__ == "__main__":
    filename = input(
        "Enter test file (valid/invalid): "
    ).strip().lower()

    if filename in ("valid", "invalid"):
        run(f"test_cases/{filename}.c")
    else:
        print("Invalid choice. Enter 'valid' or 'invalid'.")
