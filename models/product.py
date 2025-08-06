from dataclasses import dataclass, asdict

@dataclass
class Product:
    product_id: int
    name: str
    description: str
    price: float
    image: str
    # is_available:
    stock: int

    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_row(cls, row: tuple) -> "Product":
        return cls(
            product_id = row[0],
            name = row[1],
            description = row[2],
            price = row[3],
            image = row[4],
            stock = row[5],
        )
    
#hdfhgfiu