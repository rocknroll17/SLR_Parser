#This code is used to convert the tokens to the token objects.
from tokenizer import Token, VALUE, TYPE
class Token_parser:
    def parse(tokens):
        token_list = []
        tokens = tokens.split()
        for token in tokens:
            token_list.append(Token(token, ""))
        return token_list
