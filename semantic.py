
import re
from symbol_table import SymbolTable
from errors import SemanticError


def analyze(program):
    table = SymbolTable()

    for stmt in program:

        # Handle variable declarations
        if stmt.__class__.__name__ == "Declaration":

            if stmt.typ not in ("int", "float"):
                raise SemanticError(
                    f"Unsupported data type: {stmt.typ}"
                )

            if not table.add(stmt.name, stmt.typ):
                raise SemanticError(
                    f"Duplicate variable: {stmt.name}"
                )

            if stmt.value is not None:
                check_expression(stmt.value, table)

        # Handle assignments
        elif stmt.__class__.__name__ == "Assignment":

            if table.lookup(stmt.name) is None:
                raise SemanticError(
                    f"Undeclared variable: {stmt.name}"
                )

            check_expression(stmt.value, table)

    table.show()
    print("\nSEMANTIC ANALYSIS: PASSED")
    return table


def check_expression(expression, table):
    """Check whether variables used in an expression are declared."""

    keywords = {"int", "float", "return"}

    tokens = re.findall(
        r"\d+\.\d+|\d+|[A-Za-z_]\w*|==|!=|<=|>=|[^\s]",
        expression
    )

    for token in tokens:
        if token in keywords:
            continue

        if token.replace(".", "", 1).isdigit():
            continue

        if token in {
            "+", "-", "*", "/", "%", "(", ")",
            "<", ">", "=", "!", "&", "|"
        }:
            continue

        if table.lookup(token) is None:
            raise SemanticError(
                f"Undeclared variable in expression: {token}"
            )
