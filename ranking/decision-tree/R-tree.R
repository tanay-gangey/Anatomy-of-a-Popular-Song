library(rpart)
library(rpart.plot)

data <- read.csv('../../datasets/normalized-age-data-waf/au_Waf.csv')

dropcols = c("X", "Unnamed..0", "Track.Name", "Artist", "Streams", "URL", "Year", "Month", "Day", "Region")

spotify_data <- data[,!(names(data) %in% dropcols)]
print(head(spotify_data))
tree <- rpart(Position ~ ., data = spotify_data)
rpart.plot(tree, box.palette = "GnBu")
