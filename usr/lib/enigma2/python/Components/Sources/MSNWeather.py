# Embedded file name: /usr/lib/enigma2/python/Components/Sources/MSNWeather.py
import time
from Components.Sources.Source import Source
from Components.WeatherMSN import weathermsn

class MSNWeather(Source):

    def __init__(self):
        Source.__init__(self)
        weathermsn.callbacksAllIconsDownloaded.append(self.callbackAllIconsDownloaded)
        weathermsn.getData()

    def callbackAllIconsDownloaded(self):
        self.changed((self.CHANGED_ALL,))

    def getCity(self):
        return weathermsn.weatherData.city

    def getObservationPoint(self):
        skey = '-1'
        if skey in weathermsn.weatherData.weatherItems:
            return weathermsn.weatherData.weatherItems[skey].observationpoint
        else:
            return _('n/a')

    def getObservationTime(self):
        skey = '-1'
        if skey in weathermsn.weatherData.weatherItems:
            item = weathermsn.weatherData.weatherItems[skey]
            if item.observationtime != '':
                c = time.strptime(item.observationtime, '%H:%M:%S')
                return time.strftime('%H:%M', c)
            else:
                return _('n/a')
        else:
            return _('n/a')

    def getTemperature_Heigh(self, key):
        skey = str(key)
        if skey == '-1':
            skey = '1'
        if skey in weathermsn.weatherData.weatherItems:
            item = weathermsn.weatherData.weatherItems[skey]
            highTemp = item.high
            return '%s\xb0%s' % (highTemp, weathermsn.weatherData.degreetype)
        else:
            return _('n/a')

    def getTemperature_Low(self, key):
        skey = str(key)
        if skey == '-1':
            skey = '1'
        if skey in weathermsn.weatherData.weatherItems:
            item = weathermsn.weatherData.weatherItems[skey]
            lowTemp = item.low
            return '%s\xb0%s' % (lowTemp, weathermsn.weatherData.degreetype)
        else:
            return _('n/a')

    def getTemperature_Heigh_Low(self, key):
        skey = str(key)
        if skey == '-1':
            skey = '1'
        if skey in weathermsn.weatherData.weatherItems:
            item = weathermsn.weatherData.weatherItems[skey]
            highTemp = item.high
            high = '%s\xb0%s' % (highTemp, weathermsn.weatherData.degreetype)
            low = self.getTemperature_Low(key)
            return '%s - %s' % (high, low)
        else:
            return _('n/a')

    def getTemperature_Text(self, key):
        skey = str(key)
        if skey in weathermsn.weatherData.weatherItems:
            item = weathermsn.weatherData.weatherItems[skey]
            if skey == '-1':
                return item.skytext
            else:
                return item.skytextday
        else:
            return _('n/a')

    def getTemperature_Current(self):
        skey = '-1'
        if skey in weathermsn.weatherData.weatherItems:
            return '%s\xb0%s' % (weathermsn.weatherData.weatherItems[skey].temperature, weathermsn.weatherData.degreetype)
        else:
            return _('n/a')

    def getFeelslike(self):
        skey = '-1'
        if skey in weathermsn.weatherData.weatherItems:
            return weathermsn.weatherData.weatherItems[skey].feelslike
        else:
            return _('n/a')

    def getHumidity(self):
        skey = '-1'
        if skey in weathermsn.weatherData.weatherItems:
            return weathermsn.weatherData.weatherItems[skey].humidity
        else:
            return _('n/a')

    def getWinddisplay(self):
        skey = '-1'
        if skey in weathermsn.weatherData.weatherItems:
            return weathermsn.weatherData.weatherItems[skey].winddisplay
        else:
            return _('n/a')

    def getWeekday(self, key, short):
        skey = str(key)
        if skey == '-1':
            skey = '1'
        if skey in weathermsn.weatherData.weatherItems:
            item = weathermsn.weatherData.weatherItems[skey]
            if short:
                return item.shortday
            else:
                return item.day
        else:
            return _('n/a')

    def getDate(self, key):
        skey = str(key)
        if skey == '-1':
            skey = '1'
        if skey in weathermsn.weatherData.weatherItems:
            item = weathermsn.weatherData.weatherItems[skey]
            c = time.strptime(item.date, '%Y-%m-%d')
            return time.strftime('%d. %b', c)
        else:
            return _('n/a')

    def getWeatherIconFilename(self, key):
        if str(key) in weathermsn.weatherData.weatherItems:
            return weathermsn.weatherData.weatherItems[str(key)].iconFilename
        else:
            return ''

    def getCode(self, key):
        if str(key) in weathermsn.weatherData.weatherItems:
            return weathermsn.weatherData.weatherItems[str(key)].code
        else:
            return ''

    def destroy(self):
        weathermsn.callbacksAllIconsDownloaded.remove(self.callbackAllIconsDownloaded)
        Source.destroy(self)
