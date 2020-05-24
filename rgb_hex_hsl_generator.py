import os
os.system("python -m pip install -r requirements.txt")
import numpy as np
import pandas as pd


class ColorCodesGenerator:
    """
    Generates rgb, hex and hsl color codes
    """
    
    def __init__(self, n_colors):
        """
        n_colors: an integer
            The value should be <= 16777216 since the number of possible rgb combinations are 256 * 256 * 256 = 16777216
        """
        assert isinstance(n_colors, int), 'n_colors takes only integer values'
        assert n_colors <= (256 * 256 * 256), 'n_colors should be an integer value less than or equal to 16777216'
        
        self.n_colors = n_colors
        self.__rgb_0_255_list = None
        self.__rgb_0_1_list = []
        self.__hex_codes_list = []
        self.__hsl_codes_list = []
    
    @staticmethod
    def suffix_0s(value: str = None) -> str:
        """
        Suffixes a single character hexa decimal value with 0.
        
        Parameter
        =========
        value = a string
            the character length should be 1. The value should be between 0-9, A-F
        
        Returns
        =======
        Returns a string of character length of 2.
        Example:
            if value = '0', the output will be '00'
            if value = 'a', the output will be '0A'
        """
        
        if len(value) < 2:
            return '0' + value
        else:
            return value
    
    @staticmethod
    def random_int_generator() -> int:
        """
        Returns one random integer between 0 and 255
        """
        return np.random.randint(low = 0, high = 255, size = 1).tolist().pop()
    
    def rgb_0_255(self) -> list:
        """
        Generates rgb colors in range 0 to 255.
        
        Returns
        =======
        a list of tuples where each tuple contain values for Red, Green, Blue colors.
        Example:
            If n_colors = 2, the output will be:
            [(23, 100, 79), (78, 25, 14)]
        """
        if self.__rgb_0_255_list is None:
            red = []
            green = []
            blue = []
            
            for _ in range(self.n_colors):
                r = self.random_int_generator()
                while r in red:
                    r = self.random_int_generator()
                red.append(r)
                
                g = self.random_int_generator()
                while g in green:
                    g = self.random_int_generator()
                green.append(g)
                
                b = self.random_int_generator()
                while b in blue:
                    b = self.random_int_generator()
                blue.append(b)
            
            self.__rgb_0_255_list = list(zip(red, green, blue))
        
        return self.__rgb_0_255_list
    
    def rgb_0_1(self) -> list:
        """
        Converts the values in __rgb_0_255_list from range 0 to 255 to 0.0 to 1.0

        Returns
        =======
        Returns a list of tuples where each tuple contain values for Red, Green and Blue.
        Example:
            if __rgb_0_255_list = [(23, 100, 79), (78, 25, 14)], then the output will be:
            [(23/255, 100/255, 79/255), (78/255, 25/255, 14/255)] = [(0.09019, 0.39215, 0.30980), (0.30588, 0.09803, 0.05490)]
        """
        if not self.__rgb_0_1_list:
            if self.__rgb_0_255_list is None:
                self.rgb_0_255()
            
            for r, g, b in self.__rgb_0_255_list:
                self.__rgb_0_1_list.append((round(r / 255, 5), round(g / 255, 5), round(b / 255, 5)))
        
        return self.__rgb_0_1_list
    
    def hex_codes(self) -> list:
        """
        Converts the values in __rgb_0_255_list from range 0 to 255 to hexa decimal system
        
        Returns
        =======
        Returns a list of strings.
        Example:
            if __rgb_0_255_list = [(23, 100, 79), (78, 25, 14)], then the output will be:
            ['#'17644F, '#4E190E']
        """
        if not self.__hex_codes_list:
            if self.__rgb_0_255_list is None:
                self.rgb_0_255()
            
            for r, g, b in self.__rgb_0_255_list:
                hex_code = '#' + \
                           self.suffix_0s(value = str(hex(r)[2:])) + \
                           self.suffix_0s(value = str(hex(g)[2:])) + \
                           self.suffix_0s(value = str(hex(b)[2:]))
                self.__hex_codes_list.append(hex_code.upper())
        
        return self.__hex_codes_list
    
    def hsl_codes(self) -> list:
        """
        Converts the values in __rgb_0_255_list to HSL values (Hue, Saturation, Luminance)
        
        Returns
        =======
        Returns a list of tuples where each tuple contain values for Hues, Saturation and Luminance
        Example:
            if __rgb_0_255_list = [(23, 100, 79)], then the output will be:
            [(23/255), (100/255), (79/255)] = [(0.09019, 0.39215, 0.30980)]
            vmin = min(0.09019, 0.39215, 0.30980) = 0.09019
            vmax = max(0.09019, 0.39215, 0.30980) = 0.39215
            luminance = (vmin + vmax)/2 = (0.09019 + 0.39215)/2 = 0.24117 = 24%
            
            if (vmin == vmax), then saturation = 0%
            if (vmin != vmax) and (luminance is <= 0.5), then saturation = (vmax - vmin)/(vmax + vmin)
            if (vmin != vmax) and (luminance is > 0.5), then saturation = (vmax - vmin)/(2.0 - vmax - vmin)
            saturation = (vmax - vmin)/(vmax + vmin) = (0.39215 - 0.09019)/(0.39215 + 0.09019) = 0.62603 = 63%
            
            if red is max, then hue = (green - blue)/(vmax - vmin)
            if green is max, then hue = 2.0 + ((blue - red)/(vmax - vmin))
            if blue is max, then hue = 4.0 + ((red - green)/(vmax - vmin))
            In our case, green is max. So, hue = 2.0 + ((0.30980 - 0.09019)/(0.39215 - 0.09019)) = 2.72728
            if hue is positive, then hue = hue * 60
            if hue is negative, then hue = (hue * 60) + 360
            hue = 2.72728 * 60 = 163.6368 = 164 degrees
            
            So, hsl values = [(164, 63, 24)]
        """
        if not self.__hsl_codes_list:
            if not self.__rgb_0_1_list:
                self.rgb_0_1()
            
            for r, g, b in self.__rgb_0_1_list:
                # Calculating luminance
                vmin = min(r, g, b)
                vmax = max(r, g, b)
                luminance = (vmin + vmax) / 2
                
                # Calculating saturation
                if luminance <= 0.5:
                    saturation = (vmax - vmin) / (vmax + vmin)
                else:
                    saturation = (vmax - vmin) / (2.0 - vmax - vmin)
                
                # Calculating hue
                if r == vmax:
                    hue = (g - b) / (vmax - vmin)
                elif g == vmax:
                    hue = 2.0 + ((b - r) / (vmax - vmin))
                else:
                    hue = 4.0 + ((r - g) / (vmax - vmin))
                
                if hue >= 0:
                    hue *= 60
                else:
                    hue = (hue * 60) + 360
                
                h = int(round(hue, 0))
                s = int(round(saturation * 100, 0))
                l = int(round(luminance * 100, 0))
                
                self.__hsl_codes_list.append((h, s, l))
        
        return self.__hsl_codes_list
    
    def all_in_dataframe(self) -> pd.DataFrame:
        """
        This creates a dataframe of all color codes
        """
        if self.__rgb_0_255_list is None:
            self.rgb_0_255()
        if not self.__rgb_0_1_list:
            self.rgb_0_1()
        if not self.__hex_codes_list:
            self.hex_codes()
        if not self.__hsl_codes_list:
            self.hsl_codes()
        return pd.DataFrame({'rgb_0_255': self.__rgb_0_255_list,
                             'rgb_0_1'  : self.__rgb_0_1_list,
                             'hex_codes': self.__hex_codes_list,
                             'hsl_codes': self.__hsl_codes_list})


