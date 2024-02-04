<div align ="center">
  <h1>NYC Collision Study</h1>
  <img src="https://cdn-images.the-express.com/img/dynamic/10/590x/secondary/NYC-crash-24494.jpg?r=1688426470795"/>
</div>
 

<!-- ABOUT THE PROJECT -->
## Motivation for the Study
As a born and rasied New Yorker, I've always taken mass transportation and knew very little about motor vehicles. Motor vehicles play a huge role in to day to day life. From transporting people to places to transporting goods across the city and country. Considering the importance of motor vehicles, and discovering that this data was available through [NYC Open Data](https://opendata.cityofnewyork.us/), we are offer a oppurtunity to gain insight into the factors and patterns of collision that occurs on the NYC roads.

## Built With

Here are the awesome tools we used:

* [Python3](https://www.python.org/download/releases/3.0/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [Plotly](https://plotly.com/)
* [Folium](https://python-visualization.github.io/folium/)
* [Scikit-learn](https://scikit-learn.org/stable/)
* [Geopandas](https://geopandas.org/en/stable/)

### Data Used
All data can be found in the following cloud storage:
- [Dropbox](https://www.dropbox.com/scl/fo/hc058smdtlxnhzkrmqcoc/h?rlkey=sdkp7fopicas4v2zl8szy9jxr&dl=0)
- [Google Drive](https://drive.google.com/drive/folders/1buPeDXX0it8zFgjv90V684iUyqIiMwId?usp=drive_link)

### Datasets Sources
- [NYC Open Data - Motor Vehicle Collisions (Crashes)](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95)
- [NYC Open Data - Motor Vehicle Collisions (Vehicles)](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Vehicles/bm4k-52h4)
- [NYC Open Data - Motor Vehicle Collisions (Person)](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Person/f55k-p6yu)
- [NYC Planning - GIS Zoning Data](https://www.nyc.gov/site/planning/data-maps/open-data/dwn-gis-zoning.page#metadata)
- [NYC Open Data - Zip Code Boundaries](https://data.beta.nyc/en/dataset/nyc-zip-code-tabulation-areas/resource/894e9162-871c-4552-a09c-c6915d8783fb)
- [Weather Data](https://www.wunderground.com/)

## Running the Streamlit App Locally

Clone the project
```bash
$ git clone https://github.com/dwang312/NYC-Collision-Study.git
```

Install package dependencies
```bash
$ cd NYC-Collision-Study/
$ pip install -r requirements.txt
```

Start the Streamlit Project
```bash
$ cd NYC-Collision-Study/streamlit
$ streamlit run Home.py
```

## Conclusions

## Full Project Report

For a detailed analysis, findings, and in-depth exploration, please refer to our full project [report](https://github.com/dwang312/NYC-Collision-Study/blob/main/docs/Research%20Report%20(Fall%202023).pdf).



## Project Structure
```bash
├── Jupyter Notebooks
│   ├── WeatherScraping.ipynb
│   └── data-wrangling
│       ├── collisions_join_weather.ipynb
│       └── collisions_join_zone.ipynb
├── README.md
├── config.yaml
├── data
│   ├── Motor_Vehicle_Collisions_-_Crashes_20231202.csv
│   ├── Motor_Vehicle_Collisions_-_Person_20231202.csv
│   ├── Motor_Vehicle_Collisions_-_Vehicles_20231202.csv
│   ├── NYC-CollisionZonesWeather-Jun2012-Dec2023.csv
│   ├── NYC-Weather-Jan2012-Nov2023.csv
│   ├── NYC-ZipCode-Geodata.geojson
│   ├── NYC-ZoningDistrict-Geodata.json
│   └── NYC-ZoningIDs.csv
├── docs
│   ├── Research Presentation (Fall 2023).pdf
│   └── Research Report (Fall 2023).pdf
├── model
│   └── randomUnderSamplerModel.joblib
├── requirements.txt
└── streamlit
    ├── Home.py
    ├── __init__.py
    ├── __pycache__
    │   └── Home.cpython-312.pyc
    ├── images
    │   └── bk_collision.png
    └── pages
        ├── About.py
        ├── CollisionVisualization.py
        ├── Exploratory.py
        ├── MapVisualization.py
        ├── Model.py
        ├── ViewData.py
        └── __init__.py
```

<!-- MARKDOWN LINKS AND IMAGES -->
