from typing import Dict
from utils.khl_utils import KhlUtils
from datetime import datetime


class Highlight:
    def __init__(self, highlight_object: Dict, match_id: str):
        khl_utils = KhlUtils()
        self.match_id: str = match_id
        self.summary_id: int = int(highlight_object.get('@id'))
        self.match_time: str = str(highlight_object.get('@time'))
        self.title: str = str(highlight_object.get('@title'))
        self.video_url: str = str(highlight_object.get('@mp4_url'))
        self.image_url: str = str(highlight_object.get('@img'))
        self.start_time_ms: int = int(highlight_object.get('@start_ms'))
        self.start_time_date: datetime = khl_utils.milliseconds_to_date(milliseconds=self.start_time_ms)
        self.end_time_ms: int = int(highlight_object.get('@finish_ms'))
        self.end_time_date: datetime = khl_utils.milliseconds_to_date(milliseconds=self.end_time_ms)

    def to_json(self):
        return {
            "match_id": self.match_id,
            "summary_id": self.summary_id,
            "match_time": self.match_time,
            "title": self.title,
            "video_url": self.video_url,
            "image_url": self.image_url,
            "start_time_ms": self.start_time_ms,
            "start_time_date": self.start_time_date,
            "end_time_ms": self.end_time_ms,
            "end_time_date": self.end_time_date
        }
