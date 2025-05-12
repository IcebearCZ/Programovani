# try_except.py
def main():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print('Nelze dělit nulou')

if __name__ == '__main__':
    main()
