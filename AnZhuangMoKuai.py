import subprocess

# 定义要安装的模块列表
modules_to_install = ["requests", "pyside6", "playsound"]

# 构造安装命令，将每个模块名称作为单独的参数
install_command = ["pip", "install"] + modules_to_install

# 使用subprocess.run()运行安装命令
result = subprocess.run(install_command, capture_output=True, text=True)

# 检查安装结果
if result.returncode == 0:
    print("所有模块安装成功！")
    print("输出信息：")
    print(result.stdout)
else:
    print("模块安装失败！")
    print("错误信息：")
    print(result.stderr)