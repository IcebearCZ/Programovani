# class_example.py
def main():
    class Clovek:
        def __init__(self, jmeno):
            self.jmeno = jmeno

    p = Clovek('Pepa')
    print(p.jmeno)

if __name__ == '__main__':
    main()
