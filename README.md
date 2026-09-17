# TinyC Compiler

## Project Overview

TinyC is a simplified subset of the C programming language. This project focuses on developing a basic compiler frontend and demonstrates important concepts of Compiler Design through a manageable student-level project.

## Compiler Stages

- Lexical Analysis
- Syntax Analysis
- AST-like Representation
- Symbol Table
- Semantic Analysis
  

## Technology Used

- **Programming Language:** Python
- **Development Environment:** Visual Studio Code
- **Lexical Analysis:** Python Regular Expressions
- **Syntax Analysis:** Hand-written Recursive Descent Parser
- **Symbol Table:** Python Dictionary
- **Semantic Analysis:** Custom Type-Checking Logic

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
Semantic Analyzer  
↓  
Validated TinyC Program

## Implemented Components

- Lexical Analysis
- Syntax Analysis
- AST-like Program Representation
- Symbol Table
- Semantic Analysis
  

## Prototype Input

```c
int a = 10;
int b = 20;
float result;
result = a + b * 2;
