import math
import time
from .utils import get_soup
from .parser import parse_thumbnails

def yield_thumbnails_from_search_front(query, begin_date, end_date, max_page=10, sleep=5):
    """
    query: str
        single term
    begin_date : str
        2015/01/01 form
    end_date : str
        2015/01/13 form
    max_page : int
        Maximum number of page
    sleep : float
        Sleep time
    
    """

    search_url_base = 'https://www.wsj.com/search/term.html?KEYWORDS={}&min-date={}&max-date={}&daysback=4y&isAdvanced=true&andor=AND&sort=date-desc&source=wsjarticle,wsjblogs,wsjvideo,interactivemedia,sitesearch,wsjpro&page={}'
    url = search_url_base.format(query, begin_date, end_date, 1)
    soup = get_soup(url)
    max_page_ = to_max_page(get_num_search_result(soup))
    max_page = min(max_page, max_page_)

    if max_page_ == 0:
        print('Not found search result')
        return

    yield parse_thumbnails(soup)
    print('yield thumbnails of first page')

    for page in range(2, max_page + 1):
        time.sleep(sleep)
        url = search_url_base.format(query, begin_date, end_date, page)
        soup = get_soup(url)
        yield parse_thumbnails(soup)
        print('yield thumbnails of {} page'.format(page))
    print('Terminated')

def get_num_search_result(soup):
    try:
        num_news = soup.select('div[class^=results-menu-wrapper] menu[class=results] li[class=results-count]')[0].text.split(' ')[-1]
        return int(num_news)
    except Exception as e:
        return 0

def to_max_page(num):
    return math.ceil(num/20)