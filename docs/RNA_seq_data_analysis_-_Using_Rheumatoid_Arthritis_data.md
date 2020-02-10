<a id="rna_seq_data_analysis_-_using_rheumatoid_arthritis_data"> </a>


RNAseq data analysis using rheumatoid arthritis data
===========================================

*Using a dataset from Rheumatoid Arthritis a generic approach for RNA data analysis is explored*


Introduction
-----

-  A general workflow of RNA data analysis consists of the following steps 
1.  Explore your samples
  -  Unbiased unsupervised clustering
  	- PCA, tSNE, UMAP 
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


Explore your samples
-----
*Data used:*  
* Disease Rheumatoid arthritis (MTX) monotherapy - Okuzono - 336 - deseq2_vst - gpl17303
* 337 samples of T cells in each developmental stages in healthy volunteers and patients with rheumatoid arthritis 

*Techniques used:*   
* RNA Seq

*Analysis used* 
* t-SNE: t-distributed stochastic neighbor embedding statistics
* PCA: Principle Components Analysis

*References*
* [Multi-dimensional analysis identified rheumatoid arthritis-driving pathway in human T cell](https://ard.bmj.com/content/78/10/1346.long)


