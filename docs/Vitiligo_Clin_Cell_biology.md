Clinical Cell biology – Vitiligo training course
====

*Created by Walbert Bakker & R2-team:2025*

## 3.1 Introduction
In this training course, designed as part of the UvA master course Clinical Cell Biology, you will use advanced bioinformatics tools to explore, analyze and visualize mRNA expression datasets centered around the pigment producing cells (melanocytes). Both datasets from vitiligo and melanoma are part of this R2 introduction course.

You will use the freely available and web-based genomics analysis and visualization platform R2, a Core Facility of the Amsterdam UMC. R2 provides the user with many experimental and clinical data sets coupled to a wide variety of clickable bioinformatics tools. Without any coding you will gain hands-on research experience with vitiligo and melanoma omics data and bioinformatics tools.

The green buttons in this document will open up a Google form, one per section, with which you can submit answers. Information from these forms will be used in the Q&A lecture (responsie college) to discuss questions that you encounter during this online training course.


### 3.2 Selecting a dataset

Open a Chrome browser and use your R2 account to sign in in the collaborator’s server of the R2 platform: https://hgserver2.amc.nl (also accessible via https://r2platform.com/hg2)
Generally speaking, the R2 platform is easily accessible by the links https://r2.amc.nl | r2platform.com, but today we work from our collaborator’s server hgserver2.

You are now on the R2 main page. Step by step, users are guided through a web of options for data analysis. R2’s main page shows this principle: follow the 4 boxes to develop your analysis of choice. Let’s follow these steps to get a first look at gene expressions in one of the vitiligo datasets
•	Box 1: we leave box 1 as it is, because we will look only at a single datasets in this training course.
Currently the R2 platform houses a vast number of multi-omic datasets. Let’s find out which vitiligo datasets are present.
•	Box 2: click on the text
A grid pops up that shows all the datasets that are currently available to you. Each row is a dataset and each column contains a different searchable characteristic of the datasets. In the bottom right corner of the grid, you can find the exact number of rows, i.e. available datasets.


- 	Under the header **Tissue/Tumor** on top of the grid type in the keyword ‘vitiligo’.

- 	**Question 1**: How many, and what kind of vitiligo datasets are currently in R2?

Datasets have a structured naming in R2, using the following rules: Category - Tissue/ Tumor - author - number of samples (N) - normalization - chiptype. When you click on a specific dataset, in the box below you will find a description of that dataset, including a link to Pubmed (if available). 
We will start analyzing the Natarajan dataset.
The grid tells us that this dataset (of which Natarajan is author) contains 30 samples (per patient 1 Lesional (vitiligo spot) and 1 non-lesional (normal skin vitiligo patient) sample), and was analyzed by bulk sequencing of RNA [Material says DNA but this is not correct?] .
•	Select any of the two **Natarajan** datasets and click on **Confirm selection**.[it looks like these two are identical is that ok?]
In Box 2 you will now see this dataset. We can now use this dataset for further analysis.

## 3.3 Pathogenesis of vitiligo
As you know from the lectures, vitiligo is an cutaneous autoimmune disease in which the pigment-producing melanocytes are eliminated, resulting in patches of depigmented white spots. The pathogenesis of vitiligo is multifactorial in which genetic factors, environmental triggers (i.e. chemical compounds), oxidative stress, and autoimmune mechanisms play a part on the disease development. Figure 1 shows a schematic picture of lesional (left side) and non-lesional (right side) vitiligo skin.!


![](_static/images/vitiligo/vitiligo_lesion.png "lesional (left side) and non-lesional (right side) vitiligo skin")

[**lesional (left side) and non-lesional (right side) vitiligo skin**](_static/images/vitiligo/vitiligo_lesion.png)
<span class="citation_txt">(Figure source:https://doi.org/10.1146/annurev-immunol-100919-023531)</span>


## 3.4 Finding differentially expressed genes.

The Natarajan dataset contains samples from lesional and non-lesional vitiligo skin. Let’s look at the differential expression between these two different samples types.
•	Select in box 3: ‘Differential expression between two groups’. 
•	Click ‘next’.
•	In the next window you can select a statistical **test**. Select the ‘T-test’. 
•	At group by select **Tissue (2 cat(egories)**) and click **Next**.
•	In the adjustable settings window we use a **log2 transformation** as this is common practice in bioinformatics to make the dataset resemble a normal distribution, and the log2 aids in the calculating fold-changes between samples/groups. The p-value can be adjusted as well (but for now we leaf it at 0.01), and we use ‘All’ **Gene ontology** processes.
•	Click **Submit**.

**Question 2**: How many genes are significantly differentially regulated between the two groups?

**Question 3**: Which gene is het most *significantly* differentially expressed?

**Question 4**: And which gene is most *strongly upregulated and downregulated* in lesional tissue (play around with the log2FC (fold change) in the top menu to sort genes based on the fold change). You can click on the lens-icon besides each gene to make a graph. In the geneview window it is possible to change the graph type?
•	Generate a graph of the most up- or downregulated gene.
You can also quickly look into other genes. For example DCT (Tyrosine-related protein 2) which expression is melanocyte specific and performs a key role in the melanin synthesis. 
•	Go to any of the graphs you just generated. Type in “DCT” in the Gene/reporter box in the adjustable settings window, and select DCT from the dropdown list.
•	Click Submit in order to make the new graph (the violin graph is shown below). 


![](_static/images/vitiligo/vitiligo_DCT_r2.png "DCT")

[**Figure 2: violin plot of DCT (TRP2) expression in L and NL tissue.**](_static/images/vitiligo/vitiligo_DCT_r2.png )

If you go back to the tab containing the gene-list generated for Question 2, you can see on the right side of the screen several options to further explore the differentially expressed genes between lesional and non-lesional vitiligo tissue (Figure 1). For example there is already a mini-ontology analysis, but you can also perform GO-analysis  or Gene set analysis yourself, or make a heatmap of the differentially expressed genes. 
Heatmaps (hot(up)/cold(down)) are commonly used to visualize RNA-Seq results. In RNA-seq analysis, heatmaps visualize large, complex datasets of gene expression levels, showing patterns of high and low expression across samples using a color gradient. They typically feature samples (columns) and genes (rows) and often incorporate hierarchical clustering, which groups together genes or samples with similar expression patterns, making it easier to identify biological similarities and differences.
•	To generate a heatmap of all 1596 genes, click Haetmap(zscore) from the list op options presented on the right oy your screen.
It is also possible to generate a heatmap of a smaller group of differentially expressed genes. For example by changing (in the Adjustable settings window) the **P-value cutoff**, or by limiting the **Max number of results**.


•	In the adjustable settings screen set **Max number of results** to 100 and click **submit**.



![](_static/images/vitiligo/vitiligo_heatmap.png "100 genes")

[**Figure 3: Figure 3: heatmap of the 100 most differentially expressed genes between lesional and non-lesional tissue**](_static/images/vitiligo/vitiligo.png )