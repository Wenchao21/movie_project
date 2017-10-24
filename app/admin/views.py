from . import admin    # 导入蓝图 admin

@admin.route("/")
def index():
    return "this is admin"
