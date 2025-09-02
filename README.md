# Vectra-Assignment

# Assignment 1a – Student Marks Analysis


**File:** `assignment1.py`
## Description
This program reads student marks from an Excel file (`student.xlsx`) and performs the following tasks:
- Calculates **Total Marks** and **Average** for each student.  
- Assigns **Grades** based on average marks.  
- Finds the **Top 3 performers** in each subject.  
- Saves results into a new Excel file (`results.xlsx`) with:
  - **Summary** → Student details with total, average, and grade.  
  - **Top Performers** → Best 3 students in each subject.  
  - **Charts** → Bar chart of average marks per subject.

## Requirements
Make sure you have Python 3 installed along with the following libraries: pip install pandas numpy matplotlib openpyxl

 **How to Run**
Place your input Excel file as student.xlsx in the same folder.
The file should contain columns: StudentID, Name, Math, Physics, Chemistry, Biology.

**Run the script:**
python assignment1.py

Check the generated results.xlsx.

Example Output:
Grades assigned successfully.
Top performers identified.
Excel file results.xlsx created.

Files Generated:
student.xlsx    # Input file with marks
results.xlsx    # Output file with results and charts
assignment1.py  # Script


# Assignment 1b – Polygon Geometry Analysis

**File:** `polygon_gy.py`

## Description
This program performs geometric analysis on a polygon defined by its vertices.  
It calculates various properties and visualizes the polygon.

### Features
- Computes **Area** using:
  - Shoelace formula (manual)
  - Shapely library  
- Calculates **Edge Lengths** of each side.  
- Determines **Interior Angles** at each vertex.  
- Checks whether the polygon is **Convex**.  
- Finds the **Centroid** (both manual and via Shapely).  
- Plots the polygon with:
  - Labeled vertices (`V1, V2...`)  
  - Red centroid marker  
  - Interior angles displayed in degrees  

## Requirements
Install the following Python libraries: pip install numpy matplotlib shapely

**How to Run**
Run the script directly: python polygon_gy.py

It will print the results in the console and open a Matplotlib window with the polygon plot.

Example:
Polygon Area (Shoelace): 35.75
Polygon Area (Shapely): 35.75
Edge Lengths: [5.0, 3.61, 5.0, 5.0, 3.61]
Interior Angles (degrees): [108.43, 126.87, 108.43, 108.43, 108.43]
Is Convex: True
Centroid (Manual): [7.41, 2.75]
Centroid (Shapely): [7.41, 2.75]


# Assignment 2 – Room Tiling with Square Tiles

**File:** `Room_Tiling_with_Squares.py`

## Description
This program simulates filling a rectangular grid with square tiles of different sizes.  
Tiles are placed in a **spiral order** starting from the center of the grid.

### Features
- Supports tile sizes **4×4**, **3×3**, **2×2**, and **1×1**.  
- Fills the grid by checking whether a tile can fit at a given position.  
- Places the largest possible tile at each step.  
- Uses a **spiral traversal algorithm** to move through the grid.  
- Visualizes the final tiling with color-coded squares:
  - Green = 4×4  
  - Yellow = 3×3  
  - Blue = 2×2  
  - Red = 1×1  
- Displays a count of how many tiles of each size were used.

## Requirements
Install the required libraries: pip install numpy matplotlib
 
 **How to Run**
Run the script directly: python Room_Tiling_with_Squares.py


# Assignment 3 – Pyramid of Equilateral Triangles

**File:** `Pyramid.py`
## Description
This program draws a pyramid made up of **equilateral triangles** using Python.  
The pyramid is built row by row with upright triangles and inverted triangles filling the gaps.
### Features
- Function to generate coordinates of an equilateral triangle (upright or inverted).  
- Function to draw a pyramid with customizable:
  - **Side length** of triangles.  
  - **Depth** (number of rows).  
- Visualizes the pyramid with:
  - Blue upright triangles.  
  - Gold inverted triangles.  

## Requirements
Install the required libraries: pip install numpy matplotlib

**How to Run**
Run the script directly: python Pyramid.py

