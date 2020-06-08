import codecs
import serial				#import serial library
import numpy				#import numpy
import matplotlib.pyplot as plt	#import matplotlib library
from drawnow import*		#import everything from drawnow library
from tkinter import*			#Import everything from Tkinter library
from tkinter import messagebox			#Import tkMessageBox module
from PIL import ImageTk, Image	#Import the PIL.ImageTk module
from scipy.misc import imread#for background image
import matplotlib.cbook as cbook#for background image
import numpy as np #for scatter plot
#from drawnow import drawnow
import threading
import time
import math
from PIL import ImageTk, Image	#Import the PIL.ImageTk module
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

#from tkinter import *
#from tkinter.ttk import *

abc = True;
count =0
LAT1 =0
LON1 =0
LAT2 =0
LON2 =0
Axvalue=0
Ayvalue=0
Azvalue=0

Axvalue2=0
Ayvalue2=0
Azvalue2=0
HR1=0
HR2=0
Temperature1=0
Temperature2=0
Alert1 = 0
Alert2=0
sleepstate1='No Signal'
sleepstate2='No Signal'
HeartRate1=[]
HeartRate2=[]
Raw2=[]
Raw1=[]

stra =''
start_code =''

# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = '/dev/ttyUSB1'
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600
plt.ion()#interactive mode on

displayWindow = Tk()
displayWindow.title('INS Valsura , Faculty of Training Projects O-169/10 ')
displayWindow.geometry('730x600')
displayWindow.configure(background='black')

path1 = '/home/pi/Desktop/rsz_1th.png'
LogoImage = ImageTk.PhotoImage(Image.open(path1))
displayImage1 = Label(displayWindow, image = LogoImage)
displayImage1.place(x=630 ,y= 0,height = 100 , width = 100)

path2 = '/home/pi/Desktop/rsz_national_flag.png'
LogoflagImage = ImageTk.PhotoImage(Image.open(path2))
displayImage2 = Label(displayWindow, image = LogoflagImage)
displayImage2.place(x=0 ,y= 0,height = 100 , width = 150)

path3 = '/home/pi/Desktop/rsz_soldier.png'
LogosoldierImage = ImageTk.PhotoImage(Image.open(path3))
displayImage3 = Label(displayWindow, image = LogosoldierImage)
displayImage3.place(x=315 ,y= 400,height = 160 , width = 100)

def ThreadOne():
    global device
    dataArray1=[]
    dataArray2=[]
    global LAT1
    global LON1
    global LAT2
    global LON2
    global Temperature1
    global Temperature2
    global Alert1
    global Alert2
    global Axvalue
    global Ayvalue
    global Azvalue
    global Axvalue2
    global Ayvalue2
    global Azvalue2
    global HR1
    global HR2
    global RawBR1
    global RawBR2
    
    #global rootmeansqr
    global total
    global count
    '''global sleep'''
    global sleepstate1
    global sleepstate2
    
    '''
    global tempValue1
    global tempValue2
    global tempValue3
    global tempValue4
    global showtempValue1
    global showtempValue2
    global showtempValue3
    global showtempValue4
    '''
        
    while ser.inWaiting():
 
        reading_beforehex = ser.readline()        
        reading=reading_beforehex.hex().upper()
        
        start_code = reading[4:6]
        length = reading[2:6]
        Frame_type=reading[6:8]
        sixtyfouraddress=reading[10:26]
        sixteenaddress=reading[24:28]
        Receive_option=reading[28:30]
        data_set=reading[30:41]
        asciidata=reading_beforehex[17:70]

        try:
            if sixtyfouraddress == '0013A200417603A9':
                
                
                decodedasciidata1=(asciidata.decode('utf-8'))
               
                #dataArray1 =decodedasciidata.split(',')
                #print (dataArray1)
                dataArray1 =decodedasciidata1.split(',')
                #print (dataArray1)
                LAT1 = float(dataArray1[0])
                
                LON1 = float(dataArray1[1])
                                
                Axvalue=float(dataArray1[2])
                Ayvalue=float(dataArray1[3])
                Azvalue=float(dataArray1[4])
                HR1=float(dataArray1[5])
                Temperature1 =float(dataArray1[6])
                Alert1=float(dataArray1[7])
                RawBR1=float(dataArray1[8])

                
                Axvalue = (Axvalue *100)*(Axvalue *100)
                Ayvalue = (Ayvalue *100)*(Ayvalue *100)
                
                Azvalue = (Azvalue *100)*(Azvalue *100)
                
                total   = Axvalue + Ayvalue + Azvalue
                
                print ('temperature' , Temperature1)
                print ('total1' , total)
                
                if Alert1 ==1:
                    print ('Alert1' , Alert1)
                    sleepstate1 = 'Warning given'
                #else:
                    #sleepstate1 = 'awake''''
               
                count = count+1
                if total >11000:
                    count = 0
                    sleepstate1 = 'awake'
                if total <10000:
                    count =0
                    sleepstate1 = 'awake'
                if count > 15:
                    sleepstate1 = 'sleep'
                    print ('soldier1 sleep')
                   
                        
                #tempValue1 = str(x)
                #tempValue2 = str(y)

                #showtempValue1.set((str(tempValue1)))
                #showtempValue2.set((str(tempValue2)))             
                
            if sixtyfouraddress == '0013A200417603A2':
                         
                decodedasciidata2=(asciidata.decode('utf-8'))
                dataArray2 =decodedasciidata2.split(',')
                #print (dataArray2)
                
                LAT2 = float(dataArray2[0])
                
                LON2 = float(dataArray2[1])
               
                Axvalue2=float(dataArray2[2])
                Ayvalue2=float(dataArray2[3])
                Azvalue2=float(dataArray2[4])
                
                HR2 =float(dataArray2[5])
                Temperature2 =float(dataArray2[6])
                Alert2=float(dataArray2[7])

                RawBR2=float(dataArray2[8])
                RawBR2=RawBR2*0.1              
                
                print('RawBR2' , RawBR2)

                
                print ('temp' , Temperature2)         
                
                Axvalue2 = (Axvalue2 *100)*(Axvalue2 *100)
                Ayvalue2 = (Ayvalue2 *100)*(Ayvalue2 *100)
                
                Azvalue2 = (Azvalue2 *100)*(Azvalue2 *100)
                total   = Axvalue2 + Ayvalue2 + Azvalue2
                
                print ('total2' , total)
                if Alert2 ==1:
                    print ('Alert2' , Alert2)
                    sleepstate2 = 'Warning given'
                #else:
                    #sleepstate2 = 'awake''''
                    
                count = count+1
                if total >11000:
                    count = 0
                    sleepstate2 = 'Awake'
                if total <10000:
                    count =0
                    sleepstate2 = 'Awake'
                if count > 15:
                    sleepstate2 = 'sleep'
                    print ('soldier2 sleep')
    
                #tempValue1 = str(x1)
                #tempValue2 = str(y1)

                #showtempValue3.set((str(tempValue3)))
                #showtempValue4.set((str(tempValue4)))
        

                #print ('LAT2' , LAT2)  
            
        except:
            print('cannot convert ')
        
        
        #print(reading)
        #print(LAT1)
        #print(LON1)
        
        #print(bpm)
        #print (Ax)
        '''
        # for error detection
        
        print(reading)
        print(start_code)
        print(length)
        print(Frame_type)
        print(sixtyfouraddress)
        print(sixteenaddress)
        print(Receive_option)        
        print(data_set)         
        print('read without format =' , reading_beforehex)'''
        #print('read without format =' , reading_beforehex)
        print('message =' , asciidata)
        #print('read without format =' , reading_beforehex)
        #print(sixtyfouraddress)

def graphhr1():
    plt.plot(HeartRate1,'bo-',label='Heart rate')
    
    
def graphhr2():
    plt.ylim(0,50)
    plt.plot(HeartRate2,'w.-',label='Heart rate')
    plt.plot(Raw2,'y-',label='Heart rate')
    plt.title('Heart Rate values of soldiers')
    plt.xlabel('Time')
    plt.ylabel('Heart Rate')
    blue_patch = mpatches.Patch(color='yellow', label='Blood Presure Value')
    plt.legend(loc = 'lower right',handles=[blue_patch])
    
    white_line = mlines.Line2D([], [], color='white', marker='*',markersize=10, label='Heart Rate')
    plt.legend(loc = 'upper right',handles=[white_line])
    
    #/home/pi/Desktop/HR2.png
    datafile = cbook.get_sample_data('/home/pi/Downloads/Webp.net-resizeimage (1).png')
    img2 = imread(datafile)
    plt.imshow(img2, zorder=0, extent=[0,50, 0,50])
    

def SerialPortConnection():
    global ser
    try:
        print ("try to connect port 0 ")
        SERIAL_PORT = '/dev/ttyUSB0'
        ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
        print ("connected port 0 ")
    except:        
        print ("try to connect port 1 ")
        SERIAL_PORT = '/dev/ttyUSB1'
        ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
        print ("connected port 1 ")
   
def Threadfour():
    global HeartRate2
    global HR2
    global Raw2
    global RawBR2
    
    cnt=0
    plt.ion()
    fig1, ax1 = plt.subplots()    
    fig1.canvas.mpl_connect('close_event', handle_closehr1) 

    while logic==True:
         
        HeartRate2.append(HR2)
        Raw2.append(RawBR2)
        '''print (HeartRate2)'''
        
        drawnow(graphhr2)
        plt.pause(.000001)        

        cnt = cnt+ 1                    
        print ('count',cnt)                    
        if(cnt>20):
            HeartRate2.pop(0)
            Raw2.pop(0)         
        
    plt.close()

           
def Threadthree():
     
    x=LON1
    y=LAT1
    '''print (x)'''
    x1=LON2
    y1=LAT2   
    
    plt.ion()
    fig, ax = plt.subplots()
    
    ax.grid(color='b', linestyle='-', linewidth=0.2)
    plt.xlim(70.036462,70.054395,)
    plt.ylim(22.523721,22.544580)

    
    fig.canvas.mpl_connect('close_event', handle_close)

    sc = ax.scatter(x,y)
    sc1 = ax.scatter(x1,y1)
    fig.patch.set_facecolor('xkcd:mint green')
    fig.patch.set_edgecolor('green')
    fig.canvas.set_window_title('GPS position of soldiers INS Valsura')
    datafile = cbook.get_sample_data('gpsnew2.png')
    #python3.5/site-packages/matplotlib/mpl-data/sample_data/grace_hopper.png 
    img1 = imread(datafile)

    plt.scatter(x,y,zorder=1)
    plt.imshow(img1, zorder=0, extent=[70.036462,70.054395, 22.523721,22.544580 ])

    plt.draw()    

    xar=list()
    yar=list()    
        
    while abc==True:
        sc.set_offsets(np.c_[x,y])
        sc1.set_offsets(np.c_[(x1),y1])
        fig.canvas.draw_idle()                
        plt.pause(.000001)
        
def handle_close(evt):
    global abc
    
    abc = False
    print('Closed Figure!    cccccccccccccccccccc')
    print(abc)

def handle_closehr1(evt):
    global logic
    logic = False
    print('Closed Figure hr    cccccccccccccccccccc')
    print(logic)

def serialreadStart():
    threading.Thread(target=ThreadOne).start()

def serialreadlatlon():
    threading.Thread(target=Threadtwo).start()

def serialhr1():
    global logic
    logic = True
    print(logic)
    print('open Figure!hr1    oooooooooooooooooooooo')
    threading.Thread(target=Threadfour).start()
    #Threadfour()
   
