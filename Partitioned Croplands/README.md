
<div align="center">
  
# Partitioning the Watered Lands: A Framework for Distinguishing Rainfed and Irrigated Croplands at Continental Scale

</div>

<p> 

**A. Owusu<sup>1</sup>, S. Kagone<sup>2</sup>, M. Leh<sup>3</sup>, N. M. Velpuri<sup>3</sup>, M. Gumma<sup>4</sup>, B. Ghansah<sup>1</sup>, P. Thilina-Prabhath<sup>3</sup>, K. Akpoti<sup>1</sup>, K. Mekonnen<sup>5</sup>, P. Tinonetsana<sup>3</sup>, I. Mohammed<sup>4</sup>** 

</P>

<p>

<sup>1</sup>International Water Management Institute (IWMI), Accra, Ghana, <sup>2</sup>ASRC Federal Data Solutions, Contractor to U.S. Geological Survey (USGS) Earth Resources Observation and Science (EROS) Center, Sioux Falls, USA, <sup>3</sup>International Water Management Institute (IWMI), Colombo, Sri Lanka, <sup>4</sup>International Crops Research Institute for the Semi-Arid Tropics (ICRISAT), Hyderabad, India, <sup>5</sup>International Water Management Institute (IWMI), Addis Ababa, Ethiopia

</p>


## Acknowledgements

<p>This study was part of the Digital Innovation for Water Secure Africa (DIWASA) project. We gratefully acknowledge Helmsley Charitable Trust for its financial support to DIWASA project. The authors would like to acknowledge the remote sensing dataset providers and developers for producing and making their datasets available on the internet. The authors' views are their own and do not necessarily reflect the views of the funder. 
</p>




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

<div align="center">

<small> 

**Table 01 - Remote-sensing climate, and landcover and land use (LULC) products used in this study** 

</small>

</div>

<div align="center">

### Cropland Validation

</div >

![Africa Data](/Figures/Data_africa.png)

<div align="center">

<small> Figure 01 - Independent validation dataset of 955 rainfed and irrigated cropland locations across Africa </small>

</div>

### Validation dataset
- 955 (554 irrigated and 401 rainfed) cropland locations. 
- Curated by International Crops Research Institute for the Semi-Arid Tropics (ICRISAT).
- From field visits and high-resolution imagery from 2015- 2019.

## 3. Methods 

<div align="center">

### Framework for partitioning croplands into rainfed and irrigated cropland areas

</div >

![Framework](/Figures/Framework.png)

<div align="center">

![E_P_Equation](/Figures/E_P_Equation.png)
</div >

<div align="center">

<small> Figure 02 - Methodology followed in deriving rainfed and irrigated cropland areas from remote-sensing landcover products. NB: LUWA- Land Use for Water Accounting; TIF- Tag Image File format </small>

</div>

- <p > LUWA- Land Use for Water Accounting </P>
- <p>TIF- Tag Image File format</P>

<p>The framework incorporates the Budyko model, an empirical representation of a river basin’s long-term water and energy balance under steady state conditions. Considering available energy  (i.e.: potential evapotranspiration (𝐸𝑇)),  and water (i.e.: precipitation (𝑃)), it is possible to determine ‘excess’ ET using the Budyko model and thereby identify any additional water input i.e., blue water.
</P>
<div align="center">

### Validation of cropland class

</div>

1. Independent accuracy assessment of crop masks using  crop validation dataset.

<div align="center">

![Accuracy_assessment](/Figures/Accuracy_assessment_table_1.PNG)

</div>

<div align="center">

<small>Table 02 - Results of independent accuracy assessment of crop masks from landcover products (NB: GCEP30 was excluded from the accuracy assessment as the validation dataset used in this study was also used in producing GCEP30) </small>

</div>

2. Comparison of the area of each crop mask to country level data on cultivated area from FAO’s Aquastat data portal.

![Comparison of Area](/Figures/Comparison_of_areas_new.png)

<div align="center">

<small> Figure 03 - Country-level FAO Aquastat data on cultivated area versus seven remote-sensing landcover products (where R2 is the the coefficient of determination) </small>

