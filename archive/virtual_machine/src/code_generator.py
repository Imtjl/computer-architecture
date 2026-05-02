
class CodeGenerator:
    def __init__(self):
        self.code = []
        self.variables = {}
        self.current_register = 0

    def generate(self, node):
        if node['type'] == 'PROGRAM':
            for statement in node['body']:
                self.generate(statement)
        elif node['type'] == 'DECLARATION':
            self.variables[node['name']] = self.current_register
            self.generate(node['value'])
            self.code.append(f'MOV R{self.current_register}, {node["value"]["value"]}')
            self.current_register += 1
        elif node['type'] == 'ASSIGNMENT':
            reg = self.variables[node['name']]
            self.generate(node['value'])
            self.code.append(f'MOV R{reg}, {node["value"]["value"]}')
        elif node['type'] == 'PRINT':
            self.generate(node['value'])
            self.code.append(f'PRINT R{self.current_register - 1}')
        elif node['type'] == 'FOR':
            self.generate(node['init'])
            cond_label = len(self.code)
            self.generate(node['cond'])
            cond_reg = self.current_register - 1
            end_label = len(self.code) + 1
            self.code.append(f'JMP_IF_FALSE R{cond_reg}, {end_label + len(node["body"])}')
            for statement in node['body']:
                self.generate(statement)
            self.generate(node['update'])
            self.code.append(f'JMP {cond_label}')
        elif node['type'] == 'BINARY_OP':
            self.generate(node['left'])
            left_reg = self.current_register - 1
            self.generate(node['right'])
            right_reg = self.current_register - 1
            if node['operator'] == 'PLUS':
                self.code.append(f'ADD R{left_reg}, R{right_reg}')
            elif node['operator'] == 'MINUS':
                self.code.append(f'SUB R{left_reg}, R{right_reg}')
            elif node['operator'] == 'MULTIPLY':
                self.code.append(f'MUL R{left_reg}, R{right_reg}')
            elif node['operator'] == 'DIVIDE':
                self.code.append(f'DIV R{left_reg}, R{right_reg}')
        elif node['type'] == 'NUMBER':
            self.code.append(f'MOV R{self.current_register}, {node["value"]}')
            self.current_register += 1
        elif node['type'] == 'IDENTIFIER':
            reg = self.variables[node['value']]
            self.code.append(f'MOV R{self.current_register}, R{reg}')
            self.current_register += 1
