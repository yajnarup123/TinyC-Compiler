temp = 0

def new_temp():
    global temp
    temp += 1
    return f"t{temp}"


def generate(program):
    print("INTERMEDIATE CODE")

    for stmt in program:
        if stmt.__class__.__name__ == "Declaration":
            print(f"DECLARE {stmt.name}")

        elif stmt.__class__.__name__ == "Assignment":
            t = new_temp()
            print(f"{t} = {stmt.value}")
            print(f"{stmt.name} = {t}")