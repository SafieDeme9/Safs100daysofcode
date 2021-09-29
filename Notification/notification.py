import time
try:
    from plyer import notification
except ImportError:
    print("Failed")

while(True):
    notification.notify(title ="Start Coding Now!",
    message="You promised. You have to code 1hour!!",
    app_icon="code.ico",
    timeout =10
    )
    time.sleep(10)