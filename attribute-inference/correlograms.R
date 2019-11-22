library(corrgram)
library(ellipse)

path = "../datasets/"

us = read.csv(paste0(path,"normalized-age-data-waf/us_waf.csv"))
au = read.csv(paste0(path,"normalized-age-data-waf/au_waf.csv"))
gb = read.csv(paste0(path,"normalized-age-data-waf/gb_waf.csv"))
jp = read.csv(paste0(path,"normalized-age-data-waf/jp_waf.csv"))
ph = read.csv(paste0(path,"normalized-age-data-waf/ph_waf.csv"))

nc = c(1.10,11,12,13,15,16,17,18,19,20,21)

us_cor = cor(us[,nc])
plotcorr(us_cor, main = "US Correlogram", col = "blue", type = "lower")

au_cor = cor(au[,nc])
plotcorr(au_cor, main = "AU Correlogram", col = "blue", type = "lower")

gb_cor = cor(gb[,nc])
plotcorr(gb_cor, main = "GB Correlogram",  col = "blue", type = "lower")

jp_cor = cor(jp[,nc])
plotcorr(jp_cor, main = "Japan Correlogram",  col = "blue", type = "lower")

ph_cor = cor(ph[,nc])
plotcorr(ph_cor, main = "Phillipines Correlogram",  col = "blue", type = "lower")