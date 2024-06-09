import lexical_analyzer
from slr_parser import SLRParser
from token_parser import Token_parser
import sys
file_path = sys.argv[1]
f=open(file_path, "r")
file_token = f.readlines()
token = ""
token = " ".join(file_token)
token = token.replace("\n", " ")
token = token.replace("   ", " ")
print(token)
tokens = Token_parser.parse(token)
for token in tokens:
    print(token)
parser = SLRParser()

parser.parse(tokens)