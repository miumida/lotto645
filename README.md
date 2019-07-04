# lotto645 Sensor
로또 6/45 당첨번호를 알려주는 Home Assistant Sensor 입니다.

# Installation
- HA 설치 경로 아래 custom_components 에 파일을 넣어줍니다.<br>
  `<config directory>/custom_components/lotto645/__init__.py`<br>
  `<config directory>/custom_components/lotto645/manifest.json`<br>
  `<config directory>/custom_components/lotto645/sensor.py`<br>
- configuration.yaml 파일에 설정을 추가합니다.<br>
- Home-Assistant 를 재시작합니다<br>

# Usage
### configuration
- HA 설정에 anniversary sensor를 추가합니다.<br>
```XML
sensor:
  - platform: lotto645
```
