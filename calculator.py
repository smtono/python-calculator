# Calculator making time!
# Supported operations: +, -, *, /
# () Also supported

# High level pseudo
# User may press buttons or type operation to a screen
# When user presses "enter" evaluate the expression

# Evaluate how?
# +, -, *, / 
# Find a left and right partner
# Order matters for only - and / (left must be operated on by right)
# If there is (), evaluate expression inside that first

# What needs?
# Precedence system
# Based on PEMDAS, 
# Order of:
# Parentheses, [exponent], multiply, divide, add, subtract

# Maybe add exponent functionality
# First, have +, -, *, / functionality
# Add () after, then the precedence system
import enum
import token
import node

###############################
# LOOK IN NOTEBOOK FOR PSEUDO!
##############################



# used for tokenizing user input so that tokens can have values to be grabbed later
# either a number node, an operation node, or an expression node
def tokenize(input):
    tokens = []
    position = 0
    curr_char = ' '

# used for parsing expressions with ()
# finds inner-most (, counts how many there are, make sure there is a pair
# start from innermost () and push expressions into dictionary with precedence number
# priority of 1 gets evaluated first
def parse(input):
    parsed_expressions = []
    curr_expression = " "
    position = 0
    curr_char = '\0'

    # parsing each character in the user input
    for char in input:
        currChar = char
        if char == ')': # closing parentheses means we can solve the current expression
            nodes = curr_expression.split()
            input = node.Expression(nodes[0], nodes[1], nodes[2])
        elif char != '(': # push character to current expression until a () is met
            curr_expression += curr_char
        else: # use recursion to solve expressions until every () is solved
            parsed_expressions.append(curr_expression)
            curr_expression = " "
            continue


#######################################################################################
#operations = ['+', '-', '*', '/', '(', ')']
#numbers = '123456789'

# An operation is an arithmetic operation
# Such as, +, -, *, /
'''
class OperationNode(enum):
    ADDITION = '+'
    SUBTRACTION = '-'
    MULTIPLICATION = '*'
    DIVISION = '/'

# Number 
class NumberNode:
    def __init__(self, value) -> None:
        self.value = int(value) # assigning the number value of the string passed  
'''

###########
# Driver
###########
user = input("Please enter an expression (ex. 8 + 8): ")

##############
# STRETCH GOAL ::::       if there are no white spaces, add case
##############
nodes = user.split() # splits by space (if 8 + 8 was the ex, then [8, +, 8]) split splits by whitespace

# debug
for node in nodes:
    print("Value: ", node)

# parse input ()
expression = node.Expression(nodes[0], nodes[1], nodes[2])
print("Result: ", str(expression.evaluate()))
