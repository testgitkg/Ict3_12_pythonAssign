# In[3]:




# que 1 python
def product_or_sum(a, b):
    product = a * b
    if product > 1000:
        return a + b
    else:
        return product

print(product_or_sum(20, 30)) 
print(product_or_sum(50, 30)) 


# In[5]:


# que 2 python
start = 0
end = 9
previous = 0

for current in range(start, end + 1):
    sum_val = current + previous
    print(f"Current: {current}, Previous: {previous}, Sum: {sum_val}")
    previous = current


# In[6]:


# que 3 python
def even_index_chars(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i]
    return result

input_string = "Hello, World!"
print(even_index_chars(input_string))


# In[7]:


# que 4 python
def check_first_last(nums):
    if not nums:
        return False 
    return nums[0] == nums[-1]

print(check_first_last([1, 2, 3, 1]))  
print(check_first_last([5, 6, 7]))    
print(check_first_last([]))          


# In[8]:


# que 5 python
def combine_lists(list1, list2):
    odd_from_list1 = [list1[i] for i in range(1, len(list1), 2)]

    even_from_list2 = [list2[i] for i in range(0, len(list2), 2)]

    result = odd_from_list1 + even_from_list2
    return result

list1 = [10, 11, 12, 13, 14, 15]
list2 = [20, 21, 22, 23, 24, 25]

print(combine_lists(list1, list2))

# In[9]:


# que 6 python
def modify_list(lst):
    if len(lst) <= 4:
        return lst 
    
    elem = lst.pop(4)
    
    lst.insert(1, elem)
    
    lst.append(elem)
    
    return lst

my_list = [10, 20, 30, 40, 50, 60, 70]
print(modify_list(my_list))

# In[10]:


#que 7 python
def slice_and_reverse(lst):
    n = len(lst)
    if n % 3 != 0:
        return "List size is not divisible by 3"
    
    chunk_size = n // 3
    chunks = []
    
    for i in range(0, n, chunk_size):
        chunk = lst[i:i + chunk_size]
        chunks.append(chunk[::-1]) 
    
    return chunks

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = slice_and_reverse(my_list)
print(result)


# In[12]:


#que 8 python
def count_occurrences(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

my_list = [1, 2, 2, 3, 4, 3, 3, 5]
print(count_occurrences(my_list))

# In[13]:


#que 9 python

colors = {'yellow', 'orange'}

new_colors = ['blue', 'black']

colors.update(new_colors)

print(colors)

# In[14]:


#que 10 python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print() 


# In[15]:


#que 11 python
def sum_upto(n):
    if n < 1:
        return 0
    return sum(range(1, n + 1))

print(sum_upto(10)) 


# In[16]:


#que 12 python
def display_divisible_by_5(lst):
    for num in lst:
        if num > 150:
            break
        if num % 5 == 0:
            print(num)

my_list = [10, 25, 40, 160, 50, 75]
display_divisible_by_5(my_list)

# In[17]:


#que 13 python
List1 = [10, 20, 30, 40]
reversed_list = []

for i in range(len(List1) - 1, -1, -1):
    reversed_list.append(List1[i])

print(reversed_list)

# In[18]:

#que 14 python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start = 10
end = 50
print(f"Prime numbers between {start} and {end}:", display_primes(start, end))


# In[20]:


#que 15 python
import pandas as pd
import numpy as np

class Car:
    def __init__(self, brand, model, price, color, year, stock):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.year = year
        self.stock = stock

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.color}, ${self.price}, Stock: {self.stock}"

class Showroom:
    def __init__(self):
        # Dataframe to manage car inventory
        self.cars_inventory = pd.DataFrame(columns=["Brand", "Model", "Price", "Color", "Year", "Stock"])
        
    def add_car(self, car):
        """ Adds a new car to the showroom inventory """
        car_data = {
            "Brand": car.brand,
            "Model": car.model,
            "Price": car.price,
            "Color": car.color,
            "Year": car.year,
            "Stock": car.stock
        }
        self.cars_inventory = self.cars_inventory.append(car_data, ignore_index=True)

    def view_available_cars(self):
        """ Displays all available cars in the showroom """
        if not self.cars_inventory.empty:
            print("Available cars in the showroom:")
            print(self.cars_inventory)
        else:
            print("No cars available in the showroom.")

    def display_car_details(self, brand, model):
        """ Display the details of a specific car """
        car_details = self.cars_inventory[
            (self.cars_inventory["Brand"] == brand) & (self.cars_inventory["Model"] == model)
        ]
        if not car_details.empty:
            print("Car Details:")
            print(car_details)
        else:
            print("Car not found in the inventory.")

    def sell_car(self, brand, model):
        """ Sell a car if it's available in the inventory """
        try:
            car_index = self.cars_inventory[
                (self.cars_inventory["Brand"] == brand) & (self.cars_inventory["Model"] == model)
            ].index[0]
            car_stock = self.cars_inventory.at[car_index, "Stock"]
            
            if car_stock > 0:
                self.cars_inventory.at[car_index, "Stock"] -= 1
                print(f"Car {brand} {model} sold successfully!")
            else:
                print(f"Sorry, {brand} {model} is out of stock.")
        except IndexError:
            print(f"Car {brand} {model} not found in the inventory.")

    def buy_car(self, brand, model, quantity):
        """ Buy a car and add it to the showroom inventory """
        try:
            # Validate if quantity is a positive integer
            if quantity <= 0:
                raise ValueError("Quantity must be a positive number.")
            
            # Check if the car already exists in the inventory
            if self.cars_inventory[
                (self.cars_inventory["Brand"] == brand) & (self.cars_inventory["Model"] == model)
            ].empty:
                # If car doesn't exist, create a new entry for the car
                price = float(input(f"Enter the price for {brand} {model}: $"))
                color = input(f"Enter the color for {brand} {model}: ")
                year = int(input(f"Enter the year for {brand} {model}: "))
                new_car = Car(brand, model, price, color, year, quantity)
                self.add_car(new_car)
                print(f"Car {brand} {model} added to the showroom.")
            else:
                
                car_index = self.cars_inventory[
                    (self.cars_inventory["Brand"] == brand) & (self.cars_inventory["Model"] == model)
                ].index[0]
                self.cars_inventory.at[car_index, "Stock"] += quantity
                print(f"Stock of {brand} {model} updated. {quantity} more cars added.")
        except ValueError as e:
            print(f"Error: {e}")


showroom = Showroom()

# Adding some cars to the showroom
car1 = Car("Toyota", "Corolla", 20000, "Red", 2021, 10)
car2 = Car("Honda", "Civic", 22000, "Blue", 2020, 5)
car3 = Car("BMW", "X5", 55000, "Black", 2022, 3)

showroom.add_car(car1)
showroom.add_car(car2)
showroom.add_car(car3)

# 1. View all available cars in the showroom
showroom.view_available_cars()

# 2. Display details of a specific car
showroom.display_car_details("Toyota", "Corolla")

# 3. Sell a car
showroom.sell_car("Honda", "Civic")
showroom.view_available_cars()

# 4. Buy a car and add it to the inventory
showroom.buy_car("Audi", "Q7", 2)
showroom.view_available_cars()

# 5. Handling exception: invalid quantity input
showroom.buy_car("Toyota", "Corolla", -5)  # Invalid quantity


# In[ ]:




