import csv


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, 'r', newline='') as csvfile, \
                open('data/mkt_campaign.txt', 'w') as output_file:
            csv_read = csv.reader(csvfile)

            data = list(csv_read)
            possible_days, possible_items = possible_days_and_items(data)
            joao_orders, joao_days = about_joao(data)
            maria_most_ordered = about_maria(data)
            arnaldo_hamburguer_count = about_arnaldo(data)

            output_file.write(f"{maria_most_ordered}\n")
            output_file.write(f"{arnaldo_hamburguer_count}\n")
            output_file.write(f"{possible_items - joao_orders}\n")
            output_file.write(f"{possible_days - joao_days}\n")

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def possible_days_and_items(data):
    possible_items = set(row[1] for row in data)
    possible_days = set(row[2] for row in data)
    return [possible_days, possible_items]


def about_maria(data):
    maria_orders = {}
    for row in data:
        client, order = row[0], row[1]
        if client == 'maria':
            maria_orders[order] = maria_orders.get(order, 0) + 1
    maria_most_ordered = max(maria_orders, key=maria_orders.get)
    return maria_most_ordered


def about_arnaldo(data):
    arnaldo_hamburguer_count = sum(
        1 for row in data
        if row[0] == 'arnaldo'
        and row[1] == 'hamburguer'
    )
    return arnaldo_hamburguer_count


def about_joao(data):
    joao_orders = set(row[1] for row in data if row[0] == 'joao')
    joao_days = set(row[2] for row in data if row[0] == 'joao')
    return [joao_orders, joao_days]
