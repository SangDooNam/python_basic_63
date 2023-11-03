import math

from check import print_rectangle_properties

class Rectangle:
    
    def __init__(self, width:float, height:float) -> None:
        self.width = width
        self.height = height
        
    def get_area(self) -> float:
        width = self.width
        height = self.height
        return width * height
    
    def get_perimeter(self) -> float:
        width = self.width
        height = self.height
        return (2*width) + (2*height)
    
    def get_diagonal(self) -> float:
        width = self.width
        height = self.height
        return (width**2 + height**2)**0.5
    
    def get_width(self) -> float:
        width = self.width
        return width
    
    def get_height(self) -> float:
        height = self.height
        return height
    
def main():
    print_rectangle_properties(Rectangle(17.0, 13.0))
    
if __name__ == "__main__":
    main()
