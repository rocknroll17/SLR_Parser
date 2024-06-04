import lexical_analyzer
from slr_parser import SLRParser
code = '''
int x = 10;
if (x > 0) {
    x = x + 1;
}
char a = 'a';
return x;
'''

tokens = lexical_analyzer.Lexical_analyzer().tokenize(code)
for token in tokens:
    print(token)
parser = SLRParser()
parser.parse(tokens)