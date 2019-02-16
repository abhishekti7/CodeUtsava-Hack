from random import randint
def events():
    events = {
        '1':['2019-02-16','Workshop on Arduibotics', 'NIT Raipur'],
        '2':['2019-02-17','Raipur Going Pink Marathon, Raipur'],
        '3':['2019-02-17','Anand Mela',' Gaurav Garden VIP Road'],
        '4':['2019-02-22','Electika',' NIT Raipur'],
        '5':['2019-02-23','Entreprenuer Club Meetup',' Magneto Conclave'],
        '6':['2019-02-27','Music Jammer Concert',' Raipur'],
        '7':['2019-03-02','Auto show 2019',' Wood castle banquets']
    }
    x = randint(1,7)
    return ""+events[str(x)][1]+" on "+events[str(x)][0]+" at "+events[str(x)][2]
