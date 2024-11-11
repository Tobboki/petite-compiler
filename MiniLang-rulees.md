# MiniLang Language Rules

## 1. Variable Declaration and Assignment

- Variables must be declared before they can be used.
- A variable is declared using the keyword `let` followed by the variable name, an optional type, and an initial value.
- Once declared, a variable’s value can be updated using an assignment statement.
- Variables can be assigned values of different types, but the types must be compatible if the language enforces strong typing.

## 2. Data Types

- The language supports basic data types: `Integer`, `Float`, `Boolean`, and `String`.
- Type compatibility rules:
  - `Integer` and `Float` can be used in arithmetic expressions together, but an implicit or explicit type conversion is applied as necessary.
  - `Boolean` values are used in conditions (e.g., `if` statements, `while` loops).
  - `String` data type supports concatenation using the `+` operator.
- Variables are implicitly typed by default but can be explicitly typed if desired (e.g., `let x: Integer = 5;`).

## 3. Expressions and Operators

- **Arithmetic Operators**: Supports `+`, `-`, `*`, `/`, and `%` (modulus) for numeric types (`Integer` and `Float`).
- **Relational Operators**: Supports `==`, `!=`, `<`, `>`, `<=`, and `>=` to compare values.
- **Logical Operators**: Supports `&&` (AND), `||` (OR), and `!` (NOT) for `Boolean` expressions.
- **Operator Precedence**: Arithmetic operations have higher precedence than relational operations, which in turn have higher precedence than logical operations. Parentheses can override precedence.

## 4. Functions

- Functions are declared using the `function` keyword, followed by the function name, parameters, and a body.
- Functions can accept zero or more parameters, and each parameter has a name and an optional type.
- The function may return a value using the `return` statement.
- Functions must return the expected type if specified. If no return type is specified, they default to returning `null` or an equivalent value.
- Functions support recursion but should have proper base cases to avoid infinite recursion.

## 5. Error Handling

- The language has basic error handling for:
  - **Syntax Errors**: Errors due to invalid grammar, such as missing semicolons or unmatched parentheses.
  - **Type Errors**: Errors due to incompatible types, such as assigning a `String` to an `Integer` variable without conversion.
  - **Runtime Errors**: Errors that occur during execution, such as division by zero or accessing undefined variables.
- Errors should be reported with meaningful messages and line numbers to help the programmer locate and fix issues.

## 7. Comments

- Single-line comments start with `//` and continue to the end of the line.
- Multi-line comments are enclosed between `/*` and `*/` and can span multiple lines.
