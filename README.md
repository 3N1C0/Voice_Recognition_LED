# Voice-Controlled LED

Speak a command into your computer, and an LED on an Arduino switches on, switches off, or blinks. Python listens through the microphone, turns the speech into text, and sends a command over USB serial to the Arduino.

## Files

| File | What it is |
|---|---|
| `LED_Voice.py` | Python: speech recognition and serial sender |
| `Arduino_IDE_Script` | Arduino sketch: receives `ON`, `OFF` or `BLINK` and drives the LED on pin 2 |
| `Arduino_LED_Setup.png` | Wiring photo |

## How it works

1. The script lists the serial ports and asks you to pick the Arduino.
2. It listens for one phrase and sends it to Google's speech service.
3. `turn on` sends `ON`, `turn off` sends `OFF`, and `turn blink` sends `BLINK`.
4. The Arduino matches the command and changes the LED.

## Skills demonstrated

- **Speech recognition:** capturing microphone audio and converting it to text with the `speech_recognition` library.
- **Serial communication:** opening a port with `pyserial` at 9600 baud and sending commands.
- **Embedded control:** an Arduino sketch that parses commands and drives an output.
- **Python scripting:** an interactive port picker and a clear command mapping.

## Run it

1. Upload `Arduino_IDE_Script` to the Arduino and wire the LED to pin 2 as in `Arduino_LED_Setup.png`.
2. Install the Python libraries: `pip install SpeechRecognition pyaudio pyserial`.
3. Run `python LED_Voice.py`, pick the Arduino's port, then speak a command.

## Notes

- Recognition uses Google's online service, so it needs an internet connection.
- The script handles only the three phrases above. Any other speech is ignored.
