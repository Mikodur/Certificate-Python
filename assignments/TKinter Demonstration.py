import tkinter as tk
from tkinter import ttk

class DataForm(tk.Frame):#Creates and places labels, buttons and entry fields on the application.
    def __init__(self, parent):
        super().__init__(parent)
        recordinfo = tk.LabelFrame(self, text="Enter Calculations")
        recordinfo.grid(row=0, column=0)
        self.ExposureValueLabel = ttk.Label(recordinfo, text = "Enter EXPOSURE VALUE")
        self.ExposureValueLabel.grid(row=0, column=0)
        self.ExposureValue = ttk.Entry(recordinfo, text = tk.IntVar)
        self.ExposureValue.grid(row=0, column=1)
        self.AssetValueLabel = ttk.Label(recordinfo, text = "Enter ASSET VALUE")
        self.AssetValueLabel.grid(row=1, column=0)
        self.AssetValue = ttk.Entry(recordinfo, text = tk.IntVar)
        self.AssetValue.grid(row=1, column=1)
        self.ROCLabel = ttk.Label(recordinfo, text = "Enter annualised RATE OF OCCURANCE")    
        self.ROCLabel.grid(row=2, column=0)
        self.ROC = ttk.Entry(recordinfo, text = tk.IntVar)
        self.ROC.grid(row=2, column=1)
        buttonfr = tk.LabelFrame(self)
        buttonfr.grid(row=0, column=1)
        self.ca_button = ttk.Button(buttonfr, text="Calc", command = self.Calc)
        self.ca_button.grid(row=0, column=0)
        self.ch_button = ttk.Button(buttonfr, text="Clear", command = self.Clear)
        self.ch_button.grid(row=1, column=0)
        self.qu_button = ttk.Button(buttonfr, text ="Quit", command = exit)
        self.qu_button.grid(row=2, column=0)
        self.SLE = tk.Label(self, text = "SLE is 0")
        self.SLE.grid(row=3, column=0)
        self.ALE = tk.Label(self, text = "ALE is 0")
        self.ALE.grid(row=4, column=0)

    def Calc(self): #Creates the mathematics involved and changes the labels on the application to the new correct value.
        SLEMaths = (float(self.ExposureValue.get()) * float(self.AssetValue.get()))
        self.SLE.configure(text = "SLE is {}".format(float(SLEMaths)))
        ALEMaths = (float(SLEMaths) * float(self.ROC.get()))
        self.ALE.configure(text = "ALE is {}".format(float(ALEMaths)))
        
    def Clear(self): #Sets all entry and result fields back to null.
        self.ExposureValue.delete(0, 'end')
        self.AssetValue.delete(0, 'end')
        self.ROC.delete(0, 'end')
        self.ALE.configure(text = "ALE is 0")
        self.SLE.configure(text = "SLE is 0")

class Application(tk.Tk): #Creates and displays the application window in which to display the calculator app on.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Python Assessment 1")
        DataForm(self).grid(sticky = (tk.N + tk.E + tk.S + tk.W))
if __name__ == '__main__':
    app=Application()
    app.mainloop()
