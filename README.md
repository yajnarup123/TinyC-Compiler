# TinyC Compiler

## Project Overview

TinyC is a simplified subset of the C programming language. This project focuses on developing a basic compiler frontend and demonstrates important concepts of Compiler Design through a manageable student-level project.

## Compiler Stages

- Lexical Analysis
- Syntax Analysis
- AST-like Representation
- Symbol Table
- Semantic Analysis
- Basic Type Checking

## Technology Used

- **Programming Language:** Python
- **Development Environment:** Visual Studio Code
- **Lexical Analysis:** Python Regular Expressions
- **Syntax Analysis:** Hand-written Recursive Descent Parser
- **AST:** Custom AST-like representation
- **Symbol Table:** Python Dictionary
- **Semantic Analysis:** Custom Semantic Analysis Logic
- **Type Checking:** Basic Type Compatibility Checking
- 
## System Architecture

TinyC Source Code
↓
Lexical Analyzer
↓
Token Stream
↓
Syntax Analyzer
↓
AST-like Representation
↓
Symbol Table
↓
Semantic Analyzer
↓
Basic Type Checking
↓
Validated TinyC Program

## Implemented Components

- Lexical Analysis – Tokenization of TinyC source code.
- Syntax Analysis – Recursive descent parsing.
- AST Representation – AST-like structure for parsed code.
- Symbol Table – Stores identifiers and their data types.
- Semantic Analysis – Declaration and type checking.
- Error Handling – Detection and reporting of lexical, syntax, and semantic errors.
- Intermediate Code Generation – Generation of Three-Address Code (TAC).
  

## Prototype Input

```c
int a = 10;
int b = 20;
float result;
result = a + b * 2;

## Phase 2 Implementation

The TinyC compiler was extended with semantic analysis, symbol table management, basic type checking, error handling, and intermediate code generation using Three-Address Code (TAC).
