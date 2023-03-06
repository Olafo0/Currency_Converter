import matplotlib.patches as mpatches
import tkinter as tk
import customtkinter
import csv

from matplotlib import pyplot as plt


def main():
    root = tk.Tk()
    root.geometry("750x500")
    root.title("Currency converter!")
    root.resizable(False,False)



    #Reading the database
    file = open("Task4a_data.csv","r")
    datareader1 = csv.reader(file,delimiter=",")

    # Inserting the data into an array
    current_data = []
    last_30_days = []
    last_30_days_GBP_TO_EUR_VALUE = []
    last_30_days_EUR_TO_GBP_VALUE = []
    last_30_days_GBP_TO_AUD_VALUE = []
    last_30_days_AUD_TO_GBP_VALUE = []
    last_30_days_GBP_TO_JPY_VALUE = []
    last_30_days_JPY_TO_GBP_VALUE = []
    last_30_days_GBP_TO_USD_VALUE = []

    for row1 in datareader1:
        current_data.append(row1)

    for i in range(0,30):
        x = 30
        n = x - i 
        print("Value N",n)
    
        y = len(current_data) 
        print("Value Y :", y)

        v = y - n
        print("Final Value", v)
        # Appending the data to its corresponding array
        last_30_days.append(current_data[v][0])
        last_30_days_GBP_TO_EUR_VALUE.append(float(current_data[v][1]))
        last_30_days_EUR_TO_GBP_VALUE.append(float(current_data[v][2]))
        last_30_days_GBP_TO_AUD_VALUE.append(float(current_data[v][3]))
        last_30_days_AUD_TO_GBP_VALUE.append(float(current_data[v][4]))
        last_30_days_GBP_TO_JPY_VALUE.append(float(current_data[v][5]))
        last_30_days_JPY_TO_GBP_VALUE.append(float(current_data[v][6]))
        last_30_days_GBP_TO_USD_VALUE.append(float(current_data[v][7]))


    #Reading the database
    file = open("Task4a_data.csv","r")
    datareader = csv.reader(file, delimiter=",")

    currency_converter_data = []

    for row in datareader:
        currency_converter_data.append(row)

    recent_values = len(currency_converter_data) - 1

    #GBP TO EUR
    current_GPT_TO_EUR = currency_converter_data[recent_values][1]
    print("Current GBP TO EUR value - ",current_GPT_TO_EUR)

    #EUR TO GBP
    current_EUR_TO_GBP = currency_converter_data[recent_values][2]
    print("Current EUR TO GBP value - ",current_EUR_TO_GBP)

    #GBP TO AUS
    current_GBP_TO_AUS = currency_converter_data[recent_values][3]
    print("Current GBP TO AUS value - ",current_GBP_TO_AUS)

    #AUS TO GBP
    current_AUS_TO_GBP = currency_converter_data[recent_values][4]
    print("Current AUS TO GBP value - ",current_AUS_TO_GBP)

    #GBP TO JPY
    current_GBP_TO_JPY = currency_converter_data[recent_values][5]
    print("Current GBP TO JPY value - ",current_GBP_TO_JPY)

    #JPY TO GBP
    current_JPY_TO_GBP = currency_converter_data[recent_values][6]
    print("Current JPY TO GBP value - ",current_JPY_TO_GBP)

    #GBP TO USD
    current_GBP_TO_USD = currency_converter_data[recent_values][7]
    print("Current GBP TO USD value - ",current_GBP_TO_USD)

    #USD TO GBP
    current_USD_TO_GBP = currency_converter_data[recent_values][8]
    print("Current USD TO GBP value - ",current_USD_TO_GBP)

    note_label1 = tk.Label(root,font=("arial",11), text="Please select what currecny you're exchanging the money 'from'")
    note_label1.place(x=20,y=35)

    note_label2 = tk.Label(root,font=("arial",11), text="Select what currecny you're exchanging the money 'to'")
    note_label2.place(x=25,y=170)

    enter_label = tk.Label(root,text="Enter the amount: ")
    enter_label.place(x=75,y=122)

    def GBP_TO_CHART():
        # GBP TO EUR 
        plt.subplots_adjust(top)
        plt.plot(last_30_days,last_30_days_GBP_TO_EUR_VALUE)

        #GBP TO AUD
        plt.plot(last_30_days,last_30_days_GBP_TO_AUD_VALUE)

        #GBP TO USD 
        plt.plot(last_30_days,last_30_days_GBP_TO_USD_VALUE)

        #GBP TO JPY
        #plt.plot(last_30_days,last_30_days_GBP_TO_JPY_VALUE)

        plt.xticks(rotation=90)
        blue_patch = mpatches.Patch(color='blue', label='GBP TO EUR')
        green_patch = mpatches.Patch(color='green', label='GBP TO USD')
        orange_patch = mpatches.Patch(color='orange', label='GBP TO AUD')
        plt.xlabel("Dates")
        plt.ylabel("Price")
        plt.legend(handles=[blue_patch,orange_patch,green_patch])
        plt.show()

    def GBP_FROM_CHART():
        # GBP TO EUR 
        plt.plot(last_30_days,last_30_days_EUR_TO_GBP_VALUE)

        #GBP TO AUD
        plt.plot(last_30_days,last_30_days_AUD_TO_GBP_VALUE)

        #GBP TO USD 
        plt.plot(last_30_days,last_30_days_USD_TO_GBP_VALUE)

        #GBP TO JPY
        #plt.plot(last_30_days,last_30_days_GBP_TO_JPY_VALUE)

        plt.xticks(rotation=90)
        blue_patch = mpatches.Patch(color='blue', label='EUR TO GBP')
        green_patch = mpatches.Patch(color='green', label='USD TO GBP')
        orange_patch = mpatches.Patch(color='orange', label='AUD TO GBP')
        plt.legend(handles=[blue_patch,orange_patch,green_patch])
        plt.show()

























    # Transferring from

    #Declaration 
    global GBP_calculation_from
    GBP_calculation_from = False
    global EUR_calculation_from
    EUR_calculation_from = False
    global AUS_calculation_from
    AUS_calculation_from = False
    global JPY_calculation_from
    JPY_calculation_from = False
    global USD_calculation_from
    USD_calculation_from = False

    
    def GBP_flag_from():
        global GBP_calculation_from
        global EUR_calculation_from
        global AUS_calculation_from
        global JPY_calculation_from
        global USD_calculation_from

        GBP_calculation_from = True
        EUR_calculation_from = False
        AUS_calculation_from = False
        JPY_calculation_from = False
        USD_calculation_from = False
        print("after specific (from) button is pressed")
        print("GBP",GBP_calculation_from,"<-")
        print("EUR",EUR_calculation_from)
        print("AUS",AUS_calculation_from)
        print("JPY",JPY_calculation_from)
        print("USD", USD_calculation_from)
        print()
        print()

    def EUR_flag_from():
        global GBP_calculation_from
        global EUR_calculation_from
        global AUS_calculation_from
        global JPY_calculation_from
        global USD_calculation_from

        GBP_calculation_from = False
        EUR_calculation_from = True
        AUS_calculation_from = False
        JPY_calculation_from = False   
        USD_calculation_from = False
        print("after specific (from) button is pressed")
        print("GBP",GBP_calculation_from)
        print("EUR",EUR_calculation_from,"<-")
        print("AUS",AUS_calculation_from)
        print("JPY",JPY_calculation_from)
        print("USD", USD_calculation_from)
        print()
        print()

    def AUS_flag_from():
        global GBP_calculation_from
        global EUR_calculation_from
        global AUS_calculation_from
        global JPY_calculation_from
        global USD_calculation_from

        GBP_calculation_from = False
        EUR_calculation_from = False
        AUS_calculation_from = True
        JPY_calculation_from = False
        USD_calculation_from = False
        print("after specific (from) button is pressed")
        print("GBP",GBP_calculation_from)
        print("EUR",EUR_calculation_from)
        print("AUS",AUS_calculation_from,"<-")
        print("JPY",JPY_calculation_from)
        print("USD", USD_calculation_from)
        print()
        print()

    def JPY_flag_from():
        global GBP_calculation_from
        global EUR_calculation_from
        global AUS_calculation_from
        global JPY_calculation_from
        global USD_calculation_from

        GBP_calculation_from = False
        EUR_calculation_from = False
        AUS_calculation_from = False
        JPY_calculation_from = True
        USD_calculation_from = False
        print("after specific (from) button is pressed")
        print("GBP",GBP_calculation_from)
        print("EUR",EUR_calculation_from)
        print("AUS",AUS_calculation_from)
        print("JPY",JPY_calculation_from,"<-")
        print("USD", USD_calculation_from)
        print()
        print()

    def USD_flag_from():
        global GBP_calculation_from
        global EUR_calculation_from
        global AUS_calculation_from
        global JPY_calculation_from
        global USD_calculation_from

        GBP_calculation_from = False
        EUR_calculation_from = False
        AUS_calculation_from = False
        JPY_calculation_from = False
        USD_calculation_from = True
        print("after specific (from) button is pressed")
        print("GBP",GBP_calculation_from)
        print("EUR",EUR_calculation_from)
        print("AUS",AUS_calculation_from)
        print("JPY",JPY_calculation_from)
        print("USD", USD_calculation_from,"<-")
        print()
        print()

    # Transferring to 

    #Declaration 
    global GBP_calculation_to
    GBP_calculation_to = False
    global EUR_calculation_to
    EUR_calculation_to = False
    global AUS_calculation_to
    AUS_calculation_to = False
    global JPY_calculation_to
    JPY_calculation_to = False
    global USD_calculation_to
    USD_calculation_to = False

    def GBP_flag_to():
        global GBP_calculation_to
        global EUR_calculation_to
        global AUS_calculation_to
        global JPY_calculation_to
        global USD_calculation_to

        GBP_calculation_to = True
        EUR_calculation_to = False
        AUS_calculation_to = False
        JPY_calculation_to = False
        USD_calculation_to = False
        print("after specific (to) button is pressed")
        print("GBP",GBP_calculation_to,"<-")
        print("EUR",EUR_calculation_to)
        print("AUS",AUS_calculation_to)
        print("JPY",JPY_calculation_to)
        print("USD", USD_calculation_to)
        print()
        print()

    def EUR_flag_to():
        global GBP_calculation_to
        global EUR_calculation_to
        global AUS_calculation_to
        global JPY_calculation_to
        global USD_calculation_to

        GBP_calculation_to = False
        EUR_calculation_to = True
        AUS_calculation_to = False
        JPY_calculation_to = False
        USD_calculation_to = False
        print("after specific (to) button is pressed")
        print("GBP",GBP_calculation_to)
        print("EUR",EUR_calculation_to,"<-")
        print("AUS",AUS_calculation_to)
        print("JPY",JPY_calculation_to)
        print("USD", USD_calculation_to)
        print()
        print()

    def AUS_flag_to():
        global GBP_calculation_to
        global EUR_calculation_to
        global AUS_calculation_to
        global JPY_calculation_to
        global USD_calculation_to

        GBP_calculation_to = False
        EUR_calculation_to = False
        AUS_calculation_to = True
        JPY_calculation_to = False
        USD_calculation_to = False
        print("after specific (to) button is pressed")
        print("GBP",GBP_calculation_to)
        print("EUR",EUR_calculation_to)
        print("AUS",AUS_calculation_to,"<-")
        print("JPY",JPY_calculation_to)
        print("USD", USD_calculation_to)
        print()
        print()

    def JPY_flag_to():
        global GBP_calculation_to
        global EUR_calculation_to
        global AUS_calculation_to
        global JPY_calculation_to
        global USD_calculation_to

        GBP_calculation_to = False
        EUR_calculation_to = False
        AUS_calculation_to = False
        JPY_calculation_to = True
        USD_calculation_to = False
        print("after specific (to) button is pressed")
        print("GBP",GBP_calculation_to)
        print("EUR",EUR_calculation_to)
        print("AUS",AUS_calculation_to)
        print("JPY",JPY_calculation_to,"<-")
        print("USD", USD_calculation_to)
        print()
        print()

    def USD_flag_to():
        global GBP_calculation_to
        global EUR_calculation_to
        global AUS_calculation_to
        global JPY_calculation_to
        global USD_calculation_to

        GBP_calculation_to = False
        EUR_calculation_to = False
        AUS_calculation_to = False
        JPY_calculation_to = False
        USD_calculation_to = True
        print("after specific (to) button is pressed")
        print("GBP",GBP_calculation_to)
        print("EUR",EUR_calculation_to)
        print("AUS",AUS_calculation_to)
        print("JPY",JPY_calculation_to)
        print("USD", USD_calculation_to,"<-")
        print()
        print()

    def convert_cur():
        try:
            from_number = float(From_entry.get())

            # GBP TO ALL -------------------------------------------------------------------------------------------------------------------------------------------------------
            #GBP TO EUR
            if GBP_calculation_from == True and EUR_calculation_to == True:
                calculation = from_number * float(current_GPT_TO_EUR)
                cal = round(calculation,2)
                string_cal = str(cal) + " Euros"
                print(string_cal)
                Exchanged_to.config(state="normal")
                Exchanged_to.delete(0, "end")
                Exchanged_to.insert(0,string_cal)
                Exchanged_to.config(state="disabled")

            #EUR TO GBP
            elif EUR_calculation_from == True and GBP_calculation_to == True:
                calculation = from_number * float(current_EUR_TO_GBP)
                cal = round(calculation,2)
                string_cal = str(cal) + " Pounds"
                print(string_cal)
                Exchanged_to.config(state="normal")
                Exchanged_to.delete(0, "end")
                Exchanged_to.insert(0,string_cal)
                Exchanged_to.config(state="disabled")

            #GBP TO AUD
            elif GBP_calculation_from == True and AUS_calculation_to == True:
                calculation = from_number * float(current_GBP_TO_AUS)
                cal = round(calculation,2)
                string_cal = str(cal) + " A-Dollar"
                print(string_cal)
                Exchanged_to.config(state="normal")
                Exchanged_to.delete(0, "end")
                Exchanged_to.insert(0,string_cal)
                Exchanged_to.config(state="disabled")

            #AUD TO GBP
            elif AUS_calculation_from == True and GBP_calculation_to == True:
                calculation = from_number * float(current_AUS_TO_GBP)
                cal = round(calculation,2)
                string_cal = str(cal) + " Pounds"
                print(string_cal)
                Exchanged_to.config(state="normal")
                Exchanged_to.delete(0, "end")
                Exchanged_to.insert(0,string_cal)
                Exchanged_to.config(state="disabled")

            #GBP TO JPY
            elif GBP_calculation_from == True and JPY_calculation_to == True:
                calculation = from_number * float(current_GBP_TO_JPY)
                cal = round(calculation,2)
                string_cal = str(cal) + " J-YEN"
                print(string_cal)
                Exchanged_to.config(state="normal")
                Exchanged_to.delete(0, "end")
                Exchanged_to.insert(0,string_cal)
                Exchanged_to.config(state="disabled")

            #JPY TO GBP
            elif JPY_calculation_from == True and GBP_calculation_to == True:
                calculation = from_number * float(current_JPY_TO_GBP)
                cal = round(calculation,2)
                string_cal = str(cal) + " Pound"
                print(string_cal)
                Exchanged_to.config(state="normal")
                Exchanged_to.delete(0, "end")
                Exchanged_to.insert(0,string_cal)
                Exchanged_to.config(state="disabled")

            #GBP TO USD
            elif GBP_calculation_from == True and USD_calculation_to == True:
                calculation = from_number * float(current_GBP_TO_USD)
                cal = round(calculation,2)
                string_cal = str(cal) + " US Dollars"
                print(string_cal)
                Exchanged_to.config(state="normal")
                Exchanged_to.delete(0, "end")
                Exchanged_to.insert(0,string_cal)
                Exchanged_to.config(state="disabled")

            #USD TO GBP
            elif USD_calculation_from == True and GBP_calculation_to == True:
                calculation = from_number * float(current_USD_TO_GBP)
                cal = round(calculation,2)
                string_cal = str(cal) + " Pounds"
                print(string_cal)
                Exchanged_to.config(state="normal")
                Exchanged_to.delete(0, "end")
                Exchanged_to.insert(0,string_cal)
                Exchanged_to.config(state="disabled")


            # EUR TO ALL -------------------------------------------------------------------------------------------------------------------------------------------------------

        except ValueError:
            Warning_error = tk.Label(root, text=" * Make sure you enter a number in both fields.",fg="Red",font=("arial",12))
            Warning_error.place(x=120,y=410)
            From_entry.delete(0,"end")
            


    #Entry From
    From_entry = tk.Entry(root,font=("arial",15),width=10,justify="center")
    From_entry.place(x=200,y=120)

    #Exchanged To
    Exchanged_to = tk.Entry(root,font=("arial",20),width=15,state="disabled",justify="center")
    Exchanged_to.place(x=175,y=360)

    #Convert button
    Convert_button = tk.Button(root, text="Convert",font=("arial",15),command=convert_cur)
    Convert_button.place(x=220,y=295)
            
    convert_label = tk.Label(root, text="Conversion: ",font=("arial",12))
    convert_label.place(x=80,y=364)

    # (GBP TO) Chart
    GBP_converter_chart = customtkinter.CTkButton(master=root, text="Value of GBP",font=("arial",13),corner_radius=6,border_width=2,width=4,command=GBP_TO_CHART)
    GBP_converter_chart.place(x=500,y=90)

    GBP_FROM_converter_chart  = customtkinter.CTkButton(master=root, text="Value of [USD,AUD,EUR]",font=("arial",13),corner_radius=6,border_width=2,width=4,command=GBP_TO_CHART)
    GBP_FROM_converter_chart.place(x=500,y=140)


    #selection buttons(from)
    GBP_button_from = customtkinter.CTkButton(master=root, text="GBP",font=("arial",13),corner_radius=6,border_width=2,width=4,command=GBP_flag_from)
    GBP_button_from.place(x=125,y=70)
    EUR_button_from = customtkinter.CTkButton(master=root, text="EUR",font=("arial",12),corner_radius=6,border_width=2,width=4,command=EUR_flag_from)
    EUR_button_from.place(x=200,y=70)
    AUS_button_from = customtkinter.CTkButton(master=root, text="AUS",font=("arial",12),corner_radius=6,border_width=2,width=4,command=AUS_flag_from)
    AUS_button_from.place(x=275,y=70)
    JPY_button_from = customtkinter.CTkButton(master=root, text="JPY",font=("arial",12),corner_radius=6,border_width=2,width=4,command=JPY_flag_from)
    JPY_button_from.place(x=350,y=70)
    USD_button_from = customtkinter.CTkButton(master=root, text="USD",font=("arial",12),corner_radius=6,border_width=2,width=4,command=USD_flag_from)
    USD_button_from.place(x=425,y=70)

    #selection buttons(to)
    GBP_button_to = customtkinter.CTkButton(master=root, text="GBP",font=("arial",12),corner_radius=6,border_width=2,width=4,command=GBP_flag_to)
    GBP_button_to.place(x=125,y=210)
    EUR_button_to = customtkinter.CTkButton(master=root, text="EUR",font=("arial",12),corner_radius=6,border_width=2,width=4,command=EUR_flag_to)
    EUR_button_to.place(x=200,y=210)
    AUS_button_to = customtkinter.CTkButton(master=root, text="AUS",font=("arial",12),corner_radius=6,border_width=2,width=4,command=AUS_flag_to)
    AUS_button_to.place(x=275,y=210)
    JPY_button_to = customtkinter.CTkButton(master=root, text="JPY",font=("arial",12),corner_radius=6,border_width=2,width=4,command=JPY_flag_to)
    JPY_button_to.place(x=350,y=210)
    USD_button_to = customtkinter.CTkButton(master=root, text="USD",font=("arial",12),corner_radius=6,border_width=2,width=4,command=USD_flag_to)
    USD_button_to.place(x=425,y=210)
    root.mainloop()

main()
