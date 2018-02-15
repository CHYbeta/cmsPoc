def url_check(url,check_name):
    if not url.endswith(check_name):
        print("[*] Please make sure the url end with '%s'" % check_name)
        exit()