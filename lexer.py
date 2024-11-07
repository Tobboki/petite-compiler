import re

# Define language-specific rules in lists for flexibility
KEYWORDS = ['let', 'function', 'if', 'else', 'while', 'return', 'print']
DATATYPES = ['Integer', 'Float', 'Boolean', 'String']
OPERATORS = {
    "ARITHMETIC_OP": [r'\+', r'-', r'\*', r'/', r'%'],
    "RELATIONAL_OP": [r'==', r'!=', r'<', r'>', r'<=', r'>='],
    "LOGICAL_OP": [r'&&', r'\|\|', r'!']
}

# Construct TOKEN_SPECIFICATIONS dynamically based on the above lists
TOKEN_SPECS = [
    ("KEYWORD", r'\b(?:' + '|'.join(KEYWORDS) + r')\b'),              # Keywords
    ("DATATYPE", r'\b(?:' + '|'.join(DATATYPES) + r')\b'),            # Data types
    ("IDENTIFIER", r'[a-zA-Z_]\w*'),                                  # Identifiers
    ("NUMBER", r'\b\d+(\.\d+)?\b'),                                   # Integers and floats
    ("BOOLEAN", r'\b(?:true|false)\b'),                               # Boolean literals
    ("STRING", r'"[^"\\]*(?:\\.[^"\\]*)*"'),                          # String literals
    ("ASSIGN", r'='),                                                 # Assignment operator
    ("LPAREN", r'\('),                                                # Left parenthesis
    ("RPAREN", r'\)'),                                                # Right parenthesis
    ("LBRACE", r'\{'),                                                # Left brace
    ("RBRACE", r'\}'),                                                # Right brace
    ("COMMA", r','),                                                  # Comma
    ("SEMICOLON", r';'),                                              # Semicolon
    ("WHITESPACE", r'[ \t]+'),                                        # Whitespace (to skip)
    ("NEWLINE", r'\n'),                                               # Newlines
    ("COMMENT", r'//[^\n]*'),                                         # Single-line comment
    ("MULTI_COMMENT", r'/\*.*?\*/', re.DOTALL),                       # Multi-line comment
]

# Add operator regex patterns from OPERATORS dictionary
for op_type, patterns in OPERATORS.items():
    TOKEN_SPECS.append((op_type, r'(?:' + '|'.join(patterns) + r')'))

# Compile regex patterns for each token type
token_regex = [(name, re.compile(pattern)) for name, pattern in TOKEN_SPECS]

def tokenize_file(file_path):
    """ Tokenize the given .txt file and returns a list of (token_type, token_value) tuples."""
    tokens = []
    line_number = 1

    # Open and read the file
    with open(file_path, 'r') as file:
        code = file.read()
    
    position = 0
    while position < len(code):
        match = None
        for token_type, regex in token_regex:
            match = regex.match(code, position)
            if match:
                token_value = match.group(0)
                if token_type == "NEWLINE":
                    line_number += 1
                elif token_type == "WHITESPACE" or token_type == "COMMENT" or token_type == "MULTI_COMMENT":
                    # Skip whitespace and comments
                    pass
                else:
                    # Append the token to the list
                    tokens.append((token_type, token_value))
                position = match.end(0)
                break
        if not match:
            raise SyntaxError(f"Illegal character at line {line_number}: {code[position]}")
    return tokens

# Example usage: Tokenize code from a .txt file
file_path = 'code.text'
tokens = tokenize_file(file_path)

for token in tokens:
    print(token)