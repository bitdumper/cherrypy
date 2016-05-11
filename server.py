from bottle import *
import redis
r = redis.StrictRedis(host='localhost',port= 6379 , db = 0 )
@route('/')
def index():
 r.set('current',request.forms.get('i'))
 return 'ok'
run(host='127.0.0.1',port=15403,debug=True)