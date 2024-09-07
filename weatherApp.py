from tkinter import *
from tkinter import ttk
import requests

def data_get():
  city = city_name.get()
  data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
  w_label1.config(text=data["weather"][0]["main"])
  wd_label1.config(text=str(data["weather"][0]["description"]).capitalize())
  temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
  pre_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Weather App")
win.config(bg = "light blue")
win.geometry("500x500")

name_label = Label(win, text="WEATHER APP", font=("Trip Sans", 30, "bold"), background="light blue")
name_label.place(x=25, y=30, height=50, width=450)

list_name =  ["Ahmadpur East",
    "Ahmed Nager Chatha",
    "Ali Khan Abad",
    "Alipur",
    "Arifwala",
    "Attock",
    "Bhera",
    "Bhalwal",
    "Bahawalnagar",
    "Bahawalpur",
    "Bhakkar",
    "Burewala",
    "Chenab Nagar",
    "Chillianwala",
    "Choa Saidanshah",
    "Chakwal",
    "Chak Jhumra",
    "Chichawatni",
    "Chiniot",
    "Chishtian",
    "Chunian",
    "Dajkot",
    "Daska",
    "Davispur",
    "Darya Khan",
    "Dera Ghazi Khan",
    "Dhaular",
    "Dina",
    "Dinga",
    "Dhudial Chakwal",
    "Dipalpur",
    "Faisalabad",
    "Fateh Jang",
    "Ghakhar Mandi",
    "Gojra",
    "Gujranwala",
    "Gujrat",
    "Gujar Khan",
    "Harappa",
    "Hafizabad",
    "Haroonabad",
    "Hasilpur",
    "Haveli Lakha",
    "Islamabad",
    "Jalalpur Jattan",
    "Jampur",
    "Jaranwala",
    "Jhang",
    "Jhelum",
    "Jauharabad",
    "Kallar Syedan",
    "Kalabagh",
    "Karor Lal Esan",
    "Karachi",
    "Kasur",
    "Kamalia",
    "Kāmoke",
    "Khanewal",
    "Khanpur",
    "Khanqah Sharif",
    "Kharian",
    "Khushab",
    "Kot Adu",
    "Lahore",
    "Lalamusa",
    "Layyah",
    "Lawa Chakwal",
    "Liaquat Pur",
    "Lodhran",
    "Malakwal",
    "Mamoori",
    "Mailsi",
    "Mandi Bahauddin",
    "Mian Channu",
    "Mianwali",
    "Miani",
    "Multan",
    "Murree",
    "Muridke",
    "Mianwali Bangla",
    "Muzaffargarh",
    "Narowal",
    "Nankana Sahib",
    "Okara",
    "Pakpattan",
    "Pattoki",
    "Pindi Bhattian",
    "Pind Dadan Khan",
    "Pir Mahal",
    "Qaimpur",
    "Qila Didar Singh",
    "Raiwind",
    "Rajanpur",
    "Rahim Yar Khan",
    "Rawalpindi",
    "Renala Khurd",
    "Sadiqabad",
    "Sagri",
    "Sahiwal",
    "Sambrial",
    "Samundri",
    "Sangla Hill",
    "Sarai Alamgir",
    "Sargodha",
    "Shakargarh",
    "Sheikhupura",
    "Shujaabad",
    "Sialkot",
    "Sohawa",
    "Soianwala",
    "Siranwali",
    "Tandlianwala",
    "Talagang",
    "Taxila",
    "Toba Tek Singh",
    "Vehari",
    "Wah Cantonment",
    "Wazirabad",
    "Yazman",
    "Zafarwal"
  ]

city_name = StringVar()
com = ttk.Combobox(win, values=list_name, font=("Trip Sans", 20), textvariable=city_name)
com.place(x=35, y=100, height=50, width=430)

w_label = Label(win, text="Weather Climate", font=("Trip Sans", 15))
w_label.place(x=45, y=240, height=50, width=200)
w_label1 = Label(win, text="", font=("Trip Sans", 15))
w_label1.place(x=260, y=240, height=50, width=200)


wd_label = Label(win, text="Weather Description", font=("Trip Sans", 15))
wd_label.place(x=45, y=300, height=50, width=200)
wd_label1 = Label(win, text="", font=("Trip Sans", 15))
wd_label1.place(x=260, y=300, height=50, width=200)


temp_label = Label(win, text="Temperature", font=("Trip Sans", 15))
temp_label.place(x=45, y=360, height=50, width=200)
temp_label1 = Label(win, text="", font=("Trip Sans", 15))
temp_label1.place(x=260, y=360, height=50, width=200)


pre_label = Label(win, text="Pressure", font=("Trip Sans", 15))
pre_label.place(x=45, y=420, height=50, width=200)
pre_label1 = Label(win, text="", font=("Trip Sans", 15))
pre_label1.place(x=260, y=420, height=50, width=200)


done_button = Button(win, text="Done", font=("Trip Sans", 15), borderwidth=2, command=data_get)
done_button.place(x=205, y=170, height=50, width=90)


win.mainloop()
