import websocket

def on_open(ws):
    print("开始连接")

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

appkey=input('请输入appKey：')
wsapp = websocket.WebSocketApp("wss://www.dgrlm.com/wss/open/open/socket/news/{}".format(appkey),
on_open=on_open,
on_message=on_message,
on_error=on_error,
on_close=on_close)

wsapp.run_forever(ping_interval=15, ping_timeout=10, ping_payload="This is an optional ping payload")

