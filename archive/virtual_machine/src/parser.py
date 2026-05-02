class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def advance(self):
        self.pos += 1
        self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def parse(self):
        return self.program()

    def program(self):
        statements = []
        while self.current_token is not None:
            statements.append(self.statement())
        return {'type': 'PROGRAM', 'body': statements}

    def statement(self):
        if self.current_token.type == 'LET':
            return self.declaration()
        elif self.current_token.type == 'IDENTIFIER':
            return self.assignment()
        elif self.current_token.type == 'PRINT':
            return self.print_statement()
        elif self.current_token.type == 'FOR':
            return self.for_loop()
        else:
            raise Exception("Invalid statement")

    def declaration(self):
        self.advance()
        var_name = self.current_token.value
        self.advance()
        self.advance()
        expr = self.expression()
        self.advance()
        return {'type': 'DECLARATION', 'name': var_name, 'value': expr}

    def assignment(self):
        var_name = self.current_token.value
        self.advance()
        self.advance()
        expr = self.expression()
        self.advance()
        return {'type': 'ASSIGNMENT', 'name': var_name, 'value': expr}

    def print_statement(self):
        self.advance()
        self.advance()
        expr = self.expression()
        self.advance()
        return {'type': 'PRINT', 'value': expr}

    def for_loop(self):
        self.advance()
        self.advance()
        init = self.declaration()
        self.advance()
        cond = self.expression()
        self.advance()
        update = self.assignment()
        self.advance()
        self.advance()
        body = []
        while self.current_token.type != 'RBRACE':
            body.append(self.statement())
        self.advance()
        return {'type': 'FOR', 'init': init, 'cond': cond, 'update': update, 'body': body}

    def expression(self):
        return self.term()

    def term(self):
        left = self.factor()
        while self.current_token is not None and self.current_token.type in ('PLUS', 'MINUS'):
            op = self.current_token.type
            self.advance()
            right = self.factor()
            left = {'type': 'BINARY_OP', 'operator': op, 'left': left, 'right': right}
        return left

    def factor(self):
        left = self.primary()
        while self.current_token is not None and self.current_token.type in ('MULTIPLY', 'DIVIDE'):
            op = self.current_token.type
            self.advance()
            right = self.primary()
            left = {'type': 'BINARY_OP', 'operator': op, 'left': left, 'right': right}
        return left

    def primary(self):
        token = self.current_token
        if token.type == 'NUMBER':
            self.advance()
            return {'type': 'NUMBER', 'value': token.value}
        elif token.type == 'IDENTIFIER':
            self.advance()
            return {'type': 'IDENTIFIER', 'value': token.value}
        elif token.type == 'LPAREN':
            self.advance()
            expr = self.expression()
            self.advance()
            return expr
        else:
            raise Exception("Invalid primary")
