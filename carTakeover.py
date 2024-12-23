def care_takeover_distance(carSpeed1,carSpeed2,delta_t):
    d1 = t1 = None
    if(carSpeed2 <= carSpeed1):
        print("This second car will NEVER catch-up to the first car, because it's SLOW!!!!")
        return
    else:
        t1 = (carSpeed2*delta_t)/(carSpeed2-carSpeed1)
        d1 = carSpeed1*t1
        return d1
V1 = int(input("Enter the speed of firt car: "))
V2 = int(input("Enter the speed of second car: "))
delta_t = float(input("Enter the time difference between them by hour: "))
print("\n")
print("The distance at which car 2 will overtake car 1 is: " , care_takeover_distance(V1,V2,delta_t),"Km")
# tanger --> lagouira : 2315Km