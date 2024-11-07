import re

# Define language-specific rules in lists for flexibility
KEYWORDS = ['let', 'function', 'if', 'else', 'while', 'return', 'print']
DATATYPES = ['Integer', 'Float', 'Boolean', 'String']
OPERATORS = {
    "ARITHMETIC_OP": [r'\+', r'-', r'\*', r'/', r'%'],
    "RELATIONAL_OP": [r'==', r'!=', r'<', r'>', r'<=', r'>='],
    "LOGICAL_OP": [r'&&', r'\|\|', r'!']
}

# Construct core token specifications
TOKEN_SPECS = [
    ("KEYWORD", r'\b(?:' + '|'.join(KEYWORDS) + r')\b'),              # Keywords
    ("DATATYPE", r'\b(?:' + '|'.join(DATATYPES) + r')\b'),            # Data types
    ("IDENTIFIER", r'[A-Za-z_][A-Za-z0-9_]*'),                        # Identifiers
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
]

# Add operator regex patterns from OPERATORS dictionary dynamically
for op_type, patterns in OPERATORS.items():
    TOKEN_SPECS.append((op_type, r'(?:' + '|'.join(patterns) + r')'))

# Compile all regex patterns for each token type
token_regex = [(name, re.compile(pattern)) for name, pattern in TOKEN_SPECS]

def tokenize_file(file_path):
    """ Tokenize the given file, returning a list of (token_type, token_value, line_number, column) tuples. """
    tokens = []
    line_number = 1

    with open(file_path, 'r') as file:
        code = file.read()

    position = 0
    while position < len(code):
        # Handle multi-line comments explicitly
        if code[position:position+2] == '/*':
            end_comment = code.find('*/', position + 2)
            if end_comment == -1:
                raise SyntaxError(f"Unterminated multi-line comment at line {line_number}")
            # Move the position past the end of the comment
            position = end_comment + 2
            continue

        match = None
        for token_type, regex in token_regex:
            match = regex.match(code, position)
            if match:
                token_value = match.group(0)
                if token_type == "NEWLINE":
                    line_number += 1
                elif token_type not in {"WHITESPACE", "COMMENT"}:
                    # Only add meaningful tokens
                    column = position + 1
                    tokens.append((token_type, token_value, line_number, column))
                position = match.end(0)
                break

        if not match:
            raise SyntaxError(f"Illegal character '{code[position]}' at line {line_number}, column {position + 1}")

    return tokens

'''
Example usage: Tokenize code from a .txt file
Note: 'file_path' should contain the file extension at the end of the file name
e.g: file_name.file_extension
'''
file_path = 'code.txt'
tokens = tokenize_file(file_path)

for token in tokens:
    print(token)
