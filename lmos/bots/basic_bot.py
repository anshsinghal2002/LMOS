from .bot_interface import BotInterface
from typing import Dict, Any
import xml.etree.ElementTree as ET

class BasicBot:
    def __init__(self, xml_config, limb_classes):
        self.limbs = self._parse_limbs(xml_config, limb_classes)
        self.sequence = self._parse_logic_sequence(xml_config)

    def _parse_limbs(self, xml_path, limb_classes):
        tree = ET.parse(xml_path)
        root = tree.getroot()
        limbs = {}
        for limb_elem in root.find('limbs'):
            name = limb_elem.get('name')
            params = {param.get('name'): param.text for param in limb_elem.findall('param')}
            limb_class = limb_classes.get(name)
            if limb_class:
                print(f"Creating limb {name} with params: {params}")
                limbs[name] = limb_class(**params)
        return limbs

    def _parse_logic_sequence(self, xml_path):
        tree = ET.parse(xml_path)
        root = tree.getroot()
        sequence = []
        for cond in root.find('logic_sequence').findall('condition'):
            action_elem = cond.find('action')
            limb_name = action_elem.get('limb')
            params = {child.tag: child.text for child in action_elem if child.tag != 'time'}
            time = action_elem.find('time').text if action_elem.find('time') is not None else None
            sequence.append({'limb': limb_name, 'params': params, 'time': time})
        return sequence

    def execute_sequence(self):
        for step in self.sequence:
            limb = self.limbs.get(step['limb'])
            if limb:
                print(f"Executing {step['limb']} at {step['time']}")
                limb.actuate(step['params'])
            else:
                print(f"Limb {step['limb']} not found") 