</div>

<div align="center">

### Derivation of High Confidence Cropland Map (HCCM)

</div >

![Comparison of Area](/Figures/Degree_of_agreement_&_Landcover_type.PNG)

<div align="center">

<small> Figure 04 - Degree of agreement (in %) of three cropland masks with highest scores in two-fold assessment (left) and High confidence cropland mask (HCCM) based on ≥ 66 % agreement between the three cropland masks with highest scores in two-fold assessmen (right) </small>

</div>

## 4. Results

<div align="center">

### Agreement between landcover products

</div >

![Agreement between landcovers](/Figures/Agreement_landcover.png)

<div align="center">

<small align="center"> Figure 05 - Degree of agreement (%) of the eight remote sensing landcover products for the eight landcover for Water Accounting (LUWA) classes </small>

</div>

- Average similarity of each product compared to the other seven was at least 50%.

- Driven by high agreement (≥ 62%) on barren (Sahara and Namib deserts), trees (central Africa) and to a smaller areal extent, water (African Great Lakes and other permanent lakes) classes. 

- Low agreement (≤ 50%) for shrubs, grass, cropland and wetland classes. 

<div align="center">

### Partitioned cropland product

</div>

<div  align="center">
  
![Landcover Types](/Figures/Landcover_type_2.png)

<small>Figure 06 - Disaggregated cropland product for Africa showing irrigated and rainfed areas as identified using the Budyko model. A distinction is made between cropland areas with blue ET ≥ 100 mm (formal irrigation) and cropland areas with blue ET ≤ 100 mm (supplemental irrigation)</small>

</div>

- High score of 92% for precision and specificity- Low rate of false positives and therefore framework is accurate when it identifies a cropland pixel as irrigated.

- Low sensitivity - High rate of false negatives whereby some irrigated croplands are being missed and incorrectly labeled as rainfed.

<div  align="center">
  
![Irrigated Area](/Figures/Irrigated_area.PNG)

<small>Figure 07 - Amount of Irrigated Area</small>

</div>

<div  align="center">

| Class                   | Rainfed | Irrigated | Total | User's accuracy | Commission errors |
|-------------------------|---------|-----------|-------|-----------------|-------------------|
| Rainfed                 | 321     | 27        | 348   | 92%             |    8%               |
| Irrigated               | 208     | 305       | 513   | 59%             |     41%              |
| Total                   | 529     | 332       | 861   |                 |                   |
| Producer's accuracy (%) | 61%     | 92%       |       |                 |                   |
| Omission errors (%)     | 39%     | 8%        |       |                 |                   |
| Overall accuracy        |         |           |       |                 |         73%          |
| Cohen’s kappa           |         |           |       |                 |            0.48%       |

<small>Table 03 - Confusion matrix of rainfed and irrigated cropland product derived after partitioning HCCM using the Budyko model</small>

</div>

## 5. Conclusions

- The study expands on the products available for detailed agricultural water management and food security studies across Africa, quantifies the disagreement between LULC products and identifies LULC products with accurate cropland classes at continental level following twofold accuracy assessment.

- The framework performs well in disaggregating croplands into irrigated and rainfed areas across Africa, correctly identifying irrigated areas while making few errors in misidentifying rainfed areas as irrigated. 

- Applying it to study changes in cropland area and characteristics, it is found that irrigated cropland area is increasing across Africa (20%), with formal and supplemental irrigation increasing at 26% and 12% respectively since 2013. This has implications for water resources management and governance.


## Reference

Owusu A., Kagone S., Leh M., Velpuri N. M., Gumma M. K., Ghansah B., Thilina-Prabhath P., Akpoti K., Mekonnen K., Tinonetsana P., Mohammed I. (in press). A Framework for Disaggregating Remote-Sensing Cropland into Rainfed and Irrigated Classes at Continental Scale. International Journal of Applied Earth Observation and Geoinformation

<p>International Water Management Institute - December 2023</p>
<!-- <p>December 2023</p> -->



