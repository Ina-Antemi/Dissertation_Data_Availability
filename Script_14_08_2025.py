# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 13:57:34 2025

@author: Ina Antemi
"""

""" Welcome to my humble abode! This code is here to help you transform file you download into csv for
easier use, merge lists based on common ID's, and create heatmaps. It is not de-bugged or anything
like that so if you run into issues you should be able to sort them out with a bit of googling or with the
use of AI. """
###############################################################################################
###
### Code to convert snp txt file to csv 
### You might not have to use this whatsoever but I am putting it here just in case you come across
### an snp txt file.
###
### To use the following code, and any other chunk of code in this script, just highlight the wanted lines
### and press Ctrl and 1. This whil unhash everything. Then press the green triangle to run the code,
### and highlight everything and click Ctrl + 1 to hash everything again. This is important since when
### you press the green trangle, the whole script runs.


# import csv

# input_file = r"C:\Dissertation\cross_species_08_08_2025.txt"  # Replace this with the name and path of your file
# output_file = r"C:\Dissertation\cross_species_08_08_2025.csv"  # Replace this with the name you want for your new file

# try:
    
#     with open(input_file, 'r', encoding='utf-8') as txtfile, \
#          open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        
#         writer = csv.writer(csvfile)
        
#         for line in txtfile:
#             row = [field.strip() for field in line.split('\t')]
#             writer.writerow(row)
    
#     print(f"Success! File saved to {output_file}")

#     import os
#     if os.path.exists(output_file):
#         print(f"Verification: File exists ({os.path.getsize(output_file)} bytes)")
#     else:
#         print("Verification: File not found!")

# except FileNotFoundError:
#     print(f"Error: Could not find input file at {input_file}")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")  

### You should now have a csv file in the same directory as the snp txt file.
###########################################################################################################
###
### Code to transform tsv to csv

# import csv

# def tsv_to_csv(tsv_file_path, csv_file_path):
#     """Converts a TSV file to CSV."""
#     try:
#         with open(tsv_file_path, 'r', newline='', encoding='utf-8') as tsv_file, \
#              open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
#             tsv_reader = csv.reader(tsv_file, delimiter='\t')
#             csv_writer = csv.writer(csv_file)
#             for row in tsv_reader:
#                 csv_writer.writerow(row)
#         print(f"Successfully converted {tsv_file_path} to {csv_file_path}")
#     except FileNotFoundError:
#         print(f"Error: File not found: {tsv_file_path}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage:
# tsv_file_path = "mart_export_gene_descreption.tsv"   #Replace with your file name
# csv_file_path = "mart_export_gene_descreption.csv"   #Replace with new file name
# tsv_to_csv(tsv_file_path, csv_file_path)

### SUCCESS!
###########################################################################################################
###
### Code to merge two separate csv files based on the common id's
### 
### In the code below, you can replace "Gene stable ID" with "Protein stable ID" if you want to merge
### the files based on their common protein ids. But you have to make sure the heading matches the
### headings on both files otherwise this won#t work. You can always manually change the headings in 
### your files before running this code. 

# import pandas as pd

# def merge_with_pandas(file1, file2, output_file, on="Gene stable ID", how='inner'): 
#     """Merge two CSV files using pandas."""
#     df1 = pd.read_csv(file1, encoding='latin1')  # or encoding='iso-8859-1'
#     df2 = pd.read_csv(file2, encoding='latin1')
    
#     merged = pd.merge(df1, df2, on=on, how=how)
#     merged.to_csv(output_file, index=False)
    
#     return len(merged)


### The order of the files named bellow is this: 1st file, 2nd file, merged result. The 1st and 2nd file
### do not need to be in a specific order, but the output file does.

# num_merged = merge_with_pandas('cross_species_noted_08_08_2025.csv', 'Sm_v7.2_normExpr_mean_zl3.csv', 'cross_species_final_08_08_2025.csv')
# print(f"Merged {num_merged} records")

##########################################################################################################
###
### Code for Heatmaps
### This code produces interactive heatmaps that are save in your direcotry but can be opend with a web browser.

# import numpy as np
# import pandas as pd
# import plotly.graph_objects as go
# import webbrowser

# ### Load the data file (change the name to your file name)
# df = pd.read_csv("mansoni_heatmap_data_27_08_2025.csv", index_col=0)

# ### Apply log₂(x + 1) transformation 
# df_log = df.applymap(lambda x: np.log2(x + 1))

# ### Rank SMPs by average expression (row mean)
# df_log['AverageExpression'] = df_log.mean(axis=1)
# df_sorted = df_log.sort_values(by='AverageExpression', ascending=True).drop(columns='AverageExpression')

# ### Define custom row height
# row_height = 15

# ### Build the heatmap
# fig = go.Figure(data=go.Heatmap(
#     z=df_sorted.values,
#     x=df_sorted.columns,
#     y=df_sorted.index,
#     colorscale='Viridis',
#     zmin=0,
#     zmax=df_sorted.values.max(),
#     colorbar=dict(title='log₂(Raw Mean Count + 1)')
# ))

# ### Layout tweaks
# fig.update_layout(
#     #title='Top 10 Schistosoma mansoni SMP Expression Heatmap — Ranked by Mean log₂ Expression',
#     height=len(df_sorted) * row_height,
#     autosize=True,
#     margin=dict(l=80, r=80, t=80, b=80),
#     yaxis=dict(
#         automargin=True,
#         tickfont=dict(size=10)
#     )
# )

# ### Save + launch in browser
# fig.write_html("mansoni_heatmap_27_08_2025.html")
# webbrowser.open("mansoni_heatmap_27_08_2025.html")

### And you've done it! Congratulations!!!
#########################################################################################################
# ### Code for top 10 heatmap creation

# import numpy as np
# import pandas as pd
# import plotly.graph_objects as go
# import webbrowser

# # Load the full dataset (already ranked from highest to lowest)
# df = pd.read_csv("top_10_cross_species.csv", index_col=0)

# # Apply log₂(x + 1) transformation
# df_log = df.applymap(lambda x: np.log2(x + 1))

# # Select the top 10 rows without re-sorting
# df_top10 = df_log.iloc[:10]

# # Define custom row height and minimum height
# row_height = 40
# min_height = 300

# # Build the heatmap
# fig = go.Figure(data=go.Heatmap(
#     z=df_top10.values,
#     x=df_top10.columns,
#     y=df_top10.index,
#     colorscale='Viridis',
#     zmin=0,
#     zmax=max(1, df_top10.values.max()),  # Avoid flat color scale
#     colorbar=dict(title='log₂(Raw Mean Count + 1)')
# ))

# # Layout tweaks
# fig.update_layout(
#     height=max(len(df_top10) * row_height, min_height),
#     autosize=True,
#     margin=dict(l=80, r=80, t=80, b=80),
#     yaxis=dict(
#         automargin=True,
#         tickfont=dict(size=15),
#         autorange='reversed'  # This preserves your original ranking visually
#     )
# )

# # Save + launch in browser
# fig.write_html("top_10_cross_species_heatmap.html")
# webbrowser.open("top_10_cross_species_heatmap.html")
####################################################################
