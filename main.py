# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(10, 5)
print(f'\n{rect}')
print(f'Rectangle area: {rect.get_area()}')
rect.set_height(3)
print(f'Height changed to {rect.height}')
print(rect)
print(f'Rectangle perimeter: {rect.get_perimeter()}')
print(f'Rectangle picture:\n\n{rect.get_picture()}')

sq = shape_calculator.Square(9)
print(sq)
print(f'Square area: {sq.get_area()}')
sq.set_side(4)
print(f'Side changed to {sq.height}')
print(sq)
print(f'Square diagonal: {sq.get_diagonal()}')
print(f'Square picture:\n\n{sq.get_picture()}')


print(rect)
rect.set_height(8)
print(f'Height changed to {rect.height}')
rect.set_width(16)
print(f'Width changed to {rect.width}')
print(rect)
print(f'1 {rect} can contain { rect.get_amount_inside(sq)} {sq}')


# Run unit tests automatically
main(module='test_module', exit=False)