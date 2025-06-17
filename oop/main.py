from polymorphism_demo import Shape, Rectangle, Circle
def main():
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(5, 10)
    circle = Circle(7)

    # Calculate and print areas
    print(f"Area of the rectangle: {rectangle.area}")
    print(f"Area of the circle: {circle.area}")

    # Demonstrate polymorphism
    shapes = [rectangle, circle]
    for shape in shapes:
        print(f"Area of {shape.__class__.__name__}: {shape.area()}")

if __name__ == "__main__":
    main()  