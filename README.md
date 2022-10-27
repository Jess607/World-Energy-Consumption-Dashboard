# World-Energy-Consumption-dashboard
This project is a web application dashboard of the energy consumption of the countries in the world. The dashboard can be found [here](https://countriesenergyconsumption.herokuapp.com/)

# Table Of Contents
* [Installation](https://github.com/Jess607/World-Energy-Consumption-Dashboard#installation)
* [About the Project](https://github.com/Jess607/World-Energy-Consumption-Dashboard#about-the-project)
* [Data Gathering](https://github.com/Jess607/World-Energy-Consumption-Dashboard#data-gathering)
* [File Description](https://github.com/Jess607/World-Energy-Consumption-Dashboard#file-description)
* [Licensing and Authors](https://github.com/Jess607/World-Energy-Consumption-Dashboard#licensing-and-authors)

# Installation 
The code requires:
* `python versions 3 and above`
* `plotly express`
* `dash`
* `dash bootstrap components`
* `pandas`

# About The Project 
Energy transition, decarbonization, green energy- These are the buzz words of the decade. Creating sustainable energy policies to tackle climate change have become paramount for most world leaders and even average citizens. 
In order to craete these policies it is important to take into cognizance energy consumption from various sources and how they differ among regions. 
This project is a web application dashboard that holds a choropleth map of the world deployed on heroku using the gunicorn python web server that shows how energy consumption from various countries and regions differs around the world. It was created using plotly express and dash and deployed on heroku. More information about requirements can be found in the `requirements.txt` file.

# Data Gathering 
Data was gathered from Kaggle's world energy consumption data. 

# File Description 
The folder contains:
* `energy.ipynb` where data wrangling and cleaning was carried out
* `world-energy.py` where the web app dashboard was built 
* `procfile` for heroku deployment 
* `requirements.txt` also for heroku deployment 

# Licensing And Authors
This code was created by Jessica Ogwu and is protected under the Apache License 2.0. Please feel free to use it in your own projects and make modifications as you deem fit.