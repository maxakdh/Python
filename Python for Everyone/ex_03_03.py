try :
    sc = float(input('Enter Score:'))
    if sc < 0.0 :
        quit()
    elif sc > 1.0 :
        quit()
    elif sc >=0.9 :
        print ('A')
    elif sc >= 0.8 :
        print ('B')
    elif sc >= 0.7 :
        print ('C')
    elif sc >= 0.6 :
        print ('D')
    elif sc > 0.6 :
        print ('F')
except:
    print("ERROR, please enter a number from 0 to 1.0")
    quit()
