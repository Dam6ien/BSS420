df <- read.csv('water.csv')

require(ggplot2)
p <- ggplot(df, aes(x=1:2000)) 
p <- p + geom_line(aes(y=cumsum(base), color='red'), size=1)
p <- p + geom_line(aes(y=cumsum(conservative), color='blue'), size=1)
p <- p + geom_line(aes(y=cumsum(overflow), color='green'), size=1)
p + labs(title = "Reusable water collected over 5 years", x = "Days", y = 'Quantity of water (litres)')
p + guides(color=guide_legend("Usage type")) 
