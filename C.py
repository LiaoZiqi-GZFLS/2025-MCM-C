def insert_packages(tex_file):
    """
    在.tex文件中找到\documentclass后插入指定的语句
    """
    # 指定要插入的语句
    insert_text = r"""
\usepackage{fontspec, xunicode, xltxtra}
\setmainfont{Microsoft YaHei}
\usepackage{ctex}
"""
    # 读取原始.tex文件内容
    with open(tex_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 找到\documentclass所在行，并插入语句
    with open(tex_file, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if line.strip().startswith(r'\\documentclass'):
                file.write(insert_text)

    print(f"已成功修改文件：{tex_file}")


# 使用示例
tex_file_path = 'C.tex'  # 替换为你的.tex文件路径
insert_packages(tex_file_path)