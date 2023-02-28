    ██╗░░██╗██████╗░░█████╗░██████╗░░█████╗░
    ╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
    ░╚███╔╝░██████╔╝███████║██████╔╝██║░░██║
    ░██╔██╗░██╔═══╝░██╔══██║██╔══██╗██║░░██║
    ██╔╝╚██╗██║░░░░░██║░░██║██║░░██║╚█████╔╝
    ╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░


        █▀▀█ █▀▀ █▀▄▀█ █▀▀█ ▀▀█▀▀ █▀▀ 
        █▄▄▀ █▀▀ █░▀░█ █░░█ ░░█░░ █▀▀ 
        ▀░▀▀ ▀▀▀ ▀░░░▀ ▀▀▀▀ ░░▀░░ ▀▀▀

    website: <a href="https://xplauncher.me/">https://xplauncher.me/</a>
    github:  lazyxcientist/xparo_remote
    email:   xpassistantpersonal@gmail.com


    requriements = websocket_client

    <h3>how to use</h3>
    '''
    from xparo_remote.xparo import Remote
    
    remote = Remote()
    remote.connect("your_user_id","your_password","robot_id")  ### username , password, robot_id

    def callback(message): ## this fuction is called when new data is recieved from remote
        print(message)
    remote.callback = callback

    remote.send_websocket_message("hello")  ## this function is used to send data to websocket

    '''