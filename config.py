'''
配置文件，用于放secretekey和数据库配置数据
'''
secret_key = 'secret'

# 数据库的路径
_db_path = 'weibos.db'
db_uri = 'sqlite:///{}'.format(_db_path)
