from numpy.random import uniform as unirand
from numpy.random import exponential as exporand
import matplotlib.pyplot as plt
import json


class HaveAProblem:
    dictionary = {"uniform": {}, "exponential": {}, "total": {}}
    sorted_list = {"uniform": [], "exponential": [], "total": []}
    

    def __init__(self, range_of_uniform=[0, 30], average_of_exponential=10, rounds=1000, output=True):
        for r in range(rounds):
            if output:
                if r % (rounds // 15) == 0:
                    print("Running : %i percent" %(r/rounds * 100))
            uni = float("{0:.1f}".format(unirand(range_of_uniform[0], range_of_uniform[1])))
            expo = float("{0:.1f}".format(exporand(average_of_exponential)))
            total = uni + expo

            if uni not in self.dictionary["uniform"].keys():
                self.dictionary["uniform"][uni] = 0
            self.dictionary["uniform"][uni] = self.dictionary["uniform"][uni] + 1

            if expo not in self.dictionary["exponential"].keys():
                self.dictionary["exponential"][expo] = 0
            self.dictionary["exponential"][expo] = self.dictionary["exponential"][expo] + 1
                
            if total not in self.dictionary["total"].keys():
                self.dictionary["total"][total] = 0
            self.dictionary["total"][total] = self.dictionary["total"][total] + 1
        if output:
            print("Complete")
        self.sort()

    def toDict(self):
        unia = {"max": max(self.dictionary["uniform"].values()), "min": min(
            self.dictionary["uniform"].values())}
        unib = {"max": max(self.dictionary["uniform"].keys()), "min": min(
            self.dictionary["uniform"].keys())}

        s = 0
        c = 0
        for i in self.dictionary["exponential"].keys():
            s = s + (self.dictionary["exponential"][i] * i)
            c = c + self.dictionary["exponential"][i]
        expo = {"avg": s/c }

        s = 0
        c = 0
        for i in self.dictionary["total"].keys():
            s = s + (self.dictionary["total"][i] * i)
            c = c + self.dictionary["total"][i]
        total = {"avg": s/c}

        return {"data": self.dictionary, "uniform": {"keys": unib, "values": unia}, "exponential": expo, "total": total}
    
    def __repr__(self):
        return json.dumps(self.toDict())

    def sort(self):
        for i in sorted(self.dictionary["uniform"].keys()):
            self.sorted_list["uniform"].append(self.dictionary["uniform"][i])

        for i in sorted(self.dictionary["exponential"].keys()):
            self.sorted_list["exponential"].append(
                self.dictionary["exponential"][i])
        
        for i in sorted(self.dictionary["total"].keys()):
            self.sorted_list["total"].append(
                self.dictionary["total"][i])

    def saySorted(self):
        print(self.sorted_list)

    def sayDictionary(self):
        print(self.dictionary)

    def plot(self):
        plt.subplot(221)
        plt.plot(sorted(self.dictionary["uniform"].keys()), self.sorted_list["uniform"], "r")
        plt.title("uniform")
        plt.ylabel('frequency')
        plt.xlabel('value (s)')

        plt.subplot(222)
        plt.plot(sorted(self.dictionary["exponential"].keys()), self.sorted_list["exponential"], "r")
        plt.title("exponential")
        plt.ylabel('frequency')
        plt.xlabel('value (s)')

        plt.subplot(212)
        plt.plot(sorted(self.dictionary["total"].keys()), self.sorted_list["total"], "r")
        plt.title("total")
        plt.ylabel('frequency')
        plt.xlabel('value (s)')

        plt.subplots_adjust(hspace=0.4)
        # plt.savefig("output.png", dpi=300, papersize="a4")
        plt.show()

    pass

