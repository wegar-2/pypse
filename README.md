# pypse

Pull PSE data for modeling into Python. 

Single function *gpsedat* allows you to pull any data made available via GUI. 

You can view PSE API [here](https://api.raporty.pse.pl/app/home) and the API's doc [here](https://api.raporty.pse.pl/EndpointsMap.pdf).

### Example:
You can pull data on energy imbalance for Jan 1st, 2026 by running:
```commandline
from datetime import date
from pypse.gpsedat import gpsedat

data = gpsedat(
    endpoint="price-fcst",
    fields=["dtime", "imb_energy"',
    day=date(2026, 1, 1)
)
data.head()
```

The output should be:
```commandline
                 dtime  imb_energy
0  2026-01-01 00:00:00    -235.792
1  2026-01-01 00:15:00      -8.409
2  2026-01-01 00:30:00    -100.931
3  2026-01-01 00:45:00    -141.449
4  2026-01-01 01:00:00    -124.512
```

Check the API's doc (link above) for comprehensive list of available endpoints and fields.
