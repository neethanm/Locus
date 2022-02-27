from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as font
from country_list import countries_for_language
from countryinfo import CountryInfo
from icrawler.builtin import GoogleImageCrawler
import os
from geopy.geocoders import Nominatim

def interface():

    def backcommand():
        root.destroy()
        interface()
    
    def on_click():

        def function1():
            option1.destroy()
            option2.destroy()
            canvas3.destroy()

            def next1_command():
                if val != '' and  val.title() in country_list:

                    nextbutton.destroy()
                    entry.destroy()
                    listbox.destroy()
                    canvas1.delete('all')

                    country = CountryInfo(val)

                    countrylabel = Label(canvas2, text=('COUNTRY: '+val.title()+'\nCAPITAL: '+country.capital()), width=200, height=5, bg='black', fg='white')
                    otherlabel = Label(canvas2, text = 'LANGUAGES:'+(','.join(country.languages())+'\nTIME ZONE: '+(' '.join(country.timezones()))))
                    countrylabel.config(font=("Courier", 30))
                    otherlabel.config(font = ("Courier", 20))
                    countrylabel.pack(side=TOP)
                    otherlabel.pack(side = TOP)


                    google_crawler = GoogleImageCrawler(storage={'root_dir': 'C:\\Users\\91984\\Desktop\\Python_project\\images'})
                    google_crawler.crawl(keyword= 'famous landmarks in '+val, max_num=1)

                    countryimg = None
                    try:
                        countryimg = ImageTk.PhotoImage(Image.open("C:\\Users\\91984\\Desktop\\Python_project\\images\\000001.png"))
                    except:
                        countryimg = ImageTk.PhotoImage(Image.open("C:\\Users\\91984\\Desktop\\Python_project\\images\\000001.jpg"))
                    mylabel = Label(canvas1)
                    canvas1.create_image(400, 400, anchor = CENTER, image = countryimg)

                    try:
                        os.remove("C:\\Users\\91984\\Desktop\\Python_project\\images\\000001.png")
                    except:
                        os.remove("C:\\Users\\91984\\Desktop\\Python_project\\images\\000001.jpg")

                    root.mainloop()                 

            country_list = []
            countries = dict(countries_for_language('en'))
            for i in countries.values(): 
                country_list.append(i)

            def Scankey(event):
                
                global val
                val = event.widget.get()
                print(val)

                if val == '':
                    data = country_list
                else:
                    data = []
                    for item in country_list:
                        if val.lower() in item.lower():
                            data.append(item)

                Update(data)

            def Update(data):

                listbox.delete(0,'end')

                for item in data:
                    listbox.insert('end', item)

            entry = Entry(canvas2, width = 140)
            entry.pack()
            entry.bind('<KeyRelease>', Scankey)

            listbox = Listbox(canvas2, width = 140)
            listbox.pack()
            Update(country_list)

            nextbutton = Button(canvas2, text='NEXT', height = 3, width = 10, bg = 'green', fg = 'white', command = next1_command)
            nextbutton.pack(side = TOP)

           
        def function2():
            option1.destroy()
            option2.destroy()
            canvas3.destroy()

            def getinfo():
                geolocator = Nominatim(user_agent = "geoapiExercises")
                place = e.get()
                place_res.set(place)
                location = geolocator.geocode(place)
                res.set(location)

            place_res = StringVar();
            res= StringVar();

            basecanvas = Canvas(canvas2, bg = 'grey', width = 800, height = 800)

            basecanvas.pack()
            
            Label(basecanvas, text = "Enter place :" ,bg = "light grey", width = 15, height = 5, borderwidth=2, relief = "groove").grid(row = 0, sticky = W)
            Label(basecanvas, text = "Place :", bg = "light grey", width = 15, height = 5, borderwidth=2, relief = "groove").grid(row = 1, sticky = W)
            Label(basecanvas, text = "Country Address :", bg = "light grey", width = 15, height = 5, borderwidth=2, relief = "groove").grid(row = 2, sticky = W)

            Label(basecanvas, text = "", textvariable = place_res, bg = "light grey", width = 85, height = 5, relief = "groove").grid(row = 1, column = 1, sticky = W)
            Label(basecanvas, text = "", textvariable = res, bg = "light grey", width = 85, height = 5, relief = "groove").grid(row = 2, column = 1, sticky = W)

            e = Entry(basecanvas, width = 85)
            e.grid(row = 0, column = 1)

            b = Button(basecanvas, text = "Show", command = getinfo)
            b.grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 5,pady = 5)

            root.mainloop()
           
        canvas3.destroy()
        label.destroy()

        buttonfont = font.Font(family='Helvetica', size=16, weight='bold')

        option1 = Button(canvas2, text='SEARCH BY COUNTRY NAME', width=100, height=10, font=buttonfont, command=function1, relief = "groove")
        option1.pack()
        option2 = Button(canvas2, text='ADDRESS', width=100, height=10, font=buttonfont, command=function2, relief = "groove")
        option2.pack()

    root = Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()

    welcome_text = """Welcome to Locus!!!

    The Program has two modes of execution.
    1. Takes in country name from the user, displays capital and other details.
    2. Takes any place name on earth and displays the approximate address.
    
    To know more click NEXT"""

    root.attributes('-fullscreen', True)
    root.title('LOCUS')
    root.resizable(width = False, height = False)

    canvas1 = Canvas(root, width = w/2, height = h, bg = 'black')
    canvas2 = Canvas(root, width = w/2, height = h)
    canvas3 = Canvas(canvas2, width = w/2, height = h/8)
    canvas4 = Canvas(canvas2, width = 10, height = 3)

    img = ImageTk.PhotoImage(Image.open("earth.png"))
    canvas1.create_image(400, 400, anchor = CENTER, image = img)

    label = Label(canvas2, text = welcome_text, height = 50, width = 100, font = 'Times')

    nextbutton = Button(canvas3, text = 'NEXT', height = 3, width = 10, bg = 'black', fg = 'white', font = 'Aharoni', command = on_click)
    nextbutton.pack(side = LEFT)

    quitbutton = Button(canvas4, text = 'QUIT', height = 3, width = 10, bg = 'red', fg = 'white', command = quit)
    quitbutton.pack(side = RIGHT)

    backbutton = Button(canvas4, text = 'BACK', height = 3, width = 10, bg = 'blue', fg = 'white', command = backcommand)
    backbutton.pack(side = RIGHT)

    canvas1.pack(side = LEFT)
    canvas2.pack(side = RIGHT)
    canvas3.pack(side = BOTTOM)
    canvas4.pack(side = TOP)
    label.pack()

    root.mainloop()

interface()