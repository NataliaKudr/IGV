rm(list=ls()) 

par(mfrow=c(1,1))
par(mar=c(4.5, 4.5, 0.5, 0.5))
HS1 <- Kappa[2,11:35]
HS2 <- Kappa[2,4:5]
HS3 <- Kappa[2,2:3]
HS4 <- Kappa[2,6:10]

data1 <- Kappa[,11:35]
data2 <- Kappa[,4:5]
data3 <- Kappa[,2:3]
data4 <- Kappa[,6:10]

CJ <- CJREGION[,2:3]


par(mfrow=c(1,1))
boxplot(data1, cex = 1,cex.lab=.5, cex.axis=.5, cex.main=.7, cex.sub=.5, las= 2, # no ticks on y axis, all ticks on x
        family="Times New Roman") 
points(1:length(HS1),HS1, pch=19, cex = 0.5, col="red")
text(14, 40,
     "NL", family="Times New Roman", cex = 0.6, col = "blue",font =  1:5)
text(1, 47,
     "NL", family="Times New Roman", cex = 0.6, col = "blue",font =  1:5)


par(mfrow=c(1,3))
boxplot(data2, cex = 1,cex.lab=.7, cex.axis=.7, cex.main=.7, cex.sub=.7, las= 2, # no ticks on y axis, all ticks on x
        family="Times New Roman") 
points(1:length(HS2),HS2, pch=19, cex = 0.5, col="red")
boxplot(data3, cex = 1,cex.lab=.7, cex.axis=.7, cex.main=.7, cex.sub=.7, las= 2, # no ticks on y axis, all ticks on x
        family="Times New Roman") 
points(1:length(HS3),HS3, pch=19, cex = 0.5, col="red")
boxplot(data4, cex = 1,cex.lab=.7, cex.axis=.7, cex.main=.7, cex.sub=.7, las= 2, # no ticks on y axis, all ticks on x
        family="Times New Roman") 
points(1:length(HS4),HS4, pch=19, cex = 0.5, col="red")
text(1, 45,
     "PP", family="Times New Roman", cex = 0.7, col = "blue",font =  1:5)

par(mfrow=c(1,2))
plot(CJ, cex = 1,cex.lab=.7, pch = c(1:6), cex.axis=.7, cex.main=.7, cex.sub=.7, las= 2, xlim=c(0, 1), ylim=c(0, 1),xaxt='n', yaxt='n', # no ticks on y axis, all ticks on x
        family="Times New Roman") 
axis(side=2, at=0,"Unplaced",las = 1, family="Times New Roman",cex.lab=.7, pch = c(1:6), cex.axis=.7, cex.main=.7, cex.sub=.7)
axis(side=2, at=1,"Chr2",las = 1, family="Times New Roman",cex.lab=.7, pch = c(1:6), cex.axis=.7, cex.main=.7, cex.sub=.7)
axis(side=1, at=0,"Unplaced",las = 1, family="Times New Roman",cex.lab=.7, pch = c(1:6), cex.axis=.7, cex.main=.7, cex.sub=.7)
axis(side=1, at=1,"Chr2",las = 1, family="Times New Roman",cex.lab=.7, pch = c(1:6), cex.axis=.7, cex.main=.7, cex.sub=.7)

legend("center", "Times New Roman"
       , legend=c("HS","PA","PP","PT", "NL","GG"),
       pch = c(1:6), cex=0.6)


title(main="Variation in number of available kappa v-gene sequences in primate species", line=1.2, cex.lab=1.0, family="Calibri Light")

