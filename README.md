Modern Data Science in Python
================

### posit::conf(2026)

by Jeroen Janssens and Richard Iannone

-----

INSTRUCTIONS FOR INSTRUCTORS: Please insert information about your workshop below. Then, add workshop content in the materials folder and link to each session’s materials from the schedule below. You are welcome to add more rows to the schedule. We just ask that you take breaks at the specified times. Once you are done adding information, you can remove these instructions from the README.

Alternatively, you can completely redo the organization of this repo  as a Quarto website or some other format you prefer to host your workshop materials. The only requirement is that your workshop materials are hosted here.

-----

:spiral_calendar: September 14, 2026  
:alarm_clock:     09:00 - 17:00  
:hotel:           ROOM TBD  
:writing_hand:    [pos.it/conf](http://pos.it/conf)

-----

## Description


As the data science landscape evolves, many practitioners are looking to expand their toolkit to include Python. Led by Jeroen Janssens, author of the book Python Polars: The Definitive Guide, and Rich Iannone, creator of the Great Tables package, this workshop will provide a practical, hands-on introduction to an end-to-end Python workflow.

We will move beyond the basics of syntax to focus on a modern stack that prioritizes readability and performance. Using Positron as our development environment, we’ll navigate a complete project lifecycle. The workshop covers:

- Data Manipulation: performant data wrangling using Polars.
- Visualization: implementing the Grammar of Graphics in Python with Plotnine.
- Reporting: creating presentation-ready tables with Great Tables.
- Modeling: building machine learning models using Scikit-Learn.

The workshop is structured around a single case study. You’ll work through a series of exercises designed to help you get familiar with these tools. By the end of the day, you’ll have a good idea of how to translate your data science skills into a Python context and a repository of code examples to apply to future projects. 

This workshop is a great fit for those getting started with data science as well as R users who want to get their feet wet with Python for doing data science.

## Setup

Please complete these steps **before** the workshop.

### Step 1: Install Positron

Download and install the Positron IDE from <https://positron.posit.co>.

### Step 2: Download workshop materials

Clone this repository (or download and extract the ZIP file):

```bash
git clone https://github.com/posit-conf-2026/modern-ds-python.git
```

### Step 3: Install Python packages

Open the `modern-ds-python` folder in Positron and run the following command in the terminal:

```bash
uv sync
```

This will create a virtual environment and install all required packages (Plotnine, Polars, Great Tables, and scikit-learn).

### Step 4: Verify your setup

Open `00_start.ipynb` and run all cells. If everything executes without errors, you're good to go!

## Schedule

| Time          | Activity         |
| :------------ | :--------------- |
| 09:00 - 10:30 | Session 1        |
| 10:30 - 11:00 | *Coffee break*   |
| 11:00 - 12:30 | Session 2        |
| 12:30 - 13:30 | *Lunch break*    |
| 13:30 - 15:00 | Session 3        |
| 15:00 - 15:30 | *Coffee break*   |
| 15:30 - 17:00 | Session 4        |

## Instructor(s)

### Jeroen Janssens

Jeroen Janssens, PhD, is Head of Developer Relations at Posit, PBC. His expertise lies in visualizing data, implementing machine learning models, and building solutions using Python, R, JavaScript, and Bash. He’s passionate about open source and sharing knowledge. He’s the author of Python Polars: The Definitive Guide (O’Reilly, 2025) and Data Science at the Command Line (O’Reilly, 2021). Jeroen holds a PhD in machine learning from Tilburg University and an MSc in artificial intelligence from Maastricht University. He lives with his wife and two kids in Rotterdam, the Netherlands.

### Richard Iannone

ADD BIO.

-----

![](https://i.creativecommons.org/l/by/4.0/88x31.png) This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
