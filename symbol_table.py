class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add(self, name, typ):
        if name in self.symbols:
            return False
        self.symbols[name] = typ
        return True

    def lookup(self, name):
        return self.symbols.get(name)

    def show(self):
        print("SYMBOL TABLE")
        for name, typ in self.symbols.items():
            print(name, ":", typ)