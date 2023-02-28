    ██╗░░██╗██████╗░░█████╗░██████╗░░█████╗░
    ╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
    ░╚███╔╝░██████╔╝███████║██████╔╝██║░░██║
    ░██╔██╗░██╔═══╝░██╔══██║██╔══██╗██║░░██║
    ██╔╝╚██╗██║░░░░░██║░░██║██║░░██║╚█████╔╝
    ╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░


        █▀▀█ █▀▀ █▀▄▀█ █▀▀█ ▀▀█▀▀ █▀▀ 
        █▄▄▀ █▀▀ █░▀░█ █░░█ ░░█░░ █▀▀ 
        ▀░▀▀ ▀▀▀ ▀░░░▀ ▀▀▀▀ ░░▀░░ ▀▀▀


website: https://xplauncher.me/

github: https://github.com/lazyxcientist/xparo_remote

email:   xpassistantpersonal@gmail.com

linkedin: https://www.linkedin.com/in/pankaj-jangir-xp/

> requriements = websocket_client

-------------
## how to use
-------------
```python
    from xparo_remote.xparo import Remote
    
    remote = Remote()
    remote.connect("your_user_id","your_password","robot_id")  ### username , password, robot_id

    def callback(message): ## this fuction is called when new data is recieved from remote
        print(message)
    remote.callback = callback

    remote.send_websocket_message("hello")  ## this function is used to send data to websocket

```