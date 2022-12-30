

import ast

# Creating AST
code = ast.parse('a + (b * c)')
print(ast.dump(code))