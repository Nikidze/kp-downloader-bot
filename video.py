from typing import IO, Optional

import requests
import os.path


class Video:
    def __init__(self, link: str):
        self._video_stream: Optional[IO] = None
        self._video_path: str = ""
        self._link: str = link

    def stream(self) -> IO:
        self._find()
        return self._video_stream

    def is_exists(self) -> bool:
        return self._link != ""

    def _find(self):
        url_fragmnets = self._link.split('/')
        video_name = f'{url_fragmnets[-2]}_{url_fragmnets[-1]}'
        self._video_path = f'videos/{video_name}'

        if not os.path.exists(self._video_path):
            self._download()
        self._video_stream = open(self._video_path, 'rb')

    def _download(self):
        video = requests.get(self._link)
        open(self._video_path, 'wb').write(video.content)
