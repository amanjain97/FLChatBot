import speech_recognition as sr
chunk_size = 1024
sample_rate = 16000
r = sr.Recognizer()
m = sr.Microphone()

with m as source:
	r.adjust_for_ambient_noise(source)

try:
	with sr.Microphone(device_index=0, sample_rate=sample_rate, chunk_size=chunk_size) as source:
	   print("Say something!")
	   r.adjust_for_ambient_noise(source)
	   audio = r.listen(source)
	   n = (r.recognize_google(audio))
	   print(n)
except:
	print("nahi chala")


# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))