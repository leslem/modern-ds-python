from polars import scan_csv
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

fruit = pl.read_csv("data/fruit.csv")
fruit
fruit.select(
    pl.col('name'),
    pl.col('^.*or.*$'),
    pl.col('weight') / 1000,
    'is_round'
)
# The is_round column was AI-generated and doesn't seem to be accurate

fruit.with_columns(
    pl.lit(True).alias('is_fruit'),
    is_berry=pl.col('name').str.ends_with('berry')
)

fruit.filter(
    (pl.col('weight') > 1000)
     & pl.col('is_round')
)

fruit.group_by(pl.col('origin').str.split(' ').list.last()).agg(
    pl.len(),
    average_weight=pl.col('weight').mean()
)

fruit.sort(
    pl.col('name').str.len_bytes(),
    descending=True
)

origin_list = pl.col('origin').str.split(' ').list
fruit.select(
    first=origin_list.first(),
    last=origin_list.last()
)
# in polars you CANNOT refer back to new columns you've created earlier in the same expression
# because they are evaluated in parallel

# Save an expression and reuse it later
is_orange = (pl.col('color') == 'orange').alias('is_orange')
fruit.with_columns(is_orange)

# Eager vs. lazy API for a dataframe
penguins = pl.read_csv("data/penguins.csv")
penguins
summary = penguins.group_by("species", "sex").agg(
    pl.col('body_mass_g').mean().alias('avg_mass_g'),
    pl.col('body_mass_g').count().alias('count')
)
summary
summary.head(5)

penguins = pl.scan_csv("data/penguins.csv")
penguins
penguins.show_graph()
summary = penguins.group_by("species", "sex").agg(
    pl.col('body_mass_g').mean().alias('avg_mass_g'),
    pl.col('body_mass_g').count().alias('count')
)
summary
summary.show_graph()
summary.collect()
summary.head(5)
summary.head(5).collect()
summary.profile()
summary.explain()








# Work through the cheat sheet with penguins
penguins = pl.read_csv('data/penguins.csv', null_values="NA")
penguins.filter(
    pl.col('island') == 'Dream'
)
penguins.with_row_count()
# It already has a row id in the csv
penguins.with_row_index('rowid')  # this adds another column, rather than letting you set an existing column

penguins.schema
penguins.dtypes
penguins.glimpse()
penguins.describe()
penguins.estimated_size()
penguins.select(pl.col('rowid').cast(pl.UInt64))
penguins.select(pl.col('rowid').cast(pl.Int8, strict=False))

penguins.select('species', 'bill_depth_mm')
penguins.select(pl.col('body_mass_g') * 0.03527396) # convert to oz
penguins.select(body_mass_oz = pl.col('body_mass_g') * 0.03527396) # convert to oz
penguins.select(pl.col('^bill')) # without a full match, regex select doesn't work
penguins.select(pl.col('^bill.*$')) 

import polars.selectors as cs


