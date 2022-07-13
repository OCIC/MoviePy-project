import math 
from moviepy.editor import *
import matplotlib

#Function parameters
#path {string}
#b_color {string} or {tuple} - background color of the frame; can either be a tuple or a string like "dark green" or "light pink"
#x_coor {string} - can either be "left", "center" or "right"
#duration {number} - length of the video
#fps {number} - frames per second
#zoom_speed {number} - ability to change zoom speed
def zoomIn(path, b_color= (255, 255, 255), x_coor="center", zoom_speed= 0.3, duration= 10, fps= 25):

  w, h = 1920, 1080
  
  #Snippet below (lines16-19) is from https://stackoverflow.com/a/55828103
  rgb_colors = {}
  for name, hex in matplotlib.colors.cnames.items():    #Creating a dictionary with human readable color names as keys and tuples with three rgb values
   rgb_colors[name] = matplotlib.colors.to_rgb(hex)     #Example: {"darkgreen" : (0, 255, 0)}

  #print(rgb_colors)

  #MIT Li-cense for MoviePy
  #Lines (48-50 here) were modified from this page  https://github.com/Zulko/moviepy/issues/1402
  """The MIT License (MIT)
  Copyright (c) 2015 Zulko

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE."""
  
  #Image attribution from the video
  #T<a href='https://www.freepik.com/vectors/colorful-fluid'>Colorful fluid vector created by freepik - www.freepik.com</a>
  slide = ImageClip(path).set_fps(fps).set_duration(duration).resize((w,h)).set_position((x_coor, "center"))
  
  slide = slide.resize(lambda t: 1 + zoom_speed *t)    #Zoom in effect

  if type(b_color) is tuple:

    slide = CompositeVideoClip([slide], size=(h, w), bg_color= (b_color[0], b_color[1], b_color[2]))

  elif type(b_color) is str:
    
    b_color.lower() #All the keys in the dictionary are lower case strings
    b_color = b_color.split() #The dictionary of colors contains two words glued together (e.g. light blue is lightblue)
                              #So split the two word string a human would write as an argument and convert them into a list
    
    try:

      my_rgb = rgb_colors.get(b_color[0] + b_color[1])  #Combine the two words from the list
      slide = CompositeVideoClip([slide], size=(h, w), 
      bg_color= (my_rgb[0]*255, my_rgb[1]*255, my_rgb[2]*255))  #Each value in the dictionary is a tuple of three values between 0 and 1
                                                                #indicating the perecentage of the amount of color in each channel
                                                                #thus multiply each channel by 255 to get an actual RGB value
    except:
      print("No background color matches the argument")
  
  return slide


my_zommed = zoomIn(path="abstract.jpg", b_color= "light green", x_coor= "left")
my_zommed.write_videofile('zoom-test-14.mp4')    