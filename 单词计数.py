f = open("python.txt")
# 方式一：读取全部内容，通过字符串count方法统计Itheima单词数量
content = f.read()
count = content.count("itheima")
print(f"itheima在文件中出现了：{count}次")