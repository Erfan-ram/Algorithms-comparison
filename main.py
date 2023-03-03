# created
import Algorithms as alg
from time import time_ns as record


class main():
    def __init__(self) -> None:
        print("""Welcome
              i am a program to solve Fibonacci using two algorithms :
              Divide and Conquer Algorithms 
              Dynamic Programming""")

        print("then i will create a dataset contain each numbers execute duration time for both algorithms")

        self.number = int(input("\n\n calculating Fibonacci from 0 to :  "))

    def Fibonacci(self, num):
        calculated_time = []

        for nums in range(0, num+1):
            start = record()
            alg.devide_conquer(nums)
            end = record()
            devide_duration = end-start

            start = record()
            alg.dynamic_programming(nums)
            end = record()
            dynamic_duration = end-start

            calculated_time.append[num, devide_duration, dynamic_duration]
            
            return calculated_time


program = main()
program.Fibonacci(9)
