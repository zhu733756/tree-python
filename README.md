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
['http://www.bjmy.gov.cn/col/col\\d\\+/index\\.html']
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
['http://www.bjmy.gov.cn/\\[a-zA-Z\\]\\+/col\\d\\+/index\\.html', 'http://www.bjmy.gov.cn/\\[a-zA-Z\\]\\+/\\d\\+/\\d\\+/\\d\\+/art_\\d\\+_\\d\\+\\.html']
```


## **example 3**
```
print(from_csv("your-path-to-csv-file", encoding="gbk"))
```

## **results**:
```
eg:http://www.xinhuanet.com/
about 100 links
[('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/\\d\\+-\\d\\+/\\d\\+/\\[a-zA-Z\\]\\+_\\d\\+\\.htm', 48), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/\\d\\+-\\d\\+/\\d\\+/c_\\d\\+\\.htm', 29), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/\\[a-zA-Z\\]\\+\\.htm', 9), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/globe\\d\\+\\.htm', 6), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/\\[a-zA-Z\\]\\+', 4), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/\\[a-zA-Z\\]\\+/c_\\d\\+\\.htm', 2), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/\\d\\+-\\d\\+/\\d\\+/\\[a-zA-Z\\]\\+\\.htm', 2), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+', 2), ('http://www.xinhuanet.com/wzdt\\d\\+\\.htm', 2), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/\\[a-zA-Z\\]\\+/\\[a-zA-Z\\]\\+-\\[a-zA-Z\\]\\+\\.htm', 1), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/\\[a-zA-Z\\]\\+/\\[a-zA-Z\\]\\+_\\d\\+\\.htm', 1), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/\\d\\+-\\d\\+/\\d\\+/xczjc\\d\\+', 1), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/\\d\\+-\\d\\+/\\d\\+/xczjc\\d\\+/\\[a-zA-Z\\]\\+\\.htm', 1), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/xinhuaradio/\\[a-zA-Z\\]\\+\\.htm', 1), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/xinhuaradio/\\[a-zA-Z\\]\\+_\\d\\+\\.htm', 1), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/\\d\\+\\[a-zA-Z\\]\\+', 1), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/\\d\\+-\\d\\+/\\d\\+/\\[a-zA-Z\\]\\+\\d\\+\\.htm', 1), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/\\[a-zA-Z\\]\\+_\\d\\+\\.htm', 1), ('http://www.xinhuanet.com/\\[a-zA-Z\\]\\+/\\[a-zA-Z\\]\\+/\\[a-zA-Z\\]\\+\\.htm', 1)]
```


