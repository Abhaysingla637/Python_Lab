from PIL import Image, ImageFilter

def process_image():
    path = input("Enter image file path: ")

    try:
        image = Image.open(path).convert("RGB")

        print("\n1. Grayscale")
        print("2. Black and White")
        print("3. Blur")
        print("4. Red Channel Only")
        print("5. Green Channel Only")
        print("6. Blue Channel Only")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = image.convert("L")

        elif choice == "2":
            grayscale = image.convert("L")
            result = grayscale.point(
                lambda pixel: 255 if pixel > 128 else 0
            )

        elif choice == "3":
            result = image.filter(ImageFilter.BLUR)

        elif choice == "4":
            red, green, blue = image.split()
            result = Image.merge(
                "RGB", (red, green.point(lambda p: 0),
                        blue.point(lambda p: 0))
            )

        elif choice == "5":
            red, green, blue = image.split()
            result = Image.merge(
                "RGB", (red.point(lambda p: 0), green,
                        blue.point(lambda p: 0))
            )

        elif choice == "6":
            red, green, blue = image.split()
            result = Image.merge(
                "RGB", (red.point(lambda p: 0),
                        green.point(lambda p: 0), blue)
            )

        else:
            print("Invalid choice!")
            return

        result.show()
        result.save("processed_image.png")
        print("Processed image saved as processed_image.png")

    except FileNotFoundError:
        print("Error: Image file not found.")

    except Exception as error:
        print("Error:", error)

process_image()