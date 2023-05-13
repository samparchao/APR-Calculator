import tkinter as tk
import math

def calculate_apr(base_rate, scaling_factor, contract_duration):
    apr = base_rate + scaling_factor * math.log(contract_duration)
    return apr

def update_values(*args):
    product_cost = float(product_cost_entry.get())
    contract_duration = contract_duration_slider.get()

    apr = calculate_apr(base_rate, scaling_factor, contract_duration)
    final_price = product_cost * math.exp(apr)
    monthly_payment = final_price / contract_duration

    apr_var.set("APR: {:.2f}%".format(apr * 100))
    final_price_var.set("Final Price: £{:.2f}".format(final_price))
    monthly_payment_var.set("Monthly Payment: £{:.2f}".format(monthly_payment))

# Initial values
product_cost = 500
base_rate = 0.05
scaling_factor = 0.08
contract_duration = 36

# Create the main window
window = tk.Tk()
window.title("APR Calculator")

# Create and place widgets
product_cost_label = tk.Label(window, text="Product Cost (£):")
product_cost_label.grid(row=0, column=0, padx=10, pady=5)

product_cost_entry = tk.Entry(window)
product_cost_entry.insert(0, str(product_cost))
product_cost_entry.grid(row=0, column=1, padx=10, pady=5)

contract_duration_label = tk.Label(window, text="Contract Duration (months):")
contract_duration_label.grid(row=1, column=0, padx=10, pady=5)

contract_duration_slider = tk.Scale(window, from_=12, to=36, orient=tk.HORIZONTAL, length=200)
contract_duration_slider.set(contract_duration)
contract_duration_slider.grid(row=1, column=1, padx=10, pady=5)

apr_label = tk.Label(window, text="APR:")
apr_label.grid(row=3, column=0, padx=10, pady=5)

final_price_label = tk.Label(window, text="Final Price:")
final_price_label.grid(row=4, column=0, padx=10, pady=5)

monthly_payment_label = tk.Label(window, text="Monthly Payment:")
monthly_payment_label.grid(row=5, column=0, padx=10, pady=5)

# Create StringVars to store the dynamic values
apr_var = tk.StringVar()
final_price_var = tk.StringVar()
monthly_payment_var = tk.StringVar()

# Assign the StringVars to the corresponding labels
apr_label_value = tk.Label(window, textvariable=apr_var)
apr_label_value.grid(row=3, column=1, padx=10, pady=5)

final_price_label_value = tk.Label(window, textvariable=final_price_var)
final_price_label_value.grid(row=4, column=1, padx=10, pady=5)

monthly_payment_label_value = tk.Label(window, textvariable=monthly_payment_var)
monthly_payment_label_value.grid(row=5, column=1, padx=10, pady=5)

# Set up trace on product cost entry and contract duration slider
product_cost_entry.bind("<KeyRelease>", update_values)
contract_duration_slider.config(command=update_values)

# Update the initial values
update_values()

# Run the GUI event loop
window.mainloop()
