import difflib
def get_equal_rate(str1, str2):
   return difflib.SequenceMatcher(None, str1, str2).quick_ratio()

if __name__ == "__main__":
    url1="http://www.bjmy.gov.cn/art/2020/1/2/art_2051_4.html"
    url2="http://www.bjmy.gov.cn/art/2020/1/6/art_4191_93795.html"
    print(get_equal_rate(url1,url2))