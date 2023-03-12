import speech_recognition as sr
from terminal import Log

class Speach_Input():

    def __init__(self):
        self.init_Mic()
    
    def init_Mic(self):
        _reload = True
        all_mics = ""
        while True:
            if _reload is True:
                all_mics = sr.Microphone.list_working_microphones()
                numbers = []

                for mic in all_mics:
                    print(f"{mic} : {all_mics[mic]}")
                    numbers.append(mic)
                _reload = False

            print("Enter number of wished Microphone (if not listet, enter: reload)")
            _input = input("> ")
            if(_input.lower() == "reload"):
                _reload = True
                continue
            try:
                if int(_input) in numbers:
                    self.microphone = int(_input) 
                    Log.s(f"'{all_mics[int(_input)]}' got locked in")
                    break
                else:
                    Log.e("Number not available")
            except ValueError:
                Log.e("Must be Number")



    def read_input(self):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone(self.microphone) as mic:
                audio = recognizer.record(mic, duration=5)

                text = recognizer.recognize_google(audio, language="de-DE")

                return text.lower()
        except KeyboardInterrupt:
            exit()
        except:
            return "ERROR: Recognition"
    

input_speach = Speach_Input()
input_speach.read_input()


        
        
    

