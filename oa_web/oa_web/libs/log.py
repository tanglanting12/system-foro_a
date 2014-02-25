#coding=utf-8


from datetime import datetime
import logging

try:
    import codecs
except ImportError:
    codecs = None

from tornado.log import access_log, app_log, gen_log

class OaFileLogHandler(logging.FileHandler):

    _LOG_FILEFORMAT = '%Y%m%d%H'

    def __init__(self, filename, mode='a', encoding=None, delay=0):
        super(OaFileLogHandler, self).__init__(filename, mode, encoding, delay)

    def get_cur_filename(self):
        t = datetime.now()
        newlogfile = "%s/%s.log" % (self.baseFilename, t.strftime(self._LOG_FILEFORMAT))
        return newlogfile

    def _open(self):
        if self.encoding is None:
            stream = open(self.get_cur_filename(), self.mode)
        else:
            stream = codecs.open(self.get_cur_filename(), self.mode, self.encoding)
        return stream

    def _get_stream(self):
        if self.stream is None:
            self.stream = self._open()
        else:
            cur_filename = self.get_cur_filename()
            if cur_filename != self.stream.name:
                self.stream = self._open()

        return self.stream

    def emit(self, record):
        try:
            self._get_stream()
        except:
            return
        return logging.StreamHandler.emit(self, record)


def add_tornado_log_handler(path, log_level=None):

    for l in [access_log, app_log, gen_log]:
        if l.handlers:
            for h in l.handlers:
                if h.__class__ == OaFileLogHandler:
                    return
        handler = OaFileLogHandler(path)
        l.addHandler(handler)
        l.setLevel(log_level)