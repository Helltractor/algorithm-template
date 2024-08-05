# _*_ coding: utf-8 _*_
# @File : Trie.py
# @Time : 2023/12/10 21:42
# @Author : Helltractor
from collections import defaultdict


class Node:
    __slots__ = 'son', 'is_end'

    def __init__(self):
        # self.son = dict()
        self.son = defaultdict(Node)
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root  # 从根节点开始插入单词的字符
        for char in word:
            cur = cur.son[char]  # 移动到下一个节点
        cur.is_end = True  # 标记最后一个节点为单词的结尾

    def search(self, word: str) -> bool:
        cur = self.root  # 从根节点开始搜索单词
        for char in word:
            cur = cur.son.get(char)
            if cur is None:  # 如果字符不存在，单词不存在
                return False
            cur = cur.son[char]  # 移动到下一个节点
        return cur.is_end  # 返回最后一个节点是否标记为单词的结尾

    def startsWith(self, prefix: str) -> bool:  # 检查是否存在以给定前缀开头的单词
        cur = self.root
        for c in prefix:
            cur = cur.son.get(c)
            if cur is None:
                return False
        return True
