# Ref

* [python爬虫BeautifulSoup和Lxml性能对比](https://zhuanlan.zhihu.com/p/87193823)
* [簡單比較 BeautifulSoup 和 Xpath 的效能](https://www.796t.com/content/1546959607.html)
* [xpath selector](https://docs.scrapy.org/en/latest/topics/selectors.html)


parser|performance|easy to use?|how to fetch?|
------|-----------|------------|-------------|
re|fast|hard|re|
beautifulsoup|fast if use lxml|easy|find, css selector|
lxml|fast(written in C)|easy|XPath, css selector|

# XPath

[XPath Wiki](https://zh.wikipedia.org/zh-tw/XPath)

1. XML 路徑語言 (XML Path Language)，一種用來確定 XML 檔案中某部分位置的電腦語言
2. XPath 基於 XML 樹狀結構，提供資料結構樹中尋找節點的能力，起初 Xpath 提出的初衷是將其作為一個通用的、介於XPointer與XSL之間的語法模型

## 常用路徑表達式
expr|description|example|means|
----|-----------|-------|-----|
nodename|選取nodename節點的所有子節點|xpath('//div')|選取了div節點的所有子節點|
`/`|從跟節點選取|xpath('/div')|從跟節點上選取div節點|
`//`|選取所有當前節點，不考慮他們的位置|xpath('//div')|選取所有div節點|
`.`|選取當前節點|xpath('./div')|選取當前節點下的div節點
`..`|選取當前節點的父節點|xpath('..')|回到上一個節點
`@`|選取屬性|xpath('//@class')|選取所有的class屬性

## 謂語

`[]` : 用於查找某個特定節點或包含某個自訂值的節點

|example|means|
|-------|-----|
`xpath('/body/div[1]')`|選取body下的第一個div節點|
`xpath('/body/div[last()]')`|選取body下的最後一個div節點|
`xpath('/body/div[last()-1]')`|選取body下的倒數第2個div節點|
`xpath('/body/div[position()<3]')`|選取body下的前兩個div節點|
`xpath('/body/div[@class]')`|選取body下帶有class屬性的div節點|
`xpath('/body/div[@class="main"]')`|選取body下帶有class屬性為main的div節點|
`xpath('/body/div[@price>35.00]')`|選取body下price元素值 > 35 的 div節點|

## 通用符號

|example|means|
|-------|-----|
|xpath('/div/*')|div下的所有子節點|
|xpath('/div[@*]')|所有帶有屬性的div節點|
|xpath('//div|//table')|所有div和table節點|

## Xpath 軸

|軸名稱|表達式|
|-------|-----|
|xpath('/div/*')|div下的所有子節點|
|xpath('/div[@*]')|所有帶有屬性的div節點|
|xpath('//div|//table')|所有div和table節點|

...

pass

## 功能函數


|函數|用法|解釋|
|---|----|---|
|starts-with|xpath('//div[starts-with(@id,"ma")]')|選取id值以ma開頭的div節點|
|contains|xpath('//div[contains(@id, "ma")]')|選取id值包含ma的div節點|
|and|xpath('//div[contains(@id),"ma"] and contains(@id, "in")')|選取id值包含ma和in的div節點|
|text()|xpath('//div[contains(text(), "ma")]')|選取節點文本包含ma的div節點


