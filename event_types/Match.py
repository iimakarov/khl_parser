from typing import List, Dict
from requests import get as requests_get
from xmltodict import parse as xml_parse
from constants import API_URL
from event_types.Goal import Goal
from event_types.Goal import Pn
from event_types.Goal import Summary
from event_types.Goal import Scoring_chance
from event_types.Goal import Moment
from event_types.Goal import Body_checking
from event_types.Goal import Save


class Match:
    def __init__(self, match_id: str):
        res = requests_get(url=API_URL + match_id)
        xml_text = res.text
        xml_data: Dict = xml_parse(xml_input=xml_text)

        goals: List[Goal] = []
        pns: List[Pn] = []
        sums: List[Summary] = []
        sco_chs: List[Scoring_chance] = []
        moments: List[Moment] = []
        bo_chs: List[Body_checking] = []
        saves: List[Save] =[]

        for _, event in xml_data['events'].items():
            match_id = event['@khl_id']
            for goal in event['goal']:
                goals.append(Goal(match_id=match_id, goal_object=goal))
            for pn in event['pn']:
                pns.append(Pn(match_id=match_id, pn_object=pn))
            for sum in event['sum']:
                sums.append(Summary(match_id=match_id, sum_object=sum))
            for sco_ch in event['scoring_chance']:
                sco_chs.append(Scoring_chance(match_id=match_id, sco_ch_object=sco_ch))
            for moment in event['moment']:
                moments.append(Moment(match_id=match_id, moment_object=moment))
            for bo_ch in event['body_checking']:
                bo_chs.append(Body_checking(match_id=match_id, bo_ch_object=bo_ch))
            for save in event['save']:
                saves.append(Save(match_id=match_id, save_object=save))


        self.match_id: str = match_id
        self.goals: List[Goal] = goals
        self.pns: List[Pn] = pns
        self.sums: List[Summary] = sums
        self.sco_chs: List[Scoring_chance] = sco_chs
        self.moments: List[Moment] = moments
        self.bo_chs: List[Body_checking] = bo_chs
        self.saves: List[Save] = saves