import re

def del_ugly_newlines(text):
    # 使用正则表达式匹配只有单独的换行符
    pattern = re.compile(r'(?<!\n)\n(?!\n)')
    # 替换匹配的换行符为空字符串
    result = pattern.sub('', text)
    return result