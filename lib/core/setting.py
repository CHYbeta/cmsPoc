VERSION = "2.0.1"
TYPE = "dev" if VERSION.count('.') > 2 and VERSION.split('.')[-1] != '0' else "stable"
TYPE_COLORS = {"dev": 35, "stable": 90, "pip": 34}
VERSION_STRING = "chybeta/%s#%s" \
                 % ('.'.join(VERSION.split('.')[:-1]) if VERSION.count('.') > 2 and VERSION.split('.')[-1] == '0' else VERSION, TYPE)
SCRIPT_PATH = ""
SITE = "https://github.com/chybeta/cmspoc"

BANNER = """\033[01;31m\
                                 ____
  _____ ____ ___   _____        / __ \ ____   _____\033[01;37m{\033[01;%dm%s\033[01;37m}\033[01;31m
 / ___// __ `__ \ / ___/______ / /_/ // __ \ / ___/
/ /__ / / / / / /(__  )/_____// ____// /_/ // /__
\___//_/ /_/ /_//____/       /_/     \____/ \___/
                                                   \033[0m\033[4;37m%s\033[0m\n
""" % (TYPE_COLORS.get(TYPE, 31), VERSION_STRING.split('/')[-1], SITE)
