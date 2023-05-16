from zebra import Zebra
import  random

def main():
    zebra1 = Zebra("First")
    zebra2 = Zebra("Second")
    zebra3 = Zebra("Third")

    zebras = (zebra1, zebra2, zebra3)

    for _ in range(10):
        zebra = random.choice(zebras)
        print(zebra.get_stripe())

    for zebra in zebras:
        print(zebra)


    # for _ in range(4):
    #     print(zebra1.get_stripe())
    #
    # for _ in range(5):
    #     print(zebra2.get_stripe())
    #     print(zebra3.get_stripe())

if __name__ == "__main__":
    main()
