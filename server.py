from bottle import *
import redis
r = redis.StrictRedis(host='localhost',port= 15402 ,password='requirepass' db = 0 )
@route('/')
def index():
 r.set(request.query['p'],str(r.get(request.query['p']))+str(request.query['t']))
 return 'ok'
run(host='0.0.0.0',port=15403,debug=True)