
def generate_assembly(tac_code):
    lines = tac_code.strip().splitlines()
    assembly = []
    variables = set()
    temporaries = set()

    # Collect all variables and temporary values
    for line in lines:
        if "=" not in line:
            continue

        left, right = map(str.strip, line.split("=", 1))

        if left.isidentifier():
            if left.startswith("t") and left[1:].isdigit():
                temporaries.add(left)
            else:
                variables.add(left)

        for word in right.replace("+", " ").replace("-", " ").replace("*", " ").replace("/", " ").split():
            if word.isidentifier() and not (word.startswith("t") and word[1:].isdigit()):
                variables.add(word)

    # Data section
    assembly.append("; TinyC Compiler - Assembly Output")
    assembly.append("section .data")

    for var in sorted(variables | temporaries):
        assembly.append(f"    {var}: dd 0")

    # Text section
    assembly.append("")
    assembly.append("section .text")
    assembly.append("global _start")
    assembly.append("_start:")

    # Translate TAC instructions
    for line in lines:
        if "=" not in line:
            continue

        left, right = map(str.strip, line.split("=", 1))
        assembly.append(f"    ; {line}")

        operators = [
            (" + ", "add"),
            (" - ", "sub"),
            (" * ", "imul"),
        ]

        matched = False

        for operator, instruction in operators:
            if operator in right:
                a, b = map(str.strip, right.split(operator, 1))

                if a.isidentifier():
                    assembly.append(f"    mov eax, [{a}]")
                else:
                    assembly.append(f"    mov eax, {a}")

                if b.isidentifier():
                    assembly.append(f"    {instruction} eax, [{b}]")
                else:
                    assembly.append(f"    {instruction} eax, {b}")

                assembly.append(f"    mov [{left}], eax")
                matched = True
                break

        if not matched:
            if right.isidentifier():
                assembly.append(f"    mov eax, [{right}]")
            else:
                assembly.append(f"    mov eax, {right}")

            assembly.append(f"    mov [{left}], eax")

    # Exit program (Linux x86)
    assembly.append("")
    assembly.append("    mov eax, 1")
    assembly.append("    xor ebx, ebx")
    assembly.append("    int 0x80")

    return "\n".join(assembly)


if __name__ == "__main__":
    print("Enter your Three-Address Code (TAC).")
    print("Type END on a new line when finished.")

    tac_lines = []

    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        if line.strip():
            tac_lines.append(line)

    print("\n========== GENERATED ASSEMBLY CODE ==========")
    print(generate_assembly("\n".join(tac_lines)))

