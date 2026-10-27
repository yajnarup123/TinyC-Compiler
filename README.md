TinyC Compiler

Project Overview

TinyC Compiler is a Python-based compiler frontend for a simplified subset of the C programming language. The project demonstrates the fundamental stages of compiler design, including lexical analysis, syntax analysis, semantic analysis, symbol table management, and intermediate code generation.

The main objective is to understand how source code is processed and transformed through different stages of a compiler.

Objectives

Understand the basic architecture of a compiler.

Implement lexical analysis and token classification.

Parse variable declarations, assignments, and expressions.

Maintain a symbol table for declared variables.

Detect semantic errors such as duplicate and undeclared variables.

Generate Three-Address Code (TAC) as an intermediate representation.

Features

1. Lexical Analysis

The lexer processes source code and identifies tokens, including:

Keywords

Identifiers

Numeric literals

Operators

Symbols and delimiters

2. Syntax Analysis

The parser checks the syntax of supported TinyC statements, including variable declarations, assignments, and arithmetic expressions.

3. AST Representation

The project defines node classes to represent declarations, assignments, variables, numbers, and operations.

4. Symbol Table Management

The symbol table stores variable names and their declared data types. It supports variable insertion, lookup, and duplicate declaration detection.

5. Semantic Analysis

The semantic analyzer checks variable declarations and usage. It detects duplicate declarations and reports assignments or expressions that reference undeclared variables.

6. Intermediate Code Generation

The intermediate code generator produces Three-Address Code (TAC) using temporary variables to represent intermediate expression results.

7. Error Handling

The project includes error classes for reporting lexer, parser, and semantic errors.

System Architecture

TinyC Source Code
        |
        v
Lexical Analysis
        |
        v
Token Stream
        |
        v
Syntax Analysis
        |
        v
AST Representation
        |
        v
Semantic Analysis
        |
        v
Symbol Table Validation
        |
        v
Three-Address Code Generation

Technologies Used

Programming Language: Python 3

Development Environment: Visual Studio Code

Version Control: Git

Repository Hosting: GitHub

Project Structure

TinyC-Compiler/
├── main.py
├── lexer.py
├── parser.py
├── ast.py
├── symbol_table.py
├── semantic.py
├── ir_generator.py
├── errors.py
├── tinyc_semantic_analysis.py
├── test_cases/
│   ├── valid.c
│   └── invalid.c
└── README.md

Module Description

File

Description

main.py

Runs the compiler pipeline and displays results

lexer.py

Performs lexical analysis

parser.py

Performs syntax analysis

ast.py

Defines AST node classes

symbol_table.py

Stores and retrieves variable information

semantic.py

Performs semantic checks

ir_generator.py

Generates Three-Address Code

errors.py

Defines compiler error classes

test_cases/valid.c

Contains valid sample input

test_cases/invalid.c

Contains input for error testing

Requirements

Python 3

Visual Studio Code or another Python-compatible editor

Git (optional, for cloning the repository)

Installation and Execution

Step 1: Clone the Repository

git clone https://github.com/yajnarup123/TinyC-Compiler.git

Step 2: Open the Project Directory

cd TinyC-Compiler

Step 3: Run the Compiler

python main.py

Step 4: Select a Test Case

When prompted, enter:

valid to run the valid test case.

invalid to run the invalid test case.

The compiler displays the source code, token information, syntax analysis results, semantic analysis results, and intermediate code when the program passes the required checks.

Sample Input

int count = 10;
float price = 25.5;
int total = count * 2;
int result = total + 5;
result = result - 3;
price = price + 1.5;

Testing

The project includes test files to demonstrate compiler behavior.

Valid Input

The valid test case demonstrates variable declarations, arithmetic expressions, assignments, and intermediate code generation.

Invalid Input

The invalid test case includes an assignment to an undeclared variable:

int a = 5;
b = a + 2;

The semantic analyzer reports that b has not been declared. Compilation stops when this semantic error is raised.

Current Scope and Limitations

TinyC is an educational compiler frontend and does not implement the complete C programming language.

The current implementation focuses on the syntax and semantic checks supported by its lexer and parser. It does not generate native machine code.

Future Enhancements

Support for conditional statements and loops

Expanded data type compatibility checks

Improved syntax and semantic error reporting

Additional automated test cases

Intermediate code optimization

Support for more C language constructs
