from typing import Dict
from utils.milliseconds_to_date import milliseconds_to_date
from datetime import datetime


class Goal:
    def __init__(self, goal_object: Dict, match_id: str):
        self.match_id: str = match_id

        self.goal_id: int = int(goal_object.get('@id'))
        self.match_time: str = str(goal_object.get('@time'))
        self.player_id: str = str(goal_object.get('@player_id'))
        self.player_name: str = str(goal_object.get('@player_name'))
        self.title: str = str(goal_object.get('@title'))
        self.video_url: str = str(goal_object.get('@mp4_url'))
        self.image_url: str = str(goal_object.get('@img'))
        self.start_time_ms: int = int(goal_object.get('@start_ms'))
        self.start_time_date: datetime = milliseconds_to_date(milliseconds=self.start_time_ms)
        self.end_time_ms: int = int(goal_object.get('@finish_ms'))
        self.end_time_date: datetime = milliseconds_to_date(milliseconds=self.end_time_ms)

    def to_json(self):
        return {
            "match_id": self.match_id,
            "goal_id": self.goal_id
            # ToDo: остальные атрибуты дописать
        }
class Pn:
    def __init__(self, pn_object: Dict, match_id: str):
        self.match_id: str = match_id

        self.pn_id: int = int(pn_object.get('@id'))
        self.pn_time: str = str(pn_object.get('@time'))
        self.player_id: str = str(pn_object.get('@player_id'))
        self.player_name: str = str(pn_object.get('@player_name'))
        self.title: str = str(pn_object.get('@title'))
        self.video_url: str = str(pn_object.get('@mp4_url'))
        self.image_url: str = str(pn_object.get('@img'))
        self.start_time_ms: int = int(pn_object.get('@start_ms'))
        self.start_time_date: datetime = milliseconds_to_date(milliseconds=self.start_time_ms)
        self.end_time_ms: int = int(pn_object.get('@finish_ms'))
        self.end_time_date: datetime = milliseconds_to_date(milliseconds=self.end_time_ms)

    def to_json(self):
        return {
            "match_id": self.match_id,
            "pn_id": self.pn_id}
class Summary:
    def __init__(self, sum_object: Dict, match_id: str):
        self.match_id: str = match_id

        self.sum_id: int = int(sum_object.get('@id'))
        self.sum_time: str = str(sum_object.get('@time'))
        self.title: str = str(sum_object.get('@title'))
        self.video_url: str = str(sum_object.get('@mp4_url'))
        self.image_url: str = str(sum_object.get('@img'))
        self.start_time_ms: int = int(sum_object.get('@start_ms'))
        self.start_time_date: datetime = milliseconds_to_date(milliseconds=self.start_time_ms)
        self.end_time_ms: int = int(sum_object.get('@finish_ms'))
        self.end_time_date: datetime = milliseconds_to_date(milliseconds=self.end_time_ms)

    def to_json(self):
        return {
            "match_id": self.match_id,
            "sum_id": self.sum_id}

class Scoring_chance:
    def __init__(self, sco_ch_object : Dict, match_id: str):
        self.match_id: str = match_id

        self.sco_ch_id: int = int(sco_ch_object.get('@id'))
        self.sco_ch_time: str = str(sco_ch_object.get('@time'))
        self.player_id: str = str(sco_ch_object.get('@player_id'))
        self.player_name: str = str(sco_ch_object.get('@player_name'))
        self.title: str = str(sco_ch_object.get('@title'))
        self.video_url: str = str(sco_ch_object.get('@mp4_url'))
        self.image_url: str = str(sco_ch_object.get('@img'))
        self.start_time_ms: int = int(sco_ch_object.get('@start_ms'))
        self.start_time_date: datetime = milliseconds_to_date(milliseconds=self.start_time_ms)
        self.end_time_ms: int = int(sco_ch_object.get('@finish_ms'))
        self.end_time_date: datetime = milliseconds_to_date(milliseconds=self.end_time_ms)

    def to_json(self):
        return {
            "match_id": self.match_id,
            "sco_ch_id": self.sco_ch_id}

class Moment:
    def __init__(self, moment_object: Dict, match_id: str):
        self.match_id: str = match_id
        self.moment_id: int = int(moment_object.get('@id'))
        self.moment_time: str = str(moment_object.get('@time'))
        self.player_id: str = str(moment_object.get('@player_id'))
        self.player_name: str = str(moment_object.get('@player_name'))
        self.title: str = str(moment_object.get('@title'))
        self.video_url: str = str(moment_object.get('@mp4_url'))
        self.image_url: str = str(moment_object.get('@img'))
        self.start_time_ms: int = int(moment_object.get('@start_ms'))
        self.start_time_date: datetime = milliseconds_to_date(milliseconds=self.start_time_ms)
        self.end_time_ms: int = int(moment_object.get('@finish_ms'))
        self.end_time_date: datetime = milliseconds_to_date(milliseconds=self.end_time_ms)

    def to_json(self):
        return {"match_id": self.match_id,
                "moment_id": self.moment_id}

class Body_checking:
    def __init__(self, bo_ch_object: Dict, match_id: str):
        self.match_id: str = match_id

        self.bo_ch_id: int = int(bo_ch_object.get('@id'))
        self.bo_ch_time: str = str(bo_ch_object.get('@time'))
        self.player_id: str = str(bo_ch_object.get('@player_id'))
        self.player_name: str = str(bo_ch_object.get('@player_name'))
        self.title: str = str(bo_ch_object.get('@title'))
        self.video_url: str = str(bo_ch_object.get('@mp4_url'))
        self.image_url: str = str(bo_ch_object.get('@img'))
        self.start_time_ms: int = int(bo_ch_object.get('@start_ms'))
        self.start_time_date: datetime = milliseconds_to_date(milliseconds=self.start_time_ms)
        self.end_time_ms: int = int(bo_ch_object.get('@finish_ms'))
        self.end_time_date: datetime = milliseconds_to_date(milliseconds=self.end_time_ms)

    def to_json(self):
        return {"match_id": self.match_id,
                "bo_ch_id": self.bo_ch_id}

class Save:
    def __init__(self, save_object: Dict, match_id: str):
        self.match_id: str = match_id

        self.save_id: int = int(save_object.get('@id'))
        self.save_time: str = str(save_object.get('@time'))
        self.player_id: str = str(save_object.get('@player_id'))
        self.player_name: str = str(save_object.get('@player_name'))
        self.title: str = str(save_object.get('@title'))
        self.video_url: str = str(save_object.get('@mp4_url'))
        self.image_url: str = str(save_object.get('@img'))
        self.start_time_ms: int = int(save_object.get('@start_ms'))
        self.start_time_date: datetime = milliseconds_to_date(milliseconds=self.start_time_ms)
        self.end_time_ms: int = int(save_object.get('@finish_ms'))
        self.end_time_date: datetime = milliseconds_to_date(milliseconds=self.end_time_ms)

    def to_json(self):
        return {"match_id": self.match_id,
                "save_id": self.save_id}
