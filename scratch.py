import polars as pl

from plotnine import *
from plotnine.data import anscombe_quartet


anscombe_quartet
ggplot(anscombe_quartet, aes("x", "y")) + geom_point()

penguins = pl.read_csv("data/penguins.csv", null_values="NA")

(
    ggplot(penguins, aes(x="year", y="bill_length_mm")) +
    geom_boxplot()
)

(
    ggplot(penguins, aes(x="year", y="bill_length_mm")) +
    geom_point()
)

from plotnine.data import mpg

ggplot(mpg, aes("displ", "hwy")) +\
    geom_point(aes(colour="class")) +\
    geom_smooth(se=False, method="lm") +\
    scale_color_brewer(palette='Set1')
