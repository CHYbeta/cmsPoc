# cmsPoc
[![Python 2.7](https://img.shields.io/badge/python-2.7-yellow.svg)](https://www.python.org/)
![License](https://img.shields.io/badge/license-GPLv2-red.svg)

## Requirements
- python2.7
- Works on Linux, Windows

## Usage
```
usage: cmspoc.py [-h]
 -t TYPE -s SCRIPT -u URL

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  e.g.,phpcms
  -s SCRIPT, --script SCRIPT
                        Select script
  -u URL, --url URL     Input a target url
```

参数说明：
- -t：指定cms的类型，比如 -t beecms
- -s：指定要载入的POC脚本，比如 -s v40_fileupload_getshell
- -u：指定目标cms，比如 -u http://vuln/index.php

## Script
完整脚本列表请见：[cmsPoc：Wiki](https://github.com/CHYbeta/cmsPoc/wiki/Scripts)

## Examples
```
python cmspoc.py -u http://127.0.0.1/beecms/inex.php -t beecms -s v40_fileupload_getshell
```
![](https://github.com/CHYbeta/cmsPoc/blob/master/tty.gif?raw=true)

# Legal Disclaimer
本项目仅供教育和学习交流使用，请勿用于非法用途恶意攻击，否则后果作者概不负责。

This project is made for educational and ethical testing purposes only。It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.
