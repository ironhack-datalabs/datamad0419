# Supervised Machine Learning Project  

## Heart Desease Diagnostics

### Introduction

Heart disease describes a range of conditions that affect your heart. Diseases under the heart disease umbrella include blood vessel diseases, such as coronary artery disease; heart rhythm problems (arrhythmias); and heart defects you're born with (congenital heart defects), among others.

The term "heart disease" is often used interchangeably with the term "cardiovascular disease." Cardiovascular disease generally refers to conditions that involve narrowed or blocked blood vessels that can lead to a heart attack, chest pain (angina) or stroke. Other heart conditions, such as those that affect your heart's muscle, valves or rhythm, also are considered forms of heart disease.

Many forms of heart disease can be prevented or treated with healthy lifestyle choices.

From: https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118

### Project Description

In this project we want to apply different Machine Learning (ML) algorithms to try to predict if a person suffers from heart desease or not.  To train the program we used a data set from Kaggle that contains information of 70k people. 

**Data Set Features:**

* Age | Objective Feature | age | int (days)
* Height | Objective Feature | height | int (cm) |
* Weight | Objective Feature | weight | float (kg) |
* Gender | Objective Feature | gender | categorical code |
* Systolic blood pressure | Examination Feature | ap_hi | int |
* Diastolic blood pressure | Examination Feature | ap_lo | int |
* Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |
* Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal |
* Smoking | Subjective Feature | smoke | binary |
* Alcohol intake | Subjective Feature | alco | binary |
* Physical activity | Subjective Feature | active | binary |
* Presence or absence of cardiovascular disease | Target Variable | cardio | binary |

All of the dataset values were collected at the moment of medical examination.

link: https://www.kaggle.com/sulianova/cardiovascular-disease-dataset

This data set was selected because it contained clean numeric data, so we could focus on training the algorithms rather than cleaning the data.

**Pipeline:**

![flowDiagramPipeline](images/FlowDiagram.png)
