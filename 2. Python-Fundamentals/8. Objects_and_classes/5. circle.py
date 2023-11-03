class Circle:
    __pi = 3.14
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        self.circumference = self.__pi * self.radius * 2
        return self.circumference
    def calculate_area(self):
        self.area = self.__pi * self.radius**2
        return self.area
    def calculate_area_of_sector(self, angle):
        self.area_of_sector = (angle/360) * self.__pi * self.radius**2
        return  self.area_of_sector

