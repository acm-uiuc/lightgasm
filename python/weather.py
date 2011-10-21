import yql as YQL
from animations import RSL, SunClouds

class Weather():
    def __init__(self, zipCode):
        self.yql = YQL.Public()
        self.local_weather = self.get_weather(zipCode)

    def _construct_query(self, zipCode):
        return 'select * from weather.forecast where location=%d' % zipCode

    def get_weather(self, zipCode):
        query = self._construct_query(zipCode)
        return self.yql.execute(query).rows

if __name__ == "__main__":
    weather = Weather(61801)
    print weather.local_weather


