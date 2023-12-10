from typing import List, Dict
from event_types.match_attributes import Goal, Penalty, Highlight, Save, ScoringChance, BodyCheck, Moment


class Match:
    def __init__(self, match_id: str, xml_data: Dict):
        self.match_id: str = match_id

        goals: List[Goal] = []
        penalties: List[Penalty] = []
        highlights: List[Highlight] = []
        scoring_chances: List[ScoringChance] = []
        moments: List[Moment] = []
        body_checks: List[BodyCheck] = []
        saves: List[Save] = []

        for _, event in xml_data['events'].items():
            for goal in event['goal']:
                goals.append(Goal(match_id=match_id, goal_object=goal))
            for penalty in event['pn']:
                penalties.append(Penalty(match_id=match_id, penalty_object=penalty))
            for highlight in event['sum']:
                highlights.append(Highlight(match_id=match_id, highlight_object=highlight))
            for scoring_chance in event['scoring_chance']:
                scoring_chances.append(ScoringChance(match_id=match_id, scoring_chance_object=scoring_chance))
            for moment in event['moment']:
                moments.append(Moment(match_id=match_id, moment_object=moment))
            for body_check in event['body_checking']:
                body_checks.append(BodyCheck(match_id=match_id, body_check_object=body_check))
            for save in event['save']:
                saves.append(Save(match_id=match_id, save_object=save))

        self.goals = goals
        self.penalties = penalties
        self.highlights = highlights
        self.scoring_chances = scoring_chances
        self.moments = moments
        self.body_checks = body_checks
        self.saves = saves
