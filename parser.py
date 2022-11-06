import requests
from bs4 import BeautifulSoup
from video import Video


def _parse_video_link(article_link: str) -> str:
    response = requests.get(article_link)
    bs = BeautifulSoup(response.text, 'html.parser')
    video_block = bs.find('div', attrs={'data-content-type': 'video'})
    if not video_block:
        return ""
    return video_block['data-content-src']


def get_video(article_link: str) -> Video:
    return Video(_parse_video_link(article_link))
