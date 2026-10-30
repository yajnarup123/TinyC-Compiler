
# TinyC Compiler

A simple compiler project implemented in Python to demonstrate the fundamental phases of compiler design, including lexical analysis, syntax analysis, semantic analysis, symbol table management, intermediate code generation, and basic assembly-style code generation.

## Project Overview

TinyC is an educational compiler that processes a simplified subset of the C programming language. It demonstrates how source code passes through different compiler phases and how intermediate representations are generated.

The project helps students understand compiler architecture, error detection, symbol tables, and code translation.

## Objectives

- Implement lexical analysis to identify tokens.
- Perform syntax analysis to validate program structure.
- Represent program structure using an AST-like representation.
- Perform semantic analysis and detect semantic errors.
- Maintain a symbol table for identifiers and their information.
- Generate Three-Address Code (TAC).
- Demonstrate basic assembly-style code generation.

## Technologies Used

- **Programming Language:** Python
- **Editor:** Visual Studio Code
- **Version Control:** Git and GitHub

## Project Structure

```text id="s9a1c2"
tinyC_compiler/
├── test_cases/
│   ├── valid.c
│   └── invalid.c
├── ast.py
├── errors.py
├── lexer.py
├── parser.py
├── symbol_table.py
├── semantic.py
├── ir_generator.py
├── assembly_generator.py
├── main.py
├── tinyc_semantic_analysis.py
└── README.md
```

## Compiler Architecture

The compiler processes source code through the following stages:

```text id="b8c3d4"
TinyC Source Code
       |
       v
Lexical Analysis
       |
       v
Syntax Analysis
       |
       v
AST Representation
       |
       v
Symbol Table Management
       |
       v
Semantic Analysis
       |
       v
Intermediate Code Generation
       |
       v
Assembly-Style Code Generation
```

## Main Modules

### 1. Lexical Analysis — `lexer.py`

Reads the source code and identifies tokens such as keywords, identifiers, operators, constants, and punctuation symbols.

### 2. Syntax Analysis — `parser.py`

Checks whether the sequence of tokens follows the supported grammar rules and builds a representation of the program structure.

### 3. AST Representation — `ast.py`

Provides structures to represent program elements and their relationships.

### 4. Error Handling — `errors.py`

Supports reporting errors encountered during compilation.

### 5. Symbol Table — `symbol_table.py`

Stores information about identifiers, such as variable names and associated attributes.

### 6. Semantic Analysis — `semantic.py`

Checks semantic rules, including identifier declarations and other supported semantic constraints.

### 7. Intermediate Code Generation — `ir_generator.py`

Converts supported program constructs into Three-Address Code (TAC), an intermediate representation used by compilers.

### 8. Assembly-Style Code Generation — `assembly_generator.py`

Demonstrates how TAC instructions can be translated into basic assembly-style instructions.

### 9. Main Compiler — `main.py`

Coordinates the compiler phases and displays the results of compilation.

## How to Run the Project

### Prerequisites

- Python 3 installed.
- Visual Studio Code or another Python-compatible editor.

### Step 1: Open the Project

Open the `tinyC_compiler` folder in Visual Studio Code.

### Step 2: Open the Terminal

In VS Code, select **Terminal → New Terminal**.

### Step 3: Run the Main Compiler

```bash id="e5f6g7"
python main.py
```

The program runs the supported compiler phases and displays the corresponding results.

### Step 4: Run the Assembly Generator

```bash id="h8i9j0"
python assembly_generator.py
```

Follow the instructions displayed in the terminal. Enter TAC instructions one per line and type `END` on a new line when finished.

**Note:** The assembly generator currently accepts TAC as terminal input separately from the main compiler pipeline.

## Testing

Sample programs are provided in the `test_cases` directory.

### Valid Test Case

`test_cases/valid.c`

Used to test supported TinyC source code and verify the compiler's processing stages.

### Invalid Test Case

`test_cases/invalid.c`

Used to test invalid source code and observe the compiler's error handling.

## Example Three-Address Code

The following example demonstrates a possible TAC representation:

```text id="k1l2m3"
count = 10
t1 = count * 2
total = t1
t2 = total + 5
result = t2
```

Each instruction represents a simple operation or assignment.

## Example Assembly-Style Output

The following illustrates how some TAC instructions may be translated into assembly-style instructions:

```asm id="n4o5p6"
; count = 10
mov eax, 10
mov [count], eax

; t1 = count * 2
mov eax, [count]
imul eax, 2
mov [t1], eax

; total = t1
mov eax, [t1]
mov [total], eax

; t2 = total + 5
mov eax, [total]
add eax, 5
mov [t2], eax

; result = t2
mov eax, [t2]
mov [result], eax
```

**Important:** This is illustrative assembly-style output. It has not been verified as executable native machine code and may require further implementation before it can be assembled or executed.

## Current Limitations

- Supports only a simplified subset of the C programming language.
- Does not implement every feature of standard C.
- Assembly-style translation supports only the operations implemented by the generator.
- The assembly generator is currently run separately and accepts manually entered TAC.
- Native executable code generation has not been fully implemented or verified.

## Future Enhancements

- Expand support for C language constructs.
- Improve syntax and semantic error reporting.
- Integrate assembly generation directly into the main compiler pipeline.
- Add more intermediate-code optimization techniques.
- Improve test coverage and automate testing.
- Implement a proper backend for generating executable machine code.

## Learning Outcomes

This project demonstrates the core concepts of compiler design, including tokenization, parsing, semantic checking, symbol table management, intermediate representations, and basic code generation.

It also provides practical experience with Python programming, modular software design, debugging, and version control using Git and GitHub.

## Conclusion

TinyC is an educational compiler project designed to demonstrate the fundamental stages involved in transforming source code into intermediate and assembly-style representations. Its modular architecture makes it easier to understand how different compiler components work together.

The project can be extended with additional language features, code optimization, and a more complete code-generation backend.

## Author

**Yajnarup Reddy**

School: SCOPE

## Repository

[GitHub Repository — TinyC Compiler](https://github.com/yajnarup123/TinyC-Compiler)



