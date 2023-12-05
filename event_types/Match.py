from typing import List, Dict
from requests import get as requests_get
from xmltodict import parse as xml_parse
from constants import API_URL
from event_types.Goal import Goal


class Match:
    def __init__(self, match_id: str):
        res = requests_get(url=API_URL + match_id)
        xml_text = res.text
        xml_data: Dict = xml_parse(xml_input=xml_text)

        goals: List[Goal] = []

        for _, event in xml_data['events'].items():
            match_id = event['@khl_id']
            for goal in event['goal']:
                goals.append(Goal(match_id=match_id, goal_object=goal))


        self.match_id: str = match_id
        self.goals: List[Goal] = goals
