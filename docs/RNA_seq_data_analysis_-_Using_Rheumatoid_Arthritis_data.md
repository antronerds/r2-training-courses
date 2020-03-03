<a id="rna_seq_data_analysis_-_using_rheumatoid_arthritis_data"> </a>

Introduction
===========================================
Rheumatoid arthritis (RA) is a common autoimmune disorder characterised by inflammatory cell infiltration, such as T cells, B cells, macrophages and plasma cells. Production of cytokines and proteases lead to chronic inflammation of the synovial tissues and progressive joint disability. RA affects as much as 1% of the worldwide population. Although the exact causes are unknown, decades of research has led to increasingly detailed understanding of multiple disease mechanisms. Different treatments for RA have been proposed, e.g. infliximab (IFX), methotrexate (MTX), tocilizumab (TCZ). However, a significant proportion of patients do not respond to initial treatment or reach remission. Others experience recurrence or deterioration of their disease.   
   
This has led to extensive efforts to find more specific diagnostic markers. The complexity of the disease mechanisms have spurred unbiased searches using genetics, transcriptomics or proteomics. Because of difficulties in measuring markers in the inflamed joints, efforts have, to a large extent focused on analyses of peripheral blood. However, as Lee et al. point out ([Cytokine, March 2020](https://doi.org/10.1016/j.cyto.2019.154960)), clinical translation has proven difficult. Lee et al. hypothesize that inflammatory responses in peripheral blood are different from those in the arthritic joint.   
 
 ![](_static/images/KIT_rheumatoid-arthritis-drug-targets.jpg "Figure 1:  Cell types, cytokines, and chemokine receptors as rheumatoid arthritis drug targets (Source DOI: 10.1211/PJ.2016.20201090)")
   
   [**Figure 1:  Cell types, cytokines, and chemokine receptors as rheumatoid arthritis drug targets (Source DOI: 10.1211/PJ.2016.20201090)**](_static/images/KIT_rheumatoid-arthritis-drug-targets.jpg)

Today you will use the web-based genomics analysis and visualization platform R2. R2 provides you with a set of bioinformatics tools to investigate patient and experimental data.
Takeshita and Okuzono et al. have collected a large number of samples from clinically well-defined cohorts of patients with RA and age-matched healthy controls (HCs). This data and other similar studies have been uploaded into our platform R2. We will make use of these datasets to study the characteristics of T cells, look at differences and similarities between peripheral blood and synovial fluid and to look at possible effects of treatments.  
  
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

Exploring a dataset
===============================
*Data used:*  
* Disease Rheumatoid arthritis (MTX) monotherapy - Okuzono - 336 - deseq2_vst - gpl17303
* 336 samples of T cells in each developmental stages in healthy volunteers and patients with rheumatoid arthritis 

*Techniques used:*   
* RNA Seq

*Analyses used*
* Cohort Overview

*References*
* Paper: [Multi-dimensional analysis identified rheumatoid arthritis-driving pathway in human T cell](https://ard.bmj.com/content/78/10/1346.long)

<br>  



In the following steps we will explore the dataset of Okuzono. It is an RNSseq dataset with 336 samples. The button below will take you to the main page of R2.  

* Go to R2 (http://r2.amc.nl) by clicking on the button below:  
 
<form name="accessing_r2" action="https://hgserver2.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gse118829geo336_gpl17303">
  <input type="hidden" name="option" rel="studyview" value="cg_sampleannotation1">
  <button type="submit" >Go to R2</button>
</form>  
<br>
<br>  

* Log on to the R2 platform with your credentials that were provided (or apply for a login using the link).  

The main page of R2 shows 5 boxes to choose datasets and different klind of analysis. In box 2 you can see the dataset of Okuzono already selected. In box 3 you can select an analysis to perform on this dataset.  
* For a quick impression of the data select the **Cohort Overview** from the dropdown menu. R2 presents the tumor series with its annotation. Hover your mouse over the different slices of the **inss** annotation pie chart. Explore with which percentage of samples each staging is present in the current dataset.  

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

Explore your samples
------

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

Despite convincing evidence for T-cell involvement in RA pathogenesis, the specific cell subsets and states that drive the disease have been challenging to identify since T cells are highly heterogeneous, displaying diverse surface markers, developmental and activation states, and effector functions, which has led to multiple systems of classification.  

![](_static/images/KIT_fimmu-06-00384-g001_small.jpg "Figure 1:  Cell types, cytokines, and chemokine receptors involved in rheumatoid arthritis development (Rodríguez-Frade, 2015)")
  
  [**Figure 1:  Cell types, cytokines, and chemokine receptors involved in rheumatoid arthritis development (Rodríguez-Frade, 2015)**](_static/images/KIT_fimmu-06-00384-g001_small.jpg)
  
  
By *developmental stage*, peripheral blood (PB) CD4+ T cells are classified into four stages (naïve (Tn), stem cell memory (Tscm), central memory (Tcm) and effector memory (Tem)), whereas CD8+ T cells are classified into five stages (Tn, Tscm, Tcm, Tem and CD45RA-positive effector memory (Temra)).  

---------
  ![](_static/images/R2d2_logo.png)**Can you relate the samples to a type of cell?**

<br>
<br>

  ![](_static/images/R2d2_logo.png)**What do you note about the ordering of the cell types with respect to their developmental stage?**

<br>
<br>

---------

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
*Functionally*, CD4+ T cells are classified into many subfractions, such as Th1, Th17, Treg, Tfh9 10 and, recently, peripheral helper T (Tph) many of which have been reported to be involved in RA.  

![](_static/images/KIT_Important-CD4-T-cell-subsets.png "Important CD4 T-cell subsets in Rheumatoid Arthritis Synovial Fluid")
  
  [**Figure 2:  Important CD4 T-cell subsets in Rheumatoid Arthritis Synovial Fluid**](_static/images/KIT_Important-CD4-T-cell-subsets.png)

Let's have a look if we can find such differences in our dataset.  

* Click in the upper left corner on **Go to Main**
* The default analysis type is set to View a gene. In box 4, type **CXCR5** or any gene of your preference. 
* Click **Next** and click on the following page **Next** again.  

You can see a diverse expression of the gene CXCR5. In Adjustable Settings underneath the graph, select 'cell_type (7 cat)' for group separation. Set graphtype to 'Boxplot with circles' and ColorMode to 'Color by Track' and click 'Adjust settings'. 

  
  



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

Finding drug responsive pathways in RA 
===========================================

*Data used:*  
* Exp Rheumatoid arthritis tocilizumab - Takeshita - 22 - deseq2_rlog - gse113156
* 22 samples taken before and after tocilizumab treatment of CD4 and CD8 T cell in rheumatoid arthritis patients

*Techniques used:*   
* RNA Seq

*References*
* [Multi-dimensional analysis identified rheumatoid arthritis-driving pathway in human T cell](https://ard.bmj.com/content/78/10/1346.long)



References
=====================================
1. [The Pharmaceutical Journal, April 2016, Vol 296, No 7888, online | DOI: 10.1211/PJ.2016.20201090](https://www.pharmaceutical-journal.com/news-and-analysis/infographics/blocking-the-immune-system-in-rheumatoid-arthritis/20201090.article)
2. 