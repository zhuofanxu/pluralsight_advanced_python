# --* coding: utf-8 *--
"""
while ... else ... statement
"""

def is_comment(item):
    return isinstance(item, str) and item.startswith("#")

def execute(program):
    """根据算式表达式计算结果
    """
    while program:                      # 集合为空时 结果为False
        item = program.pop()            # 栈顶弹出一个元素
        if not is_comment(item):        # 找到非注释元素
            program.append(item)        # 推回栈中 
            break                       # 绕过 else statement
    else:                               # nobreak program 已为空 表示没有找到有效item
        print('Program is Empty!')
        return
    pending = []                        # 存储操作数 和最后计算结果
    while program:
        item = program.pop()
        if callable(item):              # 出栈的item是`操作符`(operator 函数)
            result = item(*pending)     # 计算结果
            pending.clear()             # 清空操作数
            program.append(result)      # 计算结果推入栈 作为一个操作数或最终计算结果
        else:
            pending.append(item)
    else:
        print('Finish, result is: ', pending)

if __name__ == '__main__':
    import operator
    # program 表示栈 stack 列表 |1|2|3|4|5| 逆时针旋转90˚ 变成栈(即逆序)
    program = list(reversed((
        # comment1,
        # comment2,
        5,
        2,
        operator.add,
        3,
        operator.mul
    )))
    execute(program)