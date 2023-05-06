# Data Science World Happiness Score Estimator: Project Overview
* Used Kaggle World Happiness Report 2021 dataset. 
* Performed Exploratory Data Analysis, created graphs and charts.
* Created a model that estimates the ladder socre for a country.
* Optimized Random Forest Regressor by using GridSearchCV. 

Note: Project code is in the master branch.

## Code Used
* Python Version: 3.9
* Packages: pandas, numpy, sklearn, matplotlib, seaborn, geopandas

## Data Insight 
The World Happiness Report is a landmark survey of the state of global happiness. The report continues to gain global recognition as governments, organizations and civil society increasingly use happiness indicators to inform their policy-making decisions. The happiness scores and rankings use data from the Gallup World Poll . The columns following the happiness score estimate the extent to which each of six factors – economic production, social support, life expectancy, freedom, absence of corruption, and generosity. 
World Happiness Report 2021 dataset has the following relevant columns for each country:
* Country name
* Regional indicator
* Ladder score
* Logged GDP per capita
* Social support
* Healthy life expectancy
* Freedom to make life choices
* Generosity
* Perceptions of corruption

## EDA
I looked at the distributions of the data, correlations between variables and I plotted various graphs and charts to better undertsand the data.
Ladder scores' distribution is close to normal distribution. 

![image](https://user-images.githubusercontent.com/132287565/236618942-0b5b723c-7f2e-4bfd-9d36-f1b568b0b365.png)

Correlations between variables.

![image](https://user-images.githubusercontent.com/132287565/236619052-b7ffe1b2-418c-44b5-9e51-3fc84d23b8d8.png)

Pivot table of ladder scores grouped by regions. 

![image](https://user-images.githubusercontent.com/132287565/236619089-72c71ca0-239d-4901-81eb-d1d4172ed620.png)

![image](https://user-images.githubusercontent.com/132287565/236619123-979b2a12-e88a-476d-b544-2b431790e917.png)

![map_happiness](https://user-images.githubusercontent.com/132287565/236619144-e7a7a8a9-6768-434e-8c64-559e56c1fba6.png)

## Model Building and Model Performance
First, I split the data into train and test sets with a test size of %20.

I tried Random Forest Regression model and  evaluated it usng Mean Absolute Error. 

RFR MAE: 0.462752

Since ladder scores change between 2.523-7.842 in the dataset, this is a relatively good error value. 

