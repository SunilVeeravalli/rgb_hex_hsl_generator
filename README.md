# RGB, HEX and HSL color codes generator

## Introduction

### RGB
For computers, television, mobile devices etc., RGB (Red Green Blue) is the most commonly used color profile. Other colors are generated from the combinations of red, green and blue colors.  

Each color in RGB can be represented using a 0 to 255 scale or a 0.0 to 1.0 scale.

For example: RGB values for the color Magenta is (202, 31, 123) on a 0 to 255 scale or (0.79215, 0.12156, 0.48235) on a 0.0 to 1.0 scale

### HEX
Hexa decimal representation of colors is mostly sen in web designers and developers. HEX color is a six characters alpha numeric generated from RGB values.

For example: the HEX code for the color Magenta is #CA1F7B

### HSL
HSL (Hue, Saturation, Luminance or Lightness) is also an alternative representation of RGB values. The value of hue is in degrees where as the values for saturation and Luminance are in percentages.

For example: the HSL code for the color Magenta is (328, 73, 46) where 328<sup>o</sup> is Hue, 73% is Saturation and 46% is Luminance.


## User guide
I developed a program that generates distinct and random color values in RGB, HEX and HSL format. Let me show you the usage in an IDE vs Terminal with some examples.

Note:  
- The RGB values on a scale 0 to 255 will be created first and these values will be used as a source to generate RGB values on a scale 0.0 to 1.0 as well as for HEX and HSL calculations.

### 1. Using an IDE or Jupyter notebook:
Run the script `rgb_hex_hsl_generator.py` which will install the required libraries mentioned in `requirements.txt` and imports them and creates the class object **ColorCodesGenerator** in memory.

To generate five colors:
```python
five_colors = ColorCodesGenerator(n_colors = 5)
```
If you are interested in RGB values on a scale 0 to 255, then:
```python
five_colors.rgb_0_255()
[(166, 98, 106), (14, 127, 8), (228, 13, 42), (247, 158, 235), (35, 77, 115)]
```
If you are interested in RGB values on a scale 0.0 to 1.0, then:
```python
five_colors.rgb_0_1()
[(0.65098, 0.38431, 0.41569), (0.0549, 0.49804, 0.03137), (0.89412, 0.05098, 0.16471), (0.96863, 0.61961, 0.92157), (0.13725, 0.30196, 0.45098)]
```
If you are interested in HEX values, then:
```python
five_colors.hex_codes()
['#A6626A', '#0E7F08', '#E40D2A', '#F79EEB', '#234D73']
```
If you are interested in HSL values, then:
```python
five_colors.hsl_codes()
[(353, 28, 52), (117, 88, 26), (352, 89, 47), (308, 85, 79), (208, 53, 29)]
```
To save all the color codes as a data frame, then:
```python
five_colors_df = five_colors.all_in_dataframe()
print(five_colors_df)

         rgb_0_255                      rgb_0_1 hex_codes      hsl_codes
0   (166, 98, 106)  (0.65098, 0.38431, 0.41569)   #A6626A  (353, 28, 52)
1     (14, 127, 8)   (0.0549, 0.49804, 0.03137)   #0E7F08  (117, 88, 26)
2    (228, 13, 42)  (0.89412, 0.05098, 0.16471)   #E40D2A  (352, 89, 47)
3  (247, 158, 235)  (0.96863, 0.61961, 0.92157)   #F79EEB  (308, 85, 79)
4    (35, 77, 115)  (0.13725, 0.30196, 0.45098)   #234D73  (208, 53, 29)
```

There is not need to go in a sequence like: first rgb_0_255(), then rgb_0_1(), then hex_codes() etc. One can directly request say hex_codes() after initializing the class as shown below.
```python
ten_colors = ColorCodesGenerator(n_colors = 10)
ten_colors.hex_codes()
['#84D691', '#A8E07F', '#3037C4', '#D5FB43', '#341000', '#83702D', '#C4385E', '#EAEA5A', '#A1D547', '#475569']
```
Or, one can directly generate the data frame by:
```python
twenty_colors = ColorCodesGenerator(n_colors = 20)
twenty_colors.all_in_dataframe()

          rgb_0_255                      rgb_0_1 hex_codes      hsl_codes
0   (221, 180, 109)  (0.86667, 0.70588, 0.42745)   #DDB46D   (38, 62, 65)
1    (112, 159, 40)  (0.43922, 0.62353, 0.15686)   #709F28   (84, 60, 39)
2     (47, 97, 175)  (0.18431, 0.38039, 0.68627)   #2F61AF  (217, 58, 44)
3     (34, 186, 66)  (0.13333, 0.72941, 0.25882)   #22BA42  (133, 69, 43)
4     (141, 41, 52)  (0.55294, 0.16078, 0.20392)   #8D2934  (353, 55, 36)
5      (209, 12, 6)  (0.81961, 0.04706, 0.02353)   #D10C06    (2, 94, 42)
6      (39, 43, 47)  (0.15294, 0.16863, 0.18431)   #272B2F   (210, 9, 17)
7      (50, 62, 55)  (0.19608, 0.24314, 0.21569)   #323E37  (145, 11, 22)
8   (224, 195, 147)  (0.87843, 0.76471, 0.57647)   #E0C393   (37, 55, 73)
9     (20, 241, 11)   (0.07843, 0.9451, 0.04314)   #14F10B  (118, 91, 49)
10  (162, 106, 229)  (0.63529, 0.41569, 0.89804)   #A26AE5  (267, 70, 66)
11   (249, 119, 87)  (0.97647, 0.46667, 0.34118)   #F97757   (12, 93, 66)
12   (27, 148, 220)  (0.10588, 0.58039, 0.86275)   #1B94DC  (202, 78, 48)
13  (142, 139, 111)   (0.55686, 0.5451, 0.43529)   #8E8B6F   (54, 12, 50)
14  (178, 245, 139)   (0.69804, 0.96078, 0.5451)   #B2F58B   (98, 84, 75)
15   (240, 24, 146)  (0.94118, 0.09412, 0.57255)   #F01892  (326, 88, 52)
16    (40, 15, 249)  (0.15686, 0.05882, 0.97647)   #280FF9  (246, 95, 52)
17    (74, 46, 192)   (0.2902, 0.18039, 0.75294)   #4A2EC0  (252, 61, 47)
18    (75, 190, 88)    (0.29412, 0.7451, 0.3451)   #4BBE58  (127, 47, 52)
19  (118, 146, 125)   (0.46275, 0.57255, 0.4902)   #76927D  (135, 11, 52)
```

### 2. Using a CLI terminal:



