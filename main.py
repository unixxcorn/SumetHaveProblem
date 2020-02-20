from problems import HaveAProblem
import JobProb
import json

rounds=20000000
sumet = HaveAProblem(rounds=rounds, output=True)
# print(sumet.toDict()['uniform'], sumet.toDict()['exponential'])
sumet.plot()

print(json.dumps({ "rounds":rounds,
                   "Q1":JobProb.chanceMoreThan(sumet.toDict()['data'], 20, "uniform")['prob'],
                   "Q2":JobProb.chanceMoreThan(sumet.toDict()['data'], 25, "total")['prob'],
                   "Q3":JobProb.average(sumet.toDict()['data'], "uniform"),
                   "Q4":JobProb.average(sumet.toDict()['data'], "total")}))
