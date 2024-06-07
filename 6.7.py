'''f = open('python.txt', 'r', encoding='UTF-8')
content = f.readlines()
# ['hello world\n', ' abcdefg\n', ’aaa\n'， 'bbb\n'. 'ccc']
print(content)
# 关闭文件
f.close()


f = open('python.txt')
content = f.readline()
print(f'第一行：(content)')
content = f.readline()
print(f'第二行：(content)')
#关闭文件
f.close()


for line in open("python.txt"):
    print(line)
with open("python.txt","r") as f:
    f.readlines()'''


f = open("python.txt")
# 方式一：读取全部内容，通过字符串count方法统计Itheima单词数量
content = f.read()
count = content.count("itheima")
print(f"itheima在文件中出现了：{count}次")