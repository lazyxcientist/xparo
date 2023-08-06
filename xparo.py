
import websocket
import json
import threading
import requests
import time
import os
import datetime
from urllib.parse import urljoin
import logging
import time
import threading



xparo_website = 'xparo-website.onrender.com'
DEBUG = True


########### config file ###########
###################################
config_path = os.path.join(os.path.dirname(__file__), 'config.json')
config = {}
if os.path.exists(config_path):
    with open(config_path) as f:
        try:
            config = json.load(f)
        except:
            config = {}
if not config:
    with open(config_path, 'w') as f:
        json.dump(config, f)
def update_config(key,value):
    config[key] = value
    with open(config_path, 'w') as f:
        json.dump(config, f)
########### shedule control ###########
#######################################
shedule_control_path = os.path.join(os.path.dirname(__file__), 'shedule_control.json')
shedule_control = {}
if os.path.exists(shedule_control_path):
    with open(shedule_control_path) as f:
        try:
            shedule_control = json.load(f)
        except:
            shedule_control = {}
if not shedule_control:
    with open(shedule_control_path, 'w') as f:
        json.dump(shedule_control, f)

def update_shedule_control(data):
    if DEBUG:
        print("updating shedule control  ",data)
    global shedule_control_path
    with open(shedule_control_path, 'w') as f:
        json.dump(data, f)

def run_shedule_control(callback_fun): # {"command":{"date": "2023-07-23","time": "21:00"}}
    while True:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        time_now = datetime.datetime.now().strftime("%H:%M")
        for i,j in shedule_control.items():
            if j['date'] == date and j['time'] == time_now:
                if DEBUG:
                    print("shedule control")
                    print(i)
                try:
                    callback_fun(i)
                except Exception as e:
                    print("unable to send sheduled message",e)


############### error #############
###################################
errors_path = os.path.join(os.path.dirname(__file__), 'xparo_errors.json')
errors = []

if os.path.exists(errors_path):
    with open(errors_path) as f:
        try:
            errors = json.load(f)
        except json.JSONDecodeError:
            errors = []
if not errors:
    with open(errors_path, 'w') as f:
        json.dump(errors, f)

def add_error(error_type, message):
    time = str(datetime.datetime.now().time())
    date = str(datetime.datetime.now().date())
    error_data = {"type": error_type, "message": message, "time": time , "date":date}
    errors.append(error_data)
    with open(errors_path, mode='w', encoding='utf-8') as f:
        json.dump(errors, f, ensure_ascii=False)


# Configure logging
logging.basicConfig(
    filename='error.log',  # Specify the log file path
    level=logging.ERROR,  # Set the log level to capture only errors and above
    format='%(asctime)s [%(levelname)s] %(message)s'  # Define the log message format
)
# Monitor log file in real-time
def monitor_log_file():
    while True:
        with open('error.log', 'r') as file:
            file.seek(0, 2)  # Move the file pointer to the end
            for line in file:
                # Process and display the error message in real-time
                print(line.strip())
        time.sleep(1)

# Start log monitoring in a separate thread
monitor_thread = threading.Thread(target=monitor_log_file, daemon=True)
# monitor_thread.start() ## FIXME: uncomment this line to start the monitor thread







############### websocket #############
#######################################

class Xparo(websocket.WebSocketApp):
    def __init__(self, *args, **kwargs):
        super(Xparo, self).__init__(*args, **kwargs)



class Remote():
    def __init__(self):
        self.websocket_connected = False
        self.email = None
        self.remote = None
        self.callback = None
        self.connection_type = "rest"  #"websocket"

    def connect(self,email,remote_id,secret="public"):
        print('''

    connencting to ...
    ██╗░░██╗██████╗░░█████╗░██████╗░░█████╗░
    ╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
    ░╚███╔╝░██████╔╝███████║██████╔╝██║░░██║
    ░██╔██╗░██╔═══╝░██╔══██║██╔══██╗██║░░██║
    ██╔╝╚██╗██║░░░░░██║░░██║██║░░██║╚█████╔╝
    ╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░


        █▀▀█ █▀▀ █▀▄▀█ █▀▀█ ▀▀█▀▀ █▀▀ 
        █▄▄▀ █▀▀ █░▀░█ █░░█ ░░█░░ █▀▀ 
        ▀░▀▀ ▀▀▀ ▀░░░▀ ▀▀▀▀ ░░▀░░ ▀▀▀

        ''')
        self.email = email
        self.remote = remote_id
        if self.connection_type == "websocket":
            if not self.websocket_connected:
                # socket_server = 'ws://xparo-robot-remote.onrender.com/ws/remote/xparo_remote/123456789/robot/'
                socket_server='wss://'+xparo_website+'/ws/remote/'+str(self.email)+'/'+str(secret)+'/'+str(self.remote)+'/'
                self.ws = Xparo(str(socket_server),
                                on_message=self.on_ws_message,
                                on_error=self.on_ws_error,
                                on_open=self.on_ws_open,
                                on_close=self.on_ws_close,)
                self.websocket_connected = True
                threading.Thread(target=self.ws.run_forever).start()
            else:
                print("already connected to xparo remote")
        elif self.connection_type == "rest":
            self.start_reset_framework()
           

    def send(self,message):
        if self.connection_type == "websocket":
            try:
                self.ws.send(json.dumps({"robot_id":self.remote,"type":"command","data":message}))
            except Exception as e:
                print(e)
        elif self.connection_type == "rest":
            try:
                api_url = 'https://'+xparo_website+'/remote/client_remote_data/'+self.email+'/'+self.remote+'/'
                response = requests.post(api_url, data=json.dumps(message),headers={'Content-type': 'application/json'})
                if response.status_code == 201:
                    self.on_ws_message('self.ws', response.json())
                    if DEBUG:
                        print(f"command sent successfully {message}")
                else:
                    print("unable to send command",str(response))
            except Exception as e:
                print(e)

    def on_ws_message(self, ws, message):
        print(message)
        if self.connection_type == "websocket":
            if self.callback:
                self.callback(message)
        elif self.connection_type == "rest":
            kk = message.keys()
            if 'commands' in kk:
                if self.callback:
                    for i in message['commands']:
                        self.callback(i)
            if 'schedule_control' in kk:
                update_shedule_control(message['schedule_control'])
            if 'change_config' in kk:
                for i,j in message['change_config'].items():
                    update_config(i,j)
            if 'error' in kk:
                with open(errors_path, 'w') as f:
                    json.dump([], f)

    def on_ws_error(self, ws, error):
        print(error)

    # def ws_connection(self, dt, **kwargs):
    #     print("connecting to websocket")
    #     threading.Thread(target=self.ws.run_forever).start()


    def on_ws_open(self, ws):
        self.websocket_connected = True
        print('''
        \\\\Connection Sussessfull//
           \\\\X.P.A.R.O remote//
            \\\\is 🄻🄸🅅🄴 now//
        
        ''')


    def on_ws_close(self, ws):
        self.websocket_connected = False
        print('''

        
         xparo remote is
    █▀▀ █── █▀▀█ █▀▀ █▀▀ █▀▀▄ 
    █── █── █──█ ▀▀█ █▀▀ █──█ 
    ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀─
        retry again !!!

        ''')




    def start_reset_framework(self):
        print("starting reset framework")
        global config
        global errors
        datas = {
                "config":config, 
                "program_bugs":errors,
                }
        self.send(datas)
        while True:
            response = requests.get('https://'+xparo_website+'/remote/client_remote_data/'+self.email+'/'+self.remote)
            if response.status_code == 201:
                data = response.json()
                self.on_ws_message('self.ws',data)

            time.sleep(0.1)


# Wait for the monitor thread to finish gracefully
# monitor_thread.join() #FIXME: uncomment it for error tracking


if __name__ == "__main__":
    
    remote = Remote()
    remote.connect("xparo_remote","robot_id","123456789")

    def callback(message):
        print(message)
    remote.callback = callback

    remote.send("hello")