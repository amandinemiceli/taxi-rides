from datetime import datetime, timedelta


class Ride:
    def __init__(self, distance, start_time, duration):
        self.distance   = distance
        self.start_time = start_time
        self.duration   = duration

    def get_human_readable_duration(self):
        """Formats ride duration in hh:mm:ss"""
        return str(timedelta(seconds=self.duration)).zfill(8)

    def get_end_time(self):
        """Returns ride end time in iso format"""
        end_time = datetime.strptime(self.start_time, '%Y-%m-%dT%H:%M:%S.%f%z') + timedelta(seconds=self.duration)
        return end_time.isoformat().replace("000+00:00", "Z")
