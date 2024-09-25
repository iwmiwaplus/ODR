# Probability Map
# Compare 10 datasets and how many pixels are the same for each land cover class
# Author: Stefanie Kagone
# Date: November 2022
# Log: script created

# modules needed for script
import os
import numpy as np
import rasterio

# Datasets for comparison
outdir = r'../../LUWA_to_LUWA8class_withLGRIP/'
d1_lc =  os.path.join(outdir, 'MCD12Q1_061_2019_300m_WA8.tif')
d2_lc = os.path.join(outdir, 'CCILCV2_2019_300m_WA8.tif')
d3_lc = os.path.join(outdir, 'sentinel_esri_2019_300m_WA8.tif')
d4_lc = os.path.join(outdir, 'CopLC100_2019_300m_WA8.tif')
d5_lc = os.path.join(outdir, 'GFSAD30_2015_300m_WA8.tif')
d6_lc = os.path.join(outdir, 'GLCShare_2013_300m_WA8.tif')
d7_lc = os.path.join(outdir, 'WAPOR_L1LCC_2019_300m_WA8_2.tif')
d8_lc = os.path.join(outdir, 'GLOBCOVER_2009_300m_WA8.tif')
# d9_lc = os.path.join(outdir, 'GLCC_1993_300m_WA8.tif')
#d9_lc = os.path.join(outdir, 'LGRIP_2015_300m_WA8.tif')
#d10_lc = os.path.join(outdir, 'worldcover_2020_300m_WA8.tif')


prob_out_dir = r'../../probability_maps_8lulc/'
#prob_out_dir = r'W:\Data\Landuse\GLOBAL\AFRICA\WA_8classes\prob_map'
meta = None

# list of land cover classes
lc_classes = {'Tree': 1, 'Shrub': 2, 'Grass': 3, 'Crop': 4, 'misc': 5, 'Wetland': 6, 'Water': 7, 'Barren': 8}
# list all raster files included in the comparison
ds_list = [d1_lc, d2_lc, d3_lc, d4_lc, d5_lc, d6_lc, d7_lc, d8_lc] 
num_of_ras = len(ds_list)

# extract a class and create the probability map
for clas, clas_num in lc_classes.items():
    print(f'creating map for class {clas} - {clas_num}')
    # loop through the rasters and extract each class to create the probability map for each one
    arr_list = []
    for dsc in ds_list:
        print(dsc)
        # convert to numpy array
        with rasterio.open(dsc, 'r') as ds:
            meta = ds.meta
            # read all raster values
            arr1 = ds.read(1)
        ac = np.count_nonzero(arr1 == clas_num)
        print(f'{ac} is how many pixels there are for class {clas}')
        mask_arr = np.zeros(shape=arr1.shape, dtype='uint8')
        mask_arr[arr1 == clas_num] = 1
        ones_count = np.count_nonzero(mask_arr == 1)
        print(f'there are {ones_count} many ones in the final mask')
        arr_list.append(mask_arr)

    # stack them all together
    arr_all = np.dstack(arr_list)  # stacks the rasters into 1 array => (col, rows, [dimensions) = number of rasters]
    del mask_arr, arr1, ac, arr_list # so no memory issues
    print(arr_all.shape)

    # Sum up each pixel by axis 2 (3rd dimension)
    arr_all = np.sum(arr_all, axis=2)
    # print(arr_all.shape)
    # calculate probability from 10% - 100% for 10 rasters
    prob_oo = ((arr_all / num_of_ras)) * 100
    # print(prob_oo)
    # print(prob_oo.shape)
    # output file
    meta['dtype'] = 'uint8'
    prob_out = os.path.join(prob_out_dir, f'probability_{clas_num}-{clas}.tif')
    prob_oo = prob_oo.astype('uint8')
    with rasterio.open(prob_out, 'w', **meta) as wfile:
        wfile.write_band(1, prob_oo)
    print(f'created output file {prob_out}')
    del arr_all
