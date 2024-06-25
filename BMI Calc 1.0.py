from tkinter import *




class BMICalc:
    def __init__(self):
        ## WINDOW ##
        window = Tk()
        window.title("Studio Super: BMI Calculator")


        ## LEFT-SIDE LABELS ##
        Label(window, text = "Enter your current height in inches: ").grid(row = 1, column = 1, sticky = W)
        Label(window, text = "Enter your current weight in pounds: ").grid(row = 2, column = 1, sticky = W)
        Label(window, text = "Your current BMI is: ").grid(row = 3, column = 1, sticky = W)


        ## RIGHT-SIDE ENTRY BOXES ##
        self.heightVar = IntVar()
        Entry(window, textvariable = self.heightVar, justify = RIGHT).grid(row = 1, column = 2)
        self.weightVar = IntVar()
        Entry(window, textvariable = self.weightVar, justify = RIGHT).grid(row = 2, column = 2)


        ## RIGHT-SIDE LABEL ##
        self.totalVar = StringVar()
        lbltotalVar = Label(window, textvariable = self.totalVar).grid(row = 3, column = 2, sticky = E)


        ## BMI BUTTON **
        btComputeBMI = Button(window, text = "Compute BMI", command = self.getBMI).grid( row = 6, column = 2, sticky = E)




        window.mainloop()


        ## BMI FORMULA ##
    def getBMI(self):
        weight = (self.weightVar.get())
        height = (self.heightVar.get())
        totalVar = (float(weight) / float(height) ** 2) * 703
        self.totalVar.set(f"{totalVar: 10.2f}")
       
        return totalVar;
BMICalc()
