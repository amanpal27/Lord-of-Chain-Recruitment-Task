import math
import time

INITIATED = "INITIATED"
ACCEPTED = "ACCEPTED"
DEPLOYED = "DEPLOYED (Driver en route)"
DELIVERED = "DELIVERED"

FREE = "FREE"
BUSY = "BUSY"

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

class Customer:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

class Restaurant:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def accept_order(self):
        choice = input(f"Restaurant {self.name}, do you accept the order? (y/n): ")
        return choice.lower() == 'y'

class DeliveryAgent:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.status = FREE

    def assign_order(self, new_x, new_y):
        self.status = BUSY
        self.x = new_x
        self.y = new_y

    def complete_delivery(self, cust_x, cust_y):
        self.x = cust_x
        self.y = cust_y
        self.status = FREE

class Order:
    def __init__(self, order_id, customer, restaurant, is_priority):
        self.order_id = order_id
        self.customer = customer
        self.restaurant = restaurant
        self.is_priority = is_priority
        self.fee = 10 * calculate_distance(customer.x, customer.y, restaurant.x, restaurant.y)
        self.status = INITIATED
        self.assigned_agent = None

    def update_status(self, new_status):
        self.status = new_status
        print(f"Order {self.order_id} status updated to: {self.status}")

def assign_driver(restaurant, agents):
    min_distance = float('inf')
    selected_agent = None
    for agent in agents:
        if agent.status == FREE:
            dist = calculate_distance(restaurant.x, restaurant.y, agent.x, agent.y)
            if dist < min_distance:
                min_distance = dist
                selected_agent = agent
    return selected_agent

def wait(seconds):
    time.sleep(seconds)

def main():
    # Input Customers
    num_customers = int(input("Enter number of customers: "))
    customers = []
    for i in range(num_customers):
        name = input(f"Enter customer {i+1} name: ")
        x, y = map(float, input(f"Enter customer {name} location (x y): ").split())
        customers.append(Customer(name, x, y))

    # Input Restaurants
    num_restaurants = int(input("\nEnter number of restaurants: "))
    restaurants = []
    for i in range(num_restaurants):
        name = input(f"Enter restaurant {i+1} name: ")
        x, y = map(float, input(f"Enter restaurant {name} location (x y): ").split())
        restaurants.append(Restaurant(name, x, y))

    # Input Delivery Agents
    num_agents = int(input("\nEnter number of delivery agents: "))
    agents = []
    for i in range(num_agents):
        name = input(f"Enter delivery agent {i+1} name: ")
        x, y = map(float, input(f"Enter delivery agent {name} starting location (x y): ").split())
        agents.append(DeliveryAgent(name, x, y))

    # Create Orders
    num_orders = int(input("\nEnter number of orders to place: "))
    orders = []
    order_id_counter = 1
    for i in range(num_orders):
        print(f"\nFor Order {order_id_counter}:")
        cust_index = int(input(f"Select customer index (0 to {num_customers - 1}): "))
        rest_index = int(input(f"Select restaurant index (0 to {num_restaurants - 1}): "))
        pri_choice = input("Is this a priority order? (y/n): ")
        is_priority = pri_choice.lower() == 'y'
        order = Order(order_id_counter, customers[cust_index], restaurants[rest_index], is_priority)
        print(f"Order {order_id_counter} created. Fee: ${order.fee:.2f}")
        orders.append(order)
        order_id_counter += 1

    # Process orders: Sort so that priority orders are processed first.
    orders.sort(key=lambda o: o.is_priority, reverse=True)

    # Process each order lifecycle.
    for order in orders:
        print(f"\nProcessing Order {order.order_id} from customer {order.customer.name} at restaurant {order.restaurant.name}")
        order.update_status(INITIATED)
        wait(1)

        # Restaurant accepts or rejects order.
        if not order.restaurant.accept_order():
            print(f"Order {order.order_id} was rejected by the restaurant.")
            continue 
        
        order.update_status(ACCEPTED)
        wait(1)

        # Assign a delivery driver to the order.
        driver = assign_driver(order.restaurant, agents)
        if driver is None:
            print(f"No available delivery agent for Order {order.order_id}. Please wait.")
            continue

        order.assigned_agent = driver
        driver.assign_order(order.restaurant.x, order.restaurant.y)
        print(f"Delivery Agent {driver.name} assigned to Order {order.order_id}.")
        order.update_status(DEPLOYED)
        wait(2)

        # Simulate delivery - driver moves to customer's location.
        driver.complete_delivery(order.customer.x, order.customer.y)
        order.update_status(DELIVERED)
        print(f"Order {order.order_id} delivered by {driver.name} to customer {order.customer.name}.")
        wait(1)

    print("\nAll orders processed. Simulation complete.")

if __name__ == '__main__':
    main()
# We can test for this input
# Enter number of customers: 2
# Enter customer 1 name: Aman
# Enter customer Aman location (x y): 0 0
# Enter customer 2 name: Aditya
# Enter customer Aditya location (x y): 10 10

# Enter number of restaurants: 2
# Enter restaurant 1 name: PizzaHut
# Enter restaurant PizzaHut location (x y): 5 5
# Enter restaurant 2 name: KFC
# Enter restaurant KFC location (x y): 15 15

# Enter number of delivery agents: 2
# Enter delivery agent 1 name: Shiva
# Enter delivery agent Shiva starting location (x y): 2 2
# Enter delivery agent 2 name: Rohan
# Enter delivery agent Rohan starting location (x y): 12 12

# Enter number of orders to place: 2

# For Order 1:
# Select customer index (0 to 1): 0
# Select restaurant index (0 to 1): 0
# Is this a priority order? (y/n): y

# For Order 2:
# Select customer index (0 to 1): 1
# Select restaurant index (0 to 1): 1
# Is this a priority order? (y/n): n