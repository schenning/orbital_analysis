from tletools import TLE

class satellite: 
    def __init__(line1, line2, line3):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3


   


with open('oneweb-20-12-29.txt') as tlefile:
    f = tlefile.readlines() 


    n = len(f)
    cnt = 0
    while cnt <= n-9:
        for i in range(3):
            print (f[i+cnt])
            cnt +=3
         
