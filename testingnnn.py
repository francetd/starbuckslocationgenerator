import tkinter
import tkinter.messagebox
import pandas as pd
import tkinter.ttk

root = tkinter.Tk()
root.configure(bg = "dark green")
root.title(" Starbucks Location Generator")


#first button that looks through starbucks.csv file
def findloc():
    """Looks through starbucks location csv file and generates nearby locations in a separate locations.csv file.  """
    #global call out boxes outside function 
    global root,country_box, city_box, state_box, zip_box
    
    
    #messagebox appears when user does not enter in any info in entry box
    if len(city_box.get())==0:
        tkinter.messagebox.showwarning("Unable to find Location", "Please make sure that you inputted all the correct information.")
    elif len(country_box.get()) == 0:
        tkinter.messagebox.showwarning("Unable to find Location", "Please make sure that you inputted all the correct information.")
    elif len(state_box.get()) == 0:
        tkinter.messagebox.showwarning("Unable to find Location", "Please make sure that you inputted all the correct information.")
    elif len(zip_box.get()) ==0:
        tkinter.messagebox.showwarning("Unable to find Location", "Please make sure that you inputted all the  correct information.")
    
    #reads directory.csv file, looks through if the location information is in directory.csv, writes all information in a seperate csv file.  
    else:
        df = pd.read_csv("directory.csv") #.lower for case sensitivity, along with .get to get string from outside 
        df1= df[df['State/Province'].str.lower().str.contains(state_box.get().lower()) & df['Country'].str.lower().str.contains(country_box.get().lower())& df['City'].str.lower().str.contains(city_box.get().lower()) & df['Postcode'].str.lower().str.contains(zip_box.get().lower())]
        if not df1.empty:
            df1.to_csv("locations.csv", index=False)
            tkinter.messagebox.showinfo(" Process Completed", "All collected information on nearby locations are printed on locations.csv")
    #end's function after user is finished using the button.
            country_box.delete(0, tkinter.END)
            city_box.delete(0, tkinter.END)
            state_box.delete(0, tkinter.END)
            zip_box.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning("Warning!", "Could not find location information.Make sure that the information you provided is accurate.")

#simplifies list already created through the "Find Nearby Locations" and simplifies any information so it's more readable
def simplified_list():
    #global calling out boxes outside of function
    global root, country_box, city_box, state_box,zip_box
    
    """Takes information from the starbucks.csv and simplifies info to another csv file.""" 
    if len(city_box.get())==0:
        tkinter.messagebox.showwarning("Unable to find Location", "Please make sure that you inputted all the correct information.")
    elif len(country_box.get()) == 0:
        tkinter.messagebox.showwarning("Unable to find Location", "Please make sure that you inputted all the correct information.")
    elif len(state_box.get()) == 0:
        tkinter.messagebox.showwarning("Unable to find Location", "Please make sure that you inputted all the correct information.")
    elif len(zip_box.get()) ==0:
        tkinter.messagebox.showwarning("Unable to find Location", "Please make sure that you inputted all the  correct information.")
    else:
        df = pd.read_csv("starbucks.csv")
        df2= df[df['State/Province'].str.lower().str.contains(state_box.get().lower()) & df['Country'].str.lower().str.contains(country_box.get().lower())& df['City'].str.lower().str.contains(city_box.get().lower()) & df['Postcode'].str.lower().str.contains(zip_box.get().lower())]
        if not df2.empty:#checks to see if the csv file is empty and if it isnt it runs this function
            final_df = df2[['Store Name','Postcode', 'Street Address', 'City','State/Province','Country', 'Phone Number']]
            final_df.to_csv("simplified_locations.csv", index=False)#prints to seperate csv file
            tkinter.messagebox.showinfo(" Process Completed", "All collected information on nearby locations are printed on simplified_locations.csv")
            #end's function after user is finished using the button.
            country_box.delete(0, tkinter.END)
            city_box.delete(0, tkinter.END)
            state_box.delete(0, tkinter.END)
            zip_box.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning("Warning!", "Could not load  nearby location informations. Make sure that you have all the correct information. ") 


def directions(): #button showcases a messagebox and it's directions on how to use this  
    """Showcases the user how to work this generator."""
    tkinter.messagebox.showinfo("Welcome!", "To use this generator, click first on the 'Find Nearby Locations' button after inputting information on the entry boxes above to view nearby Starbucks locations. Then, click on the second button 'Simplify Location Information' if you just want a the address along with the phone number of the locations. You may also rate our generator and use our exit button to end this window.")   


def label_hover(event): #hovers over directions button 
    """Hovers over directions button for more information on what it does."""
    global root
    new_label = tkinter.Label(root, text = "Click on button for directions on how to use this system")
    new_label.configure(bg = "beige", fg = "black")
    new_label.configure(font = "Arial 8 bold")
    new_label.grid(row = 0, column = 6)
       
def endgui():#allows user to end whole system
    """Quits the whole GUI window button when user is done. """
    tkinter.messagebox.showinfo("Goodbye", "Thank you for using the Starbucks Generator!")
    root.destroy()

def rate():#user can rate the system based on a combobox and dropdown window
    """Allows the user to rate the system."""
    tkinter.messagebox.showinfo("Thank you!", "Thank you for rating us! Rating recieved.")
    
    
#basic GUI set up
title_label = tkinter.Label(root, text = "Starbucks Location Generator")
title_label.configure( font = "didot 20 bold ", bg = "dark green", fg = "white")

title_label.grid(row = 0, column = 3)

#labels 
country_label = tkinter.Label(root, text = "Country(Abbreviated)")
country_label.grid(row = 1, column = 1)
country_label.configure(bg = "dark green", fg ="white")

state_label = tkinter.Label(root, text = "State (Abbreviated)")
state_label.grid(row = 1, column = 3)
state_label.configure(bg = "dark green", fg ="white")

city_label = tkinter.Label(root, text = "City")
city_label.grid(row = 2, column = 1)
city_label.configure(bg = "dark green", fg ="white")

zip_label = tkinter.Label(root, text = "ZIP Code")
zip_label.grid(row = 2, column = 3)
zip_label.configure(bg = "dark green", fg ="white")



#entry boxes for each label
country_box = tkinter.Entry(root, width = 10)
country_box.grid(row = 1, column = 2)


state_box = tkinter.Entry(root, width = 10)
state_box.grid(row = 1, column = 4)


city_box= tkinter.Entry(root, width = 10)
city_box.grid(row = 2, column = 2)


zip_box= tkinter.Entry(root, width = 10)
zip_box.grid(row = 2, column = 4)

#all buttons for user to use
find_button = tkinter.Button(root, text = " Find Nearby Locations", command = findloc)
find_button.grid(row = 3, column = 2)


simplify_button = tkinter.Button(root, text = " Simplify Location Informations", command = simplified_list)
simplify_button.grid(row = 3, column = 4)


rate_button = tkinter.Button(root, text = " Rate Generator", command = rate)
rate_button.grid(row = 3, column = 3 )


exit_button = tkinter.Button(root, text = "Exit", command = endgui)
exit_button.grid(row = 2, column = 5)
exit_button.configure(bg = "dark green")

dir_button = tkinter.Button(root, text = "Directions", command = directions)
dir_button.grid(row = 1, column = 5)
dir_button.bind("<Enter>", label_hover)

#combobox for rating
rating_box = tkinter.ttk.Combobox(root, values = ["1", "2", "3", "4", "5"], state = "readonly")
rating_box.current(0)
rating_box.grid(row = 4 , column = 3)


root.mainloop()
