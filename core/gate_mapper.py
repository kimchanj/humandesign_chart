import json
from pathlib import Path
from typing import Dict, Optional

class GateMapper:
    def __init__(self, mapping_file: str):
        self.mapping_file = Path(mapping_file)
        self.gate_data = self._load_gate_mapping()

    def _load_gate_mapping(self) -> Dict[str, Dict[str, int]]:
        if not self.mapping_file.exists():
            raise FileNotFoundError(f"Gate mapping file not found: {self.mapping_file}")
        with open(self.mapping_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def get_gate_info(self, planet_name: str) -> Optional[Dict[str, int]]:
        """
        주어진 행성 이름으로 게이트 정보 조회
        :param planet_name: ex) "Sun", "Earth"
        :return: {"gate": int, "line": int} 또는 None
        """
        return self.gate_data.get(planet_name)

    def get_all_mappings(self) -> Dict[str, Dict[str, int]]:
        return self.gate_data

# 테스트 용 메인 실행부
if __name__ == "__main__":
    gm = GateMapper("data/gate_mapping.json")
    sun_gate = gm.get_gate_info("Sun")
    print(f"Sun gate info: {sun_gate}")

    all_data = gm.get_all_mappings()
    print(f"All gate mappings: {all_data}")
