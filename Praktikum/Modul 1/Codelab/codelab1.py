def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '+':
            return add(tree(left_operand) + tree(right_operand))
        elif operator == '-':
            return minus(tree(left_operand) - tree(right_operand))
        elif operator == '*':
            return multiple(tree(left_operand) * tree(right_operand))
        elif operator == '/':
            return div(tree(left_operand) / tree(right_operand))


def minus(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '-':
            return tree(left_operand) - tree(right_operand)


def add(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '+':
            return tree(left_operand) + tree(right_operand)


def multiple(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '*':
            return tree(left_operand) * tree(right_operand)


def div(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '/':
            return tree(left_operand) / tree(right_operand)

    def add(left, right):
        return left + right

    def minus(left, right):
        return left - right

    def multiple(left, right):
        return left * right

    def div(left, right):
        return left / right


expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))
# expression_tree = ((2, '+', 3),'*', (5, '-', 1))
result = tree(expression_tree)

print(result)
