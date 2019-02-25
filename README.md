# WSJ search result thumbnail scraper

Wall Street Journal (WSJ) 은 유로로 구독해야 하는 뉴스 사이트이기 때문에 본문은 스크래핑이 되지 않습니다. 

(*유로 계정으로는 확인하지 않았습니다.)

대신 뉴스 검색에서 특정 단어를 입력하면 해당 뉴스에 대한 뉴스 기사의 url 과 함께 summary 가 있는 thumbnail 을 얻을 수 있습니다. Thumbnail 에는 기사의 summary 와 title, 날짜가 포함되어 있기 때문에 이 정보만을 수집합니다.

날짜의 포멧은 `/` 으로 구분되어 있습니다.

```python
from wsj_scraper import yield_thumbnails_from_search_front

query = 'korea'
begin_date = '2015/01/01'
end_date = '2019/01/16'

for t, thumbnails in enumerate(yield_thumbnails_from_search_front(query, begin_date, end_date, max_page=2)):
    for i, thumbnail in enumerate(thumbnails):
        print('page={} / news={}, title={}'.format(t, i, thumbnail['headline']))
```

```
page=0 / news=0, title=Ivanka Trump to Help Select Nominee for World Bank President
page=0 / news=1, title=U.S. Stocks Slip on Signs of Slowing Economic Growth
page=0 / news=2, title=Jakarta, Manila Lead Recent Rebound in Emerging Asian Stocks
page=0 / news=3, title=Forced-Labor Dispute Strains Japan-South Korea Relations
page=0 / news=4, title=Only Nuclear Energy Can Save the Planet
page=0 / news=5, title=Samsung Faces Resistance From Big Pharma in the U.S.
page=0 / news=6, title=As Fed Fuels a Global Rally, Asian Currencies Lag Behind
page=0 / news=7, title=Politics May Trip Up Amazon and Walmart in India
page=0 / news=8, title=‘The Dictator’s Playbook’ Review: Tyranny 101
page=0 / news=9, title=North Korea Signals Desire to Resume Nuclear Talks With the U.S.—Energy Journal
page=0 / news=10, title=North Korea and China Project Unity in Face of Stalled Nuclear Talks With U.S.
page=0 / news=11, title=Xi Backs Trump-Kim Summit, Calls on Two Sides to Meet Halfway
page=0 / news=12, title=U.S.-China Trade Fight Shakes Global Economy, but Isn’t All Bad for Bystanders
page=0 / news=13, title=Samsung to Show Off Its New Foldable Phone in February
page=0 / news=14, title=State-Backed Hackers Sought and Stole Singapore Leader’s Medical Data
page=0 / news=15, title=Capital Journal: Border Wall Standoff Goes Prime Time; Rosenstein to Step Down; Syria Strategy Upended
page=0 / news=16, title=WSJ Wealth Adviser Briefing: Cash is King, Small Caps Shine, Slow Mornings
page=0 / news=17, title=The Daily Shot: Workers in Higher-Paying Sectors Are Increasingly Job-Hopping
page=0 / news=18, title=The U.S. Has Always Chosen World Bank Presidents—Will It This Time?
page=0 / news=19, title=MetLife CEO Steven Kandarian to Retire in April
yield thumbnails of first page
page=1 / news=0, title=North Korean Leader’s Beijing Visit Underscores China’s Pivotal Role
page=1 / news=1, title=U.S. Seeks To Bolster Nuclear Sector—Energy Journal
page=1 / news=2, title=Chinese Bond Yields Hit Two-Year Low
page=1 / news=3, title=Samsung Echoes Apple’s Gloomy Outlook as Tech Woes Get Worse
page=1 / news=4, title=Kim Jong Un Visits China on His Birthday
page=1 / news=5, title=As U.S. Footprint Shrinks, Others Happily Fill the Void
page=1 / news=6, title=U.S. Pushes China to Follow Through on Trade Promises
page=1 / news=7, title=Why the Chip Slump May Not Hurt Chip Investors
page=1 / news=8, title=Will Netanyahu Go to Riyadh?
page=1 / news=9, title=New House Committee Chiefs Take Their Chairs
page=1 / news=10, title=Corruption Currents: Former Colombian Anticorruption Director Jailed in U.S.
page=1 / news=11, title=The Future of Work Requires Investments in Human Capital
page=1 / news=12, title=Apple Beware: Samsung’s Great Fall in China Was Swift
page=1 / news=13, title=Apple Suppliers Slide in Asia as Investors Fret About Global Growth
page=1 / news=14, title=A Nuclear Battle Is Ahead in Congress
page=1 / news=15, title=Corruption Currents: Israeli Prosecutors to Indict Supermodel Bar Refaeli
page=1 / news=16, title=Capital Journal: House Democrats Plan Busy First Day; Apple’s Warning; The Tricky First Step to 2020
page=1 / news=17, title=North Korean Diplomat in Rome Disappears
page=1 / news=18, title=New Faces of 2019: Acting Chiefs Fill Cabinet Meeting
page=1 / news=19, title=My Predictions Are 2 for 3—Thanks, Oscar
yield thumbnails of 2 page
Terminated
```

```python
print(thumbnail)
```

```
{'author': 'By Karl Rove',
 'category': 'Commentary',
 'headline': 'My Predictions Are 2 for 3—Thanks, Oscar',
 'scrap_time': '2019-01-15 20:40:02',
 'summary': 'Plus a look ahead at 2019, from Mueller and impeachment to trade with China.',
 'timestamp': 'Jan. 2, 2019 6:53 pm ET',
 'url': 'https://www.wsj.com/articles/my-predictions-are-2-for-3thanks-oscar-11546473223'}
```

Using script

| argument | type | note |
| --- | --- | --- |
| query | str | 검색어 |
| begin_date | str | 검색 기간 시작 날짜. / 으로 분리 eg.) 2015/01/01 |
| end_date | str | 검색 기간 종료 날짜. / 으로 분리 eg.) 2015/01/01 |
| directory | str | 검색 결과 저장 폴더 기본값은 ./output |
| max_page | int | 최대 검색 페이지 |
| sleep | float | 매 페이지마다의 sleep time. 검색 결과가 작으므로 큰 값으로 설정. 기본값은 10 |

```
python scraping_search_thumbnails.py --begin_date 2019/01/20 --end_date 2019/02/25
```