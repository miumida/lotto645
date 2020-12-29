# Ötös Lottó Sensor

![HAKC)][hakc-shield]
![HACS][hacs-shield]

## Installation
### Manual
- Copy the content of the custom_components folder into your HA config folder see below.<br>
  `<config directory>/custom_components/otoslotto/__init__.py`<br>
  `<config directory>/custom_components/otoslotto/manifest.json`<br>
  `<config directory>/custom_components/otoslott/sensor.py`<br>
- You can then enable it via configuration.yaml or via integrations.<br>
### HACS
- HACS > Intergrations > ... > Custom Repositories > '<https://github.com/rjulius23/OtosLotto>'<br>
- You can then enable it via configuration.yaml or via integrations.<br>
<br><br>
## Usage
### configuration(yaml)
- Configure the otoslotto sensor platform.<br>
```yaml
sensor:
  - platform: otoslotto
```
### configuration(HA integrations)
- Configuration -> Integrations -> Add Integration -> "Ötös Lottó"

[hakc-shield]: https://img.shields.io/badge/HAKC-Enjoy-blue.svg
[hacs-shield]: https://img.shields.io/badge/HACS-Custom-red.svg
