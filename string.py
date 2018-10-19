str = 'this is a string'
# 默认使用空格分割
print("默认使用空格分隔：%s" % str.split())
# 定义分割的数量
print("控制分割量为1：%s" % str.split(maxsplit=1))
# 获取数组的长度
print("获取数组的长度：%d" % str.split().__len__())
# 拼接字符串
print("原字符串:" ,str, ",使用切片反转后字符串:",str[::-1])
# 格式化输出
print("输出字符串% s" % str)
print("%s输出字符串:%s" % ('两个参数', str))

# 快速生成1-10的数组，range(1, 11)包含1不包含11
numlist = list(range(1, 11))
print('rang(1,11) 包含1不包含11: %s' % numlist)
# range(11)从0开始不包含11
numlist = list(range(11))
print('rang(11) 从0开始不包含11：%s' % numlist)

# 切片 [start:end:step]
# 全部输出
print("numlist：", numlist[:])
# 最后一项
print("最后一项：", numlist[-1])
# 从0到2，不包括2
print("从0到2，不包括2：", numlist[0:2])
# 从0到5，不包括5
print("从0到5，不包括5：", numlist[:5])
# 输出最后5项
print("输出最后5项：", numlist[-5:])
# 步长为5，每隔4项输出1项
print("步长为5，每隔4项输出1项：", numlist[::5])
# 反转字符串和数组
print("反转字符串和数组：", numlist[::-1])

# 1到10的偶数
print("1-10间的偶数:",[x for x in range(1, 11) if x % 2 == 0])
# 1到10间偶数的平方
print("1-10间偶数的平方:",[x * x for x in range(1, 11) if x % 2 == 0])
