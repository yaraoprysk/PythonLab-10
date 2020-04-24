class Printer:
    # static field
    energyConsumptionInWatts = "1.2 W"

    # constructor

    def __init__(self, producer_name=None, performance_page_per_minute=None, price_in_UAH=None,
                 wage_in_kg=None, brand=None, warranty_period_in_months=None):
        self.producer_name = producer_name
        self.performance_page_per_minute = performance_page_per_minute
        self.price_in_UAH = price_in_UAH
        self.wage_in_kg = wage_in_kg
        self.brand = brand
        self.warranty_period_in_months = warranty_period_in_months

    # destructor
    def __del__(self):
        return

    def __str__(self):
        return "The producer name is: " + str(self.producer_name) + "\n" + \
               "Performance page per minute: " + str(self.performance_page_per_minute) + "\n" + \
               "Price in UAH: " + str(self.price_in_UAH) + "\n" + \
               "Wage in kilograms: " + str(self.wage_in_kg) + "\n" + \
               "The brand of product: " + str(self.brand) + "\n" + \
               "Warranty period in months: " + str(self.warranty_period_in_months) + "\n" + \
               "Energy consumption in Watts: " + str(Printer.energyConsumptionInWatts) + "\n"

    @staticmethod
    def static_method():
        return Printer.energyConsumptionInWatts

    @staticmethod
    def main():
        print()
        no_info = Printer()
        partial_info = Printer("Epson", 4.0, 3999, 1.5)
        full_info = Printer("Canon", 7.7, 7999, 2.5, "PIXMA", 12)
        print(no_info.__str__())
        print(partial_info.__str__())
        print(full_info.__str__())


if __name__ == '__main__':
    Printer.main()
