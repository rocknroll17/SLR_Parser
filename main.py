import lexical_analyzer
from slr_parser import SLRParser
code = '''
int x = 10;
char a = 'a';
'''

tokens = lexical_analyzer.Lexical_analyzer().tokenize(code)
for token in tokens:
    print(token)
parser = SLRParser()
parser.parse(tokens)