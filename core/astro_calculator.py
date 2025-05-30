from skyfield.api import load, Topos
from datetime import datetime, timezone

class AstroCalculator:
    def __init__(self):
        # JPL 천체 궤도 데이터 로드
        self.ephemeris = load('de421.bsp')
        # 태양계 행성 객체 딕셔너리 (Skyfield 이름과 key를 맞춰 둠)
        self.planets = {
            'Sun': self.ephemeris['sun'],
            'Moon': self.ephemeris['moon'],
            'Mercury': self.ephemeris['mercury'],
            'Venus': self.ephemeris['venus'],
            'Mars': self.ephemeris['mars'],
            'Jupiter': self.ephemeris['jupiter barycenter'],
            'Saturn': self.ephemeris['saturn barycenter'],
            'Uranus': self.ephemeris['uranus barycenter'],
            'Neptune': self.ephemeris['neptune barycenter'],
            'Pluto': self.ephemeris['pluto barycenter'],
        }
        self.ts = load.timescale()

    def calculate_planet_positions(self, birth_datetime: datetime, location: tuple):
        """
        주어진 생년월일과 위치(latitude, longitude)에서
        각 행성의 적경(ra)과 적위(dec) 계산
        
        Parameters:
          birth_datetime: datetime (timezone-aware 혹은 UTC)
          location: (latitude(float), longitude(float))
        
        Returns:
          dict {
            'Sun': {'ra_degrees': float, 'dec_degrees': float},
            ...
          }
        """
        # datetime이 timezone-aware 아니면 UTC로 가정
        if birth_datetime.tzinfo is None:
            birth_datetime = birth_datetime.replace(tzinfo=timezone.utc)
        utc_dt = birth_datetime.astimezone(timezone.utc)

        # Skyfield 시간 객체 생성
        t = self.ts.utc(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour, utc_dt.minute, utc_dt.second)

        lat, lon = location
        observer = Topos(latitude_degrees=float(lat), longitude_degrees=float(lon))

        planet_positions = {}

        for name, body in self.planets.items():
            # 관측자 위치에서 본 행성 위치
            astrometric = (self.ephemeris['earth'] + observer).at(t).observe(body)
            ra, dec, distance = astrometric.radec()

            planet_positions[name] = {
                'ra_degrees': ra.hours * 15.0,  # RA 시 → 도 (360도 = 24시)
                'dec_degrees': dec.degrees,
            }

        return planet_positions
