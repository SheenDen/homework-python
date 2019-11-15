# -*- coding: utf-8 -*-
import aiml

# 创建Kernel()和 AIML 学习文件
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

demo_instruction = """
demo 演示：
     输入 hello   ->  输出 Well,hello
     输入 what are you  -> 输出 I'm a bot, silly!
     输入 以 reply * 开头文本  ->  随机回复
当输入 My hobby is pingpang
会输出 That is interesting that you have a hobby named pingpang
这时再输入 What is my hobby?
会回答 Your hobby is pingpang.

退出程序输入 exit

"""
print(demo_instruction)

while True:
    message = input("Enter your message: >> ")
    if message == "exit":
        exit()
    else:
        print(kernel.respond(message))