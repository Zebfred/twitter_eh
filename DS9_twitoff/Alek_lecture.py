Python 3.7.5 (default, Nov  1 2019, 02:16:23) 
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
App: TWITOFF.app [production]
Instance: /Users/aleks/Documents/LAMBDA_CLASSNOTES/twitoff_DS9/instance
>>> from TWITOFF.models import *
>>> DB.create_all() #creates sqlite database! (only do once)
>>> u1=User(name='austen', id=5453)
>>> t1=Tweet(text='whee', id=3)
>>> DB.session.add(u1)
>>> DB.session.add(t1)
>>> DB.session.commit()
>>> quit()