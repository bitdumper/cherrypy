from bottle import *
import redis
r = redis.StrictRedis(host='localhost',port= 6379 , db = 0 )
@route('/')
def index():
 r.set('current',request.forms.get('i'))
 return 'ok'
run(hist='0.0.0.0',port=15403,debug=True)