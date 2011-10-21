import yql as YQL

yql = YQL.Public()

def constructQuery(zipCode):
    return 'select * from weather.forecast where location=%d' % zipCode

def getWeather(zipCode):
    global yql
    query = constructQuery(zipCode)
    return yql.execute(query).rows
