# Token creates tokens for different characters in user input
# Different token types include number, operation, expression, unexpected
# Different tokens will have a token type and a value associated with it

import enum

class Token:
    def __init__(self, token_type, value) -> None:
        self.token_type = token_type
        self.value = value
    
    def is_arithmetic_operation(self):
        OPERATIONS = '+-*/'
        if self.value in OPERATIONS:
            return True
        else:
            return False

class TokenType(enum):
    NUMBER = 'number'
    OPERATION = 'operation'
    EXPRESSION = 'expression'
    UNEXPECTED = 'unexpected'

# parses user input into different tokens
class Tokenizer:
    NUMBERS = '1234567890'
    
    tokens = [] # possible user input tokens

    # pass user input and set current character and current position
    def __init__(self, text) -> None:
        self.text = text
        self.current_pos = -1
        self.current_char = '\0'
        self.advance()
    
    # proceeds to next character in input
    def advance(self) -> None:
        self.current_pos += 1
        if self.current_pos < len(self.text): # if there is still character left, advance to next character in input
            self.current_char = self.text.index(self.current_pos) # get the character at the current position (index)

    # simplifies down one expression at a time according to PEMDAS
    def simplify(input):
        if '(' in input: # input still has ()
            pass
        else:
            pass

    def make_tokens(self):
        OPERATIONS = '+-*/'

        if self.current_char == ' ': # skip spaces
            self.advance()
        elif self.current_char in self.NUMBERS: # if the current character is a number
            self.tokens.append(self.make_number())
            self.advance()
        elif self.current_char in OPERATIONS: # if the current character is an operation
            self.tokens.append(Token(TokenType.OPERATION, self.current_char))
            self.advance()
        elif self.current_char == '(': # push until ')' is met
            unedited = self.text[self.current_position] # slicing operation
            # cut off expression into 2 from beginning to this point, pass in ()
            self.simplify(self.text[self.current_postion+1:len(self.text)+1]) # slicing string from 1 after start of ( to end of string
            self.make_expression()
        

    # continues building a number until terminating character reached
    def make_number(self):
        number = ' '
        while self.current_char in self.NUMBERS and self.current_char != '\0': # while there is still a number
            number += self.current_char
        return Token(TokenType.NUMBER, number)
    
    # finish ?
    def make_expression(self):
        while self.curr_char != ')':
            return