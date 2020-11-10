from datetime import datetime, timedelta

import settings as app_settings


class Ride:
    def __init__(self, distance, start_time, duration):
        self.distance   = distance
        self.start_time = start_time
        self.duration   = duration

    def __convert_minutes_from_iso8601(self):
        """Extracts time from iso format ride and return it in hh:mm format"""
        datetime_obj = datetime.strptime(self.start_time, '%Y-%m-%dT%H:%M:%S.%f%z')
        datetime_obj.strftime('%H:%M')
        return int(datetime_obj.strftime('%H')) * 60 + int(datetime_obj.strftime('%M'))

    def get_human_readable_duration(self):
        """Formats ride duration in hh:mm:ss"""
        return str(timedelta(seconds=self.duration)).zfill(8)

    def get_end_time(self):
        """Returns ride end time in iso format"""
        end_time = datetime.strptime(self.start_time, '%Y-%m-%dT%H:%M:%S.%f%z') + timedelta(seconds=self.duration)
        return end_time.isoformat().replace("000+00:00", "Z")

    def is_busy_hour(self):
        if int(app_settings.BUSY_START_HOUR) * 60 <= self.__convert_minutes_from_iso8601() < int(app_settings.BUSY_END_HOUR) * 60:
            return True
        return False

    def is_night_hour(self):
        if int(app_settings.NIGHT_END_HOUR) * 60 <= self.__convert_minutes_from_iso8601() < int(app_settings.NIGHT_START_HOUR) * 60:
            return False
        return True

    def calculate_ride_cost(self):
        ride_cost = app_settings.INITIAL_CHARGE
        ride_cost += self.distance * app_settings.COST_PER_MILE
        if self.is_busy_hour():
            ride_cost += app_settings.BUSY_EXTRA_COST
        if self.is_night_hour():
            ride_cost += app_settings.NIGHT_EXTRA_COST
        return ride_cost
