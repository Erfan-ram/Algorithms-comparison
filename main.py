# created
import pandas as pd
import Algorithms as alg
from time import time_ns as record


class main():
    def __init__(self) -> None:
        print("""Welcome
              i am a program to solve Fibonacci using two algorithms :
              Divide and Conquer Algorithms 
              Dynamic Programming""")

        print("then i will create a dataset contain each numbers execute duration time for both algorithms")

    def Fibonacci(self, num):
        calculated_time = []

        for cur_num in range(0, num+1):
            start = record()
            alg.devide_conquer(cur_num)
            end = record()
            devide_duration = end-start

            start = record()
            alg.dynamic_programming(cur_num)
            end = record()
            dynamic_duration = end-start

            calculated_time.append([cur_num, devide_duration, dynamic_duration, abs(
                devide_duration-dynamic_duration)])

        return calculated_time

    def csv_output(self, list):
        df = pd.DataFrame(data=list, columns=[
                          "Number", "Devide-Conquer", "Dynamic-Programming", "difference"])
        df.to_csv("output.csv", index=False)
        del df

    def start(self):
        number = int(input("\n\n calculating Fibonacci from 0 to :  "))
        output_list = self.Fibonacci(number)
        self.csv_output(output_list)


program = main()
program.start()
