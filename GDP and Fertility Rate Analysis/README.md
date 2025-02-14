# Maternal Mortality and GDP Analysis 🌍📊

This project visualizes and analyzes maternal mortality rates in relation to GDP across countries over time. It leverages data from the World Bank's World Development Indicators to explore the disparities in maternal health outcomes and economic development.

## Project Overview

Maternal mortality rate, defined as the number of maternal deaths per 100,000 live births, is a critical indicator of maternal health. This project highlights:
- The relationship between economic development (GDP per capita) and maternal mortality rates.
- Disparities in healthcare access between low-income and high-income nations.
- The role of global efforts to reduce maternal mortality through improved healthcare access and affordability.

## Features

1. **Interactive Choropleth Maps**:
   - Visualize GDP per capita (`gdp.csv`) and maternal mortality rates (`mortality.csv`) globally over time.
   - Animated sliders allow users to explore changes from 1990 to 2020.

2. **Dynamic Scatter Plot**:
   - The relationship between Maternal Mortality Rate and GDP is interactive.
   - Hovering over each data point (dot) reveals details about the region, country name, GDP, and maternal mortality rate for that country.

3. **Data Sources**:
   - GDP data: `data/gdp.csv`
   - Maternal mortality data: `data/mortality.csv`

4. **Sustainable Development Goals (SDG)**:
   - Aligns with SDG Target 3.8: Achieve universal health coverage and reduce financial barriers to essential healthcare services.

## Requirements

- A web browser with JavaScript enabled.
- A local server to serve the files (e.g., Python's `http.server` or Node.js's `http-server`).

## Usage

1. Clone or download the repository.
2. Start a local server in the project directory:
   - Using Python:
     ```bash
     python -m http.server
     ```
   - Using Node.js:
     ```bash
     npx http-server
     ```
3. Open `index.html` in your browser (e.g., `http://localhost:8000`).
4. Interact with the choropleth maps, scatter plot, and sliders to explore trends.

## Data Details

### GDP Data (`gdp.csv`)
- Contains country-level GDP per capita data from 1990 to 2020.
- Key columns:
  - `Country Code`: ISO Alpha-3 country codes.
  - `Year`: Year of observation.
  - `GDP`: GDP per capita (in USD).

### Mortality Data (`mortality.csv`)
- Contains country-level maternal mortality rates from 2000 to 2020.
- Key columns:
  - `Country Code`: ISO Alpha-3 country codes.
  - `Year`: Year of observation.
  - `MortalityRate`: Maternal mortality rate (deaths per 100,000 live births).

## Contributions

This project was developed to raise awareness about global disparities in maternal health and the need for equitable healthcare access. Contributions are welcome!