def mapthreadstart():
    global abc
    abc = True
    print(abc)
    print('open Figure!    oooooooooooooooooooooo')
    threading.Thread(target=Threadthree).start()
    

showtempValue1=StringVar()
showtempValue2=StringVar()
showtempValue3=StringVar()
showtempValue4=StringVar()
showtempValue5=StringVar()
showtempValue6=StringVar()
showtempValue7=StringVar()
showtempValue8=StringVar()

def Threadtwo():
    
    while True:
        x=LON1
        y=LAT1
        x1=LON2
        y1=LAT2

        tempValue1 = str(x)
        tempValue2 = str(y)
        tempValue3 = str(x1)
        tempValue4 = str(y1)
        tempValue5 = str(sleepstate1)
        tempValue6 = str(sleepstate2)
        tempValue7 = str(Temperature1)
        tempValue8 = str(Temperature2)

        showtempValue1.set((str(tempValue1)))
        showtempValue2.set((str(tempValue2)))
        showtempValue3.set((str(tempValue3)))
        showtempValue4.set((str(tempValue4)))

        showtempValue5.set((str(tempValue5)))
        showtempValue6.set((str(tempValue6)))
        showtempValue7.set((str(tempValue7)))
        showtempValue8.set((str(tempValue8)))

# initial setting

# Place MAP  Plot Button
SerialPortConnection()
    
plotButton = Button(displayWindow, text ="DISPLAY\nGRAPH", bg = "yellow", command=mapthreadstart, font = ('Cambria', '9', 'bold'))
plotButton.place(x = 20, y = 500, height = 70, width = 70)


# Place Heart rate  Plot Button

plotButton = Button(displayWindow, text ="HR1\nGRAPH", bg = "yellow", command=serialhr1, font = ('Cambria', '9', 'bold'))
plotButton.place(x = 100, y = 500, height = 70, width = 70)


#Serial Data Read
plotButton = Button(displayWindow, text ="Serial Data", bg = "pink", command=serialreadStart, font = ('Cambria', '9', 'bold'))
plotButton.place(x = 520, y = 500, height = 70, width = 110)

# Place EXIT Buttons

exitButton = Button(displayWindow, text ="EXIT", bg = "blue",fg ="white", command = displayWindow.destroy, font = ('Cambria', '9', 'bold'))
exitButton.place(x = 640, y = 460, height = 40, width = 70)

#.......................................lat and lon reading section..................

# Placing lattitude Text Field read (DATA READ) button of soldier1 and soldier2
plotButton = Button(displayWindow, text ="Data Read", bg = "pink", command=serialreadlatlon, font = ('Cambria', '9', 'bold'))
plotButton.place(x = 630, y = 500, height = 70, width = 80)

#.......................................soldier 1 position details....................
# Placing lattitude Text Field label of soldier 1
t1 = Label(displayWindow, fg ="white",bg="green", text = 'LATTITUDE VALUE OF SOLDIER 1:', font = ('Cambria','9', 'bold'))
t1.place(x = 470, y = 160, height = 35, width = 250)

# Placing lattitude Text Field of soldier 1
    
Lattitudetxt1 = Label(displayWindow, bg= 'white', fg ="black",textvariable=showtempValue1, font= ('Cambria', '10', 'bold'))
Lattitudetxt1.place(x = 470, y = 200, height = 30, width = 150)

# Placing longitude Text Field label of soldier 1
t2 = Label(displayWindow, fg ="white", bg="red",text = 'LONGITUDE VALUE OF SOLDIER 1:', font = ('Cambria','9', 'bold'))
t2.place(x = 470, y = 240, height = 35, width = 250)

# Placing longitude Text Field of soldier 1
    
Longitudetxt2 = Label(displayWindow, bg= 'white', fg ="black",textvariable=showtempValue2, font= ('Cambria', '10', 'bold'))
Longitudetxt2.place(x = 470, y = 280, height = 30, width = 150)
# Placing sleeping state Text Field label of soldier 1
t6 = Label(displayWindow, fg ="white",bg="orange", text = 'DROWSINESS STATE OF SOLDIER 1', font = ('Cambria','9', 'bold'))
t6.place(x = 470, y = 320, height = 35, width = 250)

# Placing sleeping Text Field of soldier 1
    
Lattitudetxt5 = Label(displayWindow, bg= 'white', fg ="black",textvariable= showtempValue5 , font= ('Cambria', '10', 'bold'))
Lattitudetxt5.place(x = 470, y = 360, height = 30, width = 150)


# Placing outside temperature Text Field label of soldier 1
t8 = Label(displayWindow, fg ="white",bg="brown", text = 'Temperature near by soldier1', font = ('Cambria','9', 'bold'))
t8.place(x = 470, y = 400, height = 35, width = 250)

# Placing outside temperature Text Field of soldier 1
    
Lattitudetxt7 = Label(displayWindow, bg= 'white', fg ="black",textvariable= showtempValue7 , font= ('Cambria', '10', 'bold'))
Lattitudetxt7.place(x = 470, y = 440, height = 30, width = 150)
#.......................................soldier 2 position details....................
# Placing lattitude Text Field label of soldier 2
t3 = Label(displayWindow, fg ="white",bg="green", text = 'LATTITUDE VALUE OF SOLDIER 2:', font = ('Cambria','9', 'bold'))
t3.place(x = 10, y = 160, height = 35, width = 250)

# Placing lattitude Text Field of soldier 2
    
Lattitudetxt3 = Label(displayWindow, bg= 'white', fg ="black",textvariable=showtempValue3, font= ('Cambria', '10', 'bold'))
Lattitudetxt3.place(x = 10, y = 200, height = 30, width = 150)

# Placing longitude Text Field label of soldier 2
t4 = Label(displayWindow, fg ="white",bg="red", text = 'LONGITUDE VALUE OF SOLDIER 2:', font = ('Cambria','9', 'bold'))
t4.place(x = 10, y = 240, height = 35, width = 250)

# Placing longitude Text Field of soldier 2
    
Longitudetxt4 = Label(displayWindow, bg= 'white', fg ="black",textvariable=showtempValue4, font= ('Cambria', '10', 'bold'))
Longitudetxt4.place(x = 10, y = 280, height = 30, width = 150)
# Placing sleeping state Text Field label of soldier 2
t5 = Label(displayWindow, fg ="white",bg="orange", text = 'DROWSINESS STATE OF SOLDIER 2', font = ('Cambria','9', 'bold'))
t5.place(x = 10, y = 320, height = 35, width = 250)

# Placing sleeping Text Field of soldier 2
    
Lattitudetxt6 = Label(displayWindow, bg= 'white', fg ="black",textvariable= showtempValue6 , font= ('Cambria', '10', 'bold'))
Lattitudetxt6.place(x = 10, y = 360, height = 30, width = 150)

# Placing outside temperature Text Field label of soldier 1
t9 = Label(displayWindow, fg ="white",bg="brown", text = 'Temperature near by soldier2', font = ('Cambria','9', 'bold'))
t9.place(x = 10, y = 400, height = 35, width = 250)

# Placing outside temperature Text Field of soldier 1
    
Lattitudetxt8 = Label(displayWindow, bg= 'white', fg ="black",textvariable= showtempValue8 , font= ('Cambria', '10', 'bold'))
Lattitudetxt8.place(x = 10, y = 440, height = 30, width = 150)

# Placing topic
t7 = Label(displayWindow, fg ="yellow",bg="black", text = 'Valsura on Duty Soldiers Monitoring System (VDSMS)', font = ('Cambria','10', 'bold'))
t7.place(x = 190, y = 20, height = 35, width = 400)
    
displayWindow.mainloop()
