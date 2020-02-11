<a id="rna_seq_data_analysis_-_using_rheumatoid_arthritis_data"> </a>


RNAseq data analysis using rheumatoid arthritis data
===========================================

*Using two datasets from Rheumatoid Arthritis a generic approach for RNA data analysis is explored*


Introduction
-----

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
-----

*Data used:*  
* Exp Rheumatoid arthritis tocilizumab - Takeshita - 22 - deseq2_rlog - gse113156
* 22 samples taken before and after tocilizumab treatment of CD4 and CD8 T cell in rheumatoid arthritis patients

*Techniques used:*   
* RNA Seq

*Analyses used* 
* PCA

*References*
* [Multi-dimensional analysis identified rheumatoid arthritis-driving pathway in human T cell](https://ard.bmj.com/content/78/10/1346.long)



Determine a lineage specific RA signature
-----

*Data used:*  
* Disease Rheumatoid arthritis (MTX) monotherapy - Okuzono - 336 - deseq2_vst - gpl17303
* 337 samples of T cells in each developmental stages in healthy volunteers and patients with rheumatoid arthritis 

*Techniques used:*   
* RNA Seq

*Analyses used* 
* t-SNE: t-distributed stochastic neighbor embedding statistics

*References*
* [Multi-dimensional analysis identified rheumatoid arthritis-driving pathway in human T cell](https://ard.bmj.com/content/78/10/1346.long)

