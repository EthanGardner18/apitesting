import math

def rectangle_area():
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    return width * height

def square_area():
    side = float(input("Enter the side length of the square: "))
    return side * side

def triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    return 0.5 * base * height

def circle_area():
    radius = float(input("Enter the radius of the circle: "))
    return math.pi * radius * radius

def trapezoid_area():
    base1 = float(input("Enter the length of the first base of the trapezoid: "))
    base2 = float(input("Enter the length of the second base of the trapezoid: "))
    height = float(input("Enter the height of the trapezoid: "))
    return 0.5 * (base1 + base2) * height

def main():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle")
    print("4. Circle")
    print("5. Trapezoid")

    choice = int(input("Enter the number of the shape (1-5): "))

    if choice == 1:
        print(f"The area of the rectangle is: {rectangle_area()}")
    elif choice == 2:
        print(f"The area of the square is: {square_area()}")
    elif choice == 3:
        print(f"The area of the triangle is: {triangle_area()}")
    elif choice == 4:
        print(f"The area of the circle is: {circle_area()}")
    elif choice == 5:
        print(f"The area of the trapezoid is: {trapezoid_area()}")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
