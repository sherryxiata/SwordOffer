# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 19:56
# @Author  : wenlei

#字符串：替换空格

'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

#解法1：直接替换
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s_new = s.replace(' ','%20')
        return s_new

#解法2：遍历替换
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s_len = len(s)
        i = 0
        s_new = ''

        while(i < s_len):
            if s[i] == ' ':
                s_new = s_new + '%20'
            else:
                s_new = s_new + s[i]
            i += 1
        return s_new

#注意：空格是' '，不是''; 字符串连接用+

#解法3：正则表达式
import re
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s_new = re.sub(r' ', '%20', s)
        return s_new


if __name__ == '__main__':
    s = Solution()
    print(s.replaceSpace('hello world'))

