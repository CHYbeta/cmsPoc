import imp


def load_poc(poc_name, poc_path):
    try:
        file_name, path_name, description = imp.find_module(poc_name, poc_path)
    except ImportError:
        print(
            "\033[31m[!] Import script error.Please make sure the script name and type name are right!\033[0m\n"
        )
        exit()
    script = imp.load_module('poc', file_name, path_name, description)
    return script


def run_poc(script,url):
    try:
        script.poc(url)
        return True
    except Exception:
        return False
