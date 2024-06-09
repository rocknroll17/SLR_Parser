TYPE = 'TYPE'
VALUE = 'VALUE'

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