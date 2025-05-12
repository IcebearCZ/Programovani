# file_write.py
def main():
    with open('soubor.txt', 'w') as f:
        f.write('Zápis do souboru')

if __name__ == '__main__':
    main()
