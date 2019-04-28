#!/usr/bin/python3
"""
https://docs.python.org/3/library/tkinter.html
https://likegeeks.com/python-gui-examples-tkinter-tutorial/
"""
import tkinter as tk
import tkinter.scrolledtext

STARTING_PAIRS_TUPLE = ("(0, 1) - Trivial", "(13/84, 55/84) - Bourgain", "(9/56, 37/56) - Bombieri and Iwaniec", "(89/560, 369/560) - Watt")




#################################################
# Methods
#################################################
def searchPairs():
    """
    thetaInput is defined below as the ScrolledText where the user types the theta functions
    """
    thetaInputContents = thetaInput.get("1.0", tk.END)
    print(thetaInputContents)


#################################################
# Script start
#################################################
#setup the window
window = tk.Tk()
window.title("pairsearch: Exponent pair searcher")
window.geometry("600x500")

#add the instructions and the textbox
instructionLabel = tk.Label(window, text="Minimize the maximum of\nthe following theta functions:", font=("Arial", 12), justify=tk.LEFT)
instructionLabel.grid(row=0, column=0, sticky=tk.W)
thetaInput = tkinter.scrolledtext.ScrolledText(window, height=10, width=20, font=("consolas", 12)) 
thetaInput.grid(row=1, column=0)

#add the descriptive label
thetaText = "Each line in the box\ncorresponds to a \u03b8 function\n\n\u03b8(k,l) = (ak + bl + c)/(dk + el + f)\ncorresponds to the line\na,b,c,d,e,f"
thetaLabel = tk.Label(window, text=thetaText, font=("Arial", 12), justify=tk.LEFT)
thetaLabel.grid(row=0, column=1, rowspan=2, columnspan=2)

#add the number of operations label/spinner
processCountFrame = tk.Frame(window)
processCountFrame.grid(row=3, column=0, columnspan=2, sticky=tk.W)
processCountLabel = tk.Label(processCountFrame, text="Max number of A/B steps: ", font=("Arial", 12), justify=tk.LEFT)
processCountLabel.grid(row=0, column=0)
processCountSpinner = tk.Spinbox(processCountFrame, from_=1, to_=100, width=3)
processCountSpinner.grid(row=0, column=1)
#PIZZA - default to 5

#select starting pair from dropdown?
startPairFrame = tk.Frame(window)
startPairFrame.grid(row=4, column=0, columnspan=2, sticky=tk.W)
startPairLabel = tk.Label(startPairFrame, text="Starting pair: ", font=("Arial", 12), justify=tk.LEFT)
startPairLabel.grid(row=0, column=0)
startPairVariable = tk.StringVar()
startPairVariable.set(STARTING_PAIRS_TUPLE[0])
startPairDropdown = tk.OptionMenu(startPairFrame, startPairVariable, *STARTING_PAIRS_TUPLE)
startPairDropdown.grid(row=0, column=1)

#add the run button
runButton = tk.Button(window, text="Run", font=("Arial", 12), command=searchPairs)
runButton.grid(row=5, column=0)

#start the gui
window.mainloop()
