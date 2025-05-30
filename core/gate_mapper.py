import json

class GateMapper:
    def __init__(self, mapping_file):
        with open(mapping_file, 'r', encoding='utf-8') as f:
            self.gate_mapping = json.load(f)
        self.sorted_gates = sorted(
            (float(v['start_degree']), int(k)) for k, v in self.gate_mapping.items()
        )

    def ra_to_gate(self, ra_deg):
        """
        RA (황경) 값을 휴먼디자인 게이트 번호로 변환
        휴먼디자인은 360도를 64개 게이트로 나누며
        기준 0도가 아닌 13도부터 게이트 1번 시작(오프셋 13도 적용)
        """
        offset_deg = 13
        adjusted_deg = (ra_deg - offset_deg) % 360
        gate = int(adjusted_deg // 5.625) + 1
        if gate > 64:
            gate = 64
        return gate
