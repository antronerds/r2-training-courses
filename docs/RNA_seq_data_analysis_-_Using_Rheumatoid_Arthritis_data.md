<a id="rna_seq_data_analysis_-_using_rheumatoid_arthritis_data"> </a>

Introduction
===========================================


-  A general workflow of RNA data analysis consists of the following steps 
1.  Explore your samples
  -  Unbiased unsupervised clustering
  	- PCA, tSNE, UMAP 
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
*Analyses used* 
* PCA

##### Clustering with PCA analysis
<form name="pca_form" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" method="POST">
<input type="hidden" name="option" value="plot_pca">
<input type="hidden" name="switch" value="2">
<input type="hidden" name="table" value="ps_avgpres_gse118829geo336_gpl17303">
<input type="hidden" name="pcafile" value="pca-db9ec72f427b1110512c63a8b91ad2c1.txt">
<input type="hidden" name="cortype" value="transform_zscore">
<input type="hidden" name="subset" value="">
<button type="submit" >Go to PCA Analysis</button>
</form>

##### Clustering with tSNE maps

We've seen that the expression of genes differs among the samples and some types of tumors seem to specifically express certain genes. To further explore the type of data we're dealing with, an unbiased unsupervised type of clustering analysis is a good idea. One recently developed algorithm is the tSNE map.  


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
