class Expression():
    def evaluate(self):
        raise NotImplementedError

class Star(Expression):
    def __init__(self, op1):
        self.op1 = op1

    def evaluate(self):
        return 'Star(' + self.op1.evaluate() + ')'

class Plus(Expression):
    def __init__(self, op1):
        self.op1 = op1

    def evaluate(self):
        return 'Plus(' + self.op1.evaluate() + ')'

class Union(Expression):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def evaluate(self):
        return 'Union(' + self.op1.evaluate() + ', ' + self.op2.evaluate() + ')'

class Concat(Expression):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def evaluate(self):
        return 'Concat(' + self.op1.evaluate() + ', ' + self.op2.evaluate() + ')'

class Optional(Expression):
    def __init__(self, op1):
        self.op1 = op1

    def evaluate(self):
        return 'Union(' + self.op1.evaluate() + ', Lambda())'

class SimpleQuantifier(Expression):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def evaluate(self):
        r1 = self.op1.evaluate()
        res = ''
        for _ in range(int(self.op2) - 1):
            res += 'Concat(' + r1 + ', '
        res += r1 + ')' * (int(self.op2) - 1)
        return res

class DoubleQuantifier(Expression):
    def __init__(self, op1, op2, op3):
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3

    def evaluate(self):
        r1 = self.op1.evaluate()
        r_start = int(self.op2)
        r_end = int(self.op3)
        res = ''
        for i in range(r_start, r_end):
            res += 'Union('
            for _ in range(i-1):
                res += 'Concat(' + r1 + ', '
            res += r1 + ')' * (i-1) + ', '
        for _ in range(r_end - 1):
            res += 'Concat(' + r1 + ', '
        res += r1 + ')' * (r_end - 1 + (r_end - r_start))
        return res

class Par(Expression):
    def __init__(self, op1):
        self.op1 = op1

    def evaluate(self):
        return self.op1.evaluate()

class Id(Expression):
    def __init__(self, op1):
        self.op1 = op1

    def evaluate(self):
        return 'Char(' + self.op1 + ')'

# class Sum(Expression):
#     def __init__(self, op1, op2):
#         self.op1 = op1
#         self.op2 = op2

#     def evaluate(self):
#         return self.op1.evaluate() + self.op2.evaluate()

# class Sub(Expression):
#     def __init__(self, op1, op2):
#         self.op1 = op1
#         self.op2 = op2
        
#     def evaluate(self):
#         return self.op1.evaluate() - self.op2.evaluate()

# class Prod(Expression):
#     def __init__(self, op1, op2):
#         self.op1 = op1
#         self.op2 = op2
        
#     def evaluate(self):
#         return self.op1.evaluate() * self.op2.evaluate()

# class Div(Expression):
#     def __init__(self, op1, op2):
#         self.op1 = op1
#         self.op2 = op2
        
#     def evaluate(self):
#         return self.op1.evaluate() / self.op2.evaluate()

# class Par(Expression):
#     def __init__(self, op1):
#         self.op1 = op1
        
#     def evaluate(self):
#         return self.op1.evaluate()

# class Neg(Expression):
#     def __init__(self, op1):
#         self.op1 = op1
        
#     def evaluate(self):
#         return -self.op1.evaluate()

# class Id(Expression):
#     def __init__(self, op1):
#         self.op1 = op1
        
#     def evaluate(self):
#         return float(self.op1)

# class Term(Expression):
#     def __init__(self, op1):
#         self.op1 = op1
        
#     def evaluate(self):
#         return self.op1.evaluate()

# class Factor(Expression):
#     def __init__(self, op1):
#         self.op1 = op1
        
#     def evaluate(self):
#         return self.op1.evaluate()