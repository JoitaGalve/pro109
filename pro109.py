import csv
import pandas as pd
import plotly.express as px
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
df = pd.read_csv("C109 properties of normal distribution/StudentsPerformance.csv")

mathList = df["math score"].tolist()
readingList = df["reading score"].tolist()

meanMath = statistics.mean(mathList)
modeMath = statistics.mode(mathList)
medianMath = statistics.median(mathList)
standardDeviationMath = statistics.stdev(mathList)

meanRead = statistics.mean(readingList)
modeRead = statistics.mode(readingList)
medianRead = statistics.median(readingList)
standardDeviationRead = statistics.stdev(readingList)

print("Mean is: " + str(meanMath))
print("Median is: " + str(medianMath))
print("Mode is: " + str(modeMath))
print("Standard Deviation is: " + str(standardDeviationMath))

print("Mean is: " + str(meanRead))
print("Median is: " + str(medianRead))
print("Mode is: " + str(modeRead))
print("Standard Deviation is: " + str(standardDeviationRead))



firststdStart, firststdEnd = meanMath - standardDeviationMath, meanMath + standardDeviationMath
secondstdStart, secondstdEnd = meanMath - (standardDeviationMath * 2), meanMath + (standardDeviationMath * 2)
thirdstdStart, thirdstdEnd = meanMath - (standardDeviationMath * 3), meanMath + (standardDeviationMath * 3)

listofstd1 = [result for result in mathList if result > firststdStart and result < firststdEnd]
listofstd2 = [result for result in mathList if result > secondstdStart and result < secondstdEnd]
listofstd3 = [result for result in mathList if result > thirdstdStart and result < thirdstdEnd]

print("Percentage of data lies within one Standard deviation: ", len(listofstd1) * 100/len(mathList))
print("Percentage of data lies within one Standard deviation: ", len(listofstd2) * 100/len(mathList))
print("Percentage of data lies within one Standard deviation: ", len(listofstd3) * 100/len(mathList))

firststdStart, firststdEnd = meanRead - standardDeviationRead, meanRead + standardDeviationRead
secondstdStart, secondstdEnd = meanRead - (standardDeviationRead * 2), meanRead + (standardDeviationRead * 2)
thirdstdStart, thirdstdEnd = meanRead - (standardDeviationRead * 3), meanRead + (standardDeviationRead * 3)

listofstd1 = [result for result in mathList if result > firststdStart and result < firststdEnd]
listofstd2 = [result for result in mathList if result > secondstdStart and result < secondstdEnd]
listofstd3 = [result for result in mathList if result > thirdstdStart and result < thirdstdEnd]

print("Percentage of data lies within one Standard deviation: ", len(listofstd1) * 100/len(readingList))
print("Percentage of data lies within one Standard deviation: ", len(listofstd2) * 100/len(readingList))
print("Percentage of data lies within one Standard deviation: ", len(listofstd3) * 100/len(readingList))



fig = ff.create_distplot([mathList], ["Result"], show_hist = False)
fig.add_trace(go.Scatter(x = [meanMath, meanMath], y = [0, 0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [firststdStart, firststdStart], y = [0, 0.17], mode = "lines", name = "standardDeviation"))
fig.add_trace(go.Scatter(x = [secondstdStart, secondstdStart], y = [0, 0.17], mode = "lines", name = "standardDeviation"))
#fig.add_trace(go.Scatter(x = [thirdstdStart, thirdstdStart], y = [0, 0.17], mode = "lines", name = "standardDeviation"))

fig.add_trace(go.Scatter(x = [firststdEnd, firststdEnd], y = [0, 0.17], mode = "lines", name = "standardDeviation"))
fig.add_trace(go.Scatter(x = [secondstdEnd, secondstdEnd], y = [0, 0.17], mode = "lines", name = "standardDeviation"))
#fig.add_trace(go.Scatter(x = [thirdstdEnd, thirdstdEnd], y = [0, 0.17], mode = "lines", name = "standardDeviation"))

fig.show()