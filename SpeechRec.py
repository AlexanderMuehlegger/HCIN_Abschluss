import speech_recognition as sr
from terminal import Log
import logging

def no_op(*args, **kwargs):
    pass

sr.pprint = no_op
sr.print = no_op



class Speach_Input():
    def __init__(self):
        self.init_Mic()
    
    def init_Mic(self):
        _reload = True
        all_mics = ""
        while True:
            if _reload is True:
                all_mic_names = sr.Microphone.list_microphone_names()
                all_mics = sr.Microphone.list_working_microphones()
                numbers = []

                for mic in all_mics:
                    print(f"{mic} : {all_mics[mic]}")
                    numbers.append(mic)
                _reload = False

                # for index in range(len(all_mic_names)):
                #     print(f"{index} : {all_mics[index]}")
                #     numbers.append(index)
                # _reload = False

            print("Enter number of wished microphone (if not listet, enter: reload)")
            _input = input("> ")
            if(_input.lower() == "reload"):
                _reload = True
                Log.w("If microphone still not listed, try to speak while reload")
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
                print("Listening...")
                audio = recognizer.record(mic, duration=5)

                print("Recognizing...")
                text = recognizer.recognize_google(audio, language="de-DE")
                print("finished")
                return text.lower()
        except KeyboardInterrupt:
            exit()
        except:
            Log.e("Error interrupted recognition")
            return "ERROR: Recognition"
    


        
        
    

