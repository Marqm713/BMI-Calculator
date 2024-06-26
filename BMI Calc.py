from customtkinter import *
class BMICalc:
    def __init__(self):
        window = CTk()

        # Appearance
        set_appearance_mode("dark")
        window.title("Studio Super: BMI Calculator")


        # Label Questions
        label1 = CTkLabel(window, text = "Enter your current height (inches): ").grid(row = 2, column = 1, sticky = W)
        label2 = CTkLabel(window, text = "Enter your current weight (pounds): ").grid(row = 3, column = 1, sticky = W)
        label3 = CTkLabel(window, text = "Your current BMI is: ").grid(row = 4, column = 1, sticky = W)


        # Entry Boxes
        self.heightVar = StringVar()
        CTkEntry(window, textvariable=self.heightVar, fg_color="#663366", justify=RIGHT).grid(row=2, column=2,sticky=E)
        self.weightVar = StringVar()
        CTkEntry(window, textvariable=self.weightVar, fg_color="#663366", justify=RIGHT).grid(row=3, column=2, sticky=E)


        # Label Total Display
        self.totalVar = StringVar()
        lbltotalVar = CTkLabel(window, font=("Roboto", 20), textvariable = self.totalVar).grid(row = 4, column = 2, sticky = E)


        # Compute BMI Buttons 
        btComputeBMI = CTkButton(window, text = "Compute US BMI (imperial)", font=("Roboto", 14), fg_color="#330066", 
                                 hover_color= "#6A5ACD", command = self.getUSBMI).grid( row = 6, column = 2, sticky = E,) #HC SLATE BLUE/ FG PURPLE
        metriccomputeBMI = CTkButton(window, text = "Compute BMI (metric)", font=("Roboto", 14), fg_color="#330066", 
                                 hover_color= "#6A5ACD", command = self.getUKBMI).grid( row = 6, column = 1, sticky = W)#HC SLATE BLUE/ FG PURPLE


        window.mainloop()


        # Metric System formula
    def getUKBMI(self):
        try:
            weight = float(self.weightVar.get())
            height = float(self.heightVar.get())
            height =  (height[0] * 12 + height[2])
            totalVar = weight / height ** 2
            self.totalVar.set(f"{totalVar: 10.2f}")
        except ValueError:
            self.totalVar.set("Invalid input")

        # Imperial System Formula
    def getUSBMI(self):
        try:
            weight = float(self.weightVar.get())
            height = float(self.heightVar.get()) 
            totalVar = (weight / ((height[0] * 12 + height[2]) ** 2)) * 703
            self.totalVar.set(f"{totalVar: 10.2f}")
        except ValueError:
            self.totalVar.set("Invalid input")



BMICalc()
