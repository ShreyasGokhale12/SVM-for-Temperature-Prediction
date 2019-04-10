This was part of a project in which we had to compare the performance of SVM, Regression, Multivariate Time Series using ARIMA etc to find which model fits the data best and gives minimum error on prediction. I worked on SVM.

The datset consists of 14 year data of Temperature , Pressure ,	Relative , Humidity , Snow Depth , Wind Direction and	Wind Speed. The readings are on 30 minutes basis. The factors which will affect temperature amongst these are chosen . All of them are regarded as 'features' and temperature readings are 'label'. The testing data consists of 3 days from the month of May in 15th year. Temperature is predicted based on the feature values of these days. 

When the actual temperature readings are calculated, the predicted and actual values for these 3 days are plotted on top of other using matplotlib to show the small difference between the two.
