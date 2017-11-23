"""Farm management Soft Ware"""
#monitor inputs(seeds, fertilizers, labor, water for irrigation)
#soil profile (pH, nutrients both macro & micro, type, modification & water retention capacity)
#water retention is a function of porosity and clay content
#predicted out_puts
#farm monitoring and security measures (where does it report in case of security breaches)
#drone program
#irrigation and spray regimes (localized spraying)
#crop category (recommended growth regimes for crops of interest)

class crop(object):
    def __init__(self, crop_name=input('Enter a Crop Type:- ')):
        self.crop = crop_name
        self.veg_lst = ["tomatoes", "potatoes", "onions", "garllic", "kale"]
        if self.crop in ("vegies","veges","vegetables"):
                    print(
                        "Here is a list of possible ones below:\n",self.veg_lst,\
                        "\nWhich Vegetable Are You Interested In?"
                        )
                    _ = input(":- ")
                    if _ in self.veg_lst:
                        self.crop = _
    def croptyp(self):
            """lists a crop type/varieties and associated technology, requirements such as soil profile,
            watering regimes, fertilizer application, growing time"""
            #predictive code goes here to allow for mistypes.
            #the crop profile reads and prints information about the crop in question.
            #take the crop as argument hence it's a general function
            #information can be increased by creating more files dedicated to individual crop type
            #this information should be updatable
            if self.crop in self.veg_lst:
                    print("chosen crop is '%s'." % self.crop)
            else:
                    print("Crop not listed here. Would you like to send an inquiry?")

    def crop_profile(self, croptyp):
            """reads from a file. another function should via a secret code be able to update"""
            result = croptyp()
            result2 = str(result)+".txt"
            with open(result2) as file:
                    for line in file:
                            print(line)
            file.close()

class inputs_monitor:
    def __init__(self, seeds, fertilizer, water, pesticides, labor):
        self.seeds = seeds
        self.fertilizer = fertilizer
        self.water = water
        self.pesticides = pesticides
        self.labor = labor
    pass

class soil:
    def __init__(self, ph, nutrients, soil_type, modification, water_retention_capacity):
        self. ph = ph
        self.nutrients = nutrients
        self.soil_type = soil_type
        self.modification = modification
        self.water_rtn_cap = water_retention_capacity
    pass

class output_monitor:
    """should allow for data updates drawing on information gained from real time field data"""
    pass

c = crop()
c.croptyp()

