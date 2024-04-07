import speech_recognition as sr
# import pyfirmata

# comport = 'COM1'

# board = pyfirmata.Arduino(comport)

# red = board.get_pin('d:8:o')
# blue = board.get_pin('d:9:o')
# green = board.get_pin('d:10:o')


recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)



    try:
        print("You said: " + recognizer.recognize_google(audio))

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
