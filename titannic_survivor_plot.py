#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
display kernel density plot of passengers ages with respect to classes, survivor and sex
"""

import pandas as pd
import seaborn as sns    # seaborn is commonly imported as `sns`
import matplotlib.pyplot as plt
titanic = pd.read_csv("train.csv", usecols = ['Survived','Pclass','Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'])
titanic.dropna(inplace=True)
g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue = "Sex")
g.map(sns.kdeplot, "Age", shade=True)
g.add_legend()
sns.despine(left=True, bottom=True)
plt.show()
