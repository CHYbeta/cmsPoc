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
- -t：指定cms的类型
- -s：指定要载入的POC脚本
- -u：指定目标cms

## Examples
```
python cmspoc.py -t phpcms -s v960_sqlinject_getpasswd -u http://10.10.10.1:2500/phpcms960
```
![](https://github.com/CHYbeta/cmsPoc/blob/master/tty.gif?raw=true)

## Script
|  TYPE   | SCRIPT | DESCRIPTION  |
|:-------------:|:-------------:|:-----:|
|phpcms| v960_sqlinject_getpasswd | [phpcmsv9.6.0 wap模块 sql注入 获取passwd](https://chybeta.github.io/2017/08/04/%C2%96PHPCMS-v9-6-0-wap%E6%A8%A1%E5%9D%97sql%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90/)|
|icms| v701_sqlinject_getadmin | [icmsv7.0.1 admincp.php sql注入 后台任意登陆](https://chybeta.github.io/2017/09/12/ICMSv7-0-1-admincp-class-php-sql%E6%B3%A8%E5%85%A5%E5%88%86%E6%9E%90/)|
|discuz| v34_delete_arbitary_files | [discuz ≤ v3.4 任意文件删除](https://chybeta.github.io/2017/10/15/DiscuzX-v3-4-%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E5%88%A0%E9%99%A4%E6%BC%8F%E6%B4%9E/)|
|beecms| v40_fileupload_getshell | beecms ≤ V4.0_R_20160525 文件上传漏洞|

# Legal Disclaimer
本项目仅供教育和学习交流使用，请勿用于非法用途恶意攻击，否则后果作者概不负责。

This project is made for educational and ethical testing purposes only。It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.
