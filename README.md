# Automotive-Industry-Analysis-Report---EV-Price

Project Purpose
----------------
Due to environmental impact and concerns, the automotive industry is initiating their movement towards electric vehicles.
However, electric vehicles are readily avaialbe in the market due to their low production rate. It would be difficult for 
customers to identify the optimal price for certain vehicles depending on their specifications. The goal of this analysis is
to predict the price of a certain vehicle regardless of its brand and relying soely on their specs. Many vehicles within the
datasets are future electric vehicle models which are presented by many automotive companies.

![Screenshot](https://github.com/wjj1019/Automotive-Industry-Analysis-Report---EV-Price/blob/main/Data%20Scrape/EV%20growth.jpeg)


Data
-------
Datasets were obtained from webscraping [EV Database](https://ev-database.org/#sort:path~type~order=.rank~number~desc|range-slider-range:prev~next=0~1200|range-slider-acceleration:prev~next=2~23|range-slider-topspeed:prev~next=110~450|range-slider-battery:prev~next=10~200|range-slider-eff:prev~next=100~300|range-slider-fastcharge:prev~next=0~1500|paging:currentPage=0|paging:number=9)

Methods
----------

1. EDA
- The dataset contained vehicles that were sports based and has not yet released but their specs were too high relative to others
(Tesla Roadster - Not released but specification far beyond normal) -> Outliers and therefore removed from the dataset
- Dropping models without price

2. Machine Learning - Regression
- Cross Validation Type: Shuffle Split 
- Ensemble models: Decision Tree, Random Forest
- Boosting Models: Gradient Boost, XGBoost
*Boosting models performed well on the dataset, Ensemble model showed overfitting 

3. Hyperparameter Tunning
- Compare the difference in performance between: GridSearchCV, RandomSearchCV and Optuna -> Optuna with highest performance
- No significant improvement for Ensemble Models. 

4. Evaluation
- MSE, RMSE, MAE
- Learning Curve to identify overfitting and overall performance

5. Clustering
- Kmans: Elbow method to identify the optimal cluster number by computing WCSS (distance from centroid)
- PCA: Dimensionality Reduction for better performance for Kmeans (Due to the Euclidean measurement sensitivity to dimension)
- Kmeans + PCA: 2 overall principal components explained 90% of the variance and overall of 4 clusters from Kmeans
- Gaussian Mixture
- DBSCAN: Optimal Epsilon computation using Nearest Neighbor
- Mean Shift

6. Recommendation Systems
- Item Based recommendation using KNN 
- 

Conclusion/Findings
---------------------
- Boosting models performed well on the dataset, Ensemble model showed overfitting 
- No significant improvement for Ensemble Models when hyperparameter tunning performed
- Kmeans + PCA showed clear seperations between groups under 2 dimensional space (PCA1 PCA2)
- DBSCAN was expected to perform better due to the fact it's outlier elimination ability
- Recommendation Systems was designed so that similar vehicles within certain specifications are recommended to the customers

Deployment
-----------
Web application using Flask and Heroku

![Screenshot](https://github.com/wjj1019/Automotive-Industry-Analysis-Report---EV-Price/blob/main/Data%20Scrape/Deployment.png)

