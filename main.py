from datetime import datetime
from core.astro_calculator import AstroCalculator
from core.gate_mapper import GateMapper
from core.chart_generator import ChartGenerator

def main():
    # 생년월일과 위치 (예: 서울)
    birth_datetime = datetime(1977, 3, 20, 23, 0, 0)
    location = (37.5665, 126.9780)  # (위도, 경도)

    astro = AstroCalculator()
    mapper = GateMapper('data/gate_mapping.json')
    generator = ChartGenerator(astro, mapper, birth_datetime, location)

    chart = generator.generate_chart()

    print("🎯 Human Design Planetary Positions")
    print("-----------------------------------")
    for planet, data in chart.items():
        ra_deg = data['ra_degrees']
        dec_deg = data['dec_degrees']
        gate = mapper.ra_to_gate(ra_deg)
        print(f"{planet}: RA={ra_deg:.2f}°, DEC={dec_deg:.2f}°, Gate={gate}")

if __name__ == "__main__":
    main()
