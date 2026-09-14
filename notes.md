# Workshop notes

- The default uv behavior seems to ignore my MacPorts python installations
    - To get it to use the python I want: `uv venv --python /opt/local/bin/python3.14 --python-preference only-system`
- https://jeroenjanssens.com/heuristics/
    - Some rules for how to convert ggplot2 code to plotnine code
- Polars data frames are immutable and pandas dfs are mutable
- Why would you use polars vs. pandas dfs?
    - Usually because polars is much faster
- It's not possible to do a line by line translation from pandas to polars

## Polars
- Written in rust
- Also in R and JS, but python is the most mature
- "Blazingly fast"
- Pretty good API (though still not as good as tidyverse)
- 50% of the API is expressions
- with_columns vs. select
    - `select` gives you only the columns you specify
    - `with_columns` will give you all existing columns by default
- Jeroen doesn't like `with_columns` because it's not a very and doesn't match the rest of the API, but now it's too late
    - `with_columns` comes from Spark
- **Expressions** don't do anything themselves (they are lazy)
    - They are basically a tree describing how to construct the result (one or more series)
    - The methods are what actually get something done
- Expressions: aggregation, array, binary, categories, columns/names, computation, extension types, functions, list, manipulation/selection, meta, name, operators, string, struct, temporal, window
- `pandas` does not have expressions -- everything is evaluated eagerly, not lazily
- Q: can you generalize a set of data wrangling steps with polars expressions? e.g. remove_nas(colname="myColname")
    - Yes, but write a python function that returns an expression
- Expressions
    - Lazy
    - Function and data dependent
    - Reusable
    - Expressive
    - Efficient
    - Idiomatic
- "Without pandas, we wouldn't have polars"
- If you're working with other packages that require `pandas` dataframes as the input (e.g. require an index), you can just use `pl_df.to_pandas()`
    - The key here is to do as much as you can in polars first before converting the end result to pandas
- `plotnine` does work on polars dataframes, but only because it converts the df to a `pandas` df immediately behind the scenes
- The default way of using polars is the "eager" API, but there's also a lazy API with `.lazy()`
- The various `read_*()` functions have `scan_*()` equivalents that give you a lazy polars df instead of an eager one
- There are some cases where having the entire data workflow as a lazy operation will be slower
- Polars is not able to determine when (if you have multiples of an operation) it can be reused
    - There's an example of this in the book (in ch1 ETL showcase) where polars does the same join twice

## Great Tables

