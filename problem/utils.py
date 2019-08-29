import re
from functools import lru_cache


TEMPLATE_BASE = """//声明部分开始
{}
//声明部分结束

//前台显示模板部分，开始
{}
//前台显示模板部分，结束

//追加代码部分，开始（可用来写主函数）
{}
//追加代码部分，结束（本注释及以上注释均不能删除）"""


@lru_cache(maxsize=100)
def parse_problem_template(template_str):
    prepend = re.findall(r"//声明部分开始\n([\s\S]+?)//声明部分结束", template_str)
    template = re.findall(r"//前台显示模板部分，开始\n([\s\S]+?)//前台显示模板部分，结束", template_str)
    append = re.findall(r"//追加代码部分，开始（可用来写主函数）\n([\s\S]+?)//追加代码部分，结束（本注释及以上注释均不能删除）", template_str)
    return {"prepend": prepend[0] if prepend else "",
            "template": template[0] if template else "",
            "append": append[0] if append else ""}


@lru_cache(maxsize=100)
def build_problem_template(prepend, template, append):
    return TEMPLATE_BASE.format(prepend, template, append)
