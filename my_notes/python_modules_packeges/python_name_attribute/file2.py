import file1 as f1  # Hello from file 1
                    # bla bla
                    # file1 is being imported

print("Hello from file2")  # Hello from file2

if __name__ == "__main__":
    print("file2 is being run directly")  # file2 is being run directly
else:
    print("file2 is being imported")

