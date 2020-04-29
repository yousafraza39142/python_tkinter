from tkinter import *
from tkinter import messagebox

from Car import Car
from Customer import Customer
from rented_to import Rented_to

cars = []
customers = []
rented_to = []
selectedCustomer = -1

rented_list = []

s_c_object = None

selectedCar = -1
s_car_object = None

selected_rent = -1
rent_car_object = None


def add_customer():
    # print(customer_name.get())
    if customer_name.get() == '':
        messagebox.showerror("Empty Name", "Customer Name Cannot be Empty")
    else:
        if customers:
            customers.append(Customer(customers[-1].id + 1, customer_name.get().lower()))
        else:
            customers.append(Customer(0, customer_name.get().lower()))
        # print(customers)
        customers_list.delete('0', 'end')
        for c in customers:
            customers_list.insert('end', tuple([c.id, c.name]))
            print('ID:' + str(c.id) + 'name:' + c.name)


def add_car():
    if car_model.get() == '':
        messagebox.showerror("Empty Model Name", "Car Model Cannot be Empty")
    else:
        car_model_ = car_model.get().lower()
        if cars:
            cars.append(Car(cars[-1].id + 1, car_model.get()))
        else:
            cars.append(Car(0, car_model.get()))
        cars_list.delete('0', 'end')
        for c in cars:
            cars_list.insert('end', tuple([c.id, c.model]))


def get_selected_row_customer(event):
    global selectedCustomer
    global s_c_object
    try:
        index = customers_list.curselection()[0]
        selectedCustomer = index
        s_c_object = customers_list.get(selectedCustomer, selectedCustomer)[0]
        print('Clicked', selectedCustomer)
    except IndexError:
        pass


def get_selected_row_cars(event):
    global selectedCar
    global s_car_object
    try:
        index = cars_list.curselection()[0]
        selectedCar = index
        s_car_object = cars_list.get(selectedCar, selectedCar)[0]
    except IndexError as e:
        print(e)


root = Tk()

cutomer_label = Label(root, text='Customer Name').grid(row=0, column=0)
customer_name = StringVar()
customer_input = Entry(root, text=customer_name).grid(row=1, column=0)
customer_input_button = Button(root, text='Add Customer', command=add_customer).grid(row=1, column=3)

car_label = Label(root, text='Car Model').grid(row=0, column=4)
car_model = StringVar()
car_input = Entry(root, text=car_model).grid(row=1, column=4)
car_input_button = Button(root, text='Add Car', command=add_car).grid(row=1, column=5)

customers_list = Listbox(root, height=10, width=35)
customers_list.grid(row=6, rowspan=6, column=0, columnspan=2)

s1 = Scrollbar(root)
s1.grid(row=3, column=2, rowspan=4)

customers_list.configure(yscrollcommand=s1.set)
s1.configure(command=customers_list.yview)

customers_list.bind('<<ListboxSelect>>', get_selected_row_customer)

# CarsList
cars_list = Listbox(root, height=10, width=35)
cars_list.grid(row=6, rowspan=6, column=4, columnspan=2)

s2 = Scrollbar(root)
s2.grid(row=3, column=6, rowspan=4)

cars_list.configure(yscrollcommand=s2.set)
s2.configure(command=cars_list.yview)

cars_list.bind('<<ListboxSelect>>', get_selected_row_cars)


def update_customer():
    global selectedCustomer, s_c_object
    if selectedCustomer == -1:
        messagebox.showerror('Error', 'No Customer Selected')
    elif new_customer_name.get() == '':
        messagebox.showerror('Error', 'Cannot be Empty')
    else:
        for c in customers:
            if c.id == s_c_object[0]:
                c.name = new_customer_name.get().lower()

        customers_list.delete('0', 'end')
        for c in customers:
            customers_list.insert('end', tuple([c.id, c.name]))
            # print('ID:' + str(c.id) + 'name:' + c.name)
        selectedCustomer = -1
        s_c_object = None


def delete_customer():
    global selectedCustomer, s_c_object
    if selectedCustomer == -1:
        messagebox.showerror('Error', 'No Customer Selected')
    else:
        for c in customers:
            if c.id == s_c_object[0]:
                customers.remove(c)
        customers_list.delete('0', 'end')
        for c in customers:
            customers_list.insert('end', tuple([c.id, c.name]))
    selectedCustomer = -1
    s_c_object = None


customer_edit_button = Button(root, text='Edit Customer', command=update_customer).grid(row=13, column=3)

new_customer_name = StringVar()
customer_edit_input = Entry(root, text=new_customer_name).grid(row=13, column=0)
customer_delete_button = Button(root, text='Delete Customer', command=delete_customer).grid(row=14, column=3)


def update_car():
    global selectedCar, s_car_object
    if selectedCar == -1:
        messagebox.showerror('Error', 'No Car Selected')
    elif new_car_model.get() == '':
        messagebox.showerror('Error', 'Cannot be Empty')
    else:
        for c in cars:
            if c.id == s_car_object[0]:
                c.model = new_car_model.get().lower()

        cars_list.delete('0', 'end')
        for c in cars:
            cars_list.insert('end', tuple([c.id, c.model]))
            # print('ID:' + str(c.id) + 'name:' + c.name)
        selectedCar = -1
        s_car_object = None


car_edit_button = Button(root, text='Edit Car', command=update_car).grid(row=13, column=5)


def delete_car():
    global selectedCar, s_car_object
    if selectedCar == -1:
        messagebox.showerror('Error', 'No Customer Selected')
    else:
        for c in cars:
            if c.id == s_car_object[0]:
                cars.remove(c)
        cars_list.delete('0', 'end')
        for c in cars:
            cars_list.insert('end', tuple([c.id, c.model]))
    selectedCar = -1
    s_car_object = None


car_delete_button = Button(root, text='Delete Car', command=delete_car).grid(row=14, column=5)

new_car_model = StringVar()
car_edit_input = Entry(root, text=new_car_model).grid(row=13, column=4)


def rend_car_action():
    print("working")
    if customer_rent_to_id.get() == '':
        messagebox.showerror('Error', 'Empty Customer Id')
    elif car_rent_id.get() == '':
        messagebox.showerror('Error', 'Empty Car Id')
    else:
        try:
            print(car_rent_id.get())
            print(customer_rent_to_id.get())
            carID = int(car_rent_id.get())
            customerId = int(customer_rent_to_id.get())

            for c in customers:
                if c.id == customerId:
                    for car in cars:
                        # print(car.id)
                        if car.id == carID:
                            if rented_to:
                                rented_to.append(Rented_to(rented_to[-1].id + 1, car.id))
                            else:
                                rented_to.append(Rented_to(0, car.id))
                            cars_customers_list.delete('0', 'end')
                            for data in rented_to:
                                cars_customers_list.insert('end', tuple(['Car ', car.id, 'Rented to Customer ', c.id]))
                            return
                    messagebox.showerror('Error', 'Car with this ID does not exist')
                    return
            messagebox.showerror('Error', 'Customer does not exist with this ID')


        except:
            messagebox.showerror('Error', 'Enter only integer values')


customer_rent_to_label = Label(root, text="Customer ID").grid(row=16, column=0)
customer_rent_to_id = StringVar()
customer_rent_to_entry = Entry(root, text=customer_rent_to_id).grid(row=17, column=0)

car_rent_label = Label(root, text="Car ID").grid(row=16, column=2)
car_rent_id = StringVar()
car_rent_entry = Entry(root, text=car_rent_id).grid(row=17, column=2)

rent_button = Button(root, text='Rent Car to This Customer', command=rend_car_action).grid(rows=17, column=3)


def delete_rent():
    global selected_rent,rent_car_object
    # for data in rented_to:
    if selected_rent == -1:
        messagebox.showerror('Error', 'No rent selected')
    # print(rent_car_object[1],rent_car_object[3])
    for rent in rented_to:
        # print('rent:',rent.customer_id,rent.car_id)
        if rent_car_object[1] == rent.customer_id & rent_car_object[3] == rent.car_id:
            rented_to.remove(rent)
            cars_customers_list.delete('0', 'end')
            for data in rented_to:
                cars_customers_list.insert('end', tuple(['Car ', data.customer_id, 'Rented to Customer ', data.car_id]))
            # return
    selected_rent = -1
    rent_car_object = None


delete_rent = Button(root, text='Delete this rent', command=delete_rent).grid(rows=17, column=3)
# Rented List
rented_cars_label = Label(root, text="Rented Cars").grid(row=19, column=0)
cars_customers_list = Listbox(root, height=10, width=35)
cars_customers_list.grid(row=20, rowspan=6, column=0, columnspan=2)

s3 = Scrollbar(root)
s3.grid(row=20, column=2, rowspan=4)

cars_customers_list.configure(yscrollcommand=s3.set)
s3.configure(command=cars_customers_list.yview)


def get_selected_rented_cars(event):
    global selected_rent, rent_car_object
    try:
        index = cars_customers_list.curselection()[0]
        selected_rent = index
        rent_car_object = cars_customers_list.get(selected_rent, selected_rent)[0]
    except IndexError as e:
        print(e)


cars_customers_list.bind('<<ListboxSelect>>', get_selected_rented_cars)

# Rent Logic

root.mainloop()
