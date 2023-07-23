# D A Y F I F T Y T H R E E

[[zillow source]]

| #  | Requirements                    |
|----|---------------------------------|
| 1. | Research house prices on zillow |
| 2. | Get price, address and listing URL |
| 3. | Transfer data to a form         |
| 4. | Add data to a google sheet      |
| 5. | Have fun!                       |

it has something to do with this:
```html
https://www.zillow.com/homes/for_rent/?searchQueryState={"pagination":{},"mapBounds":{"west":-78.66288185119629,"east":-78.52795600891113,"south":35.82686045503001,"north":35.913801042853265},"isMapVisible":false,
```

pagination is the key?

use the `uncurl` library to convert from browser requests to something the requests pkg can understand. devtools -> network -> copy -> curl

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