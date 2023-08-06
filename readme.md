    ██╗░░██╗██████╗░░█████╗░██████╗░░█████╗░
    ╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
    ░╚███╔╝░██████╔╝███████║██████╔╝██║░░██║
    ░██╔██╗░██╔═══╝░██╔══██║██╔══██╗██║░░██║
    ██╔╝╚██╗██║░░░░░██║░░██║██║░░██║╚█████╔╝
    ╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░


        █▀▀█ █▀▀ █▀▄▀█ █▀▀█ ▀▀█▀▀ █▀▀ 
        █▄▄▀ █▀▀ █░▀░█ █░░█ ░░█░░ █▀▀ 
        ▀░▀▀ ▀▀▀ ▀░░░▀ ▀▀▀▀ ░░▀░░ ▀▀▀


website: https://xparo-website.onrender.com/

github: https://github.com/lazyxcientist/xparo_remote

email:   xpassistantpersonal@gmail.com


> requriements = websocket_client

-------------
## how to use
-------------
```python
    from xparo_remote.xparo import Remote
    
    remote = Remote()
    remote.connect("email","remote_id","secret_key_if_any")

    '''
        parameter
            1. your_email = a unique email or robot name , used for analytics
            2. remote_id = id of remote
            3. secret = use only if your remote is private 

    '''

    def callback(message): ## this fuction is called when new data is recieved from remote
        print(message)
    remote.callback = callback

    remote.send("hello")  ## this function is used to send data to websocket

```
