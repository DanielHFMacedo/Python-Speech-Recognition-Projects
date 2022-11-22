import speech_recognition as sr
import pyttsx3



maquina = pyttsx3.init()
maquina.say("Olá, eu sou a Alexa.")
maquina.say("Diga alguma coisa?")
maquina.runAndWait()
microfone = sr.Recognizer()

def ouvir_microfone():
    audio = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)

        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
        try:
            # Passa a variável para o algoritmo reconhecedor de padroes
            frase = microfone.recognize_google(audio, language='pt-BR')
            # Retorna a frase pronunciada
            print("Você disse: " + frase)
            # Se nao reconheceu o padrao de fala, exibe a mensagem
        except sr.UnkownValueError:
            print("Não entendi")
        return frase

ouvir_microfone()