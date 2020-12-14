# Lotto 6/45 Sensor

![HAKC)][hakc-shield]
![HACS][hacs-shield]
![Version v1.3][version-shield]

로또 6/45 당첨번호를 알려주는 Home Assistant Sensor 입니다.<br>
당첨번호 `번호1 번호2 번호3 번호4 번호5 번호6 + 보너스` 형태로 보여줍니다.

![screenshot_1](https://github.com/miumida/lotto645/blob/master/Screenshot_1.png)<br>
![screenshot_2](https://github.com/miumida/lotto645/blob/master/Screenshot_2.png)<br>

<br>

## Version history
| Version | Date        | 내용              |
| :-----: | :---------: | ----------------------- |
| v1.0    | 2020.01.15  | First version  |
| v1.1    | 2020.05.09  | 로또정보 URL 수정  |
| v1.2    | 2020.07.08  | 통합구성요소로 추가하기 적용 |
| v1.3    | 2020.08.11  | device_info 속성 추가 |
| v1.4    | 2020.12.14  | 버전체계 변경에 따른 수정   |

## Installation
### Manual
- HA 설치 경로 아래 custom_components 에 파일을 넣어줍니다.<br>
  `<config directory>/custom_components/lotto645/__init__.py`<br>
  `<config directory>/custom_components/lotto645/manifest.json`<br>
  `<config directory>/custom_components/lotto645/sensor.py`<br>
- configuration.yaml 파일에 설정을 추가합니다.<br>
- Home-Assistant 를 재시작합니다<br>
### HACS
- HACS > Intergrations > 설정 > Custom Repositories > '<https://github.com/miumida/lotto645>' 추가 후, 설치<br>
- configuration.yaml 파일에 설정을 추가합니다.<br>
- Home-Assistant 를 재시작합니다<br>
<br><br>
## Usage
### configuration(yaml)
- HA 설정에 lotto645 sensor를 추가합니다.<br>
```yaml
sensor:
  - platform: lotto645
```
### configuration(통합구성요소)
- 설정 > 통합구성요소 > 추가 > 'Lotto 6/45' 검색 후, 추가

[version-shield]: https://img.shields.io/badge/version-v1.4-orange.svg
[hakc-shield]: https://img.shields.io/badge/HAKC-Enjoy-blue.svg
[hacs-shield]: https://img.shields.io/badge/HACS-Custom-red.svg
