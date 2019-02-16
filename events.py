from random import randint
def events():
    events = {
        '1':['2019-02-16','attend Workshop on Arduibotics', 'NIT Raipur'],
        '2':['2019-02-17','run the Raipur Going Pink Marathon, Raipur'],
        '3':['2019-02-17','visit the Anand Mela',' Gaurav Garden VIP Road'],
        '4':['2019-02-22','participate in Electika',' NIT Raipur'],
        '5':['2019-02-23','attend the Entreprenuer Club Meetup',' Magneto Conclave'],
        '6':['2019-02-21','Watch Alita movie', 'Cinepolis, Raipur'],
        '7':['2019-02-27','enjoy the Music Jammer Concert',' Raipur'],
        '8':['2019-03-02','visit the Auto show 2019',' Wood castle banquets'],
        '9':['2019-02-18', 'See Gully Boy movie ','Cinemax, City Mall']
    }
    x = randint(1,9)
    # print(""+events[str(x)][1]+" on "+events[str(x)][0]+" at "+events[str(x)][2])
    return ""+events[str(x)][1]+" on "+events[str(x)][0]+" at "+events[str(x)][2]
