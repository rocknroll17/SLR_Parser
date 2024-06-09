import lexical_analyzer
from slr_parser import SLRParser
from token_parser import Token_parser
code = '''
int x = 10;
int a() {
    char b = 'b';
    return 10 int;
    }
'''

token = "vtype id assign num semi vtype id lparen rparen lbrace vtype id assign character semi return num semi rbrace"
mode = int(input("Modes\n1. Token\n2. Code\nEnter mode: "))
if mode == 1:
    #token = input("Enter the tokens: ")
    tokens = Token_parser.parse(token)
else:
    print("\n"*20+"Enter the codes with multiple lines. Press Enter with empty line to finish.")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    code = "\n".join(lines)

    tokens, code_list = lexical_analyzer.Lexical_analyzer().tokenize(code)
print(code_list)
for token in tokens:
    print(token)
parser = SLRParser()

if mode == 1:
    parser.parse(tokens)
else:
    parser.parse(tokens, additional=code_list)