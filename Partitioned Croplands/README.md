
<div align="center">
  
# Partitioning the Watered Lands: A Framework for Distinguishing Rainfed and Irrigated Croplands at Continental Scale

</div>


## 1. Introduction

- Sustainable agricultural water management (AWM) can be informed by accurate mapping of the location and extent of croplands. However, comparative analyses of many remote-sensing land use and landcover (LULC) products reveals significant disparities in global cropland identification.

- Compounding this issue, many existing products fail to differentiate between rainfed and irrigated agriculture, often aggregating them into a singular cropland category. As a result, it is difficult to identify the different sources of water, whether blue or green water, for their management. 

- Yet, agriculture is the largest consumer of freshwater globally, and therefore, meeting the Sustainable Development Goal (SDG) of ‘Zero Hunger’ and other associated SDGs, requires an understanding of the pathways, fluxes, and footprints of water in croplands. 

- In this study, a framework incorporating the Budyko model is applied to partition evapotranspiration (ET) into green and blue fluxes and thereby identify rainfed and irrigated croplands in Africa. This cropland partitioning is done using remote sensing precipitation (P), actual and reference ET, and different LULC products for continental Africa. The specific objectives are:

    - To assess the level of agreement between different LULC products for Africa; 
    - To generate an alternative composite cropland map which overcomes the high disagreement and errors inherent in individual crop masks of LULC products;
    - To demonstrate a scalable approach to partition croplands into irrigated and rainfed classes using the Budyko model; and 
    - To apply this approach in partitioning croplands to the individual LULC products and thereby demonstrate its applicability. 
## 2. Study Area and Data

### Study area
- Africa
### Climate dataset
- MSWEP precipitation
- SSEBoP actual ET
- WaPOR potential ET
### Landcover dataset
- Eight common remote sensing LULC products

| <td rowspan="5"></td>              | **Product** | **Spatial res. (m)**     | **Temporal res./ Years**   |
|------------------|-----|--------------|--------------|
| <td rowspan="3" align="center" style="transform: rotate(0deg);">**Climate datasets**</td> | MSWEP v2.0 precipitation  | ∼11,000    | Monthly    |
|                  | SSEBop v6.0 actual evapotranspiration (ET)  | ∼1,000  | Monthly     |
|                  | WaPOR v2.0 potential evapotranspiration (ETo)  | ∼19,000      | Monthly     |
| <td rowspan="8" align="center" style="transform: rotate(0deg);">**Landcover and land use (LULC) datasets**</td> |  MODIS LC (MCD12Q1)  | 500| 2003-2020      |
|                  | CCI LC V2 | 300       | 2000-2021  |
|                  | Sentinel-2  | 10       | 2017-2021       |
|                  | Copernicus (CGLS-LC100 v3.0)  | 100       | 2015-2019       |
|                  | 3GCEP30  | 30      | 2016-2020 |
|                  | GLC-SHARE  | 1000     | 2013    |
|                  | GlobCover  | 300      | 2005, 2009       |
|                  | WaPOR  v2.0  landcover  | 250  | 2009, 2020       |
<p align="center"> Table 01 - Data and Resolutions </p>

<div align="center">

### Cropland Validation

</div >

![Africa Data](/Figures/Data_africa.png)
<p align="center"> Figure 01 - Cropland Validation Points </p>

### Validation dataset
- 955 (554 irrigated and 401 rainfed) cropland locations 
- Curated by International Crops Research Institute for the Semi-Arid Tropics (ICRISAT)
- From field visits and high-resolution imagery from 2015- 2019

## 3. Methods 

<div align="center">

### Framework for partitioning croplands into rainfed and irrigated cropland areas

</div >

![Framework](/Figures/Framework.png)
<p align="center"> Figure 02 - Framework for partitioning croplands into rainfed and irrigated cropland areas </p>

<div align="center">

![E_P_Equation](/Figures/E_P_Equation.png)
</div >

- <p > LUWA- Land Use for Water Accounting </P>
- <p>TIF- Tag Image File format</P>

<p>The framework incorporates the Budyko model, an empirical representation of a river basin’s long-term water and energy balance under steady state conditions. Considering available energy  (i.e.: potential evapotranspiration (𝐸𝑇)),  and water (i.e.: precipitation (𝑃)), it is possible to determine ‘excess’ ET using the Budyko model and thereby identify any additional water input i.e., blue water.
</P>
<div align="center">

### Validation of cropland class

</div>

1. Independent accuracy assessment of crop masks using  crop validation dataset

<div align="center">

| **Product**      | **Correct points** | **Accuracy** assessment |
|--------------|----------------|---------------------|
| WaPOR        | 868            | 91%                 |
| Copernicus   | 807            | 85%                 |
| GLC-SHARE    | 779            | 82%                 |
| MODIS LC     | 604            | 63%                 |
| Sentinel-2   | 542            | 57%                 |
| CCI LC V2    | 504            | 53%                 |
| GlobCover    | 475            | 50%                 |

</div>

<p align="center">Table 02 - Independent accuracy assessment of crop masks based on validation data </p>

2. Comparison of the area of each crop mask to country level data on cultivated area from FAO’s Aquastat data portal

![Comparison of Area](/Figures/Comparison_of_areas_.png)
<p align="center"> Figure 03 - Cropland area in landcover products vs FAQ cultivated area </p>