import neopixel
import pyb
p = pyb.Pin('PC6',pyb.Pin.OUT_PP)
n = neopixel.NeoPixel(p,8)
button = pyb.Pin('PA10',mode = pyb.Pin.IN, pull = pyb.Pin.PULL_UP)
count = 0

def fade():
    for j in range(256):
        for k in range(8):
            n[k] = (j,j,0)
        n.write()
        pyb.delay(3)
    for j in range(255,-1,-1):
        for k in range(8):
            n[k] = (j,j,0)
        n.write()
        pyb.delay(3)

def wheel(pos):
    if pos < 0 or pos > 255:
        return(0,0,0)
    if pos < 85:
        return(255 - pos * 3,pos * 3,0)
    if pos < 170:
        pos -= 85
        return(0,255 - pos * 3,pos * 3)
    pos -= 170
    return (pos * 3,0,255 - pos * 3)

def cycle():
    for j in range(255):
        for i in range(8):
            rc_index = (i * 256 // 8) + j
            n[i] = wheel(rc_index & 255)
        n.write()
        pyb.delay(1)

def strobe():
    for j in range(32):
        for k in range(8):
            n[k] = (255,0,0)
        n.write()
        pyb.delay(50)
        for k in range(8):
            n[k] = (0,255,0)
        n.write()
        pyb.delay(50)
        for k in range(8):
            n[k] = (0,0,255)
        n.write()
        pyb.delay(50)

def chase():
     for j in range(32):
        for k in range(8):
               n[k] = (0,256,256)
        if (j // 8) % 2 == 0:
             n[j % 8] = (0,128,0)
        else:
             n[(j % 8) - 1] = (0,0,128)
        n.write()
        pyb.delay(50) 

def chase3led():
     for j in range(32):
        for k in range(8):
            n[k] = (0,0,0)
        n[j % 8] = (256,0,0)
        n[(j % 8) - 1] = (0,256,0)
        n[(j % 8) - 2] = (0,0,256)
        n.write()
        pyb.delay(50)

def main():
    global count
    while True:
        if button.value() == 0:
            count += 1
        if count % 5 == 0:
                cycle()
        if count % 5 == 1:
                fade()
        if count % 5 == 2:
                strobe()
        if count % 5 == 3:
                chase()
        if count % 5 == 4:
                chase3led()        
        print(count)
main()
