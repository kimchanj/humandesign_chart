class ChartGenerator:
    def __init__(self, astro_calculator, gate_mapper, birth_datetime, location):
        self.astro = astro_calculator
        self.mapper = gate_mapper
        self.birth_datetime = birth_datetime
        self.location = location  # (latitude, longitude)

    def generate_chart(self):
        """
        행성 위치 계산 → RA값을 게이트, 라인에 매핑 → 결과 딕셔너리 리턴
        {
            'Sun': {'ra_degrees': ..., 'dec_degrees': ..., 'gate': ..., 'line': ...},
            ...
        }
        """
        planet_positions = self.astro.calculate_planet_positions(self.birth_datetime, self.location)
        chart = {}

        for planet, pos in planet_positions.items():
            ra_deg = pos['ra_degrees']
            dec_deg = pos['dec_degrees']
            gate, line = self.mapper.ra_to_gate_and_line(ra_deg)
            chart[planet] = {
                'ra_degrees': ra_deg,
                'dec_degrees': dec_deg,
                'gate': gate,
                'line': line,
            }

        return chart
