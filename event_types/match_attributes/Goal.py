from typing import Dict
from utils.khl_utils import KhlUtils
from datetime import datetime


class Goal:
    def __init__(self, goal_object: Dict, match_id: str):
        khl_utils = KhlUtils()
        self.match_id: str = match_id
        self.goal_id: int = int(goal_object.get('@id'))
        self.match_time: str = str(goal_object.get('@time'))
        self.player_id: str = str(goal_object.get('@player_id'))
        self.player_name: str = str(goal_object.get('@player_name'))
        self.title: str = str(goal_object.get('@title'))
        self.video_url: str = str(goal_object.get('@mp4_url'))
        self.image_url: str = str(goal_object.get('@img'))
        self.start_time_ms: int = int(goal_object.get('@start_ms'))
        self.start_time_date: datetime = khl_utils.milliseconds_to_date(milliseconds=self.start_time_ms)
        self.end_time_ms: int = int(goal_object.get('@finish_ms'))
        self.end_time_date: datetime = khl_utils.milliseconds_to_date(milliseconds=self.end_time_ms)

    def to_json(self):
        return {
            "match_id": self.match_id,
            "goal_id": self.goal_id
            # ToDo: остальные атрибуты дописать
        }
