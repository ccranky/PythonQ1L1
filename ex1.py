class Data():
    def __init__(self, data_str):
        self.data_str = data_str

    @classmethod
    def comp_data(cls, data_str):
        year, month, day = data_str.split(".")
        year = int(year)
        month = int(month)
        day = int(day)
        cls.validate_data(year, month, day)
        print(f"{year} {month} {day}")

    @staticmethod
    def validate_data(year, month, day):
        if day > 31 or day < 1:
            print("Введен неправильный день")
        if month > 12 or month < 1:
            print("Введен неправильный месяц")


sd = Data("2014.12.32")
Data.comp_data(sd.data_str)

