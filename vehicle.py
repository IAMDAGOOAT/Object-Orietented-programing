class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speeed = max_speed
        self.mileage = mileage
        
car = vehicle(180, 15000)

print("Maximum Speed of My Car:", car.max_speeed)
print("Mileage of my Car:" , car.mileage)