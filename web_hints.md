# Records / Experiences

1. 網頁版直接回傳網頁、甚至不同的 Tab 不同的回傳方式(需考慮到對方網站可能也是經過多次修改)
   1. 例如 Tab A 是回傳 html、Tab B 是回傳 json
2. 可以切換到手機版，往下拉，去捕捉 feed 相關的 api
3. 開發者工具的 filter 可以搜尋一些特定關鍵字，例如 `data`, `json`, `graphql`, `api`, `page`, `feed` 來全文檢索，協助減少要看的 endpoint
4. 有些好用的 chrome extension - [`json viewer`](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh)

# Yahoo Movies

1. Mobile - https://movies.yahoo.com.tw/movie_comingsoon.html?page=2
2. API - https://movies.yahoo.com.tw/ajax/more_coming_soon?type=movies&page=3
   * landing 後將 event 清空 
   * 透過手機版下拉、找到 endpoint，透過 json viewer 確認 API 回傳內容 

# JustWatch

1. Mobile - https://www.justwatch.com/tw
2. API - https://apis.justwatch.com/graphql
   * landing 後將 event 清空 
   * 透過手機版下拉、找到 endpoint，看 response 之後確認資料
   * GraphQL 是另一種直接從前端 query 拉取到資料的方式(通常需要後端架構的配合)
