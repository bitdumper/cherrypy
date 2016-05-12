from bottle import *
import redis
r = redis.StrictRedis(host='localhost',port= 6379 , db = 0 )
@route('/')
def index():
 r.set(request.query['p'],r.get(request.query['p'])+request.query['t'])
 return 'ok'
run(host='0.0.0.0',port=15403,debug=True)