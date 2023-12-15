from typing import Dict
from datetime import datetime
from utils.khl_utils import KhlUtils


class Penalty:
    def __init__(self, penalty_object: Dict, match_id: str):
        khl_utils = KhlUtils()
        self.match_id: str = match_id
        self.penalty_id: int = int(penalty_object.get('@id'))
        self.match_time: str = str(penalty_object.get('@time'))
        self.player_id: str = str(penalty_object.get('@player_id'))
        self.player_name: str = str(penalty_object.get('@player_name'))
        self.title: str = str(penalty_object.get('@title'))
        self.video_url: str = str(penalty_object.get('@mp4_url'))
        self.image_url: str = str(penalty_object.get('@img'))
        self.start_time_ms: int = int(penalty_object.get('@start_ms'))
        self.start_time_date: datetime = khl_utils.milliseconds_to_date(milliseconds=self.start_time_ms)
        self.end_time_ms: int = int(penalty_object.get('@finish_ms'))
        self.end_time_date: datetime = khl_utils.milliseconds_to_date(milliseconds=self.end_time_ms)

    def to_json(self):
        return {
            "match_id": self.match_id,
            "penalty_id": self.penalty_id,
            "match_time": self.match_time,
            "player_id": self.player_id,
            "player_name": self.player_name,
            "title": self.title,
            "video_url": self.video_url,
            "image_url": self.image_url,
            "start_time_ms": self.start_time_ms,
            "start_time_date": self.start_time_date,
            "end_time_ms": self.end_time_ms,
            "end_time_date": self.end_time_date
        }
