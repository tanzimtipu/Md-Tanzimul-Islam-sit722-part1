import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://sit722_part1_n7nh_user:aHvI1vyxHR1kmvPEKIlIMfF0S551k0wB@dpg-cqq9jst6l47c73aqibsg-a.oregon-postgres.render.com/sit722_part1_n7nh")

settings = Settings()
