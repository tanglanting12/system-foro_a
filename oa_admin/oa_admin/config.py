#coding=utf-8

''' mysql 连接配置 '''
class ConfigMysql:
    host = '127.0.0.1'
    user_name = 'root'
    password = '123456'

''' 数据库名配置，开发机上每个人用自己的库 '''
class ConfigDBNames:
    oa = 'abert_oa'

''' 一般类别的配置 '''
class ConfigCommon:
    # admin管理后台能够访问的 hosts
    allowed_hosts = ('abertoa.mfhui.com', '127.0.0.1', )
    # 接口地址前缀
    http_host_prefix = 'http://abertoa.mfhui.com/'
    # 图片地址前缀，以后所有图片地址，都要拼接成全路径返回
    img_url_prefix = 'http://meilapp.mooo.com:10000/'
    # 输出日志的路径
    log_path = '/home/abert/www/log/oa/'
    # 日志等级 debug|info|warning|error|none
    log_level = 'INFO'
    # 上否调试模式，调试模式不检查签名
    debug = True
