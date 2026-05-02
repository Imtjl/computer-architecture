class Assembler:
    def __init__(self):
        self.instructions = {
            'MOV': '0001',
            'ADD': '0010',
            'SUB': '0011',
            'MUL': '0100',
            'DIV': '0101',
            'JMP': '0110',
            'JMP_IF_FALSE': '0111',
            'PRINT': '1000',
            'CMP': '1001'
        }

    def assemble(self, asm_code):
        binary_code = []
        for line in asm_code:
            parts = line.split()
            opcode = self.instructions[parts[0]]
            operands = ''.join([format(int(op[1:]), '04b') if op.startswith('R') else format(int(op), '016b') for op in parts[1:]])
            binary_code.append(opcode + operands)
        return binary_code
