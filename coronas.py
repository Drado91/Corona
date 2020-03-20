from covid.api import CovId19Data
import numpy as np
from matplotlib import pyplot as plt

def confirmed_per_counrty(country):
    #x=res.get(country)
    hist = res.get(country).get('history')
    confirmed_per_day=[]
    for day in hist.items():
        confirmed_per_day.append(day[1].get('confirmed'))
    return confirmed_per_day

def growth_factor(confirmed_per_day,day_gap):
    squarer = lambda t,t_p: t/t_p if t_p else 0
    #for ind in range(day_gap,len(confirmed_per_day)):
    squares = np.array([squarer(confirmed_per_day[ind],confirmed_per_day[ind-day_gap]) for ind in range(day_gap,len(confirmed_per_day))])
    np.pad(squares, day_gap, 'constant', constant_values=0)
    return squares


api = CovId19Data(force=False)

res = api.get_stats()
res = api.get_all_records_by_country()
res = api.get_all_records_by_provinces()
country="japan"
res = api.get_history_by_country(country)

conf_country=confirmed_per_counrty('japan')
grow_fact1=growth_factor(conf_country,1)
grow_fact2=growth_factor(conf_country,3)
grow_fact3=growth_factor(conf_country,10)


plt.figure(0)
plt.plot(conf_country)
plt.plot(grow_fact1,label='1')
plt.plot(grow_fact2,label='3')
plt.plot(grow_fact3,label='10')
plt.legend()
plt.show()
print('finito')