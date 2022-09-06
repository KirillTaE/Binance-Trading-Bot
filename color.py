import win32gui

def pixel_color_at(x, y):
    hdc = win32gui.GetWindowDC(win32gui.GetDesktopWindow())
    c = int(win32gui.GetPixel(hdc, x, y))
    return (c & 0xff), ((c >> 8) & 0xff), ((c >> 16) & 0xff)# (r, g, b)

'''def find_pixel():
    print(*win32gui.GetCursorPos())'''

for i in range(234, 238):
    print(pixel_color_at(1739, i))
#print(pixel_color_at(*win32gui.GetCursorPos()))

#(0, 230, 118) green
#(255,82,82) red
'''green, red = 0, 0
for i in range(280, 284):
    if pixel_color_at(1525, i) == (0, 230, 118):
        green = 1
        break
    if pixel_color_at(1525, i) == (255, 82, 82):
        red = 1
        break
print(green, red)'''
while True:
    print(*win32gui.GetCursorPos())