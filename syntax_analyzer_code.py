import lexical_analyzer
from slr_parser import SLRParser
import sys

file_path = sys.argv[1]
f=open(file_path, "r")
code_text = f.readlines()
lines = []
for line in code_text:
    lines.append(line)
code = "\n".join(lines)

tokens, code_list = lexical_analyzer.Lexical_analyzer().tokenize(code)
#Make code to token objects -> lexical analysis
parser = SLRParser()
#Give additional code list for error handling
parser.parse(tokens, additional=code_list)