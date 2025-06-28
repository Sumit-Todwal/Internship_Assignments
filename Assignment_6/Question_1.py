import pandas as pd
# Converting a Series of datestrings to a timeseries.
DateStrings = ["20-12-2024","21-12-2024","22-12-2024"]
timeseries = pd.to_datetime(DateStrings)
print(timeseries)