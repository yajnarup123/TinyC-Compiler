
#  TinyC Compiler

### A Python-Based Compiler Frontend for a Simplified C Language

TinyC Compiler is an educational project that demonstrates the fundamental stages of compiler design, from lexical analysis to semantic validation and Three-Address Code (TAC) generation.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Domain](https://img.shields.io/badge/Domain-Compiler%20Design-purple)
![Status](https://img.shields.io/badge/Status-Under%20Development-orange)

---

##  Project Overview

The TinyC Compiler processes a simplified subset of C through multiple stages. It identifies tokens, checks syntax, validates variable declarations, maintains a symbol table, and generates intermediate code.

###  Objectives

- Understand the fundamental architecture of a compiler.
- Implement lexical analysis and token classification.
- Parse supported variable declarations, assignments, and expressions.
- Maintain a symbol table for declared variables.
- Detect semantic errors such as duplicate and undeclared variables.
- Generate Three-Address Code (TAC) as an intermediate representation.

---

##  Features

### 1.  Lexical Analysis

The lexer processes source code and identifies tokens, including:

- Keywords
- Identifiers
- Numeric literals
- Operators
- Symbols and delimiters

### 2.  Syntax Analysis

The parser checks the syntax of supported TinyC statements, including variable declarations, assignments, and arithmetic expressions.

### 3.  AST Representation

The project uses node classes to represent program constructs, including declarations, assignments, variables, numbers, and operations.

### 4. Symbol Table Management

The symbol table stores variable names and their declared data types. It supports variable insertion, lookup, and duplicate declaration detection.

### 5.  Semantic Analysis

The semantic analyzer checks variable declarations and usage. It detects duplicate declarations and references to undeclared variables.

### 6.  Intermediate Code Generation

The intermediate code generator produces Three-Address Code (TAC) using temporary variables to represent intermediate expression results.

### 7.  Error Handling

The project includes error classes for reporting lexical, syntax, and semantic errors.

---

##  System Architecture

The following diagram illustrates the major stages of the TinyC compiler.

```text
             +---------------------------+
             |      TinyC Source Code    |
             +---------------------------+
                          |
                          v
             +---------------------------+
             |      Lexical Analysis     |
             +---------------------------+
                          |
                          v
             +---------------------------+
             |       Token Stream        |
             +---------------------------+
                          |
                          v
             +---------------------------+
             |      Syntax Analysis      |
             +---------------------------+
                          |
                          v
             +---------------------------+
             |    AST Representation     |
             +---------------------------+
                          |
                          v
             +---------------------------+
             |     Semantic Analysis     |
             |       Symbol Table        |
             +---------------------------+
                          |
                          v
             +---------------------------+
             | Three-Address Code (TAC)  |
             |        Generation         |
             +---------------------------+
                          |
                          v
             +---------------------------+
             |       Generated TAC       |
             +---------------------------+
```

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Compiler implementation |
| Visual Studio Code | Development environment |
| Git | Version control |
| GitHub | Source-code hosting |

---

##  Project Structure

```text
TinyC-Compiler/
│
├── main.py
├── lexer.py
├── parser.py
├── ast.py
├── symbol_table.py
├── semantic.py
├── ir_generator.py
├── errors.py
├── tinyc_semantic_analysis.py
│
├── test_cases/
│   ├── valid.c
│   └── invalid.c
│
└── README.md
```

###  Module Description

| File | Responsibility |
|---|---|
| `main.py` | Runs the compiler pipeline |
| `lexer.py` | Performs lexical analysis |
| `parser.py` | Performs syntax analysis |
| `ast.py` | Defines AST node classes |
| `symbol_table.py` | Manages variable information |
| `semantic.py` | Performs semantic checks |
| `ir_generator.py` | Generates intermediate code |
| `errors.py` | Defines compiler error classes |
| `test_cases/` | Contains sample input programs |

---

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3 installed on your system
- Git installed if you want to clone the repository

### 1. Clone the Repository

```bash
git clone https://github.com/yajnarup123/TinyC-Compiler.git
```

### 2. Navigate to the Project Folder

```bash
cd TinyC-Compiler
```

### 3. Run the Compiler

```bash
python main.py
```

When prompted, enter `valid` or `invalid` to select a test case.

---

##  Sample Input

The following program demonstrates variable declarations, arithmetic expressions, and assignments.

```c
int count = 10;
float price = 25.5;
int total = count * 2;
int result = total + 5;
result = result - 3;
price = price + 1.5;
```

---

## Testing

The project includes sample test cases to demonstrate compiler behavior.

| Test File | Purpose |
|---|---|
| `valid.c` | Tests supported declarations, expressions, and assignments |
| `invalid.c` | Tests semantic error detection, such as undeclared variables |

When compilation succeeds, the compiler displays analysis results and generated intermediate code.

### Example: Semantic Error Detection

```c
int a = 5;
b = a + 2;
```

Since `b` has not been declared, the semantic analyzer reports an undeclared-variable error.

---

## 📌 Current Scope and Limitations

TinyC is an educational compiler frontend, not a complete implementation of the C programming language.

- Supported syntax is limited to the constructs implemented in the lexer and parser.
- Semantic checks are limited to those implemented in the semantic analyzer.
- The compiler generates intermediate code rather than native machine code.

---

## Future Enhancements

- Expanded data type compatibility checking
- Support for conditional statements and loops
- Improved syntax and semantic error reporting
- Additional automated test cases
- Intermediate code optimization
- Support for more C language constructs

---

## Author

**Yajnarup Reddy**

---

*An educational project exploring the fundamentals of compiler design and implementation.*

