# plantbot3000
Raspberry Pi Project to monitor plants

## Setup

* Install jasper on your Raspberry Pi
* Upload `src/sensor/sensor.ino` to the Arduino
* Connect the Arduino with the Pi with USB
* Ensure that  `/dev/ttyACM0` is the correct device on your Pi (or change it in `src/python/sensor_reader.py`)
* Run `src/install.sh`
* Set the environment variable `export PLANTBOT_HOME=PATH/TO/PLANTBOT3000`

## Setup Submodule TwitterAPI

* if TwitterAPI is empty run `git submodule update --init`
* install with `pip install TwitterAPI`
* create `config.py` in `src/python`

Example config

```python
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''
```
