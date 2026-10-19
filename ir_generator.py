temp = 0

def new_temp():
    global temp
    temp += 1
    return f"t{temp}"


def expr(e):
    if e is None:
        return None

    e = str(e).strip()

    # Handle + and -
    for op in ["+", "-"]:
        parts = e.split(op, 1)
        if len(parts) == 2:
            left = expr(parts[0])
            right = expr(parts[1])
            t = new_temp()
            print(f"{t} = {left} {op} {right}")
            return t

    # Handle * and /
    for op in ["*", "/"]:
        parts = e.split(op, 1)
        if len(parts) == 2:
            left = expr(parts[0])
            right = expr(parts[1])
            t = new_temp()
            print(f"{t} = {left} {op} {right}")
            return t

    return e


def generate(program):
    print("\nTHREE-ADDRESS CODE")

    for stmt in program:

        if stmt.__class__.__name__ == "Declaration":
            if stmt.value is not None:
                value = expr(stmt.value)
                print(f"{stmt.name} = {value}")

        elif stmt.__class__.__name__ == "Assignment":
            value = expr(stmt.value)
            print(f"{stmt.name} = {value}")