class ph_ctrl:
    def __init__(self):
        self.ph = float(input("Enter Test Value:- "))
        self.ph_norm = 6.8
        
    def get_ph_reading(self):
        """takes reading from a pH probe"""
        return self.ph

    def file_write(self, filename, func):
        with filename as _:
            result = str(func) #add info to database
            _.write(result+'\n')
        _.close()

    def file_read(self, filename):
        lst = []
        with filename as _:
            for line in _:
                line = _.readlines()
                lst +=line
            print(lst)
        return lst
        
    def ph_modifier(self, ph):
        #executes ph regulation protocol
        #the reading comes from a probe
        #iterates over volumes of either acid or base
        #being added to the fertigate.
        running = True
        while running:
            if ph < self.ph_norm:
                #execute iterative addition of base code
                #function delivers the desired ph value
                func = p.t_acid() #returns titrable acid
                file = open('t_acid.txt')
                data_base = []
                data_base += p.file_read(file1) #populates data base with ph values
                if len(data_base)<3: #creates average of three values
                    filename = open('t_acid.txt', 'a')
                    p.file_write(filename, func)
                    total = 0.0
                    for item in data_base:
                        total +=float(item)
                        print(total)
                        average_t_acid = total/len(data_base)
                else:
                    average_t_acid = func
                    p.Add_base(average_t_acid, ph)

            elif ph > 7.2:
                #execute iterative addition of acid code 
                #intelligent modulation of acid volumes
                func = p.t_base()
                filename = open('t_base.txt', 'a')
                p.file_write(filename, func)
                p.Add_acid(func, ph)
        else:
            if ph == 7.0 or ph == 7.2:
                running = False

    def Dispense(self, Acid_vol = 0, Base_vol = 0):
        """Adds a known volume of either base or acid"""
        #the disensing volumes are assigned zero
        #communicates with the dispensor by sending values corresponding to acid or base
        print("Dispensed {} ml of acid and {} base ml.".format(Acid_vol, Base_vol))

    def t_acid(self):
        #add these values to a database. the average is used to get
        #working conc for which to estimate t_acid values
        return input("Enter Conc of Titrable Acid:- ")


    def t_base(self):
        #add these values to a database. the average is used to get
        #working conc for which to estimate t_base values
        return input("Enter Conc of Titrable Base:- ")

    def Add_base(self, t_acid, ph):
        #t_acid is tritable acid. the pK value of the predominant acid spp
        #will be chosen over others.
        #the acid or base conc. can be determined iteratively over a range.
        pka = 6.8
        from math import log
        #pk value of the solution in question is determined beforehand
        ph_diff = ph - 7.2
        #calculating the molarity concentration
        #calculating the volume of a fixed molarity (0.1M) solution
        base_conc = (-10**(ph_diff - pka))*average_t_acid
        vol = (base_conc/0.1)*1000
        #dispense a fraction of the calculated volume vol
        #future code should allow for statitical optimisation of the fraction frac
        while ph < 7.2:
            factor = 1
            frac = 1/4
            disp_vol = factor * frac * vol
            p.Dispense(Acid_vol=0, Base_vol=disp_vol)
            new_ph_reading = p.get_ph_reading()
            ph_diff = new_ph_reading-ph
            if ph_diff <= 0.25*(self.ph_norm-ph):
                factor +=1 #increment factor
            elif ph_diff >= 0.25*(self.ph_norm-ph) and ph_diff <= 0.5*(self.ph_norm-ph):
                factor *=0.5 #reduces the multiplying factor
                frac = factor * frac
                disp_vol = frac * vol
                p.Dispense(Acid_vol = 0, Base_vol = disp_vol)
            elif new_ph_reading>=7.0 and new_ph_reading<=7.4:
                print("pH has been normalized at {}.".format(new_ph_reading))
                break
            elif ph_diff >= 1 and new_ph_reading>7.4:
                p.Add_acid(t_base=0.35) #By now the ph reading should be above 7.5 and mixture is therefore alkaline

            from math import log
            ph_diff = self.ph - self.ph_norm
            base_conc = (-10**(ph_diff - pka))*average_t_acid
            vol = (base_conc/0.1)*1000
            while ph < 7.2:
                factor = 1
                frac = 1/4
                disp_vol = factor * frac * vol
                p.Dispense(disp_vol)
                #read ph value here
                new_ph_reading = p.get_ph_reading()
                if (new_ph_reading - ph) <= 0.25:
                    factor +=1 #increment factor
                    frac = factor * frac
                    disp_vol = frac * vol
                    p.Dispense(Acid_vol = 0, Base_vol = disp_vol)
                elif (new_ph_reading - ph) >= 0.5 and (new_ph_reading - ph) <= 0.75:
                    factor *=0.5 #reduces the multiplying factor
                    frac = factor * frac
                    disp_vol = frac * vol
                    p.Dispense(Acid_vol = 0, Base_vol = disp_vol)
                elif (new_ph_reading - ph) >= 1.0:
                    p.Add_acid(new_ph_reading) #By now the ph reading should be above 7.5 and mixture is therefore alkaline

    def Add_acid(self, t_base, ph):
        #t_base is titrable base. the pK value of the predominant base spp
        #will be chosen over others.
        #the acid or base conc. can be determined iteratively over a range.
        file2 = open('t_base.txt')
        data_base2 = []
        total = 0.0
        data_base2 += p.file_read(file2)
        from math import log
        #pk value of the solution in question is determined beforehand
        pka = 6.8
        ph_diff = ph - 7.2
        for item in data_base2:
                total +=float(item)
                average_t_base = total/len(data_base2)
            
            #calculating the molarity concentration
            #calculating the volume of a fixed molarity (0.1M) solution
            acid_conc = (10**(ph_diff - pka))*average_t_base
            vol = (acid_conc/0.1)*1000
            #dispense a fraction of the calculated volume vol
            #future code should allow for statitical optimisation of the fraction frac
            while ph > 7.4:
                factor = 1
                frac = 1/4
                disp_vol = factor * frac * vol
                p.Dispense(Acid_vol = disp_vol, Base_vol = 0)
                #read ph value here
                new_ph_reading = p.get_ph_reading()
                if (ph - new_ph_reading) <= 0.15:
                    factor +=1 #increment factor
                    frac = factor * frac
                    disp_vol = frac * vol
                    p.Dispense(Acid_vol = disp_vol, Base_vol = 0)
                elif (ph - new_ph_reading) >= 0.5 and ph - new_ph_reading <= 0.75:
                    factor *=0.5 #halves the multiplying factor
                    frac = factor * frac
                    disp_vol = frac * vol
                    p.Dispense(Acid_vol = disp_vol, Base_vol = 0)
                elif (ph - new_ph_reading) >= 1:
                    p.Add_base(t_acid=0.35, ph=new_ph_reading) #By now the ph reading should be below 7.0 and mixture is therefore acidic

            def main(self):
        ph = float(p.get_ph_reading())
        if ph >= 7.0 and ph < 7.4:
            print("pH Value is {} and is optimal.\nThere's no need to adjust pH.".format(float(ph)))
            return
        else:
            p.ph_modifier(ph)
            
if __name__ == '__main__':
    p = ph_ctrl()
    p.main()
