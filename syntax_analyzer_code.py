import lexical_analyzer
from slr_parser import SLRParser
from token_parser import Token_parser
import sys
file_path = sys.argv[1]
f=open(file_path, "r")
f.readlines()
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

code = "\n".join(lines)

tokens, code_list = lexical_analyzer.Lexical_analyzer().tokenize(code)
token_list = []
temp = []
index = 0
for token in tokens:
    print(token)
parser = SLRParser()

if mode == 1:
    parser.parse(tokens)
else:
    parser.parse(tokens, additional=code_list)