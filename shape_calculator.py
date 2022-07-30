class Rectangle:
    def __init__(self, width:int, height:int) -> None:
        self.width, self.height = width, height        

    def set_width(self, width:int) -> None:
        self.width = width
    
    def set_height(self, height:int) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
         
        return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, shape:'Rectangle|Square') -> int:
        return self.width // shape.width * self.height // shape.height

    def __str__(self) -> str: 
        return  f'{self.__class__.__name__}(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side:int) -> None:
        super().__init__(side, side)

    def set_side(self, side:int) -> None:
        self.width = self.height = side

    def set_height(self, height:int) -> None:
        self.set_side(height)

    def set_width(self, width:int) -> None:
        self.set_side(width)

    def __str__(self) -> str: 
        return  f'{self.__class__.__name__}(side={self.width})'
