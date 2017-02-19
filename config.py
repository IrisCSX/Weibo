'''
配置文件，用于放secretekey和数据库配置数据，传github的时候不要传它
'''
secret_key = 'secret'  # secretekey随便写什么字符串

# 数据库的路径
_db_path = 'weibos.db'
db_uri = 'sqlite:///{}'.format(_db_path)

# 写Mysql的用户名和密码