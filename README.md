# Lord of Chain Recruitment Task
- A Python-based simulation of a food delivery platform (like Zomato/Swiggy) using Object-Oriented Programming (OOP). This program runs in the command-line interface and models real-world interactions between customers, restaurants, delivery agents, and order processing with priority handling and driver dispatch logic based on proximity.

# Features
- Customers can place orders (priority or normal).
-  Restaurants can accept or reject incoming orders.
- Orders go through a lifecycle: INITIATED → ACCEPTED → DEPLOYED → DELIVERED.
- Delivery agents are assigned based on nearest proximity and order priority.
- Simulated delivery status updates with delays.
- Fee calculation is based on the linear distance between customer and restaurant.
- All input and output via command-line interface.

# Technologies Used
- Python 3
- OOPs Principles
- math and time standard libraries  
# How to Run
# Requirements
- Python 3.x installed on your system.
# Steps
- Clone the repository or download the fooddelivery.py file.
- Open your terminal and navigate to the project directory.
- Run the script using:
```bash
python fooddelivery.py

# Follow the prompts in the terminal to input:
Number of customers, restaurants, delivery agents, and orders.
Location coordinates for each entity.
Whether orders are priority or normal.
Restaurant acceptance.
