class AppStore:
    apps = []
    def add_application(self, app):
        self.apps += [app]
    def remove_application(self, app):
        self.apps.remove(app)

    def block_application(self, app):
        self.apps[self.apps.index(app)].blocked = True

    def total_apps(self):
        return len(self.apps)

class Application:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self, name, blocked = False):
        self.name == name
        self.blocked == blocked
