from . import home   #导入蓝图 home

@home.route("/")
def index():
    return "this is home"
