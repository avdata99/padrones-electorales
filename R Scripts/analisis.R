setwd("~/Repos/pdelboca/padrones-electorales/R Scripts")
library(plyr)
library(lubridate)

# Read Data
df <- read.csv('../datos_limpios.csv')
summary(df)

# Domicilios con más de 10 votantes por padron
agg <- aggregate(DNI ~ Domicilio + Padron, data = df, FUN = length)
agg <- agg[order(agg$DNI, decreasing = TRUE),]

votantesPorDomicilio <- agg[agg$DNI > 10, ]
votantesPorDomicilio <- votantesPorDomicilio[order(votantesPorDomicilio$Padron),]
colnames(votantesPorDomicilio) <- c("Domicilio", "Padron", "Votantes")
votantesPorDomicilio

# DNIs repetidos
dnis <- aggregate(. ~ DNI, data = df, FUN = length)
dnis <- dnis[dnis$Padron > 1, ]
personasRepetidas <- df[df$DNI %in% dnis$DNI,]
personasRepetidas <- personasRepetidas[order(personasRepetidas$DNI),]
length(unique(personasRepetidas$DNI))
personasRepetidas

# Cantidad de Votantes por Clase
print("Porcentaje de Filas con Clase:")
print(sum(!is.na(df$Clase)) / nrow(df))
hist(df$Clase, breaks = 100, main = "Histograma Clase Votantes", xlab = "Clase")


# Votantes más viejos
df$EdadAproximada <- year(Sys.Date()) - df$Clase 
hist(df$EdadAproximada, breaks = 100, main = "Histograma Edad Votantes", xlab = "Edad")

# Votantes con más de 100 años
df[!is.na(df$EdadAproximada) & df$EdadAproximada > 100, ]

