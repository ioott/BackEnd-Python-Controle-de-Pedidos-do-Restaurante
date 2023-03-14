class TrackOrders:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        orders_data = self._data
        new_order = (customer, order, day)
        orders_data.append(new_order)

    def get_most_ordered_dish_per_customer(self, customer):
        orders_data = self._data
        customer_orders = {}

        for row in orders_data:
            client, order = row[0], row[1]
            if client == customer:
                customer_orders[order] = customer_orders.get(order, 0) + 1

        return max(customer_orders, key=customer_orders.get)

    def get_never_ordered_per_customer(self, customer):
        orders_data = self._data
        possible_items = set(row[1] for row in orders_data)
        customer_orders = set(
            row[1]
            for row
            in orders_data
            if row[0] == customer
        )

        return possible_items - customer_orders

    def get_days_never_visited_per_customer(self, customer):
        orders_data = self._data
        possible_days = set(row[2] for row in orders_data)
        days_by_customer = set(
            row[2]
            for row
            in orders_data
            if row[0] == customer
        )

        return possible_days - days_by_customer

    def get_busiest_day(self):
        orders_data = self._data
        days_count = {}

        for row in orders_data:
            day = row[2]
            days_count[day] = days_count.get(day, 0) + 1

        return max(days_count, key=days_count.get)

    def get_least_busy_day(self):
        orders_data = self._data
        days_count = {}

        for row in orders_data:
            day = row[2]
            days_count[day] = days_count.get(day, 0) + 1

        return min(days_count, key=days_count.get)
