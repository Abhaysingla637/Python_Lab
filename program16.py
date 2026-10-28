import traceback

class FileProcessingError(Exception):
    pass

class InvalidFormatError(FileProcessingError):
    pass

class EmptyFileError(FileProcessingError):
    pass


def process_file(filename):
    file = None

    try:
        file = open(filename, "r")

        data = file.read()

        if not data.strip():
            raise EmptyFileError("The file is empty.")

        if not filename.endswith(".txt"):
            raise InvalidFormatError("Only .txt files are supported.")

        print("File processed successfully.")
        print("Contents:", data)

    except FileNotFoundError:
        print("Error: File not found.")

    except EmptyFileError as error:
        print("Error:", error)

    except InvalidFormatError as error:
        print("Error:", error)

    except Exception as error:
        print("Unexpected error:", error)
        traceback.print_exc()

    else:
        print("No errors occurred during processing.")

    finally:
        if file is not None:
            file.close()
            print("File closed safely.")


filename = input("Enter the file name: ")
process_file(filename)
