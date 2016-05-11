from bottle import *
import redis
r = redis.StrictRedis(host='localhost',port= 6379 , db = 0 )
@route('/')
def index():
 r.set('current',request.forms.get('i'))
 return 'ok'
run('localhost',port=15403)