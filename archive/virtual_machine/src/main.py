import argparse
from lexer import Lexer
from parser import Parser
from code_generator import CodeGenerator
from assembler import Assembler
# from virtual_machine import VirtualMachine

def main():
    parser = argparse.ArgumentParser(description="Transpiler from ALG to machine code")
    parser.add_argument('input', help="Input file with source code")
    parser.add_argument('output', help="Output file for machine code")
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        source_code = f.read()

    lexer = Lexer(source_code)
    print(lexer)
    tokens = lexer.generate_tokens()
    print(tokens)
    parser = Parser(tokens)
    print(parser)
    ast = parser.parse()
    print(ast)
    
    # generator = CodeGenerator()
    # generator.generate(ast)
    # 
    # assembler = Assembler()
    # binary_code = assembler.assemble(generator.code)
    # 
    # with open(args.output, 'wb') as f:
    #     for line in binary_code:
    #         f.write(int(line, 2).to_bytes(4, byteorder='big'))

if __name__ == '__main__':
    main()
