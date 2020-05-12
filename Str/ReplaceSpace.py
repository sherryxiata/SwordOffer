#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 19:56
# @Author  : wenlei

'''字符串：替换空格

请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

#解法1：直接替换

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

#解法4：从后往前插入（其实本题并不是考察replace的用法，而是考察算法）,用两个指针重组数组
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        p1 = len(s) - 1
        s_arr = list(s)
        for i in range(p1 + 1):
            if s_arr[i] == ' ':
                s_arr.append(' ')
                s_arr.append(' ')

        p2 = len(s_arr) - 1
        while p1 >= 0 and p2 > p1:
            if s_arr[p1] == ' ':
                s_arr[p2] = '0'
                p2 -= 1
                s_arr[p2] = '2'
                p2 -= 1
                s_arr[p2] = '%'
                p2 -= 1
            else:
                s_arr[p2] = s_arr[p1]
                p2 -= 1
            p1 -= 1
        return ''.join(s_arr)


if __name__ == '__main__':
    X = Solution()
    s = 'We Are Happy.'
    result = X.replaceSpace(s)
    print(result)

