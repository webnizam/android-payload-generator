# Android Payload Generator

This tool helps to generate android payload with the help of QT5.

# Installation

Payload Generator requires [Qt5](https://doc.qt.io/qtforpython/) to run.

Install below dependencies.

```sh
pip3 install --user pyqt5  
sudo apt-get install python3-pyqt5  
sudo apt-get install pyqt5-dev-tools
sudo apt-get install qttools5-dev-tools
pip install -r requirements.txt
```

Run by

> python3 qt_payload_gen.py

### Plugins

Payload generator is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| msfvenom | [https://github.com/rapid7/metasploit-framework/wiki/How-to-use-msfvenom]|
| qt5 | [https://doc.qt.io/qtforpython/]|
