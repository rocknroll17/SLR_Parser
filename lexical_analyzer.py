import re
from tokenizer import Token, VALUE, TYPE

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'{self.type}'
    
    def __str__(self):
        return f'{self.type}'
    
    def to_string(self, option=VALUE):
        if option == VALUE:
            return f'{self.value}'
        else:
            return f'{self.type}'
        
    
class Lexical_analyzer:
    def __init__(self):
        self.token_specification = [
            ('vtype', r'\b(int|char|bool|string)\b'),
            ('if', r'\bif\b'),
            ('else', r'\belse\b'),
            ('while', r'\bwhile\b'),
            ('return', r'\breturn\b'),
            ('boolstr', r'\b(true|false)\b'),
            ('id', r'\b[A-Za-z_][A-Za-z0-9_]*\b'),
            ('num', r'\b\d+\b'),
            ('literal', r'"[^"]*"'),
            ('character', r"'[^']*'"),
            ('addsub', r'[+-]'),
            ('multdiv', r'[*/]'),
            ('assign', r'='),
            ('comp', r'==|!=|<=|>=|<|>|&&|\|\|'),
            ('semi', r';'),
            ('comma', r','),
            ('lparen', r'\('),
            ('rparen', r'\)'),
            ('lbrace', r'\{'),
            ('rbrace', r'\}'),
            ('SKIP', r'[ \t]+'),  # Skip over spaces and tabs
            ('NEWLINE', r'\n'),   # Line endings
            ('MISMATCH', r'.'),   # Any other character
        ]
        
    def tokenize(self, code):
        tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in self.token_specification)
        #Join rules into regex ex) vtype|id|num|literal...
        get_token = re.compile(tok_regex).match
        #Tokenizing the code
        line_num = 1
        line_start = 0
        current_token_match = get_token(code)
        tokens = []
        recognized_code_list = []
            
        while current_token_match is not None:
            kind = current_token_match.lastgroup
            value = current_token_match.group(kind)
            
            if kind == 'NEWLINE':#If new line, increase line number
                line_start = current_token_match.end()
                line_num += 1
            elif kind == 'SKIP':#If space or tab, pass
                pass
            elif kind == 'MISMATCH':#If mismatch, raise error
                raise RuntimeError(f'{value!r} unexpected on line {line_num}')
            else:#If token, append to tokens
                if kind != 'SKIP' and kind != 'NEWLINE':
                    column = current_token_match.start() - line_start
                    tokens.append(Token(kind, value))
            #Append recognized code to list
            recognized_code_list.append(value)
            current_token_match = get_token(code, current_token_match.end())
        #Split recognized code list by new line for error handling at syntax analysis
        code_list = []
        temp = []
        for i in range(len(recognized_code_list)):
            if recognized_code_list[i] == " " or recognized_code_list[i] == "\t" or recognized_code_list[i] == "":
                pass
            elif recognized_code_list[i] != "\n":
                temp.append(recognized_code_list[i])
            else:
                code_list.append(temp)
                temp = []
            
        return tokens, code_list
