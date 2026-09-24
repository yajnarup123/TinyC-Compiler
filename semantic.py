from symbol_table import SymbolTable
from errors import SemanticError

def analyze(program):
    table = SymbolTable()

    for stmt in program:

        if stmt.__class__.__name__ == "Declaration":
            if not table.add(stmt.name, stmt.typ):
                raise SemanticError(f"Duplicate variable: {stmt.name}")

        elif stmt.__class__.__name__ == "Assignment":
            if table.lookup(stmt.name) is None:
                raise SemanticError(f"Undeclared variable: {stmt.name}")

    table.show()
    print("SEMANTIC ANALYSIS: PASSED")