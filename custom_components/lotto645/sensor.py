import logging
import requests
import voluptuous as vol
from bs4 import BeautifulSoup

import homeassistant.helpers.config_validation as cv

from datetime import timedelta
from datetime import datetime
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (CONF_NAME, CONF_API_KEY, CONF_ICON)
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle

REQUIREMENTS = ['beautifulsoup4==4.6.0']

_LOGGER = logging.getLogger(__name__)

CONF_NAME  = 'name'

BSE_URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
NANUM_BSE_URL = 'https://www.nlotto.co.kr/gameResult.do?method=byWin'

DEFAULT_NAME = 'lotto645'
DEFAULT_ICON = 'mdi:numeric-6-circle'

COMM_LOTTO_FORMAT = '{} {} {} {} {} {} + {}'

MIN_TIME_BETWEEN_API_UPDATES    = timedelta(seconds=21600) #
MIN_TIME_BETWEEN_SENSOR_UPDATES = timedelta(seconds=21600) #

ATTR_NAME = 'name'
ATTR_TIT  = 'title'
ATTR_LOTTERY_DATE = 'lottery_date'
ATTR_NUM_1 = 'number_1'
ATTR_NUM_2 = 'number_2'
ATTR_NUM_3 = 'number_3'
ATTR_NUM_4 = 'number_4'
ATTR_NUM_5 = 'number_5'
ATTR_NUM_6 = 'number_6'
ATTR_NUM_B = 'number_bonus'
ATTR_SYNC_DATE = 'sync_date'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    name  = config.get(CONF_NAME)

    sensors = []

    lotto = lotto645API(name)

    lottoSensor = lotto645Sensor( name, lotto )
    lottoSensor.update()
    sensors += [lottoSensor]

    add_entities(sensors, True)

class lotto645API:

    def __init__(self, name):
        """Initialize the lotto645 API."""
        self._name      = name
        self.result     = {}

    @Throttle(MIN_TIME_BETWEEN_API_UPDATES)
    def update(self):
        """Update function for updating api information."""
        try:
            dt = datetime.now()
            syncDate = dt.strftime("%Y-%m-%d %H:%M:%S")

            url = BSE_URL

            response = requests.get(url, timeout=10)
            response.raise_for_status()

            page = response.content

            soup = BeautifulSoup(page, 'html.parser')

            lotto_dict = {}

            """ lotto645 Title """
            all_div = soup.find("div", {"class":"win_result"})

            tmp = all_div.find_all("h4")
            tit = tmp[0].get_text().strip()

            """ lotto645 win date """
            dtm = all_div.find("p", {"class":"desc"})
            lottoDtm = dtm.text.replace('(','').replace(')','')

            """ win number 6 EA """
            div_num_win = soup.find("div", {"class":"num win"})
            balls = div_num_win.find_all("span")

            num_1 = balls[0].get_text().strip()
            num_2 = balls[1].get_text().strip()
            num_3 = balls[2].get_text().strip()
            num_4 = balls[3].get_text().strip()
            num_5 = balls[4].get_text().strip()
            num_6 = balls[5].get_text().strip()

            """ bonus number 1 EA"""
            div_num_bonus = soup.find("div", {"class":"num bonus"})

            bnsBalls = div_num_bonus.find_all("span")
            num_bonus = bnsBalls[0].get_text().strip();

            lotto_dict = { 'number_1' : num_1, 'number_2' : num_2, 'number_3' : num_3, 'number_4' : num_4, 'number_5' : num_5, 'number_6' : num_6, 'number_bonus' : num_bonus, 'lottery_date' : lottoDtm, 'title' : tit, 'sync_date' : syncDate }

            self.result = lotto_dict
            #_LOGGER.debug('lotto645 API Request Result: %s', self.result)
        except Exception as ex:
            _LOGGER.error('Failed to update lotto645 API status Error: %s', ex)
            raise

class lotto645Sensor(Entity):
    def __init__(self, name, api):
        self._name      = name
        self._api       = api
        self._icon      = DEFAULT_ICON
        self._state     = None
        self.numbers    = {}

    @property
    def entity_id(self):
        """Return the entity ID."""
        return 'sensor.lotto645'

    @property
    def name(self):
        """Return the name of the sensor, if any."""
        return self._name

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return self._icon

    @property
    def state(self):
        """Return the state of the sensor."""
        return COMM_LOTTO_FORMAT.format(self.numbers.get('number_1','-'), self.numbers.get('number_2','-'), self.numbers.get('number_3','-'), self.numbers.get('number_4','-'), self.numbers.get('number_5','-'), self.numbers.get('number_6','-'), self.numbers.get('number_bonus','-'))

    @property
    def attribution(self):
        """Return the attribution."""
        return 'Powered by miumida'

    @Throttle(MIN_TIME_BETWEEN_SENSOR_UPDATES)
    def update(self):
        """Get the latest state of the sensor."""
        if self._api is None:
            return
        # Saturday : 6
        dt = datetime.now()
        nWeekDay = dt.weekday()

        self._api.update()
        lotto_dict = self._api.result

        self.numbers = lotto_dict

    @property
    def device_state_attributes(self):
        """Attributes."""
        return { key: self.numbers[key] for key in sorted(self.numbers.keys()) }
