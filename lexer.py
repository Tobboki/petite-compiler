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

# Combine all regex patterns into one pattern with named groups
tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECS)

def tokenize_file(file_path):
    """Tokenize input from a .txt file and output tokens to a tokens.txt file."""
    with open(file_path, 'r') as file:
        code = file.read()

    tokens = []
    line_num = 1
    line_start = 0

    for match_object in re.finditer(tok_regex, code):
        kind = match_object.lastgroup
        value = match_object.group(kind)
        column = match_object.start() - line_start + 1  # Calculate the column number

        if kind == 'NEWLINE':
            line_start = match_object.end()
            line_num += 1
        elif kind == 'WHITESPACE':
            continue  # Ignore whitespace
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r} on line {line_num}, column {column}')
        else:
            tokens.append((kind, value, line_num, column))

    # Append EOF token at the end
    tokens.append(('EOF', '', line_num, column + 1))

    # Write tokens to output file
    with open('tokens.txt', 'w') as file:
        for token in tokens:
            file.write(f'{token}\n')

    return tokens

'''
Example usage: Tokenize code from a .txt file
Note: 'file_path' should contain the file extension at the end of the file name
e.g: file_name.file_extension
'''
file_path = 'F:\Programming\Collage\Compiler Design\Compiler Project\code.txt'
tokens = tokenize_file(file_path)

for token in tokens:
    print(token)
