import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.chart import BarChart, Reference

# input
df = pd.read_excel("student.xlsx")

# list of given subject
subjects = ["Math", "Physics", "Chemistry", "Biology"]

# Calculate total and average marks for each student
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df["Total"] / len(subjects)

# Assigning Grades based on Average marks
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average"].apply(get_grade)

# Finding the top performers
top_performers = {}
for sub in subjects:
    top_performers[sub] = df.sort_values(by=sub, ascending=False).head(3)[["StudentID", "Name", sub]]

# Converting top performers dictionary to DataFrame
top_df = pd.concat(top_performers, axis=0)

# Saving summary and top performers to an Excel file (results.xlsx)
with pd.ExcelWriter("results.xlsx", engine="openpyxl") as writer:
    summary_cols = ["StudentID", "Name", "Total", "Average", "Grade"]
    df[summary_cols].to_excel(writer, sheet_name="Summary", index=False)
    top_df.to_excel(writer, sheet_name="Top Performers")

# chart creation by using the result.xlsx
wb = load_workbook("results.xlsx")
ws = wb["Summary"]

# Compute average marks per subject for chart visualization
avg_subjects = df[subjects].mean().reset_index()
avg_subjects.columns = ["Subject", "Average Marks"]

# Adding chart data into a new sheet
ws_chart = wb.create_sheet("Charts")
for row in dataframe_to_rows(avg_subjects, index=False, header=True):
    ws_chart.append(row)

# Creating bar chart
chart = BarChart()
chart.title = "Average Marks per Subject"
chart.x_axis.title = "Subjects"
chart.y_axis.title = "Average Marks"

data = Reference(ws_chart, min_col=2, min_row=1, max_row=len(avg_subjects) + 1)
cats = Reference(ws_chart, min_col=1, min_row=2, max_row=len(avg_subjects) + 1)
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)
ws_chart.add_chart(chart, "E5")

# Saving the result
wb.save("results.xlsx")
