#coding=utf-8

''' 一般类别的配置 '''
class ConfigCommon:
    img_http_prefix = 'localoa.mfhui.com'
    # 接口地址前缀
    http_host_prefix = 'http://local.meilapp.com'
    # 输出日志的路径
    log_path = '/home/kyle/www/log/meila_app/'
    # 日志名
    log_name = 'meila_app'
    # 日志等级 debug|info|warning|error|none
    log_level = 'INFO'
    # 上否调试模式，调试模式不检查签名
    debug = True
    #
    is_xsrf_cookies = True
    #
    cookie_secret = 'ARFWE56458480023423483$%^%&^*&@fdgdfgfyh;]dev0'
