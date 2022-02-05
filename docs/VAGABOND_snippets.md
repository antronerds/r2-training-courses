<a id="VAGABOND_interim_course_R2_day2"> </a>

Some small stuff you can try
====



### Sample maps

In R2 you can  generate for each dataset 2D (3D for PCA) maps/plots based on several High Dimensional Reduction Clustering algorithms with the limition that a given dataset must contain a minimal amount of samples.  At the moment R2 is supporting PCA, tSNE and UMAP explained in more detail in Chapter 16 of the R2 tutorial [Sample maps:r2-tutorial](https://r2-tutorials.readthedocs.io/en/latest/tSNE_dimensionality_reduction.html).


<button class="course googleform" onclick="window.open('https://docs.google.com/forms/d/1irvjF5FpAmvT91WrtxG_26Fh47QzKsiOim1Y8y7Z8yU/viewform?usp=sf_link','_blank');" type="button">Open the snippet answer form </button>


For large datasets such as single cel RNA datasets it takes a lot of resources for the R2 servers if every user can generate t-SNE or UMAP maps. For this reason for many of the large datasets t-SNE/UMAP maps have been pre-generated by the R2 administrators. 

- In the left menu click "sample maps", search for Neuroblastoma 14 patients or by Author Frank Westerman in the upper  row of the grid. By clicking the select button, the t-SNE map of this single cell dataset is plotted.
- Fortunately, this set has been properly annotated, in the adjustable settings menu select color by track , select teh track "cell type" and click submit.
- You can also color the cells by gene expression in the select in the Adjustable settings menu, color by gene, and try e.g **PRRX1**

 --------

![](_static/images/R2d2_logo.png)
**Do you see something special of the PRRX1 coloring with respect the cell-type clusters ??**
<br>
<br>
 



---------
Remarks
------
 This ends the  vagabond introduction . 
 We hope that this course has been helpful. At the end of the workshop, please provide feedback on the course with <a href="https://docs.google.com/forms/d/e/1FAIpQLScy5xoA4btrYfuOOhc5qFKmYkV9_SBv1PQABPgV7eVJY8gk4A/viewform" target="_blank">this form</a>.  
 
 If you want to have your genomics data visualized and analyzed using the R2 platform you can always consult r2-support@amc.nl
 
 The R2 support team.
 