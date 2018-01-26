class Television(object):
    
    # constructor method which sets attributes
    def __init__(self, volume = 0, channel = 1):
        self.volume = volume
        self.channel = channel
    
    def volumeDown(self):
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0
            print ('Volume cannot get lower')
        else:
            print('Volume:', self.volume)
    
    def volumeUp(self):
        self.volume += 1
        if self.volume > 30:
            self.volume = 30
            print('Volume cannot get higher')
        else:
            print('Volume:', self.volume)
            
    def changeChannel(self, channel):
        if channel == 1:
            print('Nederland 1')
        elif channel == 2:
            print('RTL')
        elif channel == 3:
            print('Nickelodeon')
        else:
            print('Channel does not exist')
            
def main():
    choice = None
    
    # create an object of television
    tv = Television()
    
    while choice != "0":
        print("""Press 1 to turn down the volume, 2 to turn up the volume, 3 to choose a channel""")
        
        choice = input("Choice: ")
            
        elif choice == "1":
            tv.volumeDown()
            
        elif choice == "2":
            tv.volumeUp()
           
        elif choice == "3":
            channel = input('Which channel: ')
            tv.changeChannel(int(channel))
            
# constantly call the main function
main()
