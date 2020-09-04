from tkinter import*
from model.customer import*
from backend.connection import *



class customertier:
    def __init__(self, window):
        self.wn = window
        self.wn.title('welcome')
        self.wn.config(bg='grey')
        self.wn.geometry('900x800')

        ###############connection object#########

        self.dbconnect = DbConnection()

        self.lb_heading = Label(self.wn, text='Customer Tier Info', bg='grey', fg='brown', font=('Rockwell', 39, 'bold'))
        self.lb_heading.place(x=0, y=0, relwidth=1)

        self.frame1 = Frame(self.wn, bg='grey')
        self.frame1.place(x=100, y=100)

        self.lb_customername = Label(self.frame1, text='Customer Name:', fg='black', bg='grey', font=('Rockwell', 15, 'bold'))
        self.lb_customername.grid(row=0, column=0, padx=10, pady=10)

        self.ent_customername = Entry(self.frame1, font=('arial', 15, 'bold'))
        self.ent_customername.grid(row=0, column=1, padx=10, pady=10)

        self.lb_customerid = Label(self.frame1, text='Customer id:', fg='black', bg='grey', font=('Rockwell', 15, 'bold'))
        self.lb_customerid.grid(row=1, column=0, padx=10, pady=10)

        self.ent_customerid = Entry(self.frame1, font=('arial', 15, 'bold'))
        self.ent_customerid.grid(row=1, column=1, padx=10, pady=10)



        self.btn_add = Button(self.frame1, text='Add', fg='black', bg='white', font=('Rockwell', 10, 'bold'),
                              command=self.add)
        self.btn_add.grid(row=2, column=1)

        self.btn_reset = Button(self.frame1, text='Reset', fg='black', bg='white', font=('Rockwell', 10, 'bold'),
                                command=self.btn_reset_click)
        self.btn_reset.grid(row=2, column=2)


    def add(self):
        customer_obj=customer(self.ent_customername.get(),self.ent_customerid.get())
        query='insert into table name values(%s,%s);'
        values=(int(customer_obj.get_customerid()),customer_obj.get_customername())
        self.dbconnect.insert(query,values)


    def btn_reset_click(self):
        self.ent_customername.delete(0, "end")
        self.ent_customerid.delete(0, "end")




#wn = Tk()
#customertier(wn)
#wn.mainloop()