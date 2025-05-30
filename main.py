from datetime import datetime
from core.astro_calculator import AstroCalculator

def main():
    # 1. 생년월일과 시간 (timezone-aware 권장, 여기서는 UTC로 가정)
    birth_datetime = datetime(1990, 1, 1, 12, 0, 0)  # 예시: 1990-01-01 12:00:00 UTC

    # 2. 위치 정보 (위도, 경도)
    location = (37.5665, 126.9780)  # 서울 위도, 경도 예시

    # 3. AstroCalculator 인스턴스 생성
    astro = AstroCalculator()

    # 4. 행성 위치 계산
    planet_positions = astro.calculate_planet_positions(birth_datetime, location)

    # 5. 결과 출력 (RA, DEC 각 행성별)
    print("🎯 Human Design Planetary Positions")
    print("-----------------------------------")
    for planet, data in planet_positions.items():
        print(f"{planet}: RA={data['ra_degrees']:.2f}°, DEC={data['dec_degrees']:.2f}°")

if __name__ == "__main__":
    main()
