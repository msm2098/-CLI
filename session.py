from imlist import *
    session = requests.Session()
    def update_session(self):
        global session
        self.session.headers.update(headers)
        self.session.cookies.update(cookie_dict)