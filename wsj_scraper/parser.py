from .utils import now


def parse_thumbnails(soup):
    """
    Argument
    --------
    soup : bs4.BeautifulSoup
        BeautifulSoup format search result web page

    Returns
    -------
    thumbnails : list of dict
        Thumbnails of articles
        Each dict contains category, headline, author, url, summary, timestamp, scrap_time
    """

    def to_thumbnail(div):
        return {
            'category': parse_category(div),
            'headline': parse_headline(div),
            'author': parse_author(div),
            'url': parse_url(div),
            'summary': parse_summary(div),
            'timestamp': parse_timestamp(div),
            'scrap_time': now()
        }
    divs = soup.select('ul[class^=items] li[xmlns="http://www.w3.org/1999/html"]')
    thumbnails = [to_thumbnail(div) for div in divs]
    return thumbnails

def parse_category(thumbnail):
    try:
        return thumbnail.select('div[class=category]')[0].text.strip()
    except Exception as e:
        return ''

def parse_headline(thumbnail):
    try:
        return thumbnail.select('h3[class=headline]')[0].text.strip()
    except Exception as e:
        return ''

def parse_author(thumbnail):
    try:
        return thumbnail.select('li[class=byline]')[0].text.strip()
    except Exception as e:
        return ''

def parse_url(thumbnail):
    try:
        return 'https://www.wsj.com'+thumbnail.select('h3[class=headline] a')[0].attrs['href'].split('?')[0]
    except Exception as e:        
        return ''

def parse_summary(thumbnail):
    try:
        return thumbnail.select('div[class=summary-container]')[0].text.strip()
    except Exception as e:
        return ''

def parse_timestamp(thumbnail):
    try:
        return thumbnail.select('time[class^=date-stamp-container]')[0].text.strip()
    except Exception as e:
        return ''