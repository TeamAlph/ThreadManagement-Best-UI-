# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 03:32:17 2019

@author: usman
"""
import speedtest
import winsound
import sys
import wx
import glob
import psutil
import datetime
import platform
import matplotlib.pyplot as plt
from _thread import start_new_thread
import socket
import numpy as np
import pandas as pd
import signal
import subprocess
import os
import time
import wx.lib.agw.pygauge as PG
import platform
import threading

from psutil import virtual_memory
import matplotlib.patheffects as path_effects
pol=""
class ChildFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, None, size=(1660,1350), title='System')
       
        self.parent = parent
        pan = wx.Panel(self)
        self.ToggleWindowStyle(wx.STAY_ON_TOP)
        pan.SetBackgroundColour('CORNFLOWER BLUE')
        text=wx.StaticText(pan, 0, "WELCOME", (525, 300))
        text.SetForegroundColour(wx.WHITE)
        font = wx.Font(55,  wx.MODERN,  wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        text.Show()
        
        text1=wx.StaticText(pan, 0, "SYSTEM MANAGEMENT", (562, 370))
        text1.SetForegroundColour(wx.WHITE)
        font = wx.Font(17,  wx.MODERN,  wx.NORMAL, wx.NORMAL)
        text1.SetFont(font)
        text1.Show()
        
        
        
        gauge1 = PG.PyGauge(pan, -1, pos=(350, 590),size=(665, 20),style=wx.GA_HORIZONTAL)
        gauge1.SetValue(20)
        gauge1.SetDrawValue(draw=True, drawPercent=True, font=None, colour=wx.BLACK, formatString=None)
        gauge1.SetBackgroundColour(wx.WHITE)
        gauge1.SetBorderColor('FIREBRICK')
        gauge1.SetForegroundColour('FIREBRICK')
        
        usm7 = wx.Button(pan, -1, "", pos=(502, 233),size=(120,70))
        usm7.Bind(wx.EVT_BUTTON,self.PIKO3)
        usm7.SetBitmap(wx.Bitmap('Project Images Os\\pk783.png'))
        usm7.SetBackgroundColour('CORNFLOWER BLUE')
        usm7.SetWindowStyleFlag(wx.NO_BORDER)
        
        bg_img1='Project Images Os\\264.jpg'
        pan.bg1 = wx.Bitmap(bg_img1)
        #pan.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        #self.bg = wx.Bitmap(bg_img)
        #pan._width, pan._height = pan.bg1.GetSize()
        
        
    def PIKO3(self,event):
            pass
       #sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(gauge1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 250)
        #self.SetSizer(sizer)
        #sizer.Layout()
        
        
        
        # time.sleep(5)
        #self.txt = wx.TextCtrl(pan, -1, pos=(0,0), size=(100,20), style=wx.DEFAULT)
        #self.but = wx.Button(pan,-1, pos=(10,30), label='Tell parent')
        #self.Bind(wx.EVT_BUTTON, self.onbutton, self.but)
class SummingThread(threading.Thread):
     def __init__(self,low,high):
         super(SummingThread, self).__init__()
         self.low=low
         self.high=high
         self.total=0

     def run(self):
         for i in range(self.low,self.high):
             self.total+=i
             
class MainPanel(wx.Panel):
    
    def __init__(self, parent, bg_img='Project Images Os\\usman122.jpg'):
        
        wx.Panel.__init__(self, parent=parent)
        
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.bg = wx.Bitmap(bg_img)
        self._width, self._height = self.bg.GetSize()
        
        #panel = wx.Panel(self)
        usman = wx.Button(self, -1, "SHOW PROCESS", pos=(255,210),size=(155,56))
        usman.Bind(wx.EVT_BUTTON,self.my)
        usman.SetBitmap(wx.Bitmap('Project Images Os\\ln1.png'))
        usman.SetBackgroundColour('BLUE VIOLET')
        
        
        usman1 = wx.Button(self, -1, "SHOW CPU%", pos=(425,210),size=(155,56))
        usman1.Bind(wx.EVT_BUTTON,self.my1)
        usman1.SetBitmap(wx.Bitmap('Project Images Os\\dr.png'))
        usman1.SetBackgroundColour('BLUE VIOLET')

        usman2 = wx.Button(self, -1, "MEMORY USAGE", pos=(595,210),size=(155,56))
        usman2.Bind(wx.EVT_BUTTON,self.my2)
        usman2.SetBitmap(wx.Bitmap('Project Images Os\\mem.png'))
        usman2.SetBackgroundColour('BLUE VIOLET')
        
        usman3 = wx.Button(self, -1, "PROCESS COUNT", pos=(255, 280),size=(155,56))
        usman3.Bind(wx.EVT_BUTTON,self.my3)
        usman3.SetBitmap(wx.Bitmap('Project Images Os\\count.png'))
        usman3.SetBackgroundColour('BLUE VIOLET')
        
        usman4 = wx.Button(self, -1, "PROCESS NAMES", pos=(425, 280),size=(155,56))
        usman4.Bind(wx.EVT_BUTTON,self.my4)
        usman4.SetBitmap(wx.Bitmap('Project Images Os\\na.png'))
        usman4.SetBackgroundColour('BLUE VIOLET')
        
        usman5 = wx.Button(self, -1, "RAM USAGE", pos=(595, 280),size=(155,56))
        usman5.Bind(wx.EVT_BUTTON,self.my5) 
        usman5.SetBitmap(wx.Bitmap('Project Images Os\\db.png'))
        usman5.SetBackgroundColour('BLUE VIOLET')
        
        usman6 = wx.Button(self, -1, "KILL PROCESS", pos=(255, 350),size=(155,56))
        usman6.Bind(wx.EVT_BUTTON,self.my6)
        usman6.SetBitmap(wx.Bitmap('Project Images Os\\kill.png'))
        usman6.SetBackgroundColour('BLUE VIOLET')
        
        usman7 = wx.Button(self, -1, "SEARCH PROCESS", pos=(425, 350),size=(155,56))
        usman7.Bind(wx.EVT_BUTTON,self.my7)
        usman7.SetBitmap(wx.Bitmap('Project Images Os\\vi.png'))
        usman7.SetBackgroundColour('BLUE VIOLET')
        
        self.usmtxt1 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER,pos=(255, 420),size=(155,56))
        self.usmtxt1.SetFocus()
        self.usmtxt1.Bind(wx.EVT_TEXT_ENTER, self.On)
        self.usmtxt1.SetHint("Name To Kill Process")
        
        self.usmtxt2 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER,pos=(425, 420),size=(155,56))
        self.usmtxt2.SetFocus()
        self.usmtxt2.Bind(wx.EVT_TEXT_ENTER, self.On1)
        self.usmtxt2.SetHint("Search Process")
        
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        my_sizer.Add(self.usmtxt1, 23, wx.ALL, 500)
        self.SetSizer(my_sizer)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(usman, 23, wx.ALL, 500)
        self.SetSizer(hSizer)
        self.write("**--Welcome--**")
        
        
        self.SetSizer(hSizer)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        g=time.strftime("%H:%M ")
        
        #print today
        text = wx.StaticText(self, 0, g, (2000, 20))
        text.SetBackgroundColour('AQUAMARINE')
        font = wx.Font(45, wx.MODERN, wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        #text1 = wx.StaticText(self, 0, g,style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, 500))
        #text1.Show()
        
        text.Show()
        '''
        battery = psutil.sensors_battery()
        #print("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft)))
        gauge1 = PG.PyGauge(self, -1, pos=(200, 2000),size=(100, 25),style=wx.GA_HORIZONTAL)
        gauge1.SetValue(battery.percent)
        gauge1.SetDrawValue(draw=True, drawPercent=True, font=None, colour=wx.BLACK, formatString=None)
        gauge1.SetBackgroundColour(wx.WHITE)
        gauge1.SetBorderColor(wx.BLACK)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(gauge1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 1)
        self.SetSizer(sizer)
        sizer.Layout()'''
        
        usman21 = wx.Button(self, -1, "", pos=(95,170),size=(41,40))
        usman21.Bind(wx.EVT_BUTTON,self.mynettest)
        usman21.SetBitmap(wx.Bitmap('Project Images Os\\wifi4.png'))
       
        
        
        usman22 = wx.Button(self, -1, "", pos=(95,230),size=(41,40))
        usman22.Bind(wx.EVT_BUTTON,self.myspeaker)
        usman22.SetBitmap(wx.Bitmap('Project Images Os\\sp.png'))
       
        
        usman23 = wx.Button(self, -1, "", pos=(95,290),size=(41,40))
        usman23.Bind(wx.EVT_BUTTON,self.myexit)
        usman23.SetBitmap(wx.Bitmap('Project Images Os\\pow.png'))
        
        usman24 = wx.Button(self, -1, "", pos=(95,350),size=(41,40))
        usman24.Bind(wx.EVT_BUTTON,self.my14)
        usman24.SetBitmap(wx.Bitmap('Project Images Os\\me.png'))
        
        usman25 = wx.Button(self, -1, "", pos=(95,410),size=(41,40))
        usman25.Bind(wx.EVT_BUTTON,self.myblue)
        usman25.SetBitmap(wx.Bitmap('Project Images Os\\bl1.png'))
        
        usman26 = wx.Button(self, -1, "", pos=(95,470),size=(41,40))
        usman26.Bind(wx.EVT_BUTTON,self.mynet)
        usman26.SetBitmap(wx.Bitmap('Project Images Os\\netcheck.png'))
        
        self.usmtxt3 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER,pos=(595, 420),size=(155,56))
        self.usmtxt3.SetFocus()
        self.usmtxt3.SetHint("Search Extension")
        self.usmtxt3.Bind(wx.EVT_TEXT, self.left1)
        
        usman9 = wx.Button(self, -1, "SEARCH FILES", pos=(595, 350),size=(155,56))
        usman9.Bind(wx.EVT_BUTTON,self.my9)
        usman9.SetBitmap(wx.Bitmap('Project Images Os\\sc.png'))
        usman9.SetBackgroundColour('BLUE VIOLET')
        usman9.SetWindowStyleFlag(wx.SIMPLE_BORDER)
        
        usman10 = wx.Button(self, -1, "TOTAL THREADS", pos=(883, 170),size=(120,50))
        usman10.Bind(wx.EVT_BUTTON,self.my10)
        usman10.SetBackgroundColour('BLUE VIOLET')
        usman10.SetBitmap(wx.Bitmap('Project Images Os\\ln3.png'))
        
        usman11 = wx.Button(self, -1, "RUN THREADS", pos=(883, 230),size=(120,50))
        usman11.Bind(wx.EVT_BUTTON,self.my11)
        usman11.SetBackgroundColour('BLUE VIOLET')
        usman11.SetBitmap(wx.Bitmap('Project Images Os\\ln5.png'))
        
        usman12 = wx.Button(self, -1, "TIME THREADS", pos=(883, 290),size=(120,50))
        usman12.Bind(wx.EVT_BUTTON,self.my12)
        usman12.SetBackgroundColour('BLUE VIOLET')
        usman12.SetBitmap(wx.Bitmap('Project Images Os\\ln4.png'))
        
        self.child = ChildFrame(self)
        self.child.Show()
        self.child.SetFocus()
        
        usman13 = wx.Button(self, -1, "THREADS", pos=(883, 350),size=(120,50))
        usman13.Bind(wx.EVT_BUTTON,self.my13)
        usman13.SetBackgroundColour('BLUE VIOLET')
        usman13.SetBitmap(wx.Bitmap('Project Images Os\\to.png'))
        
        usman14 = wx.Button(self, -1, "", pos=(883, 410),size=(120,110))
        usman14.Bind(wx.EVT_BUTTON,self.my14)
        usman14.SetBackgroundColour('BLUE VIOLET')
        usman14.SetBitmap(wx.Bitmap('Project Images Os\\pro.png'))
        fname = "Project Images Os\\mb.wav"
        winsound.PlaySound(fname, winsound.SND_FILENAME)
    def mynettest(self,event):
        self.main()
    def myspeaker(self,event):
        fname = "Project Images Os\\mb.wav"
        winsound.PlaySound(fname, winsound.SND_FILENAME)
    def myexit(self,event):
        pass
    def myblue(self,event):
        mess="Not Connected"
        fig = plt.figure(figsize=(6,5))
        fig.text(0.5, 1, mess, fontsize=12, style='oblique', ha='center',
         va='top', wrap=True)
        fname = "Project Images Os\\click.wav"
        winsound.PlaySound(fname, winsound.SND_FILENAME)
    def mynet(self,event):
        results = subprocess.check_output(["netsh", "wlan", "show", "network"])
        results = results.decode("ascii") # needed in python 3
        results = results.replace("\r","")
        ls = results.split("\n")
        ls = ls[4:]
        ssids = []
        x = 0
        while x < len(ls):
            if x % 5 == 0:
                ssids.append(ls[x])
            x += 1
        print(ssids)
        fig = plt.figure(figsize=(6,5))
        fig.text(0.5, 1, ssids, fontsize=12, style='oblique', ha='center',
         va='top', wrap=True)
    def my14(self,event):
        p=os.getenv('username')
        l=socket.gethostname()
        l1=platform.system()
        l2=platform.release()
        fig = plt.figure(figsize=(3,2))
        fig.text(0.5, 1, "--User-- "+p+" --DeviceModel-- "+l+" --OperatingSystem-- "+l1+" --Version-- "+l2, fontsize=12, style='oblique', ha='center',
         va='top', wrap=True)
    def my13(self,event):
        pass
    def my12(self,event):
        start = time.time()
        time.sleep(0.11)
        f=open("testing.txt","w+")
        f.write("Woops! I have deleted the content!")
        f.close()
        end = time.time()
        j=end - start
        fig = plt.figure(figsize=(3,2))
        fig.text(0.5, 1, j, fontsize=12, style='oblique', ha='center',
         va='top', wrap=True)
    num_threads = 0
    def heron(self,a):
        new=1
        num_threads=0
        num_threads += 1
    
    # code has been left out, see above
        num_threads -= 1
        return new
    def my11(self,event):
        mik=[]
        #print(start_new_thread(self.heron,(99,)))
        mik.append(start_new_thread(self.heron,(99,)))
        #print(start_new_thread(self.heron,(999,)))
        mik.append(start_new_thread(self.heron,(999,)))
        #print(start_new_thread(self.heron,(1733,)))
        mik.append(start_new_thread(self.heron,(1733,)))
        #print(start_new_thread(self.heron,(17334,)))
        mik.append(start_new_thread(self.heron,(17334,)))
        fig = plt.figure(figsize=(3,2))
        fig.text(0.5, 1, mik, fontsize=12, style='oblique', ha='center',
         va='top', wrap=True)
    def my10(self,event):
        thread1 = SummingThread(0,500000)
        thread2 = SummingThread(500000,1000000)
        thread1.start() # This actually causes the thread to run
        thread2.start()
        thread1.join()  # This waits until the thread has completed
        thread2.join()  
# At this point, both threads have completed
        result = thread1.total + thread2.total
        print(result)
        fig = plt.figure(figsize=(3,2))
        fig.text(0.5, 1, result, fontsize=12, style='oblique', ha='center',
         va='top', wrap=True)
    def my9(self,event):
        com=[]
        i=self.usmtxt3.GetValue()
        print(i)
        os.chdir("C:\\Users\\usman\\Desktop")
        for file in glob.glob(i):
            com.append(file)
        fig = plt.figure(figsize=(19,6))
        fig.text(0.5, 1, com, fontsize=12, style='oblique', ha='center',
         va='top', wrap=True)
        
        
    def left1(self,event):
        pass
           
    def uhm(self, event):
        pass
    def OnSize(self, size):
        
        self.Layout()
        self.Refresh()
    def my(self,event):
         #text = wx.StaticText(self, -1, "Release Tool v11.0", (130, 20))
         pids = psutil.pids()
         print("psutil.pids() = ", pids)
         
         fig = plt.figure(figsize=(19, 0.5))
         text = fig.text(0.5, 0.5, "PROCESS WITH ID'S",
             va='center', size=12)
         text.set_path_effects([path_effects.Normal()])
         text = fig.text(0, 0.1, pids,
             va='center', size=8)
         text.set_path_effects([path_effects.Normal()])
         #*************first graph ends
         df=pd.DataFrame({'x': range(0,len(pids)), 'y1': pids,'y2':4 })
 
#plt.style.use('fivethirtyeight')
         plt.style.use('seaborn-darkgrid')
         my_dpi=96
         plt.figure(figsize=(480/my_dpi, 480/my_dpi), dpi=my_dpi)
 
# multiple line plot
         for column in df.drop('x', axis=1):
                plt.plot(df['x'], df[column], marker='', color='grey', linewidth=1, alpha=0.4)
 
# Now re do the interesting curve, but biger with distinct color
         plt.plot(df['x'], df['y3'], marker='', color='orange', linewidth=4, alpha=0.7)
         plt.text(1000, 5000, pids, ha='left', rotation=15,fontsize=18, wrap=True)
# Change xlim
         plt.xlim(0,1000)
         
    def my1(self,event):
        
        p=platform.processor()
        height = round(psutil.cpu_percent())
        bars = ('%')
        y_pos = np.arange(len(bars))
        plt.barh(y_pos, height)
        plt.title("CPU USAGE")
        #plt.xlabel(height)
        plt.yticks(y_pos, bars)
        plt.xlim(0,100)
        lo=psutil.cpu_percent()
        #pro="The CPU USGAE IS "
        plt.text(50,y_pos,lo, fontsize=14)
        plt.text(50, -0.5,p, fontsize=14, style='oblique', ha='center',
         va='top')
        plt.show()
        
    def my2(self,event):
        print(psutil.virtual_memory())
        height = list(psutil.virtual_memory())
        bars = ('total', 'avaliable', 'percent', 'used', 'free')
        y_pos = np.arange(len(bars))
        plt.figure(figsize=(12, 6))
        plt.barh(y_pos, height)
        plt.yticks(y_pos, bars)
        plt.title("virtual_memory")
        plt.xlabel(psutil.virtual_memory())
        plt.show()

    def my3(self,event):
        pids = psutil.pids()
        print(len(pids))
        height = (len(pids))
        bars = ('-')
        y_pos = np.arange(len(bars))
        plt.barh(y_pos, height)
        plt.title("process runnning")
        plt.xlabel(len(pids))
        plt.xlim(0,220)
        plt.yticks(y_pos, bars)
        plt.show() 
        
    def my4(self,event):
        kif=[]
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['name'])
            except psutil.NoSuchProcess:
                pass
            else:
                print(pinfo)
                kif.append(pinfo)
        fig = plt.figure(figsize=(12, 6))
        plt.axis([0, 10, 0, 10])
        #fig.axis([0, 10, 0, 10])
#plt.text(4, 1, t, ha='left', rotation=15, wrap=True)
#plt.text(6, 5, t, ha='left', rotation=15, wrap=True)
#plt.text(5, 5, t, ha='right', rotation=-15, wrap=True)
        plt.text(-0.2, 11, kif, fontsize=12, style='oblique',
         va='top', wrap=True)
#plt.text(3, 4, t, family='serif', style='italic', ha='right', wrap=True)
#plt.text(-1, 0, t, ha='left', rotation=-15, wrap=True)
        #fig.text(-0.2, 1, kif, fontsize=12, style='oblique',
         #va='top', wrap=True)
        
                
    def my5(self,event):
        mem = virtual_memory()
        p=mem.total/8000000
        print(p)
        memoryUse = psutil.virtual_memory()[2]
        height = memoryUse
        bars = ('%')
        y_pos = np.arange(len(bars))
        plt.figure(figsize=(12, 6))
        plt.barh(y_pos, height)
        plt.title("RAM USAGE")
        #plt.xlabel(height)
        plt.yticks(y_pos+10, bars)
        plt.xlim(0,p)
        plt.text(480, -0.5, mem, fontsize=11, style='oblique', ha='center',
         va='top')
        plt.show()
        
    def my6(self,event):
        input = self.usmtxt1.GetValue()
        print(input)
        #PROCNAME = input
        for proc in psutil.process_iter():
            print(proc.as_dict(attrs=['name'][0]))
            '''if proc.as_dict(attrs=['name']) == PROCNAME:
                    #os.kill(os.getpid(), signal.SIGKILL)
                    print("success")
                else:
                    print("not")'''
    def my7(self,event):
       input11 = self.usmtxt2.GetValue()
       #print(input11)
       p=self.find_procs_by_name(input11)
       #self.usmtx2=p
       print(p)
       fig=plt.figure(figsize=(6,4))
       fig.text(0.5, 1, p, fontsize=12, style='oblique', ha='center',
         va='top', wrap=True)
       #self.usmtx2=''
       #self.usmtx2=p
       
    def find_procs_by_name(self,name):
        ls = []
        for p in psutil.process_iter(attrs=['name']):
            if p.info['name'] == name:
                ls.append(p)
        return ls

    def On(self,event):
        print("i am isma")
    def On1(self,event):
        print("i am isma")
    def write(self, text):
        print(text)
        
    def OnEraseBackground(self, evt):
        pass

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        self.Draw(dc)

    def Draw(self, dc):
        cliWidth, cliHeight = self.GetClientSize()
        if not cliWidth or not cliHeight:
            return
        dc.Clear()
        xPos = (cliWidth - self._width)/2
        yPos = (cliHeight - self._height)/2
        dc.DrawBitmap(self.bg, xPos, yPos)
    def test(self):
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        return res["download"], res["upload"], res["ping"]


    def main(self):
        # write to csv
        with open('file.csv', 'w') as f:
            f.write('download,upload,ping\n')
            for i in range(1):
                print('Making test #{}'.format(i+1))
                d, u, p = self.test()
                f.write('{},{},{}\n'.format(d, u, p))
    # pretty write to txt file
        with open('file.txt', 'w') as f:
            for i in range(1):
                print('Making test #{}'.format(i+1))
                d, u, p = self.test()
                f.write('Test #{}\n'.format(i+1))
                f.write('Download: {:.2f} Kb/s\n'.format(d / 1024))
                f.write('Upload: {:.2f} Kb/s\n'.format(u / 1024))
                f.write('Ping: {}\n'.format(p))
    # simply print in needed format if you want to use pipe-style: python script.py > file
        for i in range(1):
            d, u, p = self.test()
            print('Test #{}\n'.format(i+1))
            print('Download: {:.2f} Kb/s\n'.format(d / 1024))
            print('Upload: {:.2f} Kb/s\n'.format(u / 1024))
            print('Ping: {}\n'.format(p))
        
app = wx.App()

frame = wx.Frame(None, size=(1100,650))
frame.SetIcon(wx.Icon("Project Images Os\\hvt.ico"))
panel = MainPanel(frame)

frame.Show()
app.MainLoop()
del app