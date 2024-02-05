from sympy import symbols, Eq, solve
import re

def replace_chars(input_string):
    # 使用正则表达式替换
    # 方框换成x
    output_string = re.sub(r"[口ロ□口]", "x", input_string)
    # 一，长音等符号换成减号
    output_string = re.sub(r"[一—ー一]", "-", input_string)
    return output_string

def replace_multiplication_symbol(input_str):
    # 定义正则表达式模式
    pattern = re.compile(r'[xX]')

    # 使用sub函数进行替换
    output_str = pattern.sub('*', input_str)

    return output_str

def rearrange_equation(equation):
    # 寻找等号的位置
    equal_sign_index = equation.find('=')

    # 提取等号右边的内容
    right_side = equation[equal_sign_index + 1:]

    # 将等号右边的内容加上括号，并使左边减去右边的内容
    rearranged_equation = equation[:equal_sign_index] + ' - (' + right_side + ')'

    return rearranged_equation

def solve_equation(equation_str, variable_str):
    # 定义符号
    x = symbols(variable_str)

    # 将方程字符串转换为 SymPy 的方程对象
    equation = Eq(eval(equation_str), 0)

    # 解方程
    solution = solve(equation, x)

    return solution

def proc_and_solve(scaned_equation):
    refined_equation = rearrange_equation\
        (replace_chars\
        (replace_multiplication_symbol(scaned_equation)))
    result = solve_equation(refined_equation,"x")
    print("解:", result)
    return result

# 获取用户输入的方程字符串
# user_input = "2x + 5 = 11"

# print(replace_multiplication_symbol(user_input))

# # 处理方程字符串
# result = rearrange_equation(user_input)

# # 打印结果
# print(result)

# # 例子：解方程 2x + 5 = 11
# equation_str = "2*x + 5 - 11"
# variable_str = "x"

# result = solve_equation(equation_str, variable_str)
# print("解:", result)