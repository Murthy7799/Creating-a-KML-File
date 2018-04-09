import simplekml
import pandas
import tkinter
from tkinter.filedialog import askopenfilename

"""kml=simplekml.Kml()
kml.newpoint(name="sample",coords=[(20.593684,78.96288000000004)])
kml.save("C:\\Users\\murthy\\Pictures\\Screenshots\\points.kml")"""

"""def samplekml(longitude,latitude):
    L=longitude
    LA=latitude
    kml=simplekml.Kml()
    kml.newpoint(name="sample",coords=[(L,LA)])
    kml.save("C:\\Users\\murthy\\Pictures\\Screenshots\\Graph.kml")
L=input("Please Enter the Longitude range: ")
LA=input("Please Enter the Latitude Range: ")
samplekml(L,LA)"""

def browse():
    global infile
    infile=askopenfilename()

def kmlFunction(outfile="C:\\Users\\murthy\\Pictures\\Screenshots\\points1.kml"):
    df=pandas.read_csv(infile)
    kml=simplekml.Kml()
    for lon,lat in zip(df["Longitude"],df["Latitude"]):
        kml.newpoint(coords=[(lon,lat)])
    kml.save(outfile)

root=tkinter.Tk() #here tkinter is used to create graphical user interface and its the root method
root.title("Kml Generator")
label=tkinter.Label(root,text="This program generates kml file")
label.pack()
browseButton=tkinter.Button(root,text="Browse",command=browse)
browseButton.pack()
kmlButton=tkinter.Button(root,text="Generate KML",command=kmlFunction)
kmlButton.pack()
root.mainloop()   #here main is the main loop for the window of the gui and the code we write should be in b/w root method nad mainloop
                  #if write out side the loop it will not apply to the window.




