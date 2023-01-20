<a id="x-omics_course_2023_radboud"> </a>

BMS38: Computer Practicals
============================


**Multidimensional data analysis (including visualization), biomarker signatures and X-omics network and pathway analysis (2023)**




* Associated learning objectives:

* Interpret diagrams from well-known dimension reduction and unsupervised clustering techniques

* Perform a pathway-based integration of X-omics data


*The R2 platform has completely been built in the academic medical center (AMC) in Amsterdam, the Netherlands by the team of Dr. Koster (Formerly in the Department of Oncogenomics, since 2021 within the Center for Experimental and Molecular Medicine (CEMM)).* 


Introduction
----

The practical is based on the R2 tutorial. The pdf of the tutorial is on Brightspace and can also be found online:

[tutorial PDF version](https://hgserver1.amc.nl/r2/help/r2_tutorials.pdf, ),(right mouse click)




or

[Tutorial HTML version](https://r2-tutorials.readthedocs.io/en/latest/),(right mouse click)




Assignment 1 (no answers necessary):
----


Go through pages 5 - 9 of the tutorial, [Chapter 2: Using Datasets](https://r2-tutorials.readthedocs.io/en/latest/Using_Datasets.html)  to load the neuroblastoma data and to familiarize yourself with the different options for selecting and loading data. Please note: page numbers refer to the numbers on the pages, not the numbers in the pdf. Pages 5-9 are corresponding with chapter 2 of the tutorial.


Assignment 2: K-means clustering (answers in Italics):
----

In this assignment, we will use an unsupervised, data-driven approach to identify subgroups of patients. We will check whether these subgroups have distinct clinical (such as tumour grade) and molecular characteristics (such as beta-catenin mutation or mutation in the PTCH1 gene (which is part of the sonic hedgehog (SHH) pathway). If we find such associations, we can conclude that the mRNA expression patterns associate with the clinical characteristics (and mutation status) of the tumour. This indicates that further exploration of the mRNA expression is useful.

We will use a dataset that is preloaded in the R2 platform but also available in the Gene Expression Omnibus database (GEO) with accession number [GSE10327](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE10327)

The dataset is based on the neuroblastoma microarray dataset described in this [paper by Kool et al:]( https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0003088)

An expression microarray records the mRNA expression levels for all known genes. Using this medulloblastoma dataset, go through pages 113 – 120 (chapter 11) of the tutorial. [Chapter 11: Using K-means](https://r2-tutorials.readthedocs.io/en/latest/K_Means_Clustering.html). Make sure that you select the right dataset in the start menu (Tumor Medulloblastoma PLoS One – Kool – 62). While going through the tutorial, answer the following questions:

1. Why are 10 iterations needed and is the result of the clustering procedure not always 
consistent?  


2. In the clustering with k=2 (and default settings): what is the main differentiator of the two clusters and how is that related to clinical outcome? Hint: clinical outcome is associated with mutation profiles, including beta-catenin (WNT pathway) and PTCH1 (Sonic hedgehog (SHH) pathway) 


3. Perform clustering with k=2,4,5,6,8. Which of the clusterings is most consistent with the hierarchical clustering presented in the paper from Kool and how would you best judge this? Hints – the subtype given by the paper by Kool et al. is indicated as a color bar “subtype” at the top of the diagram. Below the heatmap you find the statistics for the association of the cluster assignment with the annotation tracks. 


4. The results of this k-means clustering are not completely consistent with the hierarchical clustering results presented in the paper by Kool et al. Name a number of reasons for this. Vary some of the k-means clustering parameters and make an attempt to come closer to a clustering differentiating the original 5 subtypes. 
5. What the optimal number of clusters are remains a bit arbitrary. People have thought about ways to assess this more objectively. Find on the internet some clues on procedures that could be used to determine the optimal number of clusters

6. How do you identify the gene clusters associated with increased WNT signalling and those gene clusters with increased SHH signalling?


7. Perform the clustering again with only the genes from the WNT signalling or only the genes from the SHH pathway. Hint – In “adjustable settings” choose a KEGG pathway related to WNT signalling from the gene filter menu. What do you observe? Relate your findings to the pathway information provided by [KEGG pathway:hsa4310](https://www.genome.jp/kegg/pathway/hsa/hsa04310.html) and [KEGG pathway:hsa4340](https://www.genome.jp/kegg-bin/show_pathway?hsa04340)



Assignment 3: Principal component analysis (answers in Italics)
----

Principal component analysis (PCA) is another data-driven approach used to identify the major sources ofvariation in a multidimensional dataset. In the context of mRNA expression signatures in tumours, PCA may be used to identify subgroups of patients with similar mRNA expression profiles. This process is referred to as patient stratification.

Using the same medulloblastoma dataset, go through pages 155 – 160, [chapter 15:PCA](https://r2-tutorials.readthedocs.io/en/latest/Principle_Components_Analysis.html) of the tutorial and answer the following questions while doing this:


8.	Which of the principal com separate the tumors with increased WNT signalling from the tumors with increased SHH signalling? How much of the total variation in the dataset is explained by this principal component? 


9.	Find out (by visual inspection) which dimension (out of the 9 PCs calculated by the tool) best separates subtype e from all other tumors? 


10.	Using the lasso tool, select the samples with the lowest loadings on PC2, and make a separate sample groups from these. Perform a differential expression analysis between this groups of samples and the remaining samples (by selecting “Find differential expression between groups” from the main menu). Are some of the top differentially expressed in the expected pathways? What signalling pathway from KEGG is most differentially expressed? 

Assignment 4: Identifying a biomarker signature in gene expression data
----

This assignment is about identifying genes that are differentially expressed (have different levels of mRNA) between different types of tumors. A basic differential expression analysis is usually done by linear regression (see also the lecture on integrative X-omics analysis). For each individual gene (mRNA), the mRNA expression level is expressed as a function of the outcome (such as survival after five years (yes/no)). A significant p-value reflects that the gene expression level is different between the tumor classes. In cases where there is just a single factor and no confounding effects (such as sex), the linear model simplifies to a Student’s t-test (two groups only) or one-way ANOVA (multiple groups). We usually assume that the data are normally distributed (although this is not always the case).

**Do not forget to login with your username and password!**

Go through pages 43-59 [Chapter 6: Differential expression](https://r2-tutorials.readthedocs.io/en/latest/Differential_Expression.html) of the tutorial and answer the following questions while going through the tutorial (questions 11-14 related to the assessment of expression patterns for single genes; questions 15-17 relate to differential expression analysis for all genes. Note that a different dataset is used for this assignment: It is the public Tumor neuroblastoma dataset (number 88). The GEO link is this one:[GEO neuroblastoma, Versteeg et al](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE16476) The associated paper is this one: [Paper:Versteeg et al](https://pubmed.ncbi.nlm.nih.gov/22367537/)

11. We chose to work on log2 transformed gene expression measurements (in the case of microarrays fluorescent intensity measured from the chip). Why do we need this log2 transformation?


12. Is there a significant association between MYCN gene expression and survival? 

13. Is there a MYCN gene dosage effect? In other words: is there a significant association between MYCN gene amplification and MYCN expression? 

14. In the paper (figure 3), they mention ATRX as a gene that is frequently demonstrating larger deletions. Can you reproduce the gene expression plot and identify the samples with lower ATRX expression? 


15. What is the most differentially expressed genes between the group of MYCN amplified and tumors with normal MYCN gene dosage?


16. What is the gene that is most significantly associated with survival? Plot in a boxplot (what is displayed in a boxplot?) 


17. Create X-Y plots and Volcano plots displaying the difference between survivors and non-survivors. What are the strong aspects of both visualizations and why do not all genes with large differences (fold-changes) have low p-values? You may want to inspect some individual genes for this. 

Assignment 5: pathway analysis
----

In a pathway analysis, we evaluate in which molecular pathways or biological processes, the differentially expressed genes (or proteins or metabolites) function, and statistically evaluate whether there are many more genes (or proteins or metabolites) differentially expressed than would be expected by chance. This usually gives a stronger hint at the molecular pathways and biological processes that are altered than individual genes (or proteins or metabolites)

Go through pages 93-100 [Chapter 9: Pathway anaylsis](https://r2-tutorials.readthedocs.io/en/stable/Pathway_Finder.html) of the tutorial and answer the following questions while going through the tutorial. **Note: we will use the same dataset (Tumor neuroblastoma public – Versteeg - 88) as in the previous assignment and not the dataset that is used in the tutorial!**


18. What is the KEGG pathways most associated with survival? Does the direction of change of genes in this pathway make sense? 


19. What does the p-value in the pathway analysis represent?

20. What is the most significant gene in this pathway?

21. Create a visual representation of the pathway in which the deregulated genes are highlighted. Which protein complexes do the differentially expressed genes code for?

Assignment 6: Integrative -omics analysis (methylation and expression)
----

Now, we are going to correlate mRNA expression data with DNA methylation data. DNA methylation (in particular of promoter regions) is known to regulate gene expression levels. We will not have time to dive into very sophisticated multi-omics integration methods within the context of this assignment. Instead, we will look at simple (Pearson) correlations between the mRNA expression level of a gene and the methylation level of a genomic region in the neighborhood of that gene (so called associations in-cis). In a classical view on methylation, increased methylation levels of a genomic region is associated with more compact chromatin and suppression of gene expression levels. This means that the correlation value between mRNA and methylation level is negative, but positive associations may also occur.

Follow the tutorial pages 195-203 [chapter 20:Integrated Analysis](https://r2-tutorials.readthedocs.io/en/stable/Integrative_analysis_expression_methylation.html) and answer the following questions while doing so. Questions 22 and 23 relate to the “view in a gene in 2 datatypes” functionality. Questions 24-26 relate to the “dataset extender (within genes)” functionality. **We use the exact same datasets as are used in the tutorial.**


22. You’re first looking at the association between DDX1 methylation and MYCN expression, in conjunction with the MYCN amplification status. Search for a logical explanation why MYCN expression / amplification is linked to DDX1 methylation status.


23. Is the MYCN methylation affected by MYCN amplification as well? 


24. Going to section 20.3 you’re correlating gene expression and methylation status for the same gene (dataset extender – correlation within genes). Select neuroblastoma gse54721 data. On the next screen do not forget to select the methylation (Lavarino -41) and expression (Lavarino – 23) dataset. In the next screens, leave all the adjustable settings on the default. The running of this algorithm may take a few minutes. Find the genes with the strongest correlation between the methylation status and expression levels. Which correlations are more frequently observed, positive or negative correlations?


25. In your list of genes with significant negative associations, you’ll find the XIST gene. What strikes you in the plot of methylation vs. expression patterns for this gene and how do you explain this, given the function of the XIST gene (i.e. silencing the expression of one the X-chromosomes in females). 


26. Next to DDX1, there is another gene at chromosome 2 with a strong negative association between methylation and expression. Which gene is that and what is the approximate distance (in kilobases) between this gene and DDX1?

27. If one would be interested in all vs all associations, i.e. the association of the methylation status of any gene vs the methylation status of any other genes, how many tests would one perform? How would affect the multiple testing corrections and do you expect to find more or less significant correlations than in the within gene study?


28. In the R2 platform, the analysis is limited to correlation-based analysis. What alternative analysis method that were discussed in the lecture would be suitable for this dataset and what extra information would this give? 




*The End*
  

-----
 This concludes our series of tasks for today. If you would like to use R2 for your research in the future, then just visit http://r2.amc.nl and get started. Upon free registration, additional features become available. Thank you for your attention and we hope that you have enjoyed this microarray practical.


