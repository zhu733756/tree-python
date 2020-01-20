# **20200120 Add** [trie.py](https://github.com/zhu733756/tree-python/blob/master/trie.py)

## **example 1**
```
trie = Trie("http://www.bjmy.gov.cn")
trie.add('http://www.bjmy.gov.cn/col/col129/index.html')
trie.add('http://www.bjmy.gov.cn/col/col3334/index.html')
print(trie.extract())
```

## **results**:
```
['http://www.bjmy.gov.cn//col/col\\d\\+/index\\.html']
```

## **example 2**
```
trie = Trie("http://www.bjmy.gov.cn")
trie.add('http://www.bjmy.gov.cn/col/col129/index.html')
trie.add('http://www.bjmy.gov.cn/col/col3334/index.html')
trie.add('http://www.bjmy.gov.cn/art/2020/1/2/art_2052_6.html')
trie.add('http://www.bjmy.gov.cn/art/2020/1/2/art_2055_17.html')
print(trie.extract())
```

## **results**:
```
['http://www.bjmy.gov.cn//\\[a-zA-Z\\]\\+/col\\d\\+/index\\.html', 'http://www.bjmy.gov.cn//\\[a-zA-Z\\]\\+/\\d\\+/\\d\\+/\\d\\+/art_\\d\\+_\\d\\+\\.html']
```

