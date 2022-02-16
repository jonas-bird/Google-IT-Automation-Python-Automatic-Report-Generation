#!/usr/bin/env python3
"""
first steps to solving Week 3 lab of Google's IT Automation With Python
Automating Real World Tasks
Jonas Bird
2021-12-26
"""
import json
filename = "car_sales.json"
with open(filename, 'r') as file:
    sales_data = json.load(file)
car_year = {}
car_model = {}
for car_sales in sales_data:
    sales_year = car_sales['car']['car_year']
    model = car_sales['car']['car_model']
    car_model[model] = car_model.get(model, 0
                                     ) + int(car_sales['total_sales'])
    car_year[sales_year] = car_year.get(sales_year, 0
                                        ) + int(car_sales['total_sales'])

most_popular_year = max(k for k, v in car_year.items())
