
class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add(self, name, typ):
        """Add a variable to the symbol table."""
        if name in self.symbols:
            return False

        self.symbols[name] = typ
        return True

    def lookup(self, name):
        """Return the variable type, or None if undeclared."""
        return self.symbols.get(name)

    def update(self, name, typ):
        """Update a declared variable's type."""
        if name not in self.symbols:
            return False

        self.symbols[name] = typ
        return True

    def contains(self, name):
        """Check whether a variable is declared."""
        return name in self.symbols

    def get_all(self):
        """Return all declared variables and their types."""
        return self.symbols.copy()

    def show(self):
        """Display the symbol table."""
        print("\n========== SYMBOL TABLE ==========")
        print(f"{'Variable':<15}{'Data Type':<15}")
        print("-" * 30)

        if not self.symbols:
            print("No symbols declared.")
        else:
            for name, typ in self.symbols.items():
                print(f"{name:<15}{typ:<15}")

        print("=" * 30)
