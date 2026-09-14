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
- 