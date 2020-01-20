
from collections import defaultdict
import re


class TrieNode(object):

    def __init__(self, val=None):
        self.val = val
        self.children = {}


class Trie(object):

    def __init__(self, domains: str):
        self.domains = domains
        self.root = TrieNode(self.domains)

    def _pre_nodes(self, s: str) -> list:
        '''分割'''
        return s.replace(self.domains, "").split("/")

    def _current_regex_(self, nodes: str, pattern="d") -> str:
        nodes = nodes.replace(".", "\.").replace("?", "\?")
        if pattern == "w":
            cRegex = ".".join([re.sub("([a-zA-Z]+)", "\\\[a-zA-Z\\\]\\\+", node)
                               if not re.search("s?html?", node) else node for node in nodes.split(".")])
        else:
            cRegex = nodes
        return re.sub("\d+", "\\\d\\\+", cRegex)

    def _common_regex(self, keys: list) -> str:
        if len(keys) == 0:
            return ""
        counter = defaultdict(int)
        c = keys[0]
        pd = self._current_regex_(c, pattern="d")
        pw = self._current_regex_(c, pattern="w")
        for i in keys:
            if re.search(pd, i) or pd == i:
                counter[pd] += 1
            if re.search(pw.replace("\\", ""), i):
                counter[pw] += 1
        return pd if counter[pd] == counter[pw] else pw

    def add(self, s: str):
        """Add a string to this trie."""
        p = self.root
        nodes = self._pre_nodes(s)
        for i in range(len(nodes)):
            if nodes[i] not in p.children:
                new_node = TrieNode(nodes[i])
                p.children[nodes[i]] = new_node
                p = new_node
            else:
                p = p.children[nodes[i]]

    def category(self, root: TrieNode, pattern: str, res: list) -> str:
        if not root.children:
            if pattern not in res:
                res.append(pattern)
        children = root.children
        pattern += "/" + self._common_regex(list(children.keys()))
        for c in children:
            self.category(root=children[c], pattern=pattern, res=res)

    def extract(self):
        res = []
        self.category(self.root, pattern=self.root.val, res=res)
        return res


if __name__ == '__main__':
    trie = Trie("http://www.bjmy.gov.cn")
    trie.add('http://www.bjmy.gov.cn/col/col129/index.html')
    trie.add('http://www.bjmy.gov.cn/col/col3334/index.html')
    trie.add('http://www.bjmy.gov.cn/art/2020/1/2/art_2052_6.html')
    trie.add('http://www.bjmy.gov.cn/art/2020/1/2/art_2055_17.html')
    print(trie.extract())
