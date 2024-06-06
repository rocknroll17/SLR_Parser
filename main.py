import lexical_analyzer
from slr_parser import SLRParser
code = '''
int x = 10;
int a() {
    char b = 'b';
    return 10;
    }
'''

tokens = lexical_analyzer.Lexical_analyzer().tokenize(code)
for token in tokens:
    print(token)
parser = SLRParser()
print(parser.parse(tokens))