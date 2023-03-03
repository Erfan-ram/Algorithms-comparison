# created
import Algorithms as alg


class main():
    def __init__(self) -> None:
        print("""Welcome
              i am a program to solve Fibonacci using two algorithms :
              Divide and Conquer Algorithms 
              Dynamic Programming""")

        print("then i will create a dataset contain each numbers execute duration time for both algorithms")

    def Fibonacci(self, num):
        print(alg.devide_conquer(num), alg.dynamic_programming(num))


program = main()
program.Fibonacci(9)
