from gtts import gTTS
import wikipedia as wiki

#wiki
query = input("audiobook wut\n")
result = wiki.page(title=query)
print("Got " + result.title + ", now encoding into mp3")
# tts = Text to Speech
tts = gTTS(text=result.summary,lang='en-uk') #language is in English-UK
tts.save(result.title + '.mp3')