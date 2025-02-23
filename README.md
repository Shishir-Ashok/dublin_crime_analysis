<div align="center">
    <h1 align="center">Analyzing Crime Patterns and Infrastructure Influence in Dublin</h1>
    <p align="center">A Spatial Analysis Project using PostgreSQL and QGIS</p>
</div>

## Overview

This project explores the spatial patterns of crime across Dublin and investigates the influence of nearby infrastructure on these incidents. By combining administrative boundary data, crime records, and building/amenity information, the project provides insights into regional crime distribution, hotspots, and potential correlations with urban features.

## Features

- **Administrative Boundaries:** Visualization of Dublin’s regional divisions (Dublin City Council, Fingal, South Dublin, Dun Laoghaire-Rathdown).
- **Choropleth Mapping:** Aggregated crime statistics by region to highlight disparities.
- **Heatmap Generation:** Identification of crime hotspots using kernel density estimation.
- **Buffer Analysis:** Analysis of buildings and amenities within a 500-meter radius of crime incidents, with custom SVG markers for hospitals, schools, pubs, and more.
- **PostgreSQL Views:** Dynamic spatial queries that integrate seamlessly with QGIS.

## Data Sources

- **Crime Data:** Geolocated crime incidents in Dublin.
- **Administrative Boundaries:** GeoJSON files for Dublin regions and internal boundaries.
- **Building and Amenities Data:** OpenStreetMap data for infrastructure such as hospitals, schools, pubs, and other relevant amenities.

## Tools & Technologies

- **PostgreSQL & PostGIS:** For spatial data storage, processing, and advanced spatial queries.
- **QGIS:** For data visualization, map production, and spatial analysis.
- **OpenStreetMap:** Source for building and amenity data.
- **SQL:** For creating views and performing spatial operations (e.g., ST_Buffer, ST_Intersects, ST_DWithin).

## Analysis & Observations

- **Regional Disparity:** Dublin City Council exhibits a significantly higher crime count compared to other regions.
- **Hotspots Identification:** Heatmaps reveal concentrated crime clusters in the urban regions which supports the choropleth findings.
- **Proximity Insights:** Buffer analysis shows that many crime hotspots are in close proximity to amenities like pubs, hospitals, and schools, indicating potential correlations that urge further investigation.
- **Actionable Outcomes:** These insights can help inform resource allocation for law enforcement and urban planning to improve community safety.
