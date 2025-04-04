### INITIAL STRUCTURE ANALYSIS: FACTS

#### CUSTOMER FLIGHT ACTIVITY:
- 405624 rows
- 10 columns 
- 1864 duplicate rows
- There are no null values in the table
- Year is a float

#### CUSTOMER LOYALTY HISTORY
- 16737 rows
- 16 columns
- 0 duplicate rows
- Nulls: 
    - Salary: 25.32%
    - Cancelation Year: 87.65%
    - Cancelation Month: 87.65%
- No typos in uniques
- 20 Negative salaries 
- Text values are homogenic (No typos, format)
- Client Loyalty is a primary key


### CLEANING & NULLS MGNT

- Removed duplicate rows considering all values are absolutely the same.

- Updating data type from float to integer on columns that are date related: 'Cancellation Year' & 'Cancellation Month'

- The negative salaries are within the regular range, leading to the decision of converting them to positive values. The nulls here are representing about a quarter of the data, and the decision was to use an iterative imputer based on regression with the rest of the values.
The decisions on this column are reflected in Q2, which was initially 73455.00 to 79359.34 after the changes.

- Cancellation Year & Cancellation Month have a high percentage of nulls (87.65%), which is expected to represent a small portion compared to active members. There is also a 0.63 correlation between these variables, which is considered a high correlation. This can be viewed in G1 & G2 (Graphs in the 3. Data Analysis notebook).

- Creation of a category column to group ranges. This action is useful for better graphic visualization.


### DATA ANALYSIS

#### G1. HEATMAP: CORRELATIONAL GRAPH
Correlational heatmap using the Pearson method for the numeric columns, the method choice considering the linear visualization.  
Results show strong positive relations between:

    - *Flight Booked* & Flight Companions, Total Flights, Distance, Points accumulated
    - *Flight Companions* & Points Accumulated, Distance, Total Flights
    - *Total Flights* & Points Accumulated, Distance
    - *Distance* & Points Accumulated
    - *Points Redeemed* & Dollar Cost Points Redeemed
    - *Enrollment Year* & Cancellation Year

#### G2. REGPLOT: CORRELATION ENROLLMENT & CANCELLATION YEAR 

To represent the correlation between those tables and confirm the theory that cancellations grow as the number of members increases.

#### G3. HISTPLOT & BOXPLOT: UNDERSTANDING SALARIES

- Here you can see the concentration of the data near the median.  
- Confirms high deviation in the salary, where 75% of the data is below 82940.0 (data from .describe) and the other 25% are between this number and the max value (407228.0).  
- Also confirms the small amount of outliers below the median.

#### G4. BARPLOT: CORRELATION MONTHLY FLIGHTS PER YEAR & BOOKINGS

- It is notable the consistency in the number of monthly flights in both years. 
- It is also understandable the increase in flights in 2018 compared to the previous year.
- July, followed by June, August, and December, are consistently the high peak months for bookings.

#### G5. SCATTERPLOT: DISTANCE VS POINTS ACCUMULATED 

- There is a clear positive correlation between these variables, as both increase simultaneously.
- It can be stated that for every 1,000 units of distance, there is an increase of 100 points, which represents an average of 10%.
- The heatmap (G1) highlights this correlation, and the graph also shows data for flights with companions.
- Another interesting insight is that flights with companions are often associated with longer distances.

#### G6. BARPLOT: CLIENT DISTRIBUTION BY PROVINCES

- The graph shows that Ontario, British Columbia, and Quebec are the provinces with the most clients.
- This relation is expected, considering they are the most populated provinces (external source).

#### G7. CROSSTAB & BARPLOT: CLIENTS' SALARY VS EDUCATION LEVEL

- First, you can observe that the majority of the clients have a bachelor’s degree and are in the low salary range, followed by a small representation of other education levels in this salary range.
- Second, clients with a doctoral degree are predominantly classified in the medium and high salary ranges.

#### G8. BAR PLOT: PROPORTION OF CLIENTS AND LOYALTY CARDS

On the first graph:
    - In this graph, you can see the linear growth between the 3 loyalty programs.
    - Aurora represents nearly half of the Star clients.

On the second graph:
    - Salary scale was added in the analysis, reflecting a correlation between salary and loyalty cards.
    - It could be interpreted that Star is a higher-end loyalty program.

#### G7. PIE AND COUNTPLOT: DISTRIBUTION BASED ON GENDER AND MARITAL STATUS

- On the first figure, there is an even distribution between male and female clients.
- The same happens on the second graph, where marital status is also following a similar distribution.
- It’s safe to say that married clients are the largest group in this category, followed by singles and divorced clients, respectively.

#### EXTRA: TESTING FUNCTION
- Adding graphs into a function is something I would progress as the next step. This would encourage smoother and clearer code.