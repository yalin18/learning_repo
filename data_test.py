import csv
import pygal
from pygal.style import CleanStyle
from pygal.style import DarkGreenStyle

## pygal for python data visualisation ##
dataFile = "data_test.csv"
f = open(dataFile, "r")
reader = csv.reader(f)
myDict = {}

# headers = next(reader, None)  ## column headers
# print(headers)
# count = 0

# for x in reader:
#     ## age, gender, budget, price, cuisine_type, rating ##
#     print(x[0],x[1],x[2],x[3],x[4],x[5])
#     count = count + 1
#     if count > 10:
#         break

# print(count)
# f.close()
# age_count = 0
# for x in reader:
#         if "under_19" in x[0]:
#                 age_count = age_count + 1
# print(age_count)

age_grp= []
gender_grp = []
budget_grp = []
price_grp = []
cuisine_grp = []
rating_grp = []

for x in reader:
        if not x[0] in age_grp:
                age_grp.append(x[0])
        if not x[1] in gender_grp:
                gender_grp.append(x[1])
        if not x[2] in budget_grp:
                budget_grp.append(x[2])
        if not x[3] in price_grp:
                price_grp.append(x[3])
        if not x[4] in cuisine_grp:
                cuisine_grp.append(x[4])
        if not x[5] in rating_grp:
                rating_grp.append(x[5])
print(age_grp)
print(gender_grp)
print(budget_grp)
print(price_grp)
print(cuisine_grp)
print(rating_grp)

# line_chart = pygal.Line(style=CleanStyle)
# line_chart_title = "Food rating"
# for x in reader:
#         line_chart.x_labels = x[0]
#         line_chart.add("prices", x[3])
# line_chart.render_to_file('data_test.svg')