def main():
    ncols = int(input('Number of colors to generate: '))
    print('''Available formats:
        rgb_0_255   RGB values on a 0 to 255 scale (68, 125, 220)
        rgb_0_1     RGB values on a 0.0 to 1.0 scale (0.257, 0.745, 0.947)
        hex_code    Hexa decimal values (#B2E591)
        hsl_code    Hue Saturation Luminance values (45, 97, 58)
    ''')
    code_format = input('Format you want (rgb_0_255, rgb_0,1, hex_code, hsl_code, all): ')
    
    col_gen = ColorCodesGenerator(n_colors = ncols)
    if code_format == 'rgb_0_255':
        print('====================== RGB (0 - 255) ======================')
        print(col_gen.rgb_0_255())
    elif code_format == 'rgb_0_1':
        print('====================== RGB (0.0 - 1.0) ======================')
        print(col_gen.rgb_0_1())
    elif code_format == 'hex_code':
        print('====================== HEX ======================')
        print(col_gen.hex_codes())
    elif code_format == 'hsl_code':
        print('====================== HSL ======================')
        print(col_gen.hsl_codes())
    elif code_format == 'all':
        print('====================== RGB (0 - 255) ======================')
        print(col_gen.rgb_0_255())
        print('====================== RGB (0.0 - 1.0) ======================')
        print(col_gen.rgb_0_1())
        print('====================== HEX ======================')
        print(col_gen.hex_codes())
        print('====================== HSL ======================')
        print(col_gen.hsl_codes())


if __name__ == '__main__':
    main()
