<a id="rna_seq_data_analysis_-_using_rheumatoid_arthritis_data"> </a>

Introduction
===========================================
Rheumatoid arthritis (RA) is a common autoimmune disorder characterised by lymphocyte infiltration and chronic inflammation of the synovial tissues and progressive joint disability.  
Both genetic and environmental factors influence its pathogenesis, and the strongest contributor to disease heritability is the major histocompatibility complex (MHC) class II, which is involved in antigen presentation to CD4+ T cells.  
Genes associated with RA risk alleles outside the MHC locus are also preferentially expressed in CD4+ T cells,3 4 and multiple lines of evidence from both genetic and clinical research indicate a central role for autoreactive CD4+ T cells in RA pathogenesis.5 Emerging evidence also points to a role for CD8+ T cells in RA.6 A subset of CD8+ T cells was found to be essential for ectopic germinal centre formation in the synovial membrane in RA,7 and clonal expansion was observed for CD8+ T cells but not for CD4+ T cells in newly diagnosed patients with RA.8


-  A general workflow of RNA data analysis consists of the following steps 
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
* 337 samples of T cells in each developmental stages in healthy volunteers and patients with rheumatoid arthritis 

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
