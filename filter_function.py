# filter_function.py
def main():
    print(list(filter(lambda x: x % 2 == 0, range(10))))

if __name__ == '__main__':
    main()
