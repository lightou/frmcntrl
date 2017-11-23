class temperature:
    """ir sensor takes soil temperature readings at several points uniformly in the farm
    each temperature reading is then localised to a region. regions out of the norm
    are zeroed in and several readings upto 10 times in a diameter of 10 meters are taken"""
    #will use a matrix construct for the data and its localisation
    def __init__(self, norm = 28.0):
        self.norm = norm   

    def tmp_rdng(self):
        result = t.tmp_generator()
        print("Probe Reading is {} Celcius.".format(result))
        return result
    
    def tmp_generator(self):
        from random import randrange
        tmp = randrange(20, 35, 1)
        return float(tmp)
    
    def thrm(self, result):
        #reading current thermometer reading and update
        if result == self.norm:
            print("[Norm Temp Reading. General Temp Control Protocol Running].")
            return None
        elif result > self.norm:
            Rslt = True
            return Rslt
        else:
            Rslt = False
            return Rslt
    
    def Misting(self):
        """misting here controls the misting actuator. sprays a water mist"""
        #run misting protocol
        print("Misting Protocol Executing...") #contains device controlling code
        #this protocol runs routine intervaled misting
    
    def vent_ctrl(self, state):
        """runs the ventilation system"""
        if state>self.norm:
            print("Venting Sys Running...")
            #should run for a number of minutes. monitor temp drop per minute.
            #low energy maintenance protocol
        elif state==self.norm:
            print("Venting Sys Stopped...")
        elif state<self.norm:
            #General protocol runs here after
            t.routine_ctrl()
         
    def gen_tmp_ctrl(self, result):
        #function maintains temp around norm.
        if result>self.norm:
            print("Running Temperature Modification Protocol...")
            t.tmp_modifier(result)
        else:
            #run routine general protocol
            t.routine_ctrl()

    def tmp_modifier(self, result):
        """simulates temperature fall by a given value"""
        print('Unmodified Temperature Atmospherics is {:.2f}'.format(result))
        print("Executing Temperature Modification...")
        #function generates temperature reading. Interval time readings will be made."""
        result -=0.5
        while result>=float(self.norm - 3.0): #sets temperature below norm by 3 degrees
            print('Current Temperature Atmospherics is {:.2f}'.format(float(result)))
            if result==float(self.norm - 3.0):
                print("Temperature Atmospherics Normalized.")
                print("Routine Measures Deploying...")
                state = result
                t.vent_ctrl(state)
            else:
                state = result
                t.vent_ctrl(state)
            result -=0.5
    def routine_ctrl(self):
        """executes routine time intervaled temperature control"""
        print("Executing General Routine Protocol...")
        from time import time, sleep #simulation conditions
        from random import randrange
        time_interval = list(range(1, 5))
        for i in range(len(time_interval)):
            s = randrange(len(time_interval))
            #generating randomized time intervals to sample temperature and run routine controls
        t = time_interval[s]
        #employ a time dependent loop. at the end the of the count down function should terminate
        print("t is",t)
        start = time() #start run for program
        end = start+t
        print(start)
        print(end)
        T=0
        while T+start!=end:
            print("Routine Ventilation Running...")
            print("Routine Misting Running...")
            print("T is",T)
            #ventilation and misting execution happens here
            if T>=float(t) and T<float(t+0.5): #puts a cap to acceptable time range
                print("Routine Ventilation & Misting Completed.")
                break
            else:
                T +=float(time()-start)
        print("time loop ended")
        
    def main(self):
        from random import randrange
        moisture = randrange(50, 80, 5) #for testing purposes just. data will be got from sensor 
        result = t.tmp_rdng()
        _ = t.thrm(result)
        if _ is False:
            print("General ventilation protocol running")
            t.gen_tmp_ctrl(result)
        elif _ is None:
            print("Energy Sanitization Protocol Engaging...")
            t.gen_tmp_ctrl(result)
        else:
            print("Running misting protocol...")
            print("Running Ventilation Protocol...")
            t.gen_tmp_ctrl(result)

t = temperature()
t.main()
