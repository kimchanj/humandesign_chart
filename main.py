# main.py
from datetime import datetime
from core.chart_generator import ChartGenerator

def main():
    # 1. 생년월일과 위치 설정 (예: 서울)
    birth_datetime = datetime(1977, 3, 20, 23, 0)
    location = {"latitude": 37.5665, "longitude": 126.9780}

    # 2. 차트 생성기 초기화 및 실행
    generator = ChartGenerator(birth_datetime, location)
    chart = generator.generate_chart()

    # 3. 결과 출력
    print("📌 Human Design Chart:")
    for planet, info in chart.items():
        print(f"{planet:9}: Gate {info['gate']:2}, Line {info['line']}")

if __name__ == "__main__":
    main()
