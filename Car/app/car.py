class Car(object):
    def __init__(self, *args, **kwargs):
        self.type = ''
        if len(args)>=1:
            self.type = args[0]
        if len(args)>=2:
            self.model = args[1]
        else:
            self.model = 'GM'
        if len(args)==3:
            self.name = args[2]
        else:
            self.name = 'General'
        self.speed = 0
        if self.type != '':
            self.assign_doors()
            self.assign_wheels()												
    def assign_doors(self):
        if self.type == 'Koenigsegg' or self.type == 'Porshe':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
    def assign_wheels(self):
        if self.type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
    def is_saloon(self):
        if self.type != 'trailer':
            return True
    def drive(self, value):
        if self.type == 'trailer':
            speed = value*11
        else:
            speed = value*(1000/3)
            return Car()