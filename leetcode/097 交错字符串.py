"""
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true


输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
"""

def func(s1,s2,s3):
    l1 = list(s1)
    l2 = list(s2)
    l3 = list(s3)
