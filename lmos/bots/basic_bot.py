from .bot_interface import BotInterface
from typing import Dict, Any
import xml.etree.ElementTree as ET

class BasicBot(BotInterface):
    def __init__(self, limbs, xml_config):
        super().__init__(limbs, xml_config)
        self.limb_map = {limb.name: limb for limb in limbs}
        self.sequence = self._parse_xml(xml_config)

    def _parse_xml(self, xml_path):
        tree = ET.parse(xml_path)
        root = tree.getroot()
        sequence = []
        for action in root.findall('action'):
            limb_name = action.get('limb')
            params = {param.tag: param.text for param in action}
            sequence.append({'limb': limb_name, 'params': params})
        return sequence

    def limb_actuate(self, limb_name: str, params: Dict[str, Any]):
        limb = self.limb_map.get(limb_name)
        if limb:
            return limb.actuate(params)
        else:
            raise ValueError(f'Limb {limb_name} not found')

    def execute_sequence(self):
        for step in self.sequence:
            self.limb_actuate(step['limb'], step['params']) 