# D A Y F I F T Y T H R E E

[[zillow source]]

| #  | Requirements                    |
|----|---------------------------------|
| 1. | Research house prices on zillow |
| 2. | Get price, address and listing URL |
| 3. | Transfer data to a form         |
| 4. | Add data to a google sheet      |
| 5. | Have fun!                       |

request example:
```cmd
curl "https://www.zillow.com/raleigh-nc/rentals/" ^
  -H "authority: www.zillow.com" ^
  -H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" ^
  -H "accept-language: en-US,en;q=0.9" ^
  -H "cache-control: no-cache" ^
  -H "cookie: zguid=24^|^%^242fd81c75-a7eb-4517-ac9b-06cf624b83b0; zgsession=1^|28a5e2e7-4ad0-400a-979f-a6aa28cab08c; zjs_anonymous_id=^%^222fd81c75-a7eb-4517-ac9b-06cf624b83b0^%^22; zjs_user_id=null; zg_anonymous_id=^%^22498a8667-b89b-4acb-9346-032c978ae200^%^22; pxcts=749d91aa-2814-11ee-a5ad-414746486b52; _pxvid=749d82bf-2814-11ee-a5ad-182dd0262840; JSESSIONID=A58A0BFAB2292CE2DDEEC524944293B7; search=6^|1692573393251^%^7Crect^%^3D33.605858864133445^%^252C-86.5147698271654^%^252C33.24769256121517^%^252C-87.05447319630602^%^26rid^%^3D73386^%^26disp^%^3Dmap^%^26mdm^%^3Dauto^%^26p^%^3D1^%^26z^%^3D1^%^26listPriceActive^%^3D1^%^26fs^%^3D1^%^26fr^%^3D0^%^26mmm^%^3D0^%^26rs^%^3D0^%^26ah^%^3D0^%^26singlestory^%^3D0^%^26housing-connector^%^3D0^%^26abo^%^3D0^%^26garage^%^3D0^%^26pool^%^3D0^%^26ac^%^3D0^%^26waterfront^%^3D0^%^26finished^%^3D0^%^26unfinished^%^3D0^%^26cityview^%^3D0^%^26mountainview^%^3D0^%^26parkview^%^3D0^%^26waterview^%^3D0^%^26hoadata^%^3D1^%^26zillow-owned^%^3D0^%^263dhome^%^3D0^%^26featuredMultiFamilyBuilding^%^3D0^%^26commuteMode^%^3Ddriving^%^26commuteTimeOfDay^%^3Dnow^%^09^%^0973386^%^09^%^7B^%^22isList^%^22^%^3Atrue^%^2C^%^22isMap^%^22^%^3Atrue^%^7D^%^09^%^09^%^09^%^09^%^09; AWSALB=Yn5H4/1ZSj5ZUD4AvxcZu4YwS6L4B6w9JrnA0ZTLrBT+0c67bVdfbMCHIjAhvY/k/lBrFf1y7r89xvPL3o5yJRyyOqsu1H7Y8ooKudG/ykD3xvfdZVh7uKZ04IjJ; AWSALBCORS=Yn5H4/1ZSj5ZUD4AvxcZu4YwS6L4B6w9JrnA0ZTLrBT+0c67bVdfbMCHIjAhvY/k/lBrFf1y7r89xvPL3o5yJRyyOqsu1H7Y8ooKudG/ykD3xvfdZVh7uKZ04IjJ" ^
  -H "dnt: 1" ^
  -H "pragma: no-cache" ^
  -H "sec-ch-ua: ^\^"Not.A/Brand^\^";v=^\^"8^\^", ^\^"Chromium^\^";v=^\^"114^\^", ^\^"Google Chrome^\^";v=^\^"114^\^"" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
  -H "sec-fetch-dest: document" ^
  -H "sec-fetch-mode: navigate" ^
  -H "sec-fetch-site: none" ^
  -H "sec-fetch-user: ?1" ^
  -H "upgrade-insecure-requests: 1" ^
  -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" ^
  --compressed
```

use the `uncurl` library to convert from browser requests to something the requests pkg can understand

first 10 elements scraped by selector: `#grid-search-results ul li`:
```python

item 0 has 2 prices in it.
['1,359+ 1 bd', '1,614+ 2 bds Three Dimensional 3D TourPrevious photoChevron LeftNext photoChevron RightUse arrow keys to navigateImage 1 of 44Save this home']
1,359
1,614
item 1 has 1 prices in it.
['1,614+ 2 bds']
1,614
item 2 has 2 prices in it.
['1,302+ 1 bd', '1,435+ 2 bds Previous photoChevron LeftNext photoChevron RightUse arrow keys to navigateImage 1 of 36Save this home']
1,302
1,435
item 3 has 1 prices in it.
['1,435+ 2 bds']
1,435
item 4 has 0 prices in it.
[]
item 5 has 3 prices in it.
['1,278+ 1 bd', '1,453+ 2 bds', '1,649+ 3 bds Updated yesterdayPrevious photoChevron LeftNext photoChevron RightUse arrow keys to navigateImage 1 of 12Save this home']
1,278
1,453
1,649
item 6 has 1 prices in it.
['1,453+ 2 bds']
1,453
item 7 has 1 prices in it.
['1,649+ 3 bds']
1,649
item 8 has 3 prices in it.
['1,500+ 1 bd', '2,150+ 2 bds', '2,600+ 3 bds Three Dimensional 3D TourPrevious photoChevron LeftNext photoChevron RightUse arrow keys to navigateImage 1 of 42Save this home']
1,500
2,150
2,600
item 9 has 1 prices in it.
['2,150+ 2 bds']
2,150
```