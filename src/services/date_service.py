from datetime import datetime

from src.services.base_date_service import BaseDateService


class DateService(BaseDateService):
    def get_now(self):
        return datetime.now()
