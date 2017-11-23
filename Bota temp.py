"""ir sensor takes soil temperature readings at several points uniformly in the farm
each temperature reading is then localised to a region. regions out of the norm
are zeroed in and several readings upto 10 times in a diameter of 10 meters are taken"""
#will use a matrix construct for the data and its localisation
def thrm_rdng():
	#takes thermometer reading and returns it
	return float(input(":- "))
	except ValueError:
		print("Please a numerical figure.")

def thrm(thrm_rdng):
	#reading current thermometer reading and update 
	tmp = thrm_rdng() 
	Rslt = True #initialize condition.
	if tmp > 28.0:
		Rslt = True
	else:
		Rslt = False
	return Rslt

def Misting(thrm):
	"""misting here controls the misting actuator. sprays a water mist"""
	mst = thrm()
	if mst is True:
		#run misting protocol
		print("run_misting") #contains device controlling code
	else:
		print("General Protocol Running.") #this protocol runs routine intervaled misting
def vent_ctrl(thrm):
	"""runs the ventilation system"""
	running = True
	while running and thrm is True:
		print("run_temp_ctrl protocol.") #should run for a number of minutes. monitor temp drop per minute.
	else:
		running = False
def main():
	moisture = randrange(50, 80, 10) #for testing purposes just. data will be got from sensor
	thrm(thrm_rdng)
	if thrm is False:
		print("general ventilation rotocol running")
	elif thrm is True and moisture <= 60:
		Misting(thrm)
	else:
		print("Running temperature control protocol.")
		vent_crl(thrm)

if __name__ == '__main__':
	main()
