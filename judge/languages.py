from problem.models import ProblemIOMode


default_env = ["LANG=en_US.UTF-8", "LANGUAGE=en_US:en", "LC_ALL=en_US.UTF-8"]

_c_lang_config = {
    "template": """//声明部分开始（本注释及以下注释均不能删除）
#include <stdio.h>
//声明部分结束

//前台显示模板部分，开始
int add(int a, int b) {
  // Please fill this blank
  return ___________;
}
//前台显示模板部分，结束

//追加代码部分，开始（可用来写主函数）
int main() {
  printf("%d", add(1, 2));
  return 0;
}
//追加代码部分，结束（本注释及以上注释均不能删除）""",
    "compile": {
        "src_name": "main.c",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 10000,
        "max_memory": 256 * 1024 * 1024,
        "compile_command": "/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c11 {src_path} -lm -o {exe_path}",
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": {ProblemIOMode.standard: "c_cpp", ProblemIOMode.file: "c_cpp_file_io"},
        "env": default_env
    }
}

_c_lang_spj_compile = {
    "src_name": "spj-{spj_version}.c",
    "exe_name": "spj-{spj_version}",
    "max_cpu_time": 3000,
    "max_real_time": 10000,
    "max_memory": 1024 * 1024 * 1024,
    "compile_command": "/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c11 {src_path} -lm -o {exe_path}"
}

_c_lang_spj_config = {
    "exe_name": "spj-{spj_version}",
    "command": "{exe_path} {in_file_path} {user_out_file_path}",
    "seccomp_rule": "c_cpp"
}

_cpp_lang_config = {
    "template": """//声明部分开始
#include <iostream>
//声明部分结束

//前台显示模板部分，开始
int add(int a, int b) {
  // Please fill this blank
  return ___________;
}
//前台显示模板部分，结束

//追加代码部分，开始（可用来写主函数）
int main() {
  std::cout << add(1, 2);
  return 0;
}
//追加代码部分，结束（本注释及以上注释均不能删除）""",
    "compile": {
        "src_name": "main.cpp",
        "exe_name": "main",
        "max_cpu_time": 10000,
        "max_real_time": 20000,
        "max_memory": 1024 * 1024 * 1024,
        "compile_command": "/usr/bin/g++ -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c++14 {src_path} -lm -o {exe_path}",
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": {ProblemIOMode.standard: "c_cpp", ProblemIOMode.file: "c_cpp_file_io"},
        "env": default_env
    }
}

_cpp_lang_spj_compile = {
    "src_name": "spj-{spj_version}.cpp",
    "exe_name": "spj-{spj_version}",
    "max_cpu_time": 10000,
    "max_real_time": 20000,
    "max_memory": 1024 * 1024 * 1024,
    "compile_command": "/usr/bin/g++ -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c++14 {src_path} -lm -o {exe_path}"
}

_cpp_lang_spj_config = {
    "exe_name": "spj-{spj_version}",
    "command": "{exe_path} {in_file_path} {user_out_file_path}",
    "seccomp_rule": "c_cpp"
}

_java_lang_config = {
    "template": """//声明部分开始
//声明部分结束

//前台显示模板部分，开始
//前台显示模板部分，结束

//追加代码部分，开始（可用来写主函数）
//追加代码部分，结束（本注释及以上注释均不能删除）""",
    "compile": {
        "src_name": "Main.java",
        "exe_name": "Main",
        "max_cpu_time": 5000,
        "max_real_time": 10000,
        "max_memory": -1,
        "compile_command": "/usr/bin/javac {src_path} -d {exe_dir} -encoding UTF8"
    },
    "run": {
        "command": "/usr/bin/java -cp {exe_dir} -XX:MaxRAM={max_memory}k -Djava.security.manager -Dfile.encoding=UTF-8 "
                   "-Djava.security.policy==/etc/java_policy -Djava.awt.headless=true Main",
        "seccomp_rule": None,
        "env": default_env,
        "memory_limit_check_only": 1
    }
}


_py2_lang_config = {
    "template": """//声明部分开始
//声明部分结束

//前台显示模板部分，开始
//前台显示模板部分，结束

//追加代码部分，开始（可用来写主函数）
//追加代码部分，结束（本注释及以上注释均不能删除）""",
    "compile": {
        "src_name": "solution.py",
        "exe_name": "solution.pyc",
        "max_cpu_time": 3000,
        "max_real_time": 10000,
        "max_memory": 128 * 1024 * 1024,
        "compile_command": "/usr/bin/python -m py_compile {src_path}",
    },
    "run": {
        "command": "/usr/bin/python {exe_path}",
        "seccomp_rule": "general",
        "env": default_env
    }
}
_py3_lang_config = {
    "template": """//声明部分开始
//声明部分结束

//前台显示模板部分，开始
//前台显示模板部分，结束

//追加代码部分，开始（可用来写主函数）
//追加代码部分，结束（本注释及以上注释均不能删除）""",
    "compile": {
        "src_name": "solution.py",
        "exe_name": "__pycache__/solution.cpython-35.pyc",
        "max_cpu_time": 3000,
        "max_real_time": 10000,
        "max_memory": 128 * 1024 * 1024,
        "compile_command": "/usr/bin/python3 -m py_compile {src_path}",
    },
    "run": {
        "command": "/usr/bin/python3 {exe_path}",
        "seccomp_rule": "general",
        "env": default_env + ["PYTHONIOENCODING=utf-8"]
    }
}

languages = [
    {"config": _c_lang_config, "spj": {"compile": _c_lang_spj_compile, "config": _c_lang_spj_config},
     "name": "C", "description": "GCC 5.4", "content_type": "text/x-csrc"},
    {"config": _cpp_lang_config, "spj": {"compile": _cpp_lang_spj_compile, "config": _cpp_lang_spj_config},
     "name": "C++", "description": "G++ 5.4", "content_type": "text/x-c++src"},
    {"config": _java_lang_config, "name": "Java", "description": "OpenJDK 1.8", "content_type": "text/x-java"},
    {"config": _py2_lang_config, "name": "Python2", "description": "Python 2.7", "content_type": "text/x-python"},
    {"config": _py3_lang_config, "name": "Python3", "description": "Python 3.5", "content_type": "text/x-python"},
]
