import tkinter as tk
import serial.tools.list_ports
import serial

class ArmGui :
    def __init__(self , master):
        self.gripper_angle = 0
        self.top_angle = 0
        self.bottom_angle = 0
        self.base_angle = 0

        self.ser = None
        self.connectionState = tk.StringVar()
        self.connectionState.set("Not Connected")

        self.currentAngles = tk.StringVar()
        self.currentAngles.set("Current angles ")

        self.serialInfo = tk.StringVar()
        self.serialInfo.set("Serial Monitoring")

        self.screen_x = 1920
        self.screen_y = 1080
        self.master = master
        master.title('Arm Control Gui')
        master.geometry(str(self.screen_x)+'x'+str(self.screen_y))

        self.textColor = '#00b3b3'
        self.backgroundColor = '#000000'
        self.currentLabelColor = '#6600cc'
        self.anglesColor = '#99ffff'
        self.btnColor = '#ffe6cc'
        self.btnBgColor ='#404040'
        self.notActivColor = '#ff0000'
        self.activColor = '#00ff00'
        self.exitBtnBgColor = '#660000'
        self.exitTextColor = '#ff6666'
        self.startBtnBgColor = '#009933'
        self.startBtnColor = '#79ff4d'
        self.endBtnBgColor = '#e60000'
        self.endBtnColor = '#ffcccc'
        self.titleColor = '#ffff66'
        self.serialInfoColor = '#ffcc00'
        self.serialMonitorColor = '#404040'
        master.configure(background=self.backgroundColor)

        name = tk.Label(master , text='Control Arm' , bg=self.backgroundColor , fg=self.titleColor , font = "Verdana 40 bold")
        name.place(x = self.screen_x/2-100 , y=10)

        start_connection_btn = tk.Button(master , text="Start Connection"  , width = 30, bg=self.startBtnBgColor , fg=self.startBtnColor , font = "Verdana 20 bold" , command = self.start_connection)
        start_connection_btn.place(x = self.screen_x/2-200 , y=90)

        end_connection_btn = tk.Button(master , text="End Connection " , bg=self.endBtnBgColor , fg=self.endBtnColor , width = 30 , font = "Verdana 20 bold" ,  command = self.end_connection)
        end_connection_btn.place(x = self.screen_x/2-200 , y = 150 )

        self.connection_status = tk.Label(master , textvariable = self.connectionState ,bg=self.backgroundColor , fg=self.notActivColor , font = "Verdana 20 bold" )
        self.connection_status.place(x = self.screen_x/2 , y = 220 )

        self.current_angles = tk.Label(master , textvariable = self.currentAngles , bg=self.backgroundColor , fg=self.currentLabelColor ,  font = "Verdana 20 bold" )
        self.current_angles.place(x = self.screen_x/2 , y = self.screen_y - 400 )

        self.current_gripper_label = tk.Label(master , text = "gripper angle" , bg=self.backgroundColor , fg=self.textColor , font = "Verdana 20 ")
        self.current_gripper_label.place(x = self.screen_x/2-200 , y = self.screen_y -350 )
        self.decrease_gripper_btn = tk.Button(master , text = "-" , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.decreaseGripper)
        self.decrease_gripper_btn.place(x = self.screen_x/2+60 , y = self.screen_y-350 , height = 35 , width = 35 )
        self.current_gripper_angle = tk.Label(master , text = self.gripper_angle  ,bg=self.backgroundColor , fg=self.anglesColor,font ="Verdana 20 bold")
        self.current_gripper_angle.place(x = self.screen_x/2+100 , y = self.screen_y-350 )
        self.increase_gripper_btn = tk.Button(master , text = "+" , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.increaseGripper)
        self.increase_gripper_btn.place(x = self.screen_x/2+165 , y = self.screen_y-350 , height = 35 , width = 35 )

        self.current_top_label = tk.Label(master , text = "top angle" , bg=self.backgroundColor , fg=self.textColor ,  font = "Verdana 20 ")
        self.current_top_label.place(x = self.screen_x/2-200 , y = self.screen_y-310)
        self.decrease_top_btn = tk.Button(master , text = "-" , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.decreaseTop)
        self.decrease_top_btn.place(x = self.screen_x/2+60 , y = self.screen_y-310 , height = 35 , width = 35 )
        self.current_top_angle = tk.Label(master , text = self.top_angle  , bg=self.backgroundColor , fg=self.anglesColor , font ="Verdana 20 bold")
        self.current_top_angle.place(x = self.screen_x/2+100 , y = self.screen_y-310 )
        self.increase_top_btn = tk.Button(master , text = "+" , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.increaseTop)
        self.increase_top_btn.place(x = self.screen_x/2+165 , y = self.screen_y-310 , height = 35 , width = 35 )

        self.current_bottom_label = tk.Label(master , text = "bottom angle" , bg=self.backgroundColor , fg=self.textColor , font = "Verdana 20 ")
        self.current_bottom_label.place(x = self.screen_x/2-200 , y = self.screen_y-270)
        self.decrease_bottom_btn = tk.Button(master , text = "-" , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.decreaseBottom)
        self.decrease_bottom_btn.place(x = self.screen_x/2+60 , y = self.screen_y-270 , height = 35 , width = 35 )
        self.current_bottom_angle = tk.Label(master , text = self.bottom_angle  , bg=self.backgroundColor , fg=self.anglesColor , font ="Verdana 20 bold")
        self.current_bottom_angle.place(x = self.screen_x/2+100 , y = self.screen_y-270 )
        self.increase_bottom_btn = tk.Button(master , text = "+" , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.increaseBottom)
        self.increase_bottom_btn.place(x = self.screen_x/2+165 , y = self.screen_y-270 , height = 35 , width = 35 )

        self.current_base_label = tk.Label(master , text = "base angle" , bg=self.backgroundColor , fg=self.textColor ,  font = "Verdana 20 ")
        self.current_base_label.place(x = self.screen_x/2-200 , y = self.screen_y-230)
        self.decrease_base_btn = tk.Button(master , text = "-" , bg=self.btnBgColor , fg= self.btnColor ,font = "Verdana 20 bold" , command = self.decreaseBase)
        self.decrease_base_btn.place(x = self.screen_x/2+60 , y = self.screen_y-230 , height = 35 , width = 35 )
        self.current_base_angle = tk.Label(master , text = self.base_angle  , bg=self.backgroundColor , fg=self.anglesColor , font ="Verdana 20 bold")
        self.current_base_angle.place(x = self.screen_x/2+100 , y = self.screen_y-230 )
        self.increase_base_btn = tk.Button(master , text="+"  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold"  , command = self.increaseBase)
        self.increase_base_btn.place(x = self.screen_x/2+165 , y = self.screen_y-230 , height = 35 , width = 35)


        gripper_label = tk.Label(master , text='Gripper' , bg=self.backgroundColor , fg=self.textColor , font = "Verdana 30 bold")
        gripper_label.place(x = 10 , y=300)

        g_0 = tk.Button(master , text="0" , width = 5  , bg=self.btnBgColor , fg= self.btnColor, font = "Verdana 20 bold" ,  command = self.g_0 )
        g_0.place(x = 200 , y = 300 )

        g_30 = tk.Button(master , text="30", width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.g_30 )
        g_30.place(x = 350 , y = 300 )

        g_45 = tk.Button(master , text="45", width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.g_45 )
        g_45.place(x = 500 , y = 300 )

        g_60 = tk.Button(master , text="60", width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.g_60 )
        g_60.place(x = 650 , y = 300 )

        g_90 = tk.Button(master , text="90", width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.g_90)
        g_90.place(x = 800 , y = 300 )

        g_120 = tk.Button(master , text="120", width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.g_120)
        g_120.place(x = 950 , y = 300 )

        g_135 = tk.Button(master , text="135", width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.g_135)
        g_135.place(x = 1100 , y = 300 )

        g_150 = tk.Button(master , text="150", width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.g_150)
        g_150.place(x = 1250 , y = 300 )

        g_180 = tk.Button(master , text="180", width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.g_180)
        g_180.place(x = 1400 , y = 300 )

        self.g_text = tk.Entry(master , font = "Verdana 20 bold" )
        self.g_text.place( x = 1550 , y = 300  , height = 50 , width = 70 )

        send_gripper_btn = tk.Button(master , text="send" , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.send_gripper_angle)
        send_gripper_btn.place(x = 1650 , y = 300 , height = 50 , width = 90)

        top_label = tk.Label(master , text='Top' , bg=self.backgroundColor , fg=self.textColor , font = "Verdana 30 bold")
        top_label.place(x = 10 , y = 400 )

        t_0 = tk.Button(master , text="0", width = 5  ,bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.t_0 )
        t_0.place(x = 200 , y = 400 )

        t_30 = tk.Button(master , text="30", width = 5  ,bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.t_30 )
        t_30.place(x = 350 , y = 400 )

        t_45 = tk.Button(master , text="45", width = 5  ,bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.t_45)
        t_45.place(x = 500 , y = 400 )

        t_60 = tk.Button(master , text="60", width = 5  ,bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.t_60 )
        t_60.place(x = 650 , y = 400 )

        t_90 = tk.Button(master , text="90", width = 5  ,bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.t_90)
        t_90.place(x = 800 , y = 400 )

        t_120 = tk.Button(master , text="120", width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.t_120 )
        t_120.place(x = 950 , y = 400 )

        t_135 = tk.Button(master , text="135", width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.t_135 )
        t_135.place(x = 1100 , y = 400 )

        t_150 = tk.Button(master , text="150", width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold"  , command = self.t_150)
        t_150.place(x = 1250 , y = 400 )

        t_180 = tk.Button(master , text="180", width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.t_180 )
        t_180.place(x = 1400 , y = 400 )

        self.t_text = tk.Entry(master , font = "Verdana 20 bold" )
        self.t_text.place( x = 1550 , y = 400  , height = 50 , width = 70 )

        send_t_btn = tk.Button(master , text="send" , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.send_top_angle)
        send_t_btn.place(x = 1650 , y = 400 , height = 50 , width = 90)

        bottom_label = tk.Label(master , text='Bottom' , bg=self.backgroundColor , fg=self.textColor , font = "Verdana 30 bold")
        bottom_label.place(x = 10 , y = 500 )

        buttom_0 = tk.Button(master , text="0" , width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.bottom_0)
        buttom_0.place(x = 200 , y = 500 )

        buttom_30 = tk.Button(master , text="30" , width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.bottom_30)
        buttom_30.place(x = 350 , y = 500 )

        buttom_45 = tk.Button(master , text="45" , width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.bottom_45)
        buttom_45.place(x = 500 , y = 500 )

        buttom_60 = tk.Button(master , text="60" , width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.bottom_60)
        buttom_60.place(x = 650 , y = 500 )

        buttom_90 = tk.Button(master , text="90" , width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.bottom_90)
        buttom_90.place(x = 800 , y = 500 )

        buttom_120 = tk.Button(master , text="120" , width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.bottom_120)
        buttom_120.place(x = 950 , y = 500 )

        buttom_135 = tk.Button(master , text="135" , width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.bottom_135)
        buttom_135.place(x = 1100 , y = 500 )

        buttom_150 = tk.Button(master , text="150" , width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.bottom_150 )
        buttom_150.place(x = 1250 , y = 500 )

        buttom_180 = tk.Button(master , text="180" , width = 5  , bg=self.btnBgColor , fg= self.btnColor ,  font = "Verdana 20 bold" , command = self.bottom_180 )
        buttom_180.place(x = 1400 , y = 500 )

        self.buttom_text = tk.Entry(master , font = "Verdana 20 bold" )
        self.buttom_text.place( x = 1550 , y = 500  , height = 50 , width = 70 )

        send_buttom_btn = tk.Button(master , text="send" , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.send_buttom_angle)
        send_buttom_btn.place(x = 1650 , y = 500 , height = 50 , width = 90)

        base_label = tk.Label(master , text='Base' , bg=self.backgroundColor , fg=self.textColor , font = "Verdana 30 bold")
        base_label.place(x = 10 , y = 600 )

        base_0 = tk.Button(master , text="0" , width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.base_0)
        base_0.place(x = 200 , y = 600 )

        base_30 = tk.Button(master , text="30" , width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.base_30)
        base_30.place(x = 350 , y = 600 )

        base_45 = tk.Button(master , text="45" , width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold"  , command = self.base_45)
        base_45.place(x = 500 , y = 600 )

        base_60 = tk.Button(master , text="60" , width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.base_60)
        base_60.place(x = 650 , y = 600 )

        base_90 = tk.Button(master , text="90" , width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.base_90)
        base_90.place(x = 800 , y = 600 )

        base_120 = tk.Button(master , text="120" , width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.base_120)
        base_120.place(x = 950 , y = 600 )

        base_135 = tk.Button(master , text="135" , width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.base_135)
        base_135.place(x = 1100 , y = 600 )

        base_150 = tk.Button(master , text="150" , width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.base_150)
        base_150.place(x = 1250 , y = 600 )

        base_180 = tk.Button(master , text="180" , width = 5  , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.base_180)
        base_180.place(x = 1400 , y = 600 )

        self.base_text = tk.Entry(master , font = "Verdana 20 bold" )
        self.base_text.place( x = 1550 , y = 600  , height = 50 , width = 70 )

        send_base_btn = tk.Button(master , text="send" , bg=self.btnBgColor , fg= self.btnColor , font = "Verdana 20 bold" , command = self.send_base_angle)
        send_base_btn.place(x = 1650 , y = 600 , height = 50 , width = 90)

        exit_btn = tk.Button(master ,text="Exit", width = 30, bg=self.exitBtnBgColor  , fg=self.exitTextColor,  font = "Verdana 20 bold" ,  command=self.quit)
        exit_btn.place(x = self.screen_x/2-200 , y=self.screen_y-150)

        self.serialMonitor = tk.Label(master , text = "serial mointor" , bg=self.backgroundColor , fg=self.serialMonitorColor , font="Verdana 15 bold")
        self.serialMonitor.place(x = self.screen_x - 550 , y = self.screen_y - 360 )

        self.serial_info = tk.Label(master , textvariable = self.serialInfo , bg=self.backgroundColor , fg=self.serialInfoColor ,  font = "Verdana 15 " )
        self.serial_info.place(x = self.screen_x - 550 , y = self.screen_y - 300 )

    def increaseGripper(self):
        try :
            if self.gripper_angle < 180 :
                self.gripper_angle = self.gripper_angle + 1
                self.ser.write( ('4/'+str(self.gripper_angle)).encode())
                self.serialInfo.set( "angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)) )
                print("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
                self.current_gripper_angle.configure(text = str(self.gripper_angle))
            else :
                self.gripper_angle = 0
                self.ser.write( ('4/'+str(self.gripper_angle)).encode())
                self.serialInfo.set( "angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)) )
                print("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
                self.current_gripper_angle.configure(text = str(self.gripper_angle))
        except :
            print("connection dosen't established yet ")

    def decreaseGripper(self):
        try :
            if self.gripper_angle > 0 :
                self.gripper_angle = self.gripper_angle - 1
                self.ser.write( ('4/'+str(self.gripper_angle)).encode())
                self.serialInfo.set( "angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)) )
                print("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
                self.current_gripper_angle.configure(text = str(self.gripper_angle))
            else :
                self.gripper_angle = 0
                self.ser.write( ('4/'+str(self.gripper_angle)).encode())
                self.serialInfo.set( "angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)) )
                print("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
                self.current_gripper_angle.configure(text = str(self.gripper_angle))
        except :
            print("connection dosen't established yet ")

    def increaseTop(self):
        try :
            if self.top_angle < 180 :
                self.top_angle = self.top_angle + 1
                self.ser.write( ('3/'+str(self.top_angle)).encode())
                self.serialInfo.set("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
                print("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
                self.current_top_angle.configure(text = str(self.top_angle))
            else :
                self.top_angle = 0
                self.ser.write( ('3/'+str(self.top_angle)).encode())
                self.serialInfo.set("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
                print("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
                self.current_top_angle.configure(text = str(self.top_angle))
        except :
            print("connection dosen't established yet ")

    def decreaseTop(self):
        try :
            if self.top_angle > 0 :
                self.top_angle = self.top_angle - 1
                self.ser.write( ('3/'+str(self.top_angle)).encode())
                self.serialInfo.set("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
                print("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
                self.current_top_angle.configure(text = str(self.top_angle))
            else :
                self.top_angle = 0
                self.ser.write( ('3/'+str(self.top_angle)).encode())
                self.serialInfo.set("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
                print("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
                self.current_top_angle.configure(text = str(self.top_angle))
        except :
            print("connection dosen't established yet ")

    def increaseBottom(self):
        try :
            if self.bottom_angle < 180 :
                self.bottom_angle = self.bottom_angle + 1
                self.ser.write(('2/'+str(self.bottom_angle)).encode())
                self.serialInfo.set("angle [ {} ] sent to bottom successfully  ".format(str(self.bottom_angle)))
                print("angle [ {} ] sent to bottom successfully  ".format(str(self.bottom_angle)))
                self.current_bottom_angle.configure(text = str(self.bottom_angle))
            else :
                self.bottom_angle = 0
                self.ser.write(('2/'+str(self.bottom_angle)).encode())
                self.serialInfo.set("angle [ {} ] sent to bottom successfully  ".format(str(self.bottom_angle)))
                print("angle [ 0 ] sent to bottom successfully  ")
                self.current_bottom_angle.configure(text = str(self.bottom_angle))
        except :
            print("connection dosen't established yet ")

    def decreaseBottom(self):
        try :
            if self.bottom_angle > 0 :
                self.bottom_angle = self.bottom_angle - 1
                self.ser.write(('2/'+str(self.bottom_angle)).encode())
                self.serialInfo.set("angle [ {} ] sent to bottom successfully  ".format(str(self.bottom_angle)))
                print("angle [ 0 ] sent to bottom successfully  ")
                self.current_bottom_angle.configure(text = str(self.bottom_angle))
            else :
                self.bottom_angle = 0
                self.ser.write(('2/'+str(self.bottom_angle)).encode())
                self.serialInfo.set("angle [ {} ] sent to bottom successfully  ".format(str(self.bottom_angle)))
                print("angle [ 0 ] sent to bottom successfully  ")
                self.current_bottom_angle.configure(text = str(self.bottom_angle))
        except :
            print("connection dosen't established yet ")

    def increaseBase(self):
        try :
            if self.base_angle < 180 :
                self.base_angle = self.base_angle + 1
                self.ser.write(('1/'+str(self.base_angle)).encode())
                self.serialInfo.set("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
                print("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
                self.current_base_angle.configure(text=str(self.base_angle))
            else :
                self.base_angle = 0
                self.ser.write(('1/'+str(self.base_angle)).encode())
                self.serialInfo.set("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
                print("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
                self.current_base_angle.configure(text=str(self.base_angle))
        except :
            print("connection dosen't established yet ")

    def decreaseBase(self):
        try :
            if self.base_angle > 0 :
                self.base_angle = self.base_angle - 1
                self.ser.write(('1/'+str(self.base_angle)).encode())
                self.serialInfo.set("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
                print("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
                self.current_base_angle.configure(text=str(self.base_angle))
            else :
                self.base_angle = 0
                self.ser.write(('1/'+str(self.base_angle)).encode())
                self.serialInfo.set("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
                print("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
                self.current_base_angle.configure(text=str(self.base_angle))
        except :
            print("connection dosen't established yet ")

    def send_gripper_angle(self):
        try :
            angle = int(self.g_text.get())
            self.gripper_angle = angle
            self.ser.write( ('4/'+str(self.gripper_angle)).encode())
            self.current_gripper_angle.configure(text=str(self.gripper_angle))
            self.serialInfo.set("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
            print("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
        except :
            if ( self.ser == None ) :
                print("Connection isn't established yet !")
            elif ( self.ser.isOpen() and self.g_text.get() =='') :
                print("Enter Angle Please !")
            else :
                print("Numeric Values Only Accepted ! ")

    def send_top_angle(self):
        try :
            angle = int(self.t_text.get())
            self.top_angle = angle
            self.ser.write( ('3/'+str(self.top_angle)).encode())
            self.current_top_angle.configure(text=str(self.top_angle))
            self.serialInfo.set("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
            print("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
        except :
            if( self.ser == None ) :
                print("Connection isn't established yet !")
            elif ( self.ser.isOpen() and self.t_text.get()==''):
                print("Enter angle Please !")
            else :
                print("Numeric Values Only Accepted ! ")
    def send_buttom_angle(self) :
        try :
            angle = int(self.buttom_text.get())
            self.bottom_angle = angle
            self.ser.write( ('2/'+str(self.bottom_angle)).encode())
            self.current_bottom_angle.configure(text=str(self.bottom_angle))
            self.serialInfo.set("angle [ {} ] sent to bottom successfully ".format(str(self.bottom_angle)))
            print("angle [ {} ] sent to bottom successfully ".format(str(self.bottom_angle)))
        except :
            if( self.ser == None ) :
                print("Connection isn't established yet !")
            elif ( self.ser.isOpen() and self.buttom_text.get()==''):
                print("Enter angle Please !")
            else :
                print("Numeric Values Only Accepted ! ")
    def send_base_angle(self) :
        try :
            angle = int(self.base_text.get())
            self.base_angle = angle
            self.ser.write(('1/'+str(self.base_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
            self.current_base_angle.configure(text=str(self.base_angle))
            print("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
        except :
            if( self.ser == None ) :
                print("Connection isn't established yet !")
            elif ( self.ser.isOpen() and self.base_text.get()==''):
                print("Enter angle Please !")
            else :
                print("Numeric Values Only Accepted ! ")

    def g_0(self):
        try :
            self.gripper_angle = 0
            self.ser.write(('4/'+ str(self.gripper_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
            print("angle [ 0 ] sent to gripper successfully  ")
            self.current_gripper_angle.configure(text = str(self.gripper_angle))
        except :
            print("Connection isn't established yet !")

    def g_30(self):
        try :
            self.gripper_angle = 30
            self.ser.write(('4/'+str(self.gripper_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
            print("angle [ 30 ] sent to gripper successfully  ")
            # self.current_gripper_angle = self.gripper_angle
            self.current_gripper_angle.configure(text = str(self.gripper_angle))
        except :
            print("Connection Dosen't established yet ! ")
    def g_45(self):
        try :
            self.gripper_angle = 45
            self.ser.write(('4/'+str(self.gripper_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
            print("angle [ 45 ] sent to gripper successfully  ")
            self.current_gripper_angle.configure(text = str(self.gripper_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def g_60(self):
        try :
            self.gripper_angle = 60
            self.ser.write(('4/'+str(self.gripper_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
            print("angle [ 60 ] sent to gripper successfully  ")
            self.current_gripper_angle.configure(text = str(self.gripper_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def g_90(self):
        try :
            self.gripper_angle = 90
            self.ser.write(('4/'+str(self.gripper_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
            print("angle [ 90 ] sent to gripper successfully  ")
            self.current_gripper_angle.configure(text = str(self.gripper_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def g_120(self):
        try :
            self.gripper_angle = 120
            self.ser.write(('4/'+str(self.gripper_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
            print("angle [ 120 ] sent to gripper successfully  ")
            self.current_gripper_angle.configure(text = str(self.gripper_angle))
        except :
            print("Connection Dosen't established yet ! ")
    def g_135(self):
        try :
            self.gripper_angle = 135
            self.ser.write(('4/'+str(self.gripper_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
            print("angle [ 135 ] sent to gripper successfully  ")
            self.current_gripper_angle.configure(text = str(self.gripper_angle))
        except :
            print("Connection Dosen't established yet ! ")
    def g_150(self):
        try :
            self.gripper_angle = 150
            self.ser.write(('4/'+str(self.gripper_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
            print("angle [ 150 ] sent to gripper successfully  ")
            self.current_gripper_angle.configure(text = str(self.gripper_angle))
        except :
            print("Connection Dosen't established yet ! ")
    def g_180(self):
        try :
            self.gripper_angle = 180
            self.ser.write(('4/'+str(self.gripper_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to gripper successfully ".format(str(self.gripper_angle)))
            print("angle [ 180 ] sent to gripper successfully  ")
            self.current_gripper_angle.configure(text = str(self.gripper_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def t_0(self):
        try :
            self.top_angle = 0
            self.ser.write(('3/'+str(self.top_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
            print("angle [ 0 ] sent to top successfully  ")
            self.current_top_angle.configure(text = str(self.top_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def t_30(self):
        try :
            self.top_angle = 30
            self.ser.write(('3/'+str(self.top_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
            print("angle [ 30 ] sent to top successfully  ")
            self.current_top_angle.configure(text = str(self.top_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def t_45(self):
        try :
            self.top_angle = 45
            self.ser.write(('3/'+str(self.top_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
            print("angle [ 45 ] sent to top successfully  ")
            self.current_top_angle.configure(text = str(self.top_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def t_60(self):
        try :
            self.top_angle = 60
            self.ser.write(('3/'+str(self.top_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
            print("angle [ 60 ] sent to top successfully  ")
            self.current_top_angle.configure(text = str(self.top_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def t_90(self):
        try :
            self.top_angle = 90
            self.ser.write(('3/'+str(self.top_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
            print("angle [ 90 ] sent to top successfully  ")
            self.current_top_angle.configure(text = str(self.top_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def t_120(self):
        try :
            self.top_angle = 120
            self.ser.write(('3/'+str(self.top_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
            print("angle [ 120 ] sent to top successfully  ")
            self.current_top_angle.configure(text = str(self.top_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def t_135(self):
        try :
            self.top_angle = 135
            self.ser.write(('3/'+str(self.top_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
            print("angle [ 135 ] sent to top successfully  ")
            self.current_top_angle.configure(text = str(self.top_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def t_150(self):
        try :
            self.top_angle = 150
            self.ser.write(('3/'+str(self.top_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
            print("angle [ 150 ] sent to top successfully  ")
            self.current_top_angle.configure(text = str(self.top_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def t_180(self):
        try :
            self.top_angle = 180
            self.ser.write(('3/'+str(self.top_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to top successfully ".format(str(self.top_angle)))
            print("angle [ 180 ] sent to top successfully  ")
            self.current_top_angle.configure(text = str(self.top_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def bottom_0(self):
        try :
            self.bottom_angle = 0
            self.ser.write(('2/'+str(self.bottom_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to bottom successfully ".format(str(self.bottom_angle)))
            print("angle [ 0 ] sent to bottom successfully  ")
            self.current_bottom_angle.configure(text = str(self.bottom_angle))
        except :
            print("Connection Dosen't established yet ! ")
    def bottom_30(self):
        try :
            self.bottom_angle = 30
            self.ser.write(('2/'+str(self.bottom_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to bottom successfully ".format(str(self.bottom_angle)))
            print("angle [ 30 ] sent to bottom successfully  ")
            self.current_bottom_angle.configure(text = str(self.bottom_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def bottom_45(self):
        try :
            self.bottom_angle = 45
            self.ser.write(('2/'+str(self.bottom_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to bottom successfully ".format(str(self.bottom_angle)))
            print("angle [ 45 ] sent to bottom successfully  ")
            self.current_bottom_angle.configure(text = str(self.bottom_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def bottom_60(self):
        try :
            self.bottom_angle = 60
            self.ser.write(('2/'+str(self.bottom_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to bottom successfully ".format(str(self.bottom_angle)))
            print("angle [ 60 ] sent to bottom successfully  ")
            self.current_bottom_angle.configure(text = str(self.bottom_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def bottom_90(self):
        try :
            self.bottom_angle = 90
            self.ser.write(('2/'+str(self.bottom_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to bottom successfully ".format(str(self.bottom_angle)))
            print("angle [ 90 ] sent to bottom successfully  ")
            self.current_bottom_angle.configure(text = str(self.bottom_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def bottom_120(self):
        try :
            self.bottom_angle = 120
            self.ser.write(('2/'+str(self.bottom_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to bottom successfully ".format(str(self.bottom_angle)))
            print("angle [ 120 ] sent to bottom successfully  ")
            self.current_bottom_angle.configure(text = str(self.bottom_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def bottom_135(self):
        try :
            self.bottom_angle = 135
            self.ser.write(('2/'+str(self.bottom_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to bottom successfully ".format(str(self.bottom_angle)))
            print("angle [ 135 ] sent to bottom successfully  ")
            self.current_bottom_angle.configure(text = str(self.bottom_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def bottom_150(self):
        try :
            self.bottom_angle = 150
            self.ser.write(('2/'+str(self.bottom_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to bottom successfully ".format(str(self.bottom_angle)))
            print("angle [ 150 ] sent to bottom successfully  ")
            self.current_bottom_angle.configure(text = str(self.bottom_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def bottom_180(self):
        try :
            self.bottom_angle = 180
            self.ser.write(('2/'+str(self.bottom_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to bottom successfully ".format(str(self.bottom_angle)))
            print("angle [ 180 ] sent to bottom successfully  ")
            self.current_bottom_angle.configure(text = str(self.bottom_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def base_0(self):
        try :
            self.base_angle = 0
            self.ser.write(('1/'+str(self.base_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
            print("angle [ 0 ] sent to base successfully  ")
            self.current_base_angle.configure(text = str(self.base_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def base_30(self):
        try :
            self.base_angle = 30
            self.ser.write(('1/'+str(self.base_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
            print("angle [ 30 ] sent to base successfully  ")
            self.current_base_angle.configure(text = str(self.base_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def base_45(self):
        try :
            self.base_angle = 45
            self.ser.write(('1/'+str(self.base_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
            print("angle [ 45 ] sent to base successfully  ")
            self.current_base_angle.configure(text = str(self.base_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def base_60(self):
        try :
            self.base_angle = 60
            self.ser.write(('1/'+str(self.base_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
            print("angle [ 60 ] sent to base successfully  ")
            self.current_base_angle.configure(text = str(self.base_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def base_90(self):
        try :
            self.base_angle = 90
            self.ser.write(('1/'+str(self.base_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
            print("angle [ 90 ] sent to base successfully  ")
            self.current_base_angle.configure(text = str(self.base_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def base_120(self):
        try :
            self.base_angle = 120
            self.ser.write(('1/'+str(self.base_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
            print("angle [ 120 ] sent to base successfully  ")
            self.current_base_angle.configure(text = str(self.base_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def base_135(self):
        try :
            self.base_angle = 135
            self.ser.write(('1/'+str(self.base_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
            print("angle [ 135 ] sent to base successfully  ")
            self.current_base_angle.configure(text = str(self.base_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def base_150(self):
        try :
            self.base_angle = 150
            self.ser.write(('1/'+str(self.base_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
            print("angle [ 150 ] sent to base successfully  ")
            self.current_base_angle.configure(text = str(self.base_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def base_180(self):
        try :
            self.base_angle=180
            self.ser.write(('1/'+str(self.base_angle)).encode())
            self.serialInfo.set("angle [ {} ] sent to base successfully ".format(str(self.base_angle)))
            print("angle [ 180 ] sent to base successfully  ")
            self.current_base_angle.configure(text = str(self.base_angle))
        except :
            print("Connection Dosen't established yet ! ")

    def start_connection(self):
        ports = list(serial.tools.list_ports.comports())
        flag = 0
        port =''
        for p in ports :
            if 'Arduino' in str(p) :
                flag = 1
                port = str(p).split('-')[0]
                self.ser = serial.Serial( port , 9600)
                print(" connected at : " + str(p).split('-')[0] )
                self.connectionState.set(" Connected at : " + str(p).split('-')[0] )
                self.connection_status['fg'] = self.activColor

        if flag == 0 :
            self.connectionState.set("Arduino Not Found" )
            print("Not Found !")

    def end_connection(self):
        try :
            if self.ser.isOpen():
                self.ser.close()
                self.connectionState.set("Disconnected")
                self.connection_status['fg'] = self.notActivColor
                print("connection closed successfully ")
            else :
                self.connection_status['fg'] = self.notActivColor
                self.connectionState.set("Already Disconnected !")
                print("Already Closed .....")
        except :
            self.connectionState.set("connection isn't created yet !")
            self.connection_status['fg'] = 'red'
            print("Serial Object is not created yet !")

    def display_current_angles(self):
            self.connection_status = tk.Label(master , textvariable = self.connectionState ,  font = "Verdana 20 bold" )
            self.connection_status.place(x = self.screen_x/2 , y = 220 )

    def quit(self):
        exit()

if __name__=='__main__':
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    ArmGui(root)
    root.mainloop()
