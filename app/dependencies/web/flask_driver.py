from flask import Flask as WebApp
from flask import request as WebRequest

# NOTE: for the sake of keeping a consistent API in the entire application, we will
# provide all the things that are needed inside the driver within this module by
# adding that functionality on top of the current library.
#
# e.g.
#
# def get(self, path: str): return self.route(path, methods=["GET"])
# WebApp.get = get
