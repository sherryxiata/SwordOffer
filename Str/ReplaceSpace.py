#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 19:56
# @Author  : wenlei

'''字符串：替换空格

请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

# 解法1：直接替换

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s1 = s.replace(' ','%20')
        return s1

# 解法2：遍历替换

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s1 = ''
        n = len(s)
        for i in range(n):
            if s[i] == ' ':
                s1 += '%20'
            else:
                s1 += s[i]
        return s1

#注意：空格是' '，不是''; 字符串连接用+

#解法3：正则表达式

import re
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s1 = re.sub(r' ', '%20', s)
        return s1


if __name__ == '__main__':
    X = Solution()
    s = 'We Are Happy.'
    result = X.replaceSpace(s)
    print(result)

