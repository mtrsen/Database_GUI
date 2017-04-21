from tkinter import *
import tkinter.messagebox as messagebox
import datetime as datetime
from datetime import date
from tkinter import ttk as ttk


class Project:
    
    def __init__(self, root):
        self.root = root
        self.currDate = date.today()
        self.today = self.currDate.strftime("%Y-%m-%d")
        self.LoginPage()

    def LoginPage(self):
        # Log-in page. It starts the application by asking the user
        # its username or password or a new user registration.
        aWin = Toplevel()
        aWin.title("Login")
        aWin.geometry("500x350+0+0")
        self.aWin = aWin
        header = Canvas(aWin, width=700, height=100)
        header.pack()
        header.create_rectangle(10,5,490,50)
        title = header.create_text(250,27.5)
        header.itemconfig(title, text="Login", font=('normal', 14), fill =  "goldenrod") #changed
        frame1 = Frame(aWin)
        frame1.pack()
        frame1.config(pady=15)
        L1 = Label(frame1, anchor="e", text="Username:", width=15)
        L1.grid(row=0, column=0)

        L2 = Label(frame1, anchor="e", text="Password:", width=15)
        L2.grid(row=1, column=0)
    
        self.E1_aWin = Entry(frame1, state="normal", bd=1, width=20)
        self.E1_aWin.grid(row=0, column=3, padx = 50, pady = 10)

        self.E2_aWin = Entry(frame1, state="normal", bd=1, width=20, show="*")
        self.E2_aWin.grid(row=1, column=3, padx=50, pady = 10)
       
        B1 = Button(frame1, text="Login", command=self.LoginCheck, width=5)
        B1.grid(row=2, column=0, pady=20, ipadx=5, sticky=NE)
        
        B2 = Button(frame1, text="Register", command=self.CreateAccount, width=10)
        B2.grid(row=2, column=3, pady=20, padx= 10, ipadx=10, sticky=S)

    def CreateAccount(self):
        # Creates the window for the new user registration.
        # Gets all the values from the user type from the database, as well as the combinations of city and state
        self.aWin.withdraw()
        bWin = Toplevel()
        bWin.title("New User Registration")
        bWin.geometry("600x600+0+0")
        self.bWin=bWin

        header = Canvas(bWin, width=500, height=80)
        header.pack()
        header.create_line(10,10,490,10)
        header.create_line(10,10,10,70)
        header.create_line(10,70,490,70)
        header.create_line(490,10,490,70)
        title = header.create_text(250, 40)

        header.itemconfig(title, text="New User Registration", font=('normal', 14), fill = "goldenrod") #changed
        Frame1 = Frame(bWin)
        Frame1.pack(pady=10)

        L1 = Label(Frame1, anchor="e", text="Username:", width=15)
        L1.grid(row=0, column=0, sticky = W)
        self.E1_bWin = Entry(Frame1, state="normal", bd=1, width=20)
        self.E1_bWin.grid(row=0, column=1,padx = 20, pady = 10)

        L2 = Label(Frame1, anchor="e", text="Email Address:", width=15)
        L2.grid(row=1, column=0, sticky = W)
        self.E2_bWin = Entry(Frame1, state="normal", bd=1, width=20)
        self.E2_bWin.grid(row=1, column=1, padx = 20, pady = 10)
        L3 = Label(Frame1, anchor="e", text="Password:", width=15)
        L3.grid(row=2, column=0)
        self.E3_bWin = Entry(Frame1, state="normal", bd=1, width=20, show="*")
        self.E3_bWin.grid(row=2, column=1, padx = 20, pady = 10)
        L4 = Label(Frame1, anchor="e", text="Confirm Password:", width=15)
        L4.grid(row=3, column=0)
        self.E4_bWin = Entry(Frame1, state="normal", bd=1, width=20)
        self.E4_bWin.grid(row=3, column=1, padx = 20, pady = 10)
        L5 = Label(Frame1, text="User Type", width=20)
        L5.grid(row=4, column=0, columnspan=2, pady=10, padx=15, sticky=W)

        db = self.Connect()
        c = db.cursor()
        c.execute("SELECT UserType FROM USER")
        newtup = c.fetchall()
        newlist= list(newtup)
        options = []
        for element in newlist:
            if element[0] not in options and element[0] != "Admin":
                options.append(element[0])
        var = StringVar()
        var.set("User Type")
        drop = OptionMenu(Frame1, var, *options)
        drop.grid(row=4, column=1, padx=10)
        self.drop = drop

        canv2=Canvas(bWin, width=500, height=20)
        canv2.pack()
        canv2.create_text(150,8,  fill="black",font=("Purisa", 10),text="Fill out the following "
                                                                        "if you chose City Officials")
        canv2.create_line(70,20,430,20)

        Frame2=Frame(bWin)
        Frame2.pack(pady=10)

        L1_1 = Label(Frame2, anchor="e", text="City:", width=15)
        L1_1.grid(row=0, column=0, sticky = W)
        
        db = self.Connect()
        c = db.cursor()
        c.execute("SELECT City, State FROM CITYSTATE")
        newtup = c.fetchall()
        L1_2 = Label(Frame2, anchor="e", text="State:", width=15)
        L1_2.grid(row=1, column=0, sticky = W)

        newlist= list(newtup)
        citylist = []
        statelist = []
        for element in newlist:
            if element[0] not in citylist:
                citylist.append(element[0])
            if element[1] not in statelist:
                statelist.append(element[1])
        options2 = citylist
        var2 = StringVar()
        var2.set("City")
        drop2 = OptionMenu(Frame2, var2, *options2)
        drop2.grid(row=0, column=1, padx=10)
        self.drop2 = drop2
        var3 = StringVar()
        options3 = statelist
        var3.set("State")
        drop3 = OptionMenu(Frame2, var3, *options3)
        drop3.grid(row=1, column=1, padx=10)
        self.drop3 = drop3
        L1_3 = Label(Frame2, anchor="e", text="Title:", width=15)
        L1_3.grid(row=2, column=0, sticky = W)
        self.E1_1_bWin = Entry(Frame2, state="normal", bd=1, width=20)
        self.E1_1_bWin.grid(row=2, column=1,padx=10)
        B1 = Button(Frame2, text="Create", command=self.RegisterNew, width=10)
        B1.grid(row=3, column=1, pady=10)
       
        B2 = Button(Frame2, text="Back", command=self.backtoLogin0, width=10)
        B2.grid(row=4, column=1, pady=10)

    def backtoLogin0(self):
        # function used to close and open a new window
        self.LoginPage()
        self.bWin.withdraw()

    def LoginCheck(self):
        # checks if the values that the user inputs are valid.
        # If the selected statements bring no results, then an error occurs.
        # the sql statement gives our the values for the usertype.
        # We create new variables and we do error checking from those variables
        username = self.E1_aWin.get()
        username = username.lower()
        self.username = username
        password = self.E2_aWin.get()
        db = self.Connect()
        c = db.cursor()
        c.execute("SELECT UserType FROM USER WHERE Username = %s AND Password = %s", (username, password))
        try:
            userType = c.fetchone()[0]
            if userType.lower() == "city scientist":
                self.addNewDataPoint()
                self.aWin.withdraw()
            elif userType.lower() == "admin" or userType.lower() == "administrator":
                self.AdminFunct()
                self.aWin.withdraw()
            elif userType.lower() == "city official":
                c = db.cursor()
                print("Hola")
                c.execute("SELECT Approved FROM CITYOFFICIAL NATURAL JOIN USER WHERE USERNAME = %s",(username))
                validation = c.fetchone()[0]
                if validation == "None":
                    messagebox.showwarning("Account not yet accepted", "Your account has not been accepted. Please allow more time until the account accepted.")
                    return
                if validation == "No":
                    messagebox.showwarning("Your account has been rejected", "You do not have access to the application")
                    return
                self.CityOffFunct()
                self.aWin.withdraw()
        except:
            messagebox.showerror("Invalid Username/Password", "You have entered an unrecognizable username/password "
                                                              "combination. Please try again.")
            return

    def RegisterNew(self):
        # based on the data that the user input in the database,
        # we make sure everything is input correctly and we excecute statements based on the values inserted.
        response = self.drop.cget("text")
        title = self.E1_1_bWin.get()
        response1 = self.drop2.cget("text")
        response2 = self.drop3.cget("text")
        if response == "User Type":
            messagebox.showwarning("Invalid Selection.","""Invalid Selection. \n\n Please make a valid selection.""")
            return
        if response.lower == "city official":
            if response1 == "City":
                messagebox.showwarning("Invalid Selection.","""Invalid Selection. \n\n Please select a city.""")
                return
            if response2 == "State":
                messagebox.showwarning("Invalid Selection.","""Invalid Selection. \n\n Please select a state.""")
                return
            db = self.Connect()
            c = db.cursor()
            c.execute("SELECT City, State FROM CITYSTATE WHERE City= %s AND State = %s", (response1, response2))
            ans = c.fetchone()
            if not ans:
                messagebox.showerror("Invalid Selection.","""Invalid Selection. \n\n The city and State doesn't
                exist.""")
                return
        username = self.E1_bWin.get()
        username = username.lower()
        emailAddress = self.E2_bWin.get()
        emailAddress = emailAddress.lower()
        self.username = username
        password = self.E3_bWin.get()
        confirm = self.E4_bWin.get()
        city = self.drop2.cget("text")
        state = self.drop3.cget("text")
        entry_list = [username, emailAddress, password, confirm]
        flag = False
        for entry in entry_list:
            if not entry:
                messagebox.showerror("Invalid Format.", """Invalid Insertion. \n\n
                The field can not be empty. Please fill all fields!""")
                break
            flag = True
        if flag:
            if password != confirm:
                messagebox.showerror("Invalid Selection.","""Wrong Password Confirmation. \n\n Please same passwords.""")
                return
            if response.lower() == "city official":
                db= self.Connect()
                c = db.cursor()
                ans = c.execute("SELECT City, State FROM CITYSTATE WHERE City = %s AND State = %s", (city, state))
                if ans == 0:
                    messagebox.showerror("Invalid City/State", "The City and State you entered are not valid. "
                                                           "Please provide an accessible area.")
                    return
                else:
                    pass

            db = self.Connect()
            c = db.cursor()
            ans = c.execute("SELECT EmailAddress FROM USER WHERE Username = %s", (username))
            ans1 = c.execute("SELECT Username FROM USER WHERE EmailAddress = %s", (emailAddress))

            if ans >= 1:
                messagebox.showwarning("Invalid Username", "The username you entered is already taken. "
                                                       "Please choose another.")
            elif ans1 >= 1:
                messagebox.showwarning("Invalid Email-Address", "The Email Address that you entered is already taken. "
                                                            "Please choose another.")
            else:
                try:
                    c.execute("INSERT INTO USER VALUES (%s,%s, %s,%s)", (emailAddress, username,password, response))

                    if response.lower() == "city official":
                        if title == "":
                            messagebox.showerror("Invalid Title Format." ,"""Invalid Insertion. \n\n The title can
                            not be empty. Please input a valid title""")
                            return
                        c2 = db.cursor()
                        c2.execute("INSERT INTO CITYOFFICIAL VALUES (%s,%s, %s, %s, %s)",(emailAddress, title, "None", city, state))
                        messagebox.showinfo("Account Created Successfully!!", "Please sign-in with your new account.")
                    c.close()
                    self.LoginPage()
                    self.bWin.withdraw()
                except:
                    messagebox.showerror("Invalid input","""Invalid input. \n\n Please insert a valid input""")

    def addNewDataPoint(self):
        # Builds the window for adding new data points.
        # Gets locations and data types from the database. Window gets all the values for further use.
        cWin = Toplevel()
        cWin.title("Add a new data point")
        cWin.geometry("900x350+0+0")

        self.cWin=cWin

        header = Canvas(cWin, width=500, height=65)
        header.pack()
        header.create_rectangle(10,10,490, 50)
        title = header.create_text(250,30)

        header.itemconfig(title, text="Add a new data point", font=('normal', 14), fill = "goldenrod") #changed
        Frame1=Frame(cWin)
        Frame1.pack(pady=10)

        db = self.Connect()
        c = db.cursor()
        c.execute("SELECT LocationName FROM POI")
        newtup = c.fetchall()
        
        newlist= list(newtup)
        citylist = []
        for element in newlist:
            if element[0] not in citylist:
                citylist.append(element[0])

        L2_1 = Label(Frame1, anchor="e", text="POI Location Name:", width=15) 
        L2_1.grid(row=0, column=0, sticky = W)
        options1 = citylist 
        var1 = StringVar()
        var1.set("Select POI Location") 
        drop4 = OptionMenu(Frame1, var1, *options1)
        drop4.grid(row=0, column=1, padx=10)
        self.drop4 = drop4

        L2_2 = Label(Frame1, anchor="e", text="date of reading:", width=15)
        L2_2.grid(row=1, column=0, sticky = W)

        L21_2 = Label(Frame1, anchor="e", text="time of reading:", width=15)
        L21_2.grid(row = 1, column = 2, sticky = W)
        #datetime

        L2_3 = Label(Frame1, anchor="e", text="Data type:", width=15)
        L2_3.grid(row=2, column=0, sticky = W)

        c = db.cursor()
        c.execute("SELECT Type FROM DATATYPE")
        newtup10 = c.fetchall()
        newlist10= list(newtup10)
        typelist = []
        for element in newlist10:
            if element[0] not in typelist:
                typelist.append(element[0])

        var2 = StringVar()
        var2.set("DataType")
        drop5 = OptionMenu(Frame1, var2, *typelist)
        drop5.grid(row=2, column=1, padx=10)
        self.drop5 = drop5
        L2_4 = Label(Frame1, anchor="e", text="Data Value:", width=15)
        L2_4.grid(row=3, column=0, sticky = W)

        var2 = StringVar(root, value="")
        self.E1_1_cWin = Entry(Frame1, state="normal", bd=1, width=20, textvariable= var2)
        self.E1_1_cWin.grid(row=3, column=1,padx = 10)
        self.var2= var2
        v = StringVar(root, value='yyyy-mm-dd')
        self.E1_4_cwin = Entry(Frame1, state= "normal", textvariable= v)
        self.E1_4_cwin.grid(row = 1, column = 1)
        self.v = v
        var = StringVar(root, value='hh:mm')
        self.E1_5_cwin = Entry(Frame1, state= "normal", textvariable= var)
        self.E1_5_cwin.grid(row=1, column =3)
        self.var=var


        B1 = Button(Frame1, text="Back", command=self.BacktoLogin, width=10)
        B1.grid(row=4, column=1, pady=10)

        B2 = Button(Frame1, text="Sumbit", command=self.submitNewDataPoint, width=10)
        B2.grid(row=4, column=2, pady=10)

        B3 = Button(Frame1, text="Add a new location", command=self.addNewLocation,fg = "blue", width=11, padx= 20, bd=0)
        B3.grid(row=0, column=2, pady=10)


    def submitNewDataPoint(self):
        # upon the values inserted in the data point window, this function processes the sql
        # statemens bases on the values inserted.
        # Used datastrp time to have it organized in python and to add the object in the database.
        db = self.Connect() 
        c = db.cursor()
        city = self.drop4.cget("text")

        if city == "Select City":
            messagebox.showerror("Invalid Input", "Please insert a vaild city.")
            return

        date = self.v.get()
        time = self.var.get()
        datatype = self.drop5.cget("text")
        value = self.var2.get()

        try:
            int(value)
        except:
            messagebox.showerror("Invalid Data Value", "The value must be an integer.")
            return
        datetimefinal = date+" " +time
        try:
            timedate = datetime.datetime.strptime(datetimefinal, "%Y-%m-%d %H:%M")
        except: 
            messagebox.showerror("Invalid Date/Time Format",
                                 "The format of the day or time is incorrect. Please insert a vaild one.")
            return
        try:
            c.execute("INSERT INTO DATAPOINT (DateTime, DLocationName, DataValue, DType) VALUES "
                      "(%s, %s, %s, %s)", (timedate, city, value, datatype))
            messagebox.showinfo ("Operation Successfull!", "Point was sent for confirmation approval")
            self.cWin.withdraw()
            self.addNewDataPoint()    
        except:
            messagebox.showerror("Invalid Point", "The point already exists!.")
            return

    def addNewLocation(self):
        # This function creates the layout for adding a new location. We are abstracting
        # the combination between city and state from the batabase.
        dWin = Toplevel()
        dWin.title("Add a new location")
        dWin.geometry("500x350+0+0")
        self.dWin=dWin
        header = Canvas(dWin, width=500, height=65)
        header.pack()
        header.create_rectangle(10,5,490,50)
        title = header.create_text(250,27.5)

        header.itemconfig(title, text="Add a new location", font=('normal', 14), fill = "goldenrod")
        Frame1=Frame(dWin)
        Frame1.pack(pady=10)

        db = self.Connect()
        c = db.cursor()
        c.execute("SELECT City, State FROM CITYSTATE")
        newtup = c.fetchall()
        newlist= list(newtup)
        citylist = []
        statelist = []
        print(newlist)
        for element in newlist:
            print(element[0])
            if element[0] not in citylist:
                citylist.append(element[0])
            if element[1] not in statelist:
                statelist.append(element[1])
        L3_1 = Label(Frame1, anchor="e", text="POI Location Name:", width=15)
        L3_1.grid(row=0, column=0, sticky = W)
        self.E1_1_dWin = Entry(Frame1, state="normal", bd=1, width=20)
        self.E1_1_dWin.grid(row=0, column=1,padx = 30, sticky = W)

        L4_1 = Label(Frame1, anchor="e", text="City:", width=15)
        L4_1.grid(row=1, column=0, sticky = W)
        var2 = StringVar()
        var2.set("City")
        options2 = citylist
        drop6 = OptionMenu(Frame1, var2, *options2)
        drop6.grid(row=1, column=1, padx=10, sticky = W)
        self.drop6 = drop6

        L5_1 = Label(Frame1, anchor="e", text="State:", width=15)
        L5_1.grid(row=2, column=0, sticky = W)
        var3 = StringVar()
        options3 = statelist
        var3.set("State")
        drop7 = OptionMenu(Frame1, var3, *options3)
        drop7.grid(row=2, column=1, padx=10, sticky =W)
        self.drop7 = drop7

        L6_1 = Label(Frame1, anchor="e", text="Zip Code:", width=15)
        L6_1.grid(row=3, column=0, sticky = W)
        self.E1_2_dWin = Entry(Frame1, state="normal", bd=1, width=20)
        self.E1_2_dWin.grid(row=3, column=1,padx = 30, sticky =W)

        B1 = Button(Frame1, text="Back", command=self.BacktoAddPoint, width=10)
        B1.grid(row=4, column=0, pady=10)

        B2 = Button(Frame1, text="Sumbit", command=self.includePoint, width=10)
        B2.grid(row=4, column=1, pady=10)

        self.cWin.withdraw()

    def includePoint(self):
        # inserts the information from the desired location. Checks that for correct input
        # if all the format is met, includes the given data into the database.
        db = self.Connect()
        c = db.cursor()
        POI = self.E1_1_dWin.get()
        zipCode = self.E1_2_dWin.get()
        Pstate = self.drop7.cget("text")
        Pcity = self.drop6.cget("text")

        try:
            int(zipCode)
        except:
            messagebox.showerror("Error!!", "Zip Code must be an integer!.")

        if POI == "":
            messagebox.showwarning("Error!!", "Please add a valid location.")

        try:

            c.execute("INSERT INTO POI (LocationName,ZipCode, Pcity, Pstate) VALUES (%s, %s, %s, %s)", (POI, zipCode, Pcity, Pstate))
            db.commit()
            messagebox.showinfo("Process Successful!!", "The new location has been added.")
            self.dWin.withdraw()
            self.addNewDataPoint()

        except:
            messagebox.showwarning("Error!!", "Please add a valid location.")
            return

    def CityOffFunct(self):
        # Function builds the main window for the city official functionality.
        cityWin = Toplevel()
        cityWin.title('City Official')
        cityWin.geometry("650x350+1+1")
        self.cityWin = cityWin

        body = Canvas(cityWin, width=650, height=300)

        body.create_line(0, 50, 650, 50)
        body.create_line(0, 290, 650, 290)
        title = body.create_text(325, 100)
        button2 = Button(body, text="Filter/Search POI", command=self.viewPois, anchor=W)
        button2.place(x=260,y=140)
        button3 = Button(body, text="POI Report", command=self.POIReport , anchor=W)
        button3.place(x=280, y=180)
        body.itemconfig(title, text="Choose Functionality", font=('normal', 20), fill="goldenrod")
        body.pack()

        frame = Frame(cityWin, bg='white', width=650, height=40)
        frame.pack(side=RIGHT)
        button1 = Button(frame, text='Log out', command=self.CityOffLogOut)
        button1.pack(side=TOP, fill=BOTH, padx=100)

    def viewPois(self):
        # Creates the first layout for the first functionality for city officials.
        # Gets the values from the database, and creates the necessary spaces for the user data input
        self.cityWin.withdraw()
        fWin = Toplevel()
        fWin.title("View POIs") 
        fWin.geometry("800x350+0+0")

        self.fWin=fWin

        header = Canvas(fWin, width=500, height=65)
        header.pack()
        header.create_rectangle(10,10,490,50)
        title = header.create_text(250,27.5)

        header.itemconfig(title, text="View POIs", font=('normal', 14), fill = "goldenrod")
        Frame1=Frame(fWin)
        Frame1.pack(pady=10)

        db = self.Connect()
        c = db.cursor()
        c.execute("SELECT LocationName FROM POI")
        newtup = c.fetchall()
        
        newlist= list(newtup)
        POIlist = []
        for element in newlist:
            print(element[0])
            if element[0] not in POIlist:
                POIlist.append(element[0])

        LF_1 = Label(Frame1, anchor="e", text="POI Location:", width=15)
        LF_1.grid(row=0, column=0, sticky = W)
        options1 = POIlist 
        var1 = StringVar()
        var1.set("POI Location")
        drop8 = OptionMenu(Frame1, var1, *options1)
        drop8.grid(row=0, column=1, padx=10)
        self.drop8 = drop8

        c = db.cursor()
        c.execute("SELECT Pcity FROM POI")
        newtup1 = c.fetchall()
        
        newlist1= list(newtup1)
        citylist = []
        for element in newlist1:
            if element[0] not in citylist:
                citylist.append(element[0])

        LF_2 = Label(Frame1, anchor="e", text="City:", width=15)
        LF_2.grid(row=1, column=0, sticky = W)
        options2 = citylist 
        var2 = StringVar()
        var2.set("Select City")
        drop9 = OptionMenu(Frame1, var2, *options2)
        drop9.grid(row=1, column=1, padx=10)
        self.drop9 = drop9

        c = db.cursor()
        c.execute("SELECT Pstate FROM POI")
        newtup2 = c.fetchall()
        
        newlist2= list(newtup2)
        statelist = []
        for element in newlist2:
            if element[0] not in statelist:
                statelist.append(element[0])

        LF_3 = Label(Frame1, anchor="e", text="State:", width=15)
        LF_3.grid(row=2, column=0, sticky = W)
        options3 = statelist 
        var3 = StringVar()
        var3.set("Select State")
        drop10 = OptionMenu(Frame1, var3, *options3)
        drop10.grid(row=2, column=1, padx=10)
        self.drop10 = drop10

        LF_4 = Label(Frame1, anchor="e", text="Zip Code:", width=15)
        LF_4.grid(row=3, column=0, sticky = W)
        self.E1_fWin = Entry(Frame1, state="normal", bd=1, width=20)
        self.E1_fWin.grid(row=3, column=1,padx = 30, sticky =W)
        LF_5 = Label(Frame1, anchor="e", text="Flagged?:", width=15)
        LF_5.grid(row=4, column=0, sticky = W)

        var4 = IntVar()
        c = Checkbutton(Frame1 , text="", variable=var4)
        c.grid(row=4, column = 1)
        self.var4 = var4
        LF_6 = Label(Frame1, anchor="e", text="Date Flagged:", width=15)
        LF_6.grid(row=5, column=0, sticky = W)

        LF_7 = Label(Frame1, anchor="e", text="to", width=2)
        LF_7.grid(row=5, column=3, sticky = W)

        var5 = StringVar(root, value='yyyy-mm-dd')
        self.E1_fwin = Entry(Frame1, state= "normal", textvariable= var5)
        self.E1_fwin.grid(row = 5, column = 1)
        self.var5 = var5  

        var6 = StringVar(root, value='yyyy-mm-dd')
        self.E2_fwin = Entry(Frame1, state= "normal", textvariable= var6)
        self.E2_fwin.grid(row=5, column =5, sticky= E)
        self.var6=var6

        B1 = Button(Frame1, text="Apply Filter", command=self.CreateUI, width=10)
        B1.grid(row=6, column=4, pady=10)

        B2 = Button(Frame1, text="Reset Filter", command=self.reset2, width=10)
        B2.grid(row=6, column=5, pady=10)

        B3 = Button(Frame1, text="Back", command=self.goBack2, width=10)
        B3.grid(row=6, column=1, pady=10)

    def goBack2(self):
        # allows to close window and to redirect to another one
        self.fWin.withdraw()
        self.CityOffFunct()

    def reset2(self):
        # allows to close window and to redirect to another one
        self.fWin.withdraw()
        self.viewPois()

    def CreateUI(self):
        # ased on the parameters of search from the user, a new report is created, using the tool "treeview".
        # The treeview is built
        from tkinter import ttk as ttk
        self.var4 = self.var4.get()
        if self.var4 ==1:   
            try:
                datetime.datetime.strptime(self.var5.get(), "%Y-%m-%d")
                datetime.datetime.strptime(self.var6.get(), "%Y-%m-%d")
            except: 
                messagebox.showerror("Invalid Date/Time Format",
                                     "The format of the day or time is incorrect. Please insert a vaild one.")
                return

        self.fWin.withdraw()

        gWin = Toplevel()
        gWin.title("POIs")
        gWin.geometry("700x350+0+0")
        self.gWin=gWin
        header = Canvas(gWin, width=500, height=65)
        header.pack()
        header.create_rectangle(10,5,490,50)
        title = header.create_text(250,27.5)
        header.itemconfig(title, text="View POIs (filtered)", font=('normal', 14), fill = "goldenrod")

        warning = header.create_text(120, 61)
        header.itemconfig(warning, text="Please double click to view details of POI", font=('normal', 12), fill="red")

        Frame1=Frame(gWin)
        Frame1.pack(pady=10)

        tv = ttk.Treeview(Frame1)
        self.tv = tv      
        var = StringVar()
        print(var)
        tv['columns'] = ('City','State', 'Zip Code', 'Flagged?', "Date Flagged")
        tv.heading("#0", text='Location Name', anchor='w')
        tv.column("#0", anchor="w", width=100, stretch=False)
        tv.heading("City", text='City', anchor='w')
        tv.column("City", anchor="w", width=100, stretch=False)
        tv.heading('State', text='State')
        tv.column('State', anchor='center', width=100, stretch=NO)
        tv.heading('Zip Code', text='Zip Code')
        tv.column('Zip Code', anchor='center', width=100)
        tv.heading("Flagged?", text='Flagged?')
        tv.column('Flagged?', anchor='center', width=100)
        tv.heading("Date Flagged", text='Date Flagged')
        tv.column('Date Flagged', anchor='center', width=100)
        tv.grid(row = 0, column = 1)
        self.tv.bind("<Double-1>", self.OnDoubleClick)
        self.treeview = tv
        B1 = Button(Frame1, text="Back", command=self.gobackPOIS, width=10)
        B1.grid(row=1, column=1, pady=10)
        self.LoadTable()

    def gobackPOIS(self):
        # allows to close window and to redirect to another one
        self.gWin.withdraw()
        self.viewPois()

    def LoadTable(self):
        # Function that allows the treeview to be completed. Inserting all of the necessary parameters and using our sql statements.
        if self.var4 == 0:
            LocationName = self.drop8.cget("text")
            City = self.drop9.cget("text")
            State = self.drop10.cget("text")
            ZipCode = self.E1_fWin.get()
            db = self.Connect()
            c = db.cursor()
            c.execute("SELECT * FROM POI WHERE LocationName = %s AND Pcity = %s AND Pstate= %s AND ZipCode = %s AND Flag = 'No'",(LocationName, City, State, ZipCode))
            newtup = c.fetchall()
            print(newtup)
            newlist = list(newtup)
            var = StringVar()
            for values in newlist:
                self.treeview.insert("", 'end', text=values[0], values=(values[4],values[5], values[3],values[2], "N/A"))
        else:
            LocationName = self.drop8.cget("text")
            City = self.drop9.cget("text")
            State = self.drop10.cget("text")
            ZipCode = self.E1_fWin.get()
            startdate = self.var5.get()
            enddate = self.var6.get()

            db = self.Connect()
            c = db.cursor()
            c.execute("SELECT * FROM POI WHERE LocationName = %s AND Pcity = %s AND Pstate= %s AND ZipCode = %s AND DateFlagged >= %s and DateFlagged <= %s",(LocationName, City, State, ZipCode, startdate, enddate))
            newtup = c.fetchall()
            print(newtup)
            newlist = list(newtup)
            var = StringVar()
            for values in newlist:
                self.treeview.insert("", 'end', text=values[0], values=(values[4],values[5], values[3],values[2],values[1] ))

    def OnDoubleClick(self, event):
        # function that allows to take any actions when the row is clicked
        item = self.tv.selection()[0]
        self.item = item
        self.POIDetail()
        print("you clicked on", self.tv.item(item,"text"))

    def POIDetail(self):
        # When the value gets clicked, this function is called.
        # Function builds the interface for POI detail. Gets the datatypes from the database.
        # Filters the information by using entries.
        self.gWin.withdraw()

        hWin = Toplevel()
        hWin.title("POI Location: " + self.tv.item(self.item,"text") )
        hWin.geometry("900x300+0+0")

        self.hWin=hWin

        header = Canvas(hWin, width=500, height=65)
        header.pack()
        header.create_rectangle(10,5,490,50)
        title = header.create_text(250,27.5)

        header.itemconfig(title, text="Details of the " + self.tv.item(self.item,"text") + " POI", fill = "goldenrod", font=('normal', 14)) #changed
        Frame1=Frame(hWin)
        Frame1.pack(pady=10)

        db = self.Connect()
        c = db.cursor()
        c.execute("SELECT Type FROM DATATYPE")
        newtup2 = c.fetchall()
        
        newlist2= list(newtup2)
        typelist = []
        for element in newlist2:
            if element[0] not in typelist:
                typelist.append(element[0])
        LH_1 = Label(Frame1, anchor="e", text="Type:", width=15)
        LH_1.grid(row=1, column=0, sticky = W)
        options3 = typelist 
        var3 = StringVar()
        var3.set("Select Type")
        drop11 = OptionMenu(Frame1, var3, *options3)
        drop11.grid(row=1, column=1, padx=10)
        self.drop11 = drop11
        LH_2 = Label(Frame1, anchor="e", text="Data Value", width=15)
        LH_2.grid(row=2, column=0, sticky = W)

        var7 = StringVar()
        self.E1_hwin = Entry(Frame1, state= "normal", textvariable= var7)
        self.E1_hwin.grid(row = 2, column = 1)
        self.var7 = var7

        LH_2 = Label(Frame1, anchor="e", text="to", width=2)
        LH_2.grid(row=2, column=2, sticky = S)  

        var8 = StringVar()
        self.E2_hwin = Entry(Frame1, state= "normal", textvariable= var8)
        self.E2_hwin.grid(row=2, column =3, sticky= E)
        self.var8=var8

        LH_3 = Label(Frame1, anchor="e", text="time&date", width=10)
        LH_3.grid(row=3, column=0, sticky = W)

        LH_4 = Label(Frame1, anchor="e", text="to", width=2)
        LH_4.grid(row=3, column=2, sticky = S)

        var9 = StringVar(root, value='yyyy-mm-dd hh:mm')
        self.E3_hwin = Entry(Frame1, state= "normal", textvariable= var9)
        self.E3_hwin.grid(row = 3, column = 1)
        self.var9 = var9  

        var10 = StringVar(root, value='yyyy-mm-dd hh:mm')
        self.E4_hwin = Entry(Frame1, state= "normal", textvariable= var10)
        self.E4_hwin.grid(row=3, column =3, sticky= E)
        self.var10=var10

        B1 = Button(Frame1, text="Apply Filter", command=self.CreateUI2, width=10)
        B1.grid(row=4, column=4, pady=10)

        B2 = Button(Frame1, text="Reset Filter", command=self.resetFilter, width=10)
        B2.grid(row=4, column=5, pady=10)

        B3 = Button(Frame1, text="Back", command=self.goBack, width=10)
        B3.grid(row=4, column=1, pady=10)

    def goBack(self):
        # allows to close window and to redirect to another one
        self.hWin.withdraw()
        self.viewPois()

    def resetFilter(self):
        # allows to close window and to redirect to another one
        self.hWin.withdraw()
        self.POIDetail()

    def CreateUI2(self):
        # based on the filter parameters on the POI Detail search, we create another window
        # with the tkinter "treeview".

        try:
            int(self.var7.get())
            int(self.var8.get())
        except:
            messagebox.showerror("Invalid Data Value", "The Data Value is not an integer. Please insert a vaild one.")
            return
        try:
            datetime.datetime.strptime(self.var9.get(), "%Y-%m-%d %H:%M")
            datetime.datetime.strptime(self.var10.get(), "%Y-%m-%d %H:%M")
        except: 
            messagebox.showerror("Invalid Date/Time Format", "The format of the day or time is incorrect. Please insert a vaild one.")
            return

        self.hWin.withdraw()

        jWin = Toplevel()
        jWin.title("POI Detail Search")
        jWin.geometry("800x400+0+0")

        self.jWin=jWin

        header = Canvas(jWin, width=500, height=65)
        header.pack()
        header.create_rectangle(10,5,500,50)
        title = header.create_text(250,27.5)
        header.itemconfig(title, text="POI Details Search", font=('normal', 14), fill = "goldenrod")
        warning = header.create_text(110,61)
        header.itemconfig(warning, text="Please double click to select POI detail", font=('normal',12), fill="red")

        Frame1=Frame(jWin)
        Frame1.pack(pady=10)

        tv2 = ttk.Treeview(Frame1)
        self.tv2 = tv2   
        var = StringVar()
        print(var)
        tv2['columns'] = ('Data Value','Time & Data of Reading')
        tv2.heading("#0", text='Data Type', anchor='w')
        tv2.column("#0", anchor="w", width=100, stretch=False)
        tv2.heading("Data Value", text='Data Value', anchor='w')
        tv2.column("Data Value", anchor="w", width=100, stretch=False)
        tv2.heading('Time & Data of Reading', text='Time & Data of Reading')
        tv2.column('Time & Data of Reading', anchor='center', width=200, stretch=NO)

        tv2.grid(row=0, column = 1)
        self.treeview2 = tv2

        B1 = Button(Frame1, text="Back/Reset Filter", command=self.backorReset, width=15)
        B1.grid(row=1, column=0, pady=10)

        B2 = Button(Frame1, text="Flag", command=self.setFlag, width=10)
        B2.grid(row=1, column=2, pady=10)

        self.LoadTable2()

    def LoadTable2(self):
        #getting the values from the filters will allow to populate the treeview. Once we get all the values, we do an SQL statement that filters our desired tuples.
        Type = self.drop11.cget("text")
        lowerBound = int(self.var7.get())
        upperBound = int(self.var8.get())
        startdate = self.var9.get()
        enddate = self.var10.get()
        name = (self.tv.item(self.item,"text"))

        dateandtime1 = datetime.datetime.strptime(startdate, "%Y-%m-%d %H:%M")
        dateandtime2 = datetime.datetime.strptime(enddate, "%Y-%m-%d %H:%M")

        db = self.Connect()
        c = db.cursor()
        c.execute("SELECT DType, DataValue, DateTime FROM DATAPOINT WHERE DLocationName = %s "
                        "AND Dtype = %s AND DataValue BETWEEN %s AND %s AND DateTime BETWEEN %s AND %s "
                  "AND Accepted = 'YES'",(name, Type, lowerBound, upperBound, startdate, enddate))
        newtup = c.fetchall()
        print(newtup)
        newlist = list(newtup)
        var = StringVar()
        for values in newlist:
            self.tv2.insert("", 'end', text=values[0], values=(values[1],values[2]))

    def setFlag(self):
        # updates the flag when the button of "flagged" is clicked
        db = self.Connect()
        c = db.cursor()
        c.execute("UPDATE POI SET Flag = 'Yes', DateFlagged = %s WHERE LocationName =%s",(self.today, self.tv.item(self.item,"text")))
        messagebox.showinfo("POI Flagged Successfull!!", "The selected POI is now flagged.")

    def backorReset(self):
        self.jWin.withdraw()
        self.POIDetail()

    def CityOffLogOut(self):
        self.cityWin.withdraw()
        self.LoginPage()

    def AdminFunct(self):
        adminWin=Toplevel()
        adminWin.title('Admin')
        adminWin.geometry("650x350+1+1")
        self.adminWin = adminWin

        body = Canvas(adminWin, width=900, height=300)

        body.create_line(0, 50, 650,50)
        body.create_line(0, 290, 650, 290)
        title = body.create_text(325, 100)
        button2 = Button(body, text="Pending Data Points", command=self.PendingPoints, anchor=W)
        button2.place(x=250, y=140)
        button3 = Button(body, text="Pending City Official Accounts", command=self.PendingCityOfficial, anchor=W)
        button3.place(x=220, y=180)

        body.itemconfig(title, text="Choose Functionality", font=('normal', 20), fill="goldenrod")
        body.pack()

        frame = Frame(adminWin, bg='white', width=650, height=40)
        frame.pack(side=RIGHT)
        button1 = Button(frame, text='Log out', command=self.AdminLogOut)
        button1.pack(side=TOP, fill=BOTH, padx=100)

    def PendingPoints(self):

        from tkinter import ttk as ttk

        pendingWin=Toplevel()
        pendingWin.title('Pending Data Points')
        pendingWin.geometry("800x350+1+1")
        self.pendingWin = pendingWin

        header = Canvas(pendingWin, width=500, height=65)
        header.pack()
        header.create_rectangle(10,5,500,50)
        title = header.create_text(250,27.5)
        header.itemconfig(title, text="Pending Data Points", font=('normal', 14), fill = "goldenrod")
        warning = header.create_text(110, 61)
        header.itemconfig(warning, text="Please double click to select data point", font=('normal', 12), fill="red")

        Frame1=Frame(pendingWin)
        Frame1.pack(pady=10)

        tv3 = ttk.Treeview(Frame1)
        self.tv3 = tv3      
        var = StringVar()
        print(var)
        tv3['columns'] = ('POI location ^', 'Data Type ^', 'Data Value ^', 'Time&date of data reading ^')
        tv3.heading("#0", text="", anchor='w')
        tv3.column("#0", width=0)
        tv3.heading("POI location ^", text='POI LOcation ^', anchor='w')
        tv3.column("POI location ^", anchor="w", width=100, stretch=False)
        tv3.heading("Data Type ^", text='Data Type ^', anchor='w')
        tv3.column("Data Type ^", anchor="w", width=100, stretch=False)
        tv3.heading('Data Value ^', text='Data Value ^')
        tv3.column('Data Value ^', anchor='center', width=100, stretch=False)
        tv3.heading('Time&date of data reading ^', text='Time&date of data reading ^')
        tv3.column('Time&date of data reading ^', anchor='center', width=200)
        tv3.grid(row=0, column=1)
        tv3.heading('POI location ^', text='POI location ^',
                    command=lambda: self.treeview_sort_cha(tv3, 'POI location ^', False))
        tv3.heading('Data Value ^', text='Data Value ^',
                    command=lambda: self.treeview_sort_num(tv3, 'Data Value ^', False))
        tv3.heading('Data Type ^', text='Data Type ^',
                    command=lambda: self.treeview_sort_cha(tv3, 'Data Type ^', False))
        tv3.heading('Time&date of data reading ^', text='Time&date of data reading ^',
                    command=lambda: self.treeview_sort_cha(tv3, 'Time&date of data reading ^', False))
        self.treeview3 = tv3
        self.LoadTable3()
        self.tv3.bind("<Double 1>", self.OnDoubleClick2)
        B1 = Button(Frame1, text="Accept", command=self.changeButton1, width=10)
        B1.grid(row=1, column=0, pady=10)
        B2 = Button(Frame1, text="Reject", command=self.changeButton2, width=10)
        B2.grid(row=1, column=2, pady=10)

        B3 = Button(Frame1, text="Go back", command=self.AdminWindow, width=10)
        B3.grid(row=0, column=2, pady=10)

    def LoadTable3(self):
        self.adminWin.withdraw()
        db = self.Connect()
        c = db.cursor()
        c.execute("SELECT DLocationName, DType, DataValue,DateTime  FROM DATAPOINT WHERE Accepted = 'None'")
        newtup = c.fetchall()
        newlist = list(newtup)
        var = StringVar()
        for values in newlist:
            self.treeview3.insert("", 'end', text="", values=(values[0], values[1], values[2], values[3]))
   
    def changeButton1(self):
        try:
            print(self.newitem3)
        except:
            messagebox.showerror("Invalid Selection.","""Invalid Selection. \n\n Please select the row with a double click""")
            return
        db = self.Connect()
        c = db.cursor()
        c.execute("SELECT DLocationName FROM DATAPOINT WHERE Accepted = 'Yes' AND DateTime = %s AND DLocationName = %s AND DataValue = %s AND Dtype = %s",(self.newitem3, self.item10, self.newitem2, self.newitem1))
        newtup1 = c.fetchall()
        newlist1 = list(newtup1)
        if len (newlist1) == 1:
            messagebox.showerror("Invalid Selection.","""Invalid Selection. \n\n Please select the row with a double click""")
            return

        c = db.cursor()
        c.execute("UPDATE DATAPOINT SET Accepted = 'Yes' WHERE DateTime = %s AND DLocationName = %s AND DataValue = %s AND Dtype = %s",(self.newitem3, self.item10, self.newitem2, self.newitem1))
        db.commit()
        newtup = c.fetchall()
        list(newtup)
        messagebox.showinfo("Successfully Approved!!", "Data Point was approved successfully.")

        self.pendingWin.withdraw()
        self.PendingPoints()

    def changeButton2(self):
        db = self.Connect()
        c = db.cursor()
        c.execute("UPDATE DATAPOINT SET Accepted = 'No' WHERE DateTime = %s AND DLocationName = %s AND DataValue = %s AND Dtype = %s",(self.newitem3, self.item10, self.newitem2, self.newitem1))
        messagebox.showinfo("Successfully Rejected!!", "Data Point was rejected successfully.") 
        self.pendingWin.withdraw()
        self.PendingPoints()

    def OnDoubleClick2(self, event):
        curItem = self.treeview3.focus()
        NewDic = self.treeview3.item(curItem)
        newlist = NewDic['values']
        self.item10 = newlist[0]
        self.newitem1 = newlist[1]
        self.newitem2 = newlist[2]
        self.newitem3 = newlist[3]

    def PendingCityOfficial(self):
        self.adminWin.withdraw()
        cityoffWin=Toplevel()
        cityoffWin.title('Pending Data Points')
        cityoffWin.geometry("800x350+1+1")
        self.cityoffWin = cityoffWin

        header = Canvas(cityoffWin, width=500, height=65)
        header.pack()
        header.create_rectangle(10,5,500,50)
        title = header.create_text(250,27.5)
        header.itemconfig(title, text="Pending City Officials", font=('normal', 14), fill="goldenrod")
        warning = header.create_text(120, 61)
        header.itemconfig(warning, text="Please double click to select city official", font=('normal', 12), fill="red")

        Frame1=Frame(cityoffWin)
        Frame1.pack(pady=10)

        tv4 = ttk.Treeview(Frame1)
        self.tv4 = tv4      
        var = StringVar()
        print(var)

        tv4['columns'] = ('Email','City', 'State', 'Title')
        tv4.heading("#0", text='Username', anchor='w')
        tv4.column("#0", anchor="w", width=100, stretch=False)
        tv4.heading("Email", text='Email', anchor='w')
        tv4.column("Email", anchor="w", width=100, stretch=False)
        tv4.heading('City', text='City')
        tv4.column('City', anchor='center', width=100, stretch=NO)
        tv4.heading('State', text='State')
        tv4.column('State', anchor='center', width=100)
        tv4.heading('Title', text='Title')
        tv4.column('Title', anchor='center', width=100)
        tv4.grid(row = 0, column = 1)
        self.tv4.bind("<Double 1>", self.OnDoubleClick3)
        self.treeview4 = tv4

        B1 = Button(Frame1, text="Accept", command=self.changeButton3, width=10)
        B1.grid(row=1, column=0, pady=10)
        B2 = Button(Frame1, text="Reject", command=self.changeButton4, width=10)
        B2.grid(row=1, column=2, pady=10)
        B3 = Button(Frame1, text="Go back", command=self.AdminWindow2, width=10)
        B3.grid(row=0, column=2, pady=10)

        self.LoadTable4()

    def LoadTable4(self):
        db = self.Connect()
        c = db.cursor()
        c.execute("SELECT USER.Username, CITYOFFICIAL.EmailAddress, CITYOFFICIAL.Ocity, CITYOFFICIAL.Ostate, CITYOFFICIAL.Title FROM USER Natural JOIN CITYOFFICIAL WHERE CITYOFFICIAL.Approved =  'None'")
        newtup = c.fetchall()
        newlist = list(newtup)
        var = StringVar()
        for values in newlist:
            self.treeview4.insert("", 'end', text=values[0], values=(values[1],values[2], values[3], values[4]))
   
    def OnDoubleClick3(self, event):
        try:
            item11 = self.tv4.selection()[0]
        except:
            pass
        self.item11 = self.tv4.item(item11,"text")
        curItem = self.treeview4.focus()
        NewDic = self.treeview4.item(curItem)
        print (self.treeview4.item(curItem))
        newlist = NewDic['values']
        self.newitem4 = newlist[0]

    def treeview_sort_cha(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
            tv.heading(col,
                       command=lambda: self.treeview_sort_cha(tv, col, not reverse))

    def treeview_sort_num(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(key=lambda t: int(t[0]), reverse=reverse)
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
            tv.heading(col,
                       command=lambda: self.treeview_sort_num(tv, col, not reverse))

    def POIReport(self):
        self.cityWin.withdraw()
        from tkinter import ttk as ttk
        reportWin=Toplevel()
        reportWin.title('POI Report')
        reportWin.geometry("1500x350+1+1")
        self.reportWin = reportWin
        header = Canvas(reportWin, width=500, height=65)
        header.pack()
        header.create_rectangle(10,5,500, 50)
        title = header.create_text(250, 27.5)
        header.itemconfig(title, text="POI Report", font=('normal', 14), fill = "goldenrod")

        Frame1=Frame(reportWin)
        Frame1.pack(pady=10)

        tv5 = ttk.Treeview(Frame1)
        self.tv5 = tv5
        var = StringVar()
        print(var)

        tv5['columns'] = ('POI Location', 'City', 'State', 'Mold Min ^', 'Mold Avg ^', 'Mold Max ^', 'AQ Min ^',
                          'AQ Avg ^', 'AQ Max ^', 'Number of data points ^', 'Flagged? ^')
        tv5.heading("#0", text='', anchor='w')
        tv5.column("#0", anchor="w", width=0, stretch=False)
        tv5.heading('POI Location', text='POI Location', anchor='w')
        tv5.column('POI Location', anchor="w", width=100, stretch=False)
        tv5.heading("City", text='City', anchor='w')
        tv5.column("City", anchor="w", width=100, stretch=False)
        tv5.heading('State', text='State')
        tv5.column('State', anchor='center', width=100, stretch=NO)
        tv5.heading(tv5["columns"][3], text=tv5["columns"][3])
        tv5.column(tv5["columns"][3], anchor='center', width=100)
        tv5.heading(tv5["columns"][4], text=tv5["columns"][4], anchor='w')
        tv5.column(tv5["columns"][4], anchor="w", width=100, stretch=False)
        tv5.heading(tv5["columns"][5], text=tv5["columns"][5], anchor='w')
        tv5.column(tv5["columns"][5], anchor="w", width=100, stretch=False)
        tv5.heading(tv5["columns"][6], text=tv5["columns"][6], anchor='w')
        tv5.column(tv5["columns"][6], anchor="w", width=100, stretch=False)
        tv5.heading(tv5["columns"][7], text=tv5["columns"][7], anchor='w')
        tv5.column(tv5["columns"][7], anchor="w", width=120, stretch=False)
        tv5.heading(tv5["columns"][8], text=tv5["columns"][8], anchor='w')
        tv5.column(tv5["columns"][8], anchor="w", width=100, stretch=False)
        tv5.heading(tv5["columns"][9], text=tv5["columns"][9], anchor='w')
        tv5.column(tv5["columns"][9], anchor="w", width=150, stretch=False)
        tv5.heading(tv5["columns"][10], text=tv5["columns"][10], anchor='w')
        tv5.column(tv5["columns"][10], anchor="w", width=100, stretch=False)
        tv5.grid(row=0, column=1)  # sticky = (N,S,W,E))
        tv5.heading(tv5["columns"][3], text=tv5["columns"][3],
                    command=lambda: self.treeview_sort_num(tv5, tv5["columns"][3], False))
        tv5.heading(tv5["columns"][4], text=tv5["columns"][4],
                    command=lambda: self.treeview_sort_num(tv5, tv5["columns"][4], False))
        tv5.heading(tv5["columns"][5], text=tv5["columns"][5],
                    command=lambda: self.treeview_sort_num(tv5, tv5["columns"][5], False))
        tv5.heading(tv5["columns"][6], text=tv5["columns"][6],
                    command=lambda: self.treeview_sort_num(tv5, tv5["columns"][6], False))
        tv5.heading(tv5["columns"][7], text=tv5["columns"][7],
                    command=lambda: self.treeview_sort_num(tv5, tv5["columns"][7], False))
        tv5.heading(tv5["columns"][8], text=tv5["columns"][8],
                    command=lambda: self.treeview_sort_num(tv5, tv5["columns"][8], False))
        tv5.heading(tv5["columns"][9], text=tv5["columns"][9],
                    command=lambda: self.treeview_sort_num(tv5, tv5["columns"][9], False))
        tv5.heading(tv5["columns"][10], text=tv5["columns"][10],
                    command=lambda: self.treeview_sort_cha(tv5, tv5["columns"][10], False))
        self.treeview5 = tv5

        B3 = Button(Frame1, text="Go back", command=self.gobck3, width=10)
        B3.grid(row=1, column=1, pady=10) #changed

        self.LoadTableReport()

    def gobck3(self):
        self.CityOffFunct()
        self.reportWin.withdraw()

    def LoadTableReport(self):
        db = self.Connect()
        c = db.cursor()
        c.execute("SELECT DLocationName AS POILocation, Pcity AS City, Pstate AS State, MoldMIN, MoldAVG, MoldMAX, AQMIN, AQAVG, AQMAX, ( NumberDataPoints + NumberDataPoints1) AS NumberDataPoints, Flag AS Flagged FROM (SELECT DLocationName, Pcity, Pstate, Flag, MIN( DataValue ) AS MoldMIN, AVG(DataValue ) AS MoldAVG, MAX( DataValue ) AS MoldMAX, COUNT( * ) AS NumberDataPoints1 FROM DATAPOINT NATURAL JOIN POI WHERE DATAPOINT.DLocationName = POI.LocationName AND DType =  'Mold' AND Accepted ='Yes' GROUP BY DLocationName) AS MOLD NATURAL JOIN (SELECT DLocationName, Pcity, Pstate, Flag, MIN( DataValue ) AS AQMin, AVG( DataValue ) AS AQAVG, MAX( DataValue )AS AQMAX, COUNT( * ) AS NumberDataPoints FROM DATAPOINT NATURAL JOIN POI WHERE DATAPOINT.DLocationName = POI.LocationName AND DType =  'Air Quality' AND Accepted ='Yes' GROUP BY DLocationName) AS AQ")
        newtup = c.fetchall()
        print(newtup)
        newlist = list(newtup)
        for values in newlist:
            self.tv5.insert("", 'end', text="", values=(values[0], values[1], values[2], int(values[3]), int(values[4]),
                                                        int(values[5]), int(values[6]), int(values[7]), int(values[8]),
                                                        int(values[9]), values[10]))

    def changeButton3(self):
        try:
            a = self.newitem4
        except:
            messagebox.showerror("Invalid Selection.","""Invalid Selection. \n\n Please select the row with a double click""")
            return

        db = self.Connect()
        c = db.cursor()
        c.execute("SELECT EmailAddress FROM CITYOFFICIAL WHERE Approved = 'Yes' AND EmailAddress = %s",(self.newitem4))
        newtup=c.fetchall()
        newlist = list(newtup)
        if len(newlist) ==1 :
            messagebox.showerror("Invalid Selection.","""Invalid Selection. \n\n Please select the row with a double click""")
            return

        c = db.cursor()
        c.execute("UPDATE CITYOFFICIAL SET Approved = 'Yes' WHERE EmailAddress = %s",(self.newitem4))
        messagebox.showinfo("City Official Successfully Approved!!", "City Official was approved successfully.") 
        self.cityoffWin.withdraw()
        self.PendingCityOfficial()

    def changeButton4(self):

        try:
            a = self.newitem4
        except:
            messagebox.showerror("Invalid Selection.","""Invalid Selection. \n\n Please select the row with a double click""")
            return

        db = self.Connect()
        c = db.cursor()
        c.execute("SELECT EmailAddress FROM CITYOFFICIAL WHERE Approved = 'No' AND EmailAddress = %s",(self.newitem4))
        newtup = c.fetchall()
        newlist = list(newtup)
        if len(newlist) ==1 :
            messagebox.showerror("Invalid Selection.","""Invalid Selection. \n\n Please select the row with a double click""")
            return
        c = db.cursor()
        c.execute("UPDATE CITYOFFICIAL SET Approved = 'No' WHERE EmailAddress = %s",(self.newitem4))
        messagebox.showinfo("City Official Successfully Rejected!!", "City Official was rejected successfully.") 
        self.cityoffWin.withdraw()
        self.PendingCityOfficial()

    def AdminLogOut(self):
        self.adminWin.withdraw()
        self.LoginPage()
        # opens login page

    def AdminWindow(self):
        self.pendingWin.withdraw()
        self.AdminFunct()

    def AdminWindow2(self):
        self.cityoffWin.withdraw()
        self.AdminFunct()

    def BacktoAddPoint(self):
        self.addNewDataPoint()
        self.dWin.withdraw()

    def BacktoLogin(self):
        self.LoginPage()
        self.cWin.withdraw()
        self.dWin.withdraw()

    def Connect(self):
        import pymysql
        db = pymysql.connect(host = "academic-mysql.cc.gatech.edu", user = "cs4400_72", passwd = "3KWi_FQU", db="cs4400_72")
        self.db = db
        db.autocommit(True)
        return db
root = Tk()
root.withdraw()
root.title("Login")
app = Project(root)
root.mainloop()