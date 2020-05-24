import os
os.sys("pip install -r requirements.txt")

import numpy as np

# Creating a function that will create random rgb colors




class ColorCodesGenerator:
    
    def __init__(self, n_colors):
        self.n_colors = n_colors
        self.__rgb_0_255_list = None
        self.__rgb_0_1_list = []
        
    def rgb_0_255(self):
        '''
        Generates rgb colors in range 0 to 255.
        
        Returns
        =======
        a list of tuples where each tuple contain values for Red, Green, Blue colors.
        Example:
            If n_colors = 2, the output will be:
            [(23, 100, 79), (78, 25, 14)]
        '''
        
        red = []
        green = []
        blue = []
        
        for _ in range(self.n_colors):
            while True:
                r = np.random.randint(low = 0, high = 255, size = 1).tolist().pop()
                if r not in red:
                    red.append(r)
                    break
            
            while True:
                g = np.random.randint(low = 0, high = 255, size = 1).tolist().pop()
                if g not in green:
                    green.append(g)
                    break
            
            while True:
                b = np.random.randint(low = 0, high = 255, size = 1).tolist().pop()
                if b not in blue:
                    blue.append(b)
                    break
        
        self.__rgb_0_255_list = list(zip(red, green, blue))
        
        return self.__rgb_0_255_list

    def rgb_0_1(self):
        '''
        Converts the values in __rgb_0_255_list from range 0 to 255 to 0.0 to 1.0

        Returns
        =======
        Returns a list of tuples where each tuple contain values for Red, Green and Blue.
        Example:
            if __rgb_0_255_list = [(23, 100, 79), (78, 25, 14)], then the output will be:
            [(23/255, 100/255, 79/255), (78/255, 25/255, 14/255)] = [(0.09019, 0.39215, 0.30980), (0.30588, 0.09803, 0.05490)]
        '''
    
        for r, g, b in self.__rgb_0_255_list:
            self.__rgb_0_1_list.append((round(r/255, 5), round(g/255, 5), round(b/255, 5)))
        
        return self.__rgb_0_1_list

    def hex_codes(self):
        '''
        Converts the values in __rgb_0_255_list from range 0 to 255 to hexa decimal system
        
        Returns
        =======
        Returns a list of strings.
        Example:
            if __rgb_0_255_list = [(23, 100, 79), (78, 25, 14)], then the output will be:
            ['#', '#']
        '''
        





x = ColorCodesGenerator(n_colors = 3)
x.rgb_0_255()
x.rgb_0_1()
y = ColorCodesGenerator(n_colors = 3)
y.rgb_0_255()
