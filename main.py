import time
import BuBrain;
import sniper;
def main(CRN, username, password, season, semesterNumber):
    if(BuBrain.hasSeats(CRN,season, semesterNumber)):
        sniper.register(username, password, CRN);
    else:
        time.sleep(rand.randomint(30,60));
        main(CRN, username, password);
