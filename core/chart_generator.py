from typing import Dict
from core.astro_calculator import AstroCalculator
from core.gate_mapper import GateMapper

class ChartGenerator:
    def __init__(self, birth_datetime, location, mapping_file="data/gate_mapping.json"):
        self.birth_datetime = birth_datetime
        self.location = location
        self.astro = AstroCalculator()
        self.gate_mapper = GateMapper(mapping_file)

    def generate_chart(self) -> Dict[str, Dict[str, int]]:
        """
        사용자의 탄생 정보 기반 휴먼디자인 차트 생성
        :return: 행성명 → {"gate": int, "line": int}
        """
        planet_positions = self.astro.calculate_planet_positions(self.birth_datetime, self.location)

        chart = {}
        for planet, position in planet_positions.items():
            gate_info = self.gate_mapper.get_gate_info(planet)
            if gate_info:
                chart[planet] = gate_info
            else:
                chart[planet] = {"gate": None, "line": None}

        return chart
