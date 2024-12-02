import lex_op
while True:
    text=input('basic >')
    result,error=lex_op.run('<stdin>',text)
    if  error:
        print(error.as_string())
    else:print(result)