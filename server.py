#!/usr/bin/env python


from __future__ import print_function


from circuits import handler, Event, Component
from circuits.web import redirect, Controller, Server, Sessions, Static

from jinja2 import Environment, FileSystemLoader


defaults = {
    "appname": "MyApp",
    "version": "0.0.1",
}


class render(Event):
    """render Event"""


class JinjaRenderer(Component):

    channel = "web"

    def init(self, env, defaults):
        self.env = env
        self.defaults = defaults

    def render(self, name, **data):
        context = self.defaults.copy()
        context.update(data)
        template = self.env.get_template("{0:s}.html".format(name))

        return template.render(**context)


class Root(Controller):

    def GET(self, view=None):
        return self.fire(render("views/{0}".format(view or "index"), session=self.session), "web")


class Login(Controller):

    channel = "/login"

    def GET(self):
        return self.fire(render("login"), "web")

    def POST(self, username=None, password=None):
        if username == "admin" and password == "admin":
            self.session.update(active=True, username=username)

            return self.redirect("/")

        error = "Invalid Username or Password!"

        return self.fire(render("login", error=error), "web")


class Logout(Controller):

    channel = "/logout"

    def GET(self):
        return self.fire(render("logout"), "web")

    def POST(self):
        self.session.clear()

        return self.redirect("/login")


class LoginManager(Component):

    channel = "web"

    def init(self, login="/login", logout="/logout"):
        self.login = login
        self.logout = logout

        Login(self.login).register(self)
        Logout(self.logout).register(self)

    @handler("request", priority=0.2)
    def _on_request(self, event, req, res):
        if req.path == self.login:
            return

        if not req.session.get("active", False):
            print("No active session found!")
            print(req.session)
            event.stop()
            return redirect(req, res, self.login)


def main():
    app = Server(("0.0.0.0", 8000))

    Root().register(app)
    Static(docroot="static").register(app)

    env = Environment(loader=FileSystemLoader("templates"))
    JinjaRenderer(env, defaults).register(app)

    Sessions().register(app)
    # LoginManager().register(app)

    app.run()


if __name__ == "__main__":
    main()
