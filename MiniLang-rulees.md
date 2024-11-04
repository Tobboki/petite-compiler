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

## 4. Control Flow

- **If Statements**:
  - An `if` statement requires a `Boolean` expression condition.
  - The `if` block runs only if the condition evaluates to true.
  - An optional `else` block can execute if the `if` condition is false.
- **While Loops**:
  - A `while` loop requires a `Boolean` expression as a condition.
  - The loop will repeat as long as the condition is true.
  - There should be a way to break out of a loop to prevent infinite loops (either by updating the condition or using a `break` statement).

## 5. Functions

- Functions are declared using the `function` keyword, followed by the function name, parameters, and a body.
- Functions can accept zero or more parameters, and each parameter has a name and an optional type.
- The function may return a value using the `return` statement.
- Functions must return the expected type if specified. If no return type is specified, they default to returning `null` or an equivalent value.
- Functions support recursion but should have proper base cases to avoid infinite recursion.

## 6. Scope and Lifetime

- Variables declared within a function or control flow block are local to that block (block scope).
- Variables declared outside any block are global and accessible throughout the program.
- Functions have their own scope, and variables within a function are not accessible outside of it.
- **Lifetime**:
  - Global variables exist for the duration of the program.
  - Local variables are created when a block or function is entered and are destroyed when the block or function ends.

## 7. Error Handling

- The language has basic error handling for:
  - **Syntax Errors**: Errors due to invalid grammar, such as missing semicolons or unmatched parentheses.
  - **Type Errors**: Errors due to incompatible types, such as assigning a `String` to an `Integer` variable without conversion.
  - **Runtime Errors**: Errors that occur during execution, such as division by zero or accessing undefined variables.
- Errors should be reported with meaningful messages and line numbers to help the programmer locate and fix issues.

## 8. Comments

- Single-line comments start with `//` and continue to the end of the line.
- Multi-line comments are enclosed between `/*` and `*/` and can span multiple lines.

## 9. Input and Output

- **Input**: Supports an `input()` function to read user input as a `String` which can be converted to other types if needed.
- **Output**: Supports a `print()` function to display text or variable values on the screen.

## 10. Standard Library (Optional)

- The language may include a minimal standard library with commonly-used functions, such as:
  - **Math Functions**: e.g., `abs()`, `sqrt()`, `pow()`
  - **String Functions**: e.g., `length()`, `substring()`
  - **Array Functions**: e.g., `push()`, `pop()`, `length`