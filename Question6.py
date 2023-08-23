# Q6. Consider a dataset with a mean of 50 and a standard deviation of 10. If we assume that the dataset
# is normally distributed, what is the probability that a randomly selected observation will be greater
# than 60? Use the appropriate formula and show your calculations.

# Answer - 

# Mean = 50 
# Standard deviation = 10 
# X,datapoint = 60

# The formaula which we used is:
#   Z_score = (datapoint - mean) / standard deviation 

z_score = (60 - 50)/10
print(z_score)  # O/p = 1

# and the probability associated with Z score 1 is 0.8413 which 84%

# 84% is the probability of getting dataset greater then 60