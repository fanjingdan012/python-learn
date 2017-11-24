import urllib.request
import json
import eastmoneyStockList
import readStockList
def getHeaders ():
    return {#'X-Requested-With': 'XMLHttpRequest',
           #'Referer': 'http://xueqiu.com/p/ZH010389',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
           #'Host': 'xueqiu.com',
           #'Connection':'keep-alive',
           #'Accept':'*/*',
           'cookie':'xq_a_token=a8d434ddd975f5752965fa782596bd0b5b008376; xq_a_token.sig=ke78qTMMk1J4blZPe-jY53Uy9Ec; xq_r_token=437547d929e3cc54630bfd58136879694e1ae4a9; xq_r_token.sig=iYuNwCitZuVpyfkOu6_LLtaQn6E; s=et11okl5s2; u=811511157993130; device_id=da9025ffdb657b9460445f57e7be5368; aliyungf_tc=AQAAADToGVkdRgIACbB+3oLvs1StU/PX; __utma=1.800988467.1511158014.1511339632.1511406223.5; __utmc=1; __utmz=1.1511158014.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1511157995,1511226946,1511233574,1511329392; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1511406315'
    }
def getData(shOrSz,rangeStart,rangeEnd,urlPattern):
    XUEQIU_DOMAIN='https://xueqiu.com'
    headers = getHeaders()
    stockList = readStockList.readStockList(shOrSz,rangeStart,rangeEnd)
    print(stockList)
    results = []
    for stock in stockList:
        result=[]
        url = XUEQIU_DOMAIN+urlPattern+'?symbol=' + stock+'&size=100&page='+page
        print(url)
        result.append(url)
        req = urllib.request.Request(url, headers=headers)
        content = urllib.request.urlopen(req).read().decode('utf-8')
        print(content)
        result.append(content)
        results.append(result)
    return results

def getFieldColDict(workbook):
    fieldColDict = dict()
    oldSheet = workbook.sheet_by_index(0)
    if (shOrSz == 'SZ'):
        oldSheet = workbook.sheet_by_index(1)
    for col in range(oldSheet.ncols):
        fieldColDict[oldSheet.cell_value(0, col)] = col
    return fieldColDict
