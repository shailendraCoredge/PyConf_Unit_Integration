from typing import List

class TravellerDb:

    def __init__(self):
        print("db connected ")

    def get_traveller_membership(self, name: str) -> int:
        if name == "Sachin":
            return 2
        elif name == "Virat":
            return 1.5
        return 1

    def close(self):
        print("DB connection Closed.")

class Plane:

    def __init__(self, max: int, price: int) -> None:
        self.max: int = max
        self.price: int = price
        self.traveller: List[str] = []

    def add_trveller(self, name: str) -> None:
        """insert passenger into passenger list"""
        booked = self.number_of_traveller()
        if booked == self.max:
            raise OverflowError("Flight have no vacant seeats!")
        self.traveller.append(name)
        return

    def number_of_traveller(self) -> int:
        return len(self.traveller)

    def get_traveller_list(self) -> List[str]:
        return self.traveller

    def calculate_total(self, db_object) -> float:
        total = 0
        for name in self.traveller:
            total += round(self.price / db_object.get_traveller_membership(name),1)
        return total