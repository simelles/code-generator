import os

from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr


def listen_command():
    # получение звука с микрофона
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю Ваш код... ")
        audio = r.listen(source)

    try:
        our_speech = r.recognize_google(audio, language="ru")
        print("Вы сказали: " + our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError:
        return "ошибка"


def do_this_command(message):
    if 'конец' in message:
        exit()
    message = message.lower()
    say_message(message)
    with open(r'D:\Python\xak_24.11.22\message.txt', 'w', encoding='UTF-8') as file:
        file.write(message)
        file.write('\n')


def say_message(message):
    voice = gTTS(message, lang="ru")
    # запись разговорных mp3данных в файл
    file_voice_name = "_audio_" + str(time.time()) + "_" + str(random.randint(0, 100000)) + ".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    # print("Голосовой ассистент: " + message)
    os.remove(file_voice_name)


def main():
    while True:
        command = listen_command()
        do_this_command(command)


if __name__ == '__main__':
    main()
