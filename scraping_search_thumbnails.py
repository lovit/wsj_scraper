import argparse
import json
import os
from wsj_scraper import yield_thumbnails_from_search_front


def save(json_obj, directory):
    timestamp = '-'.join(json_obj['timestamp'].split(' ')[:3])
    headline = json_obj['headline'][:30]
    filepath = '{}/{}_{}.json'.format(directory, timestamp, headline)
    with open(filepath, 'w', encoding='utf-8') as fp:
        json.dump(json_obj, fp, indent=2, ensure_ascii=False)

def scraping(query, begin_date, end_date, max_page, sleep, directory):
    for t, thumbnails in enumerate(yield_thumbnails_from_search_front(query, begin_date, end_date, max_page, sleep)):
        for i, thumbnail in enumerate(thumbnails):
            save(thumbnail, directory)
            print('page={} / news={}, title={}'.format(t, i, thumbnail['headline']))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, default='korea', help='Single term')
    parser.add_argument('--begin_date', type=str, default='2018/01/01', help='datetime YYYY/mm/dd')
    parser.add_argument('--end_date', type=str, default='2019/01/01', help='datetime YYYY/mm/dd')
    parser.add_argument('--directory', type=str, default='./output/', help='Output directory')
    parser.add_argument('--max_page', type=int, default=1000, help='Maximum number of pages to be scraped')
    parser.add_argument('--sleep', type=float, default=10, help='Sleep time for each submission (post)')

    args = parser.parse_args()
    query = args.query
    begin_date = args.begin_date
    end_date = args.end_date
    directory = args.directory
    max_page = args.max_page
    sleep = args.sleep

    # check output directory
    if not os.path.exists(directory):
        os.makedirs(directory)

    scraping(query, begin_date, end_date, max_page, sleep, directory)

if __name__ == '__main__':
    main()