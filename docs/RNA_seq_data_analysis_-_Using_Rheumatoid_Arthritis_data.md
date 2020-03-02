<a id="rna_seq_data_analysis_-_using_rheumatoid_arthritis_data"> </a>

Introduction
===========================================
Rheumatoid arthritis (RA) is a common autoimmune disorder characterised by lymphocyte infiltration and chronic inflammation of the synovial tissues and progressive joint disability.  

Both genetic and environmental factors influence its pathogenesis, and the strongest contributor to disease heritability is the major histocompatibility complex (MHC) class II, which is involved in antigen presentation to CD4+ T cells. Emerging evidence also points to a role for CD8+ T cells in RA.

![](_static/images/KIT_fimmu-06-00384-g001_small.jpg "Figure 1:  Cell types, cytokines, and chemokine receptors involved in rheumatoid arthritis development (Rodríguez-Frade, 2015)")
  
  [**Figure 1:  Cell types, cytokines, and chemokine receptors involved in rheumatoid arthritis development (Rodríguez-Frade, 2015)**](_static/images/KIT_fimmu-06-00384-g001_small.jpg)
  
  
Despite convincing evidence for T-cell involvement in RA pathogenesis, the specific cell subsets and states that drive the disease have been challenging to identify since T cells are highly heterogeneous, displaying diverse surface markers, developmental and activation states, and effector functions, which has led to multiple systems of classification.  

*Functionally*, CD4+ T cells are classified into many subfractions, such as Th1, Th17, Treg, Tfh9 10 and, recently, peripheral helper T (Tph) many of which have been reported to be involved in RA.  

![](_static/images/KIT_Important-CD4-T-cell-subsets.png "Important CD4 T-cell subsets in Rheumatoid Arthritis Synovial Fluid")
  
  [**Figure 2:  Important CD4 T-cell subsets in Rheumatoid Arthritis Synovial Fluid**](_static/images/KIT_Important-CD4-T-cell-subsets.png)

By *developmental stage*, peripheral blood (PB) CD4+ T cells are classified into four stages (naïve (Tn), stem cell memory (Tscm), central memory (Tcm) and effector memory (Tem)), whereas CD8+ T cells are classified into five stages (Tn, Tscm, Tcm, Tem and CD45RA-positive effector memory (Temra)).  
  
Different treatments for RA have been studied, e.g. infliximab (IFX), methotrexate (MTX), tocilizumab (TCZ).  
Takeshita and Okuzono et al. have collected a large number of samples from clinically well-defined cohorts of patients with RA and age-matched healthy controls (HCs). This data has been uploaded into our platform R2 and we will make use of these and other datasets to clarify the characteristics of T cells in RA and study the transcriptomic features of T cells in RA.  


 TAKE OUT: A general workflow of RNA data analysis consists of the following steps 
===========
1.  Explore your samples
  -  Unbiased unsupervised clustering
  	-0 PCA, tSNE, UMAP 
  -  Toplister
  	- Genes that do make a difference in this set
  - Goals
  	- Data check; bias?
	- Groups?
	
2. Explore differences between groups
  - Differential expression
  - Specific (groups of) genes

3. Explore patterns
  - Overrepresentation
    - Gene Ontology
    - Pathways

4. Explore relations
  - Generate a signature
  - Compare with other signatures

Exploring the dataset
===============================
*Data used:*  
* Disease Rheumatoid arthritis (MTX) monotherapy - Okuzono - 336 - deseq2_vst - gpl17303
* 336 samples of T cells in each developmental stages in healthy volunteers and patients with rheumatoid arthritis 

*Techniques used:*   
* RNA Seq

*References*
* [Multi-dimensional analysis identified rheumatoid arthritis-driving pathway in human T cell](https://ard.bmj.com/content/78/10/1346.long)

<br>  


* Go to R2 (http://r2.amc.nl) by clicking on the button below:  
 
<form name="accessing_r2" action="https://hgserver2.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_nbadam88_u133p2">
  <button type="submit" >Go to R2</button>
</form>  
<br>
<br>  

* Log on to the R2 platform with your credentials that were provided (or apply for a login using the link).
* For a quick impression of the data select the **Cohort Overview**. R2 presents the tumor series with its annotation. Hover your mouse over the different slices of the **inss** annotation pie chart. Explore with which percentage of samples each staging is present in the current dataset.  

The samples of a dataset can be annotated with e.g clinical data or molecular biology parameters, each group of annotated data is called a “track” in R2. These tracks can be used to filter datasets, to compare groups of samples, to color scatter plots of samples with meta information, or to correlate genomics patterns in your data with e.g. different phenotypes or demographic characteristics.  
  
The pie charts in the cohort overview allow you to look at the distribution of the annotation values of each available track. If you click on one of the pie slices, this value is used as a filter: both the charts and the table at the bottom now only show the characteristics of the samples with the filtered value.  
<br>
---------
  ![](_static/images/R2d2_logo.png)**With the dropdown menu below the main pie chart, select the 'cell_type' annotation. Click on the 'tn_cd4' to see what proportion of which cell type is available in the dataset.  
  Now choose the annotation 'tissue' from the dropdown and double click on the 'synovial fluid' slice.**  
   
  **How many synovial fluid samples does this dataset have?**
<br>

---------
<br>  

Finding drug responsive pathways in RA 
===========================================

*Data used:*  
* Exp Rheumatoid arthritis tocilizumab - Takeshita - 22 - deseq2_rlog - gse113156
* 22 samples taken before and after tocilizumab treatment of CD4 and CD8 T cell in rheumatoid arthritis patients

*Techniques used:*   
* RNA Seq

*References*
* [Multi-dimensional analysis identified rheumatoid arthritis-driving pathway in human T cell](https://ard.bmj.com/content/78/10/1346.long)


Explore your samples
------
We've seen that the expression of genes differs among the samples and some types of cells seem to specifically express certain genes. 
To further explore the type of data we're dealing with, an unbiased unsupervised type of clustering analysis is a good idea.  
PCA and t-SNE are two commonly used algorithms to obtain a visual representation of which samples show similar expression profiles.  

##### Clustering with PCA analysis
*Analyses used* 
* PCA and t-SNE

First we will have a look at the dataset with 336 samples of Okuzono. 
 
* Click the button below to show the 2D PCA plot in R2 

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

* Colors are not set by default, under **ColorMode** select **Color by Track** and use the *cell_type (7cat)* track, click **Next** to show the changes 
* PC stands for Principal Component. Each PC shows a different important variation in the dataset. You can  
---------
  ![](_static/images/R2d2_logo.png)**Can you relate the samples to a type of cell?**

<br>
<br>

  ![](_static/images/R2d2_logo.png)**What do you note about the ordering of the cell types with respect to their developmental stage?**

<br>
<br>

---------
##### Clustering with tSNE maps



* Click the button below to show the tSNE map in R2 

<form name='tsne_map' action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" method='POST' target='_gv'>
<input type='hidden' name='switch' value='2'>
<input type='hidden' name='minpres' value='1'>
<input type='hidden' name='perplexity' value='7'>
<input type='hidden' name='dotsize' value='6'>
<input type='hidden' name='option' value='plot_tsne'>
<input type='hidden' name='table' value='ps_avgpres_gse113156geo22_gse113156'>
<input type='hidden' name='cortype' value='transform_zscore'>
<button type="submit" >Go to R2 tSNE map</button>
</form>
<br>
<br>


* Colors are not set by default, under **ColorMode** select **Color by Track** and use the *itcc_model* track, click **Next** to show the changes 

Explore differences between groups
------

Explore patterns
------

Explore relations
------


Determine a lineage specific RA signature
===========================================

*Data used:*  
* Disease Rheumatoid arthritis (MTX) monotherapy - Okuzono - 336 - deseq2_vst - gpl17303
* 336 samples of T cells in each developmental stages in healthy volunteers and patients with rheumatoid arthritis 

*Techniques used:*   
* RNA Seq

*References*
* [Multi-dimensional analysis identified rheumatoid arthritis-driving pathway in human T cell](https://ard.bmj.com/content/78/10/1346.long)

Explore your samples
------
*Analyses used* 
* t-SNE: t-distributed stochastic neighbor embedding statistics

Explore differences between groups
------

Explore patterns
------

Explore relations
------
