class Car:
    # ...

    def __str__(self):
        return f"{self.make} {self.model}, 
                    {self.color} ({self.year})"

    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f'(make="{self.make}", '
            f'model="{self.model}", '
            f"year={self.year}, "
            f'color="{self.color}")'
        )