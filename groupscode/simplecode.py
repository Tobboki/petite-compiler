import string

# تعريف الثوابت
DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS

TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_EOF = 'EOF'

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f'{self.type}:{self.value}' if self.value else f'{self.type}'

class Lex:
    def __init__(self, text):
        self.text = text
        self.idx = 0

    def advance(self):
        if self.idx < len(self.text):
            char = self.text[self.idx]
            self.idx += 1
            return char
        return None

    def make_tokens(self):
        tokens = []
        while self.idx < len(self.text):
            char = self.advance()
            if char in ' \t':
                continue
            if char.isdigit():
                num_str = char
                while self.idx < len(self.text) and self.text[self.idx].isdigit():
                    num_str += self.advance()
                tokens.append(Token(TT_INT, int(num_str)))
            elif char == '+':
                tokens.append(Token(TT_PLUS))
            elif char == '-':
                tokens.append(Token(TT_MINUS))
            elif char == '*':
                tokens.append(Token(TT_MUL))
            elif char == '/':
                tokens.append(Token(TT_DIV))
            else:
                continue
        
        tokens.append(Token(TT_EOF))
        return tokens

class numberNode:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f"{self.tok}"

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.op} {self.right})"


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = 0
        self.current_tok = self.tokens[self.tok_idx]

    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]

    def factor(self):
        if self.current_tok.type == TT_INT:
            tok = self.current_tok
            self.advance()
            return numberNode(tok)

    def bin_op(self, func, ops):
        left = func()
        while self.current_tok.type in ops:
            op_tok = self.current_tok
            self.advance()
            right = func()
            left = BinOpNode(left, op_tok, right)
        return left

    def term(self):
        return self.bin_op(self.factor, [TT_MUL, TT_DIV])

    def expr(self):
        return self.bin_op(self.term, [TT_PLUS, TT_MINUS])


if __name__ == "__main__":
    # اختبار Lexer
    text = "5 + 3 * 6*6+7"
    lexer = Lex(text)
    tokens = lexer.make_tokens()
    print("lexer:", tokens)

    # اختبار Parser
    parser = Parser(tokens)
    tree = parser.expr()
    print("Parser", tree)
