# Lotto 6/45 Sensor
로또 6/45 당첨번호를 알려주는 Home Assistant Sensor 입니다.<br>
당첨번호 번호1 번호2 번호3 번호4 번호5 번호6 + 보너스 형태로 보여줍니다.

![screenshot_1](https://github.com/miumida/lotto645/blob/master/Screenshot_1.png)<br>
![screenshot_2](https://github.com/miumida/lotto645/blob/master/Screenshot_2.png)

## Installation
- HA 설치 경로 아래 custom_components 에 파일을 넣어줍니다.<br>
  `<config directory>/custom_components/lotto645/__init__.py`<br>
  `<config directory>/custom_components/lotto645/manifest.json`<br>
  `<config directory>/custom_components/lotto645/sensor.py`<br>
- configuration.yaml 파일에 설정을 추가합니다.<br>
- Home-Assistant 를 재시작합니다<br>


## Usage
### configuration
- HA 설정에 lotto645 sensor를 추가합니다.<br>
```XML
sensor:
  - platform: lotto645
```
