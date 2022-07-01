# https://leetcode.com/contest/weekly-contest-287/problems/encrypt-and-decrypt-strings/
from collections import deque
from typing import Dict, List

_end = "_end_"

class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dict: List[str]):
        # self.dict = dictionary
        self.encoder = {}
        for key, value in zip(keys, values):
            self.encoder[key] = value

        self.decoder: Dict[List] = {}
        for key, value in zip(keys, values):
            if value in self.decoder:
                self.decoder[value].append(key)
            else:
                self.decoder[value] = [key]

        trie = {}
        for word in dict:
            current_dict = trie
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[_end] = _end
        self.trie = trie

    def encrypt(self, word1: str) -> str:
        return "".join(map(lambda x: self.encoder[x], word1))

    def decrypt(self, word2: str) -> int:
        word2 = [word2[i : i + 2] for i in range(0, len(word2), 2)]
        arr = [self.trie]
        for val in word2:
            if val not in self.decoder:
                return 0
            keys = self.decoder[val]
            tmp = []
            for key in keys:
                for trie in arr:
                    if key in trie:
                        tmp.append(trie[key])
            arr = tmp
        count = 0
        for trie in arr:
            count += _end in trie
        return count


keys = ["a", "b", "c", "d"]
values = ["ei", "zf", "ei", "am"]
dictionary = ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]

e = Encrypter(keys, values, dictionary)
print(e.encrypt("abcd"))
print(e.decrypt("eizfeiam"))

["Encrypter", "decrypt", "decrypt", "decrypt", "decrypt", "decrypt", "decrypt"]

keys = ["a", "b", "c", "z"]
values = ["aa", "bb", "cc", "zz"]
dictionary = ["aa", "aaa", "aaaa", "aaaaa", "aaaaaaa"]
e = Encrypter(keys, values, dictionary)
print(e.decrypt("aaaa"))
print(e.decrypt("aa"))
print(e.decrypt("aaaa"))
print(e.decrypt("aaaaaaaa"))
print(e.decrypt("aaaaaaaaaaaaaa"))
print(e.decrypt("aefagafvabfgshdthn"))
