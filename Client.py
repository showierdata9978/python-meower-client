from threading import Thread

from  MeowerBot import Client

def on_raw_msg(msg):
    pass

def setup(user_cl:Client):

    user_cl.callback(on_raw_msg)
    cl_thread = Thread(target=user_cl.start)

    cl_thread.start()