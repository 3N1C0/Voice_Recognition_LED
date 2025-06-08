import speech_recognition as sr 
import serial
import serial.tools.list_ports

# List all available ports
ports = serial.tools.list_ports.comports()
portsList = []

print("Available Serial Ports:")
for i, port in enumerate(ports):
    portsList.append(port.device)
    print(f"[{i}] {port.device} - {port.description}")

# Ask the user to choose a port by index
index = int(input("Select the port index for your Arduino: "))
use = portsList[index]

# Configure and open the serial connection
serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()

print(f"Connected to {use}")

def ar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Listening")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        if text == "turn on":
            command = "ON"
            return(command)
        elif text == "turn off":
            command = "OFF"
            return(command)
        elif text == "turn blink":
            command = "BLINK"
            return(command)
        elif text == "exit pass":
            command = "quit"
            return(command)
    except:
        print("Say something to get started")


while True:
    command = str(ar())
    serialInst.write(command.encode('utf-8'))
    if command == 'quit':
        print("Currently quitting...")
        quit()
    else:
        print("ON/OFF/BLINK:",command)
