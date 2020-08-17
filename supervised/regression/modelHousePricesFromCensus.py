'''
Notes:
1) Dataset: Housing Prices dataset from StatLib repoistory.
    a) Data from 1990 California census
    b) metrics: population, median income, median house price, ... per each
        "block group" in California (Block groups are smallest unit for US 
        Census Bureau data. Referring to as districts for simplicity.)
    c) Supervised, regression (multiregression, univariate), batch learning.
        .Multiregression b/c multiple features (population, median income, etc)
        .Univariate b/c value prediction (district's median house price)
    d) Using a model to learn from the dataset and predict median housing price
        in any district, given all the other metrics for that 
    e) RMSE (Root Mean Square Error) equation:
        RMSE(X, h) = sqrt( (1/m) SUMMATION(1-m) [h(x^i) - y^i]^2 )
        where:
        - m is the number of instances in the dataset
        - x^i is the vector ith instance's feature values (excluding the label)
        - y^i is the ith label (ouput value for that instance)
        - X is matrix containing all feature values (excluding labels) of all
            instances in the dataset.
            The ith row in X = (x^i)^T , i.e. x^i is the tranpose of the ith row
            in X.
        - h is the system's prediction function (or hypothesis)
            y^1 = h(x^1) ... machine learning version of y = f(x)
        - RMSE(X, h) is the cost function measured on the set of the examples
            using hypothesis h
        - Remember X and x^i are vectors, but m and y^i are scalars.
        - RMSE is sensitive to outliers. It is usually best suited for error
            measuring with regression, but if there are signicant amounts of 
            outliers, something such as MAE (mean absolute error) may be better.
            RMSE does well with bell-shaped curve distributions where outliers
            are exponentially rare.

        - Both RMSE and MAE are ways to measure the distance b/w vectors (the
            distance formula is in it just with different symbols. So this is 
            essentially measuring error by calculating the "distance" between
            the values of the hypothesis vector and given/"label" vector).
        
'''
