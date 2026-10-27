
import re

temp = 0


def new_temp():
    """Generate a unique temporary variable."""
    global temp
    temp += 1
    return f"t{temp}"


def expr(expression):
    """Convert an expression into three-address code."""

    tokens = re.findall(
        r"\d+\.\d+|\d+|[A-Za-z_]\w*|==|!=|<=|>=|[()+\-*/%<>]",
        expression
    )

    if not tokens:
        raise ValueError("Empty expression")

    output = []
    operators = []
    precedence = {
        "==": 1, "!=": 1, "<": 1, ">": 1, "<=": 1, ">=": 1,
        "+": 2, "-": 2,
        "*": 3, "/": 3, "%": 3
    }

    def reduce_once():
        op = operators.pop()
        right = output.pop()
        left = output.pop()
        t = new_temp()
        print(f"{t} = {left} {op} {right}")
        output.append(t)

    for token in tokens:
        if re.fullmatch(r"\d+\.\d+|\d+|[A-Za-z_]\w*", token):
            output.append(token)

        elif token == "(":
            operators.append(token)

        elif token == ")":
            while operators and operators[-1] != "(":
                reduce_once()

            if not operators:
                raise ValueError("Mismatched parentheses")

            operators.pop()

        elif token in precedence:
            while (
                operators
                and operators[-1] in precedence
                and precedence[operators[-1]] >= precedence[token]
            ):
                reduce_once()

            operators.append(token)

        else:
            raise ValueError(f"Invalid expression token: {token}")

    while operators:
        if operators[-1] == "(":
            raise ValueError("Mismatched parentheses")
        reduce_once()

    if len(output) != 1:
        raise ValueError("Invalid expression")

    return output[0]


def generate(program):
    """Generate three-address code for declarations and assignments."""

    global temp
    temp = 0

    print("\n========== THREE-ADDRESS CODE ==========")

    for stmt in program:

        if stmt.__class__.__name__ == "Declaration":
            if stmt.value is not None:
                result = expr(stmt.value)
                print(f"{stmt.name} = {result}")

        elif stmt.__class__.__name__ == "Assignment":
            result = expr(stmt.value)
            print(f"{stmt.name} = {result}")

    print("========================================")
