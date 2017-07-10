library(capushe)
#data(datacapushe)
#capushe(datacapushe)
#plot(capushe(datacapushe))

setwd('desktop');
getwd();
#setwd('EMAlgo');

library(xlsx)
data=read.xlsx(file="Slope\ 3\ Adjusted\ -\ Model\ Selection\ via\ CAPUSHE\ -\ 12\ Jun\ 2017\ 14-24-41.xls",sheetIndex =1, header=TRUE)
ddse = DDSE(data)
djump = Djump(data)

plot(capushe(data))

plot(ddse)
#png(filename="DDSEonNIPSAdjustedEM.png")
#dev.off()
summary(ddse)
summary(djump)
