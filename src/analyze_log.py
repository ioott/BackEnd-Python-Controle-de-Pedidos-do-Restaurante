import csv


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, 'r', newline='') as csvfile, \
                open('data/mkt_campaign.txt', 'w') as output_file:
            csv_read = csv.reader(csvfile)

            orders_data = list(csv_read)
            possible_days, possible_items = days_and_items(orders_data)
            customer_orders, days_by_customer = customer_info(orders_data)
            items_most_ordered = items_most_ordered_function(orders_data)
            items_count = items_count_function(orders_data)

            output_file.write(f"{items_most_ordered}\n")
            output_file.write(f"{items_count}\n")
            output_file.write(f"{possible_items - customer_orders}\n")
            output_file.write(f"{possible_days - days_by_customer}\n")

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def days_and_items(orders_data):
    possible_items = set(row[1] for row in orders_data)
    possible_days = set(row[2] for row in orders_data)
    return [possible_days, possible_items]


def items_most_ordered_function(orders_data):
    customer_orders = {}
    for row in orders_data:
        client, order = row[0], row[1]
        if client == 'maria':
            customer_orders[order] = customer_orders.get(order, 0) + 1
    items_most_ordered = max(customer_orders, key=customer_orders.get)
    return items_most_ordered


def items_count_function(orders_data):
    items_count = sum(
        1 for row in orders_data
        if row[0] == 'arnaldo'
        and row[1] == 'hamburguer'
    )
    return items_count


def customer_info(orders_data):
    customer_orders = set(row[1] for row in orders_data if row[0] == 'joao')
    days_by_customer = set(row[2] for row in orders_data if row[0] == 'joao')
    return [customer_orders, days_by_customer]
