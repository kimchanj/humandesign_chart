from skyfield.api import load, Topos
from skyfield.data import mpc
from datetime import datetime
from typing import Dict

class AstroCalculator:
    def __init__(self):
        self.planets = load('de421.bsp')  # 천문학적 데이터 파일
        self.ts = load.timescale()

    def calculate_planet_positions(self, birth_datetime: datetime, location: Dict[str, float]) -> Dict[str, float]:
        """
        행성별 황도좌표 (Ecliptic Longitude)를 계산
        :param birth_datetime: datetime 객체
        :param location: {"latitude": float, "longitude": float}
        :return: {"Sun": 120.54, "Moon": 48.32, ...}
        """
        t = self.ts.utc(birth_datetime.year, birth_datetime.month, birth_datetime.day,
                        birth_datetime.hour, birth_datetime.minute)

        observer = Topos(latitude_degrees=location['latitude'], longitude_degrees=location['longitude'])

        result = {}
        for planet_name in ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars',
                            'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Earth']:
            planet = self.planets[planet_name]
            astrometric = (planet - self.planets['earth']).at(t)
            ecliptic = astrometric.ecliptic_latlon()
            longitude_deg = ecliptic[1].degrees
            result[planet_name] = round(longitude_deg, 2)

        return result
