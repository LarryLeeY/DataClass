#-*-coding:utf-8-*-
import tornado.web
import simplejson as json

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("test.html")
    def post(self):
        str=self.get_argument("dat",None)#此处的'dat'对应ajax里的data:{dat:temp}的dat,即字典的键
        print str
        data = {'status':0,'message':'successfully','data':[str,]}#封装数据
        self.write(json.dumps(data))
        #调用json将数据格式化，使用write方法把数据传回到ajax在success情况下的的arg参数里