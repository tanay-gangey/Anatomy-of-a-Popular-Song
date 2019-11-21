library(rpart)
library(rpart.plot)

data <- read.csv('C:/Users/Tanay/College/3rd_year/5th_sem/Data-Analytics/Project/Anatomy-of-a-Popular-Song/normdata/au_Waf.csv')
spotify_data_2 <- read.csv('C:/Users/Tanay/College/3rd_year/5th_sem/Data-Analytics/Project/Anatomy-of-a-Popular-Song/norm-age-data/au.csv')
data$Age.on.Chart = spotify_data_2$Age.on.Chart

spotify_data <- data[,-(c(1,3,4,5,6,7,8,9,10))]
print(head(spotify_data))
#spotify_data$standing <- c(1:100)
tree <- rpart(Position ~ ., data = spotify_data)
rpart.plot(tree, box.palette = "GnBu")
