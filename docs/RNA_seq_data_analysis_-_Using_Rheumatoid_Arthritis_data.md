<a id="rna_seq_data_analysis_-_using_rheumatoid_arthritis_data"> </a>

Introduction
===========================================
Rheumatoid arthritis (RA) is a common autoimmune disorder characterised by inflammatory cell infiltration, such as T cells, B cells, macrophages and plasma cells. Production of cytokines and proteases lead to chronic inflammation of the synovial tissues and progressive joint disability. RA affects as much as 1% of the worldwide population. Although the exact causes are unknown, decades of research has led to increasingly detailed understanding of multiple disease mechanisms. Different treatments for RA have been proposed, e.g. infliximab (IFX), methotrexate (MTX), tocilizumab (TCZ). However, a significant proportion of patients do not respond to initial treatment or reach remission. Others experience recurrence or deterioration of their disease.   
   
This has led to extensive efforts to find more specific diagnostic markers. The complexity of the disease mechanisms have spurred unbiased searches using genetics, transcriptomics or proteomics. Because of difficulties in measuring markers in the inflamed joints, efforts have, to a large extent focused on analyses of peripheral blood. However, as Lee et al. point out ([Cytokine, March 2020](https://doi.org/10.1016/j.cyto.2019.154960)), clinical translation has proven difficult. Lee et al. hypothesize that inflammatory responses in peripheral blood are different from those in the arthritic joint.   
 
 ![](_static/images/KIT_rheumatoid-arthritis-drug-targets.jpg "Figure 1:  Cell types, cytokines, and chemokine receptors as rheumatoid arthritis drug targets (Source DOI: 10.1211/PJ.2016.20201090)")
   
   [**Figure 1:  Cell types, cytokines, and chemokine receptors as rheumatoid arthritis drug targets (Source DOI: 10.1211/PJ.2016.20201090)**](_static/images/KIT_rheumatoid-arthritis-drug-targets.jpg)

Today you will use the web-based genomics analysis and visualization platform R2. R2 provides you with a set of bioinformatics tools to investigate patient and experimental data.
Takeshita and Okuzono et al. (2019) and Lauwerys et al. (2014) have collected a large number of samples from clinically well-defined cohorts of patients with RA and age-matched healthy controls (HCs). This data and other similar studies have been uploaded into our platform R2. We will make use of these datasets to explore the  differences and similarities between peripheral blood and synovial fluid, to study the characteristics of T cells, and to look for possible effects of treatments.  
  
 
  
 A first look at gene expression with the R2 platform
 =============================== 
 *Data used:*  
 * Disease Rheumatoid arthritis (MTX) monotherapy - Okuzono - 336 - deseq2_vst - gpl17303
 * 336 samples of T cells in each developmental stages in healthy volunteers and patients with rheumatoid arthritis 
 
 *Techniques used:*   
 * RNA Seq
 
 *Analyses used*
 * One Gene View
 
 *References*
 * Paper: [Multi-dimensional analysis identified rheumatoid arthritis-driving pathway in human T cell](https://ard.bmj.com/content/78/10/1346.long)
  
 
--- 
 Let's first take a glance at the platform. Click on the following button to go to R2:  
  
<form name="accessing_r2" action="https://hgserver2.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gse118829geo336_gpl17303">
  <button type="submit" >Go to R2</button>
</form>  
<br>
<br>

* Log on to the R2 platform with your credentials that were provided (or apply for a login using the link).  

The main page of R2 shows five numbered boxes, or steps, in the middle with which you can choose a dataset and a type of analysis. In box 2 you can see the dataset of Okuzono already selected. In box 3 you can select an analysis to perform on this dataset. 

* The default analysis is View a gene. Type in the textbox **Gene / Probeset: CD4**.   
* Click the **Next** button and click **Next** again in the following page.  
 
 ---------
   ![](_static/images/R2d2_logo.png)**The dots in the graph show the expression value of each sample of the dataset for the gene CD4. Under the graph you can see different types of annotation.**  
    
   **Do you notice anything in the expression between the two  colors of the t-cell annotation? Hover with your mouse over the green and red colors of this first annotation row. Which cell type has high expression of CD4?**
 <br>
 
 ---------   
Tumor necrosis factor‐alpha (TNF‐α) is a proinflammatory cytokine that plays a pivotal role in regulating the inflammatory response in rheumatoid arthritis (RA). 

* Click the link of **Go to:  Main** in the upper left corner to go back to the main page.
 
To understand better how this cytokine relates to different tissue and cell types, we do the same process but now we take a look at the gene TNF

* Type in the textbox **Gene / Probeset: TNF**.   
* Click the **Next** button and click **Next** again in the following page.    

We can make use of the annotations to group the results of our samples in groups.

* Scroll down in the page to make some adjustments in the *Adjustable settings* menu under the graph. Under Group Separations change use track to **use track: tissue (2cat)**
* Adjust under Graphics **Graphtype: Boxplot with circles** and **ColorMode: Color by Track**.
* After you selected your preferred adjustments, click **Adjust Settings** 


The immune system is a complex system of different cell types that interact with each other with chemokines and other cytokines. T cells are one of two primary types of white blood cells —B cells being the second type—that determine the specificity of immune response to antigens (foreign substances) in the body. T cells originate in the bone marrow and mature in the thymus. In the thymus, T cells multiply and differentiate into helper, regulatory, or cytotoxic T cells or become memory T cells.  
  
  Despite convincing evidence for T-cell involvement in RA pathogenesis, the specific cell subsets and states that drive the disease have been challenging to identify since T cells are highly heterogeneous, displaying diverse surface markers, developmental and activation states, and effector functions, which has led to multiple systems of classification.  
![](_static/images/KIT_Tcelldifferentiation.png "Figure 2: Differentiation of T-cells, each subtype having its specific role in the immune system.")


[**Figure 2: Differentiation of T-cells, each subtype having its specific role in the immune system.**](_static/images/KIT_Tcelldifferentiation.png)

By *developmental stage*, peripheral blood (PB) CD4+ T cells are classified into four stages: naïve (Tn), stem cell memory (Tscm), central memory (Tcm) and effector memory (Tem), whereas CD8+ T cells are classified into five stages: Tn, Tscm, Tcm, Tem and CD45RA-positive effector memory (Temra).

---------
   ![](_static/images/R2d2_logo.png)**What can you conclude about the expression of the gene TNF in blood tissue versus synovial fluid?**
 <br> <br>
 **Under the graph, change "use track" to "t-cell-stage-type". What can you conclude about the expression of TNF in the different T-cell subtypes?**
 ---------
<br>

Exploring a dataset
===============================
*Analyses used*
* Cohort Overview

*References*
* Paper: [Multi-dimensional analysis identified rheumatoid arthritis-driving pathway in human T cell](https://ard.bmj.com/content/78/10/1346.long)

<br>  

We have seen that the samples of a dataset can be annotated with e.g clinical data or molecular biology parameters. Each group of annotated data is called a **track** in R2. These tracks can be used to filter datasets, to compare groups of samples, to color scatter plots of samples with meta information, or to correlate genomics patterns in your data with, for example, different phenotypes or demographic characteristics.  

To get a better look at the available annotation of a dataset, we can use the tool Cohort Overview in R2. 

* Go back to the main page and select Cohort Overview as type of analysis in box 3.

R2 presents the dataset with its available annotation. Each pie chart shows a different track. 
* Hover your mouse over the different slices of the **drug-group** annotation pie chart.  Explore with which percentage of samples each cell type is present in the current dataset.
* Do the same for the other pie charts and double click on a slice to explore that group of the samples (you can click on the button **Clear Filters** to undo your selection). 
  
<br>

---------
  ![](_static/images/R2d2_logo.png)**Above the main pie chart you can read the number of samples in your current selection (the "n= " number).**  
   
  **Filter for synovial fluid samples with the "tissue" annotation. How many synovial fluid samples are present in this dataset? Glance over the table at the bottom that provides an overview of the selection**
  <br>

---------
We would also like to have a kind of overview of the different behavior of the samples. Do some behave similarly, considering their expression profiles? Before we used the analysis of One Gene View to plot the gene expression of a single gene. Often a dataset has about 20.000 genes. We cannot check all these genes one by one. Let's see if we can find out more information with a Principle Component Analysis.  

Clustering with PCA analysis
===

*Analyses used* 
* PCA
---
Principle Component Analysis or PCA analysis, can summarize the characteristics of many genes in new, more abstract variables, called principle components (PCs). PCA will plot the samples that behave similarly in their expression profiles closer together. This type of analysis is very useful to see if we will be able to find interesting groups with different expression profiles among our samples or if there are outliers that we might want to exclude from our dataset.

* Click the button below to show a 2D PCA plot of the Okuzono dataset in R2

<form name="pca_form" target="_blank" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" method="POST">
<input type="hidden" name="option" value="plot_pca">
<input type="hidden" name="switch" value="2">
<input type="hidden" name="pca_projections" value="PC2:PC3">
<input type="hidden" name="table" value="ps_avgpres_gse118829geo336_gpl17303">
<input type="hidden" name="pcafile" value="pca-db9ec72f427b1110512c63a8b91ad2c1.txt">
<input type="hidden" name="cortype" value="transform_zscore">
<input type="hidden" name="subset" value="">
<button type="submit" >Go to PCA Analysis</button>
</form>  
<br>
<br>  

Each dot is a sample and the axes are the more abstract PC variables. To have a better understanding what biological process might determine the similarity in expression profiles, we can try to color the dots with a track. 
* Colors are not set by default. Under the graph, first adjust **ColorMode: Color by Track** and **Track for color: drug-group**; click next for the changes to take effect.  

Clearly the drug-group does not explain the similarities and differences as found by these PCs.
*  Try instead the **tcell-stage-type (7cat)** track as **Track for Color**. Click next to show the changes.
  
  
---------
  ![](_static/images/R2d2_logo.png)**Can you relate the samples to a type of cell?**

<br>

  ![](_static/images/R2d2_logo.png)**What do you note about the ordering of the cell types with respect to their developmental stage?**

<br>

---------
