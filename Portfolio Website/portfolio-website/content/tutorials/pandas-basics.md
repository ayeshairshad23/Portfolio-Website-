---
title: Getting Started with Pandas
date: 2024-01-15
readingTime: 8
category: Python
excerpt: Learn the fundamentals of data manipulation with Python Pandas library
---

# Getting Started with Pandas

Pandas is one of the most powerful data manipulation libraries in Python. In this tutorial, we'll cover the basics to get you started.

## What is Pandas?

Pandas is a Python library that provides data structures and data analysis tools. The two main data structures are:

1. **Series** - A one-dimensional labeled array
2. **DataFrame** - A two-dimensional labeled table

## Installation

\`\`\`bash
pip install pandas
\`\`\`

## Loading Data

\`\`\`python
import pandas as pd

# From CSV
df = pd.read_csv('data.csv')

# From Excel
df = pd.read_excel('data.xlsx')

# Display first 5 rows
print(df.head())
\`\`\`

## Basic Operations

\`\`\`python
# Get shape
print(df.shape)  # (rows, columns)

# Get column names
print(df.columns)

# Get data types
print(df.dtypes)

# Get summary statistics
print(df.describe())
\`\`\`

Continue learning and explore more advanced features!
