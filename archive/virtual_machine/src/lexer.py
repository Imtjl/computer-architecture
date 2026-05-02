class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, input):
        self.input = input
        self.tokens = []
        self.current_char = None
        self.pos = -1
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.input[self.pos] if self.pos < len(self.input) else None

    def generate_tokens(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char.isdigit():
                self.tokens.append(self.generate_number())
            elif self.current_char.isalpha():
                self.tokens.append(self.generate_identifier())
            elif self.current_char == '=':
                self.tokens.append(Token('EQUAL', '='))
                self.advance()
            elif self.current_char == '+':
                self.tokens.append(Token('PLUS', '+'))
                self.advance()
            elif self.current_char == '-':
                self.tokens.append(Token('MINUS', '-'))
                self.advance()
            elif self.current_char == '*':
                self.tokens.append(Token('MULTIPLY', '*'))
                self.advance()
            elif self.current_char == '/':
                self.tokens.append(Token('DIVIDE', '/'))
                self.advance()
            elif self.current_char == ';':
                self.tokens.append(Token('SEMICOLON', ';'))
                self.advance()
            elif self.current_char == '(':
                self.tokens.append(Token('LPAREN', '('))
                self.advance()
            elif self.current_char == ')':
                self.tokens.append(Token('RPAREN', ')'))
                self.advance()
            elif self.current_char == '{':
                self.tokens.append(Token('LBRACE', '{'))
                self.advance()
            elif self.current_char == '}':
                self.tokens.append(Token('RBRACE', '}'))
                self.advance()
            else:
                raise Exception(f"Illegal character '{self.current_char}'")
        return self.tokens

    def generate_number(self):
        num_str = ''
        while self.current_char is not None and self.current_char.isdigit():
            num_str += self.current_char
            self.advance()
        return Token('NUMBER', int(num_str))

    def generate_identifier(self):
        id_str = ''
        while self.current_char is not None and self.current_char.isalnum():
            id_str += self.current_char
            self.advance()
        if id_str == 'let':
            return Token('LET', id_str)
        elif id_str == 'print':
            return Token('PRINT', id_str)
        elif id_str == 'for':
            return Token('FOR', id_str)
        else:
            return Token('IDENTIFIER', id_str)
