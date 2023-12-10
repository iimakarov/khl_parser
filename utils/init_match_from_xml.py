from event_types.Match import Match
from requests import get as requests_get
from xmltodict import parse as xml_parse
from constants import API_URL
from typing import Dict


def init_match_from_xml(match_id: str) -> Match:
    res = requests_get(url=API_URL + match_id)
    xml_text = res.text
    xml_data: Dict = xml_parse(xml_input=xml_text)
    match = Match(match_id=match_id, xml_data=xml_data)
    return match
