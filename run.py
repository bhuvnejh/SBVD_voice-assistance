

# to run alexa
import multiprocessing


def startAlexa():
    print("Alexa is starting...")
    from main import start
    start()

#to run hotword   
def listenHotword():
    print("Listening for hotword...")
    from engine.features import hotword
    hotword()
    
    
#start both processes
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=startAlexa)
    p2 = multiprocessing.Process(target=listenHotword)
    p1.start()
    p2.start()
    p1.join()
    
    if p2.is_alive():
        p2.terminate()
        p2.join()
    
    print("system stop")
