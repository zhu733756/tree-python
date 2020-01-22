
from collections import defaultdict
import re
from dateparser.date import DateDataParser

date_format = [
    "(\d{4}[-|/|.]\d{1,2}[-|/|.]\d{1,2})",
]

url_patterns = ["\+", "\?", "#", "&", "=", "_"]


class TrieNode(object):

    def __init__(self, val=None):
        self.val = val
        self.children = {}


class Trie(object):

    def __init__(self, domains: str, keep=False):
        self.domains = domains if not domains.endswith("/") else domains[:-1]
        self.keep = keep
        self.root = TrieNode(self.domains)

    def _pre_nodes(self, s: str) -> list:
        '''split and keep date format with one node'''
        s = s.replace(self.domains + "/", "")
        for df in date_format:
            search = re.search(df, s)
            if search:
                matched = search.group(0)
                ns = s.split(matched)
                return ([ns[0].replace("/", "")] if ns[0] else []) + [matched] + ([ns[-1].replace("/", "")] if ns[-1] else [])
        else:
            return [n for n in s.split("/") if n]

    def _current_regex_(self, nodes: str, pattern="d") -> str:
        nodes = nodes.replace(".", "\.").replace("?", "\?")

        include_patterns = ""
        for p in url_patterns:
            if re.search(p, nodes):
                include_patterns += p

        node_list = []
        for node in nodes.split("."):
            cRegex = node
            if not re.search("s?html?", node):
                if pattern == "w":
                    cRegex = re.sub("([a-zA-Z]+)", "[a-zA-Z]+", cRegex)
                cRegex = re.sub("\d+", "\\\d+", cRegex)
                if include_patterns:
                    x = "".join(cRegex.split(include_patterns)).replace(
                        "+", "").replace("[", "").replace("]", "")
                    cRegex = f"[{x}{include_patterns}]+"
            node_list.append(cRegex)
        new_nodes = ".".join(node_list) 
        return new_nodes

    def _common_regex(self, keys: list) -> str:
        if len(keys) == 0:
            return ""
        if len(keys) == 1:
            return self._current_regex_(keys[0], pattern="w")
        counter = defaultdict(int)
        c = keys[0]
        pd = self._current_regex_(c, pattern="d")
        pw = self._current_regex_(c, pattern="w")
        for i in keys:
            if re.search(pd, i) or pd == i:
                counter[pd] += 1
            if re.search(pw, i):
                counter[pw] += 1
        return pd if counter[pd] >= counter[pw] else pw

    def add(self, s: str):
        """Add a string to this trie."""
        p = self.root
        nodes = [n for n in self._pre_nodes(s) if n]
        for i in range(len(nodes)):
            if nodes[i] not in p.children:
                new_node = TrieNode(nodes[i])
                p.children[nodes[i]] = new_node
                p = new_node
            else:
                p = p.children[nodes[i]]

    def category(self, root: TrieNode, pattern: str, res: defaultdict):
        '''if the node is a file-like node,pick it out;otherwise, let it go'''
        if not root.children:
            res[pattern] += 1
            return
        children = root.children
        # two buckets
        nan_file_keys, file_keys = [], []
        for key in children:
            if not re.search("\.?s?html?", key):
                nan_file_keys.append(key)
            else:
                file_keys.append(key)

        if nan_file_keys:
            nan_file_pattern = pattern + "/" + \
                self._common_regex(nan_file_keys)
            for c in nan_file_keys:
                self.category(root=children[c],
                              pattern=nan_file_pattern, res=res)
        if file_keys:
            file_pattern = pattern + "/" + self._common_regex(file_keys)
            for c in file_keys:
                res[file_pattern] += 1

    def extract(self, nums=5) -> list:
        '''
        return the top nums of the results
        nums:int
        '''
        res = defaultdict(int)
        if self.keep:
            # keep first node
            for c in self.root.children:
                self.category(self.root.children[
                              c], pattern=self.root.val + "/" + c, res=res)
        else:
            self.category(self.root, pattern=self.root.val, res=res)
        return sorted(res.items(), key=lambda x: x[1], reverse=True)[:nums]

    def search(self, s) -> bool:
        if not s:
            return False
        nodes = [n for n in self._pre_nodes(s) if n]
        p = self.root.children
        for node in nodes:
            if node not in p:
                return False
            p = p[node].children
        return True


def from_csv(path, encoding="utf-8"):
    import pandas as pd
    try:
        target = list(
            set(pd.read_csv(path, encoding=encoding).loc[:, "link"].values))
        trie = Trie("http://" + target[0].split("/")[2])
        for link in target:
            trie.add(link)
        else:
            return trie.extract(nums=100)
    except Exception as e:
        print(e.args)


if __name__ == '__main__':
    # trie = Trie("http://www.bjmy.gov.cn",keep=True)
    # trie.add('http://www.bjmy.gov.cn/col/col129/index.html')
    # trie.add('http://www.bjmy.gov.cn/col/col3334/index.html')
    # trie.add('http://www.bjmy.gov.cn/art/2020/1/2/art_2052_6.html')
    # trie.add('http://www.bjmy.gov.cn/art/2020/1/2/art_2055_17.html')
    # print(trie.extract())
    # print(trie.search('http://www.bjmy.gov.cn/artwewqewq/2020/1/2/art_2055_15555.html'))
    print(from_csv("C:\\Users\\Lenovo\\Desktop\\core_urls_category.csv", encoding="gbk"))
