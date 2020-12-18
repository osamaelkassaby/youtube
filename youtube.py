from pafy import new
url = input("Enter you link     :  ") 
video= new(url)
audio = video.audiostreams
print(video)
hv = video.getbest()
stream = video.streams
print("          HIGH quality  chosess number 1 ")
print("          LOW qulality  chosess number 0     ")
print("          audio    chosess 2 ")
dl = input("Enter qulty :  ")
while dl == "1":
    hv.download()
while dl == "0":
    stream[0].download()
while dl == "2" :
    audio[0].download()    