class Car(object):
    """
        Added constructor taking arguments *args and **kwargs where *args
        expects a list of items and **kwargs expects a dictionary. This allows 
        a class to be initialised with dynamic number of variables
    """
    def __init__(self, *args, **kwargs):
        self.type = ''
        #Check whether args has three variables and if so, then the third is assigned to self.type
        if len(args)==3:
            self.type = args[2]
        #Check whether args has two or more variables and if so, then the second is assigned to self.model
        if len(args)>=2:
            self.model = args[1]
        #If args does not hold two or more variables then self.model is assigned GM
        else:
            self.model = 'GM'
        #Check whether args has one or more variables and if so, then the first is assigned to self.name
        if len(args)>=1:
            self.name = args[0]
        #If args does not hold one or more variables then self.name is assigned General
        else:
            self.name = 'General'
        self.speed = 0
        self.assign_doors()
        self.assign_wheels()
    
    #Function used to assign the number of doors the car has
    def assign_doors(self):
        if self.name == 'Koenigsegg' or self.name == 'Porshe':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
    #Function used to assign the number of wheels the car has
    def assign_wheels(self):
        if self.type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
    #Function used to check whether the car is a saloon car or not
    def is_saloon(self):
        if self.type != 'trailer':
            return True
        else:
            return False
    #Function used to compute the speed of the car, depending on whether it's a trailer or not
    def drive(self, value):
        if self.type == 'trailer':
            self.speed = 11*value
        else:
            self.speed = 10**value
        return self