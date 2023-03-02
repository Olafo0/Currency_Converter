import tkinter as tk
import csv

def main():
    root = tk.Tk()
    root.geometry("500x500")

    #Reading the database
    file = open("Task3_data.csv","r")
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




    note_label1 = tk.Label(root,font=("arial",12), text="Select what currecny you're transferring the money 'from'")
    note_label1.place(x=95,y=35)

    note_label2 = tk.Label(root,font=("arial",12), text="Select what currecny you're transferring the money 'to'")
    note_label2.place(x=95,y=170)


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
    
    def GBP_flag_from():
        global GBP_calculation_from
        global EUR_calculation_from
        global AUS_calculation_from
        global JPY_calculation_from

        GBP_calculation_from = True
        EUR_calculation_from = False
        AUS_calculation_from = False
        JPY_calculation_from = False
        print("after specific (from) button is pressed")
        print("GBP",GBP_calculation_from,"<-")
        print("EUR",EUR_calculation_from)
        print("AUS",AUS_calculation_from)
        print("JPY",JPY_calculation_from)
        print()
        print()

    def EUR_flag_from():
        global GBP_calculation_from
        global EUR_calculation_from
        global AUS_calculation_from
        global JPY_calculation_from

        GBP_calculation_from = False
        EUR_calculation_from = True
        AUS_calculation_from = False
        JPY_calculation_from = False     
        print("after specific (from) button is pressed")
        print("GBP",GBP_calculation_from)
        print("EUR",EUR_calculation_from,"<-")
        print("AUS",AUS_calculation_from)
        print("JPY",JPY_calculation_from)
        print()
        print()

    def AUS_flag_from():
        global GBP_calculation_from
        global EUR_calculation_from
        global AUS_calculation_from
        global JPY_calculation_from

        GBP_calculation_from = False
        EUR_calculation_from = False
        AUS_calculation_from = True
        JPY_calculation_from = False
        print("after specific (from) button is pressed")
        print("GBP",GBP_calculation_from)
        print("EUR",EUR_calculation_from)
        print("AUS",AUS_calculation_from,"<-")
        print("JPY",JPY_calculation_from)
        print()
        print()

    def JPY_flag_from():
        global GBP_calculation_from
        global EUR_calculation_from
        global AUS_calculation_from
        global JPY_calculation_from

        GBP_calculation_from = False
        EUR_calculation_from = False
        AUS_calculation_from = False
        JPY_calculation_from = True
        print("after specific (from) button is pressed")
        print("GBP",GBP_calculation_from)
        print("EUR",EUR_calculation_from)
        print("AUS",AUS_calculation_from)
        print("JPY",JPY_calculation_from,"<-")
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
    
    def GBP_flag_to():
        global GBP_calculation_to
        global EUR_calculation_to
        global AUS_calculation_to
        global JPY_calculation_to

        GBP_calculation_to = True
        EUR_calculation_to = False
        AUS_calculation_to = False
        JPY_calculation_to = False
        print("after specific (to) button is pressed")
        print("GBP",GBP_calculation_to,"<-")
        print("EUR",EUR_calculation_to)
        print("AUS",AUS_calculation_to)
        print("JPY",JPY_calculation_to)
        print()
        print()

    def EUR_flag_to():
        global GBP_calculation_to
        global EUR_calculation_to
        global AUS_calculation_to
        global JPY_calculation_to

        GBP_calculation_to = False
        EUR_calculation_to = True
        AUS_calculation_to = False
        JPY_calculation_to = False
        print("after specific (to) button is pressed")
        print("GBP",GBP_calculation_to)
        print("EUR",EUR_calculation_to,"<-")
        print("AUS",AUS_calculation_to)
        print("JPY",JPY_calculation_to)
        print()
        print()

    def AUS_flag_to():
        global GBP_calculation_to
        global EUR_calculation_to
        global AUS_calculation_to
        global JPY_calculation_to

        GBP_calculation_to = False
        EUR_calculation_to = False
        AUS_calculation_to = True
        JPY_calculation_to = False
        print("after specific (to) button is pressed")
        print("GBP",GBP_calculation_to)
        print("EUR",EUR_calculation_to)
        print("AUS",AUS_calculation_to,"<-")
        print("JPY",JPY_calculation_to)
        print()
        print()

    def JPY_flag_to():
        global GBP_calculation_to
        global EUR_calculation_to
        global AUS_calculation_to
        global JPY_calculation_to

        GBP_calculation_to = False
        EUR_calculation_to = False
        AUS_calculation_to = False
        JPY_calculation_to = True
        print("after specific (to) button is pressed")
        print("GBP",GBP_calculation_to)
        print("EUR",EUR_calculation_to)
        print("AUS",AUS_calculation_to)
        print("JPY",JPY_calculation_to,"<-")
        print()
        print()

    def convert_cur():
        try:
            from_number = float(From_entry.get())
            print(from_number)
        except ValueError:
            Warning_error = tk.Label(root, text="Make sure you enter a number in both fields.",fg="Red",font=("arial",12))
            Warning_error.place(x=120,y=410)
            From_entry.delete(0,"end")


            if GBP_calculation_from == True and EURAUS_calculation_to:
                print("")

    #Entry From
    From_entry = tk.Entry(root)
    From_entry.place(x=200,y=120)

    #Exchanged To
    Exchanged_to = tk.Entry(root)
    Exchanged_to.place(x=200,y=360)

    #Convert button
    Convert_button = tk.Button(root, text="Convert",font=("arial",15),command=convert_cur)
    Convert_button.place(x=220,y=295)

    #selection buttons(from)
    GBP_button_from = tk.Button(root, text="GBP",font=("arial",12),command=GBP_flag_from)
    GBP_button_from.place(x=125,y=70)
    EUR_button_from = tk.Button(root, text="EUR",font=("arial",12),command=EUR_flag_from)
    EUR_button_from.place(x=200,y=70)
    AUS_button_from = tk.Button(root, text="AUS",font=("arial",12),command=AUS_flag_from)
    AUS_button_from.place(x=275,y=70)
    JPY_button_from = tk.Button(root, text="JPY",font=("arial",12),command=JPY_flag_from)
    JPY_button_from.place(x=350,y=70)

    #selection buttons(to)
    GBP_button_to = tk.Button(root, text="GBP",font=("arial",12),command=GBP_flag_to)
    GBP_button_to.place(x=125,y=210)
    EUR_button_to = tk.Button(root, text="EUR",font=("arial",12),command=EUR_flag_to)
    EUR_button_to.place(x=200,y=210)
    AUS_button_to = tk.Button(root, text="AUS",font=("arial",12),command=AUS_flag_to)
    AUS_button_to.place(x=275,y=210)
    JPY_button_to = tk.Button(root, text="JPY",font=("arial",12),command=JPY_flag_to)
    JPY_button_to.place(x=350,y=210)

    root.mainloop()

main()
