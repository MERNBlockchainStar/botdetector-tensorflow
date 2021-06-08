"""Author: Nagabhushan S Baddi (InStep Intern)\nOrganization: Infosys Ltd.\nGUI app (module) to detect botnet traffic using Machine Learning"""

#import the modules
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import dataset_load as dload
import models
import threading
import time
import os
import pickle
from tkinter.filedialog import askopenfilename
import testfunction
import numpy as np

#load data set


def callSuitable( v2, scenario ):
    """use and evaluate the selected Machine Learning algorithm"""
    
    #load data set
    scenario_filename = scenario.get()
    _name = scenario_filename.split('.')
    pickle_path = '../pickle/' + _name[0] + ".pickle"
    print(pickle_path)
    print(os.path.exists(pickle_path))
    if not os.path.exists(pickle_path):
        print("data loading .....")
        v2.set("data loading ....")
        X, Y, XT, YT = dload.loaddata(scenario_filename)
        print("finished data loading")
        v2.set("finished data loading")
    else:
        file = open(pickle_path, 'rb')
        sd = pickle.load(file)
        X, Y, XT, YT = sd[0] , sd[1] , sd[2], sd[3]

    _name = scenario_filename.split('.')
    if scenario_filename != "":
        print("start training...")
        v2.set("start training")
        model = models.ANNModel(X, Y, XT, YT, v2, _name[0])
        model.start()
    else:
        messagebox.showwarning(title="warning", message="select netflow file in datasets diretory, no other directory")

def test( v2, scenario ):
    """use and evaluate the selected Machine Learning algorithm"""
    
    #load data set
    scenario_filename = scenario.get()
    _name = scenario_filename.split('.')
    pickle_path = '../pickle/' + _name[0] + ".pickle"
    file = open(pickle_path, 'rb')
    sd = pickle.load(file)
    X, Y = sd[0] , sd[1] 

    if scenario_filename != "":
        print("start testing...")
        v2.set("start testing")
        _in_data = testfunction.get_result_models(X[:2500])
        pred = testfunction.predict(_in_data)
        print(pred)
        print(Y[:2500])
        _sum = np.equal(pred, Y[:2500])
        acc = np.sum(_sum) * 100/2500
        print(acc)
        v2.set("test accuracy: %.2f" % (acc)+" %")
    else:
        messagebox.showwarning(title="warning", message="select netflow file in datasets diretory, no other directory")


if __name__ == "__main__":
    #code for the GUI
    root = Tk()
    root.title('GUI to train and save model')
    root.resizable(width=False, height=False)

    frame1 = Frame(root, padding=(0, 0, 0, 0), width=300)

    label = Label(frame1, text='Dataset File:\n(.binetflow file)')
    label.grid(row=0, column=0, rowspan=1, columnspan=1, padx=10, pady=10, sticky=(W, E))

    v = StringVar(frame1, value='')
    entry = Entry(frame1, textvariable = v)
    entry.grid(row=0, column=1, rowspan=1, columnspan=1, padx=10, pady=10, sticky=(W, E))

    button = Button(frame1, text='Browse')
    button.bind('<1>', lambda e: v.set(askopenfilename().split('/')[-1]))
    button.grid(row=0, column=2, rowspan=1, columnspan=1, padx = 10, pady=10)


    v2 = StringVar(frame1, value='Accuracy: ')
    resultLabel = Label(frame1, textvariable=v2)

    calButton = Button(frame1, text='Train')
    calButton.bind('<1>', lambda e: callSuitable(v2, v))
    calButton.grid(row=1, column=2, sticky = (S, W), padx=10, pady=10)

    testButton = Button(frame1, text='Test')
    testButton.bind('<1>', lambda e: test(v2, v))
    testButton.grid(row=2, column=2, sticky = (S, W), padx=10, pady=10)

    resultLabel.grid(row=2, pady=10, padx=10, columnspan=3, sticky=(W, ))

    frame1.grid()

    #run the GUI
    root.mainloop()
