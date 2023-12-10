from datetime import datetime, timedelta


class KhlUtils:
    @staticmethod
    def milliseconds_to_date(milliseconds: int) -> datetime:
        start_time = datetime(year=1970, month=1, day=1)
        end_time = start_time + timedelta(milliseconds=milliseconds)
        return end_time
