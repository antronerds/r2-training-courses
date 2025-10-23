Clinical Cell biology – Vitiligo training course
====

*Created by Walbert Bakker & R2-team:2025*

## 3.1 Introduction
In this training course, designed as part of the UvA master course Clinical Cell Biology, you will use advanced bioinformatics tools to explore, analyze and visualize mRNA expression datasets centered around the pigment producing cells (melanocytes). Both datasets from vitiligo and melanoma are part of this R2 introduction course.

You will use the freely available and web-based genomics analysis and visualization platform R2, a Core Facility of the Amsterdam UMC. R2 provides the user with many experimental and clinical data sets coupled to a wide variety of clickable bioinformatics tools. Without any coding you will gain hands-on research experience with vitiligo and melanoma omics data and bioinformatics tools.

The green buttons in this document will open up a Google form, one per section, with which you can submit answers. Information from these forms will be used in the Q&A lecture (responsie college) to discuss questions that you encounter during this online training course.


### 3.2 Selecting a dataset

Open a Chrome browser and use your R2 account to sign in in the collaborator’s server of the R2 platform: https://hgserver1.amc.nl (also accessible via https://r2platform.com/hg2)
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
The grid tells us that this dataset (of which Natarajan is author) contains 30 samples (per patient 1 Lesional (vitiligo spot) and 1 non-lesional (normal skin vitiligo patient) sample), and was analyzed by bulk sequencing of RNA. 
•	Select any of the two **Natarajan** datasets and click on **Confirm selection**, 
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

If you go back to the tab containing the gene-list generated for Question 2, you can see on the right side of the screen several options to further explore the differentially expressed genes between lesional and non-lesional vitiligo tissue. For example there is already a mini-ontology analysis, but you can also perform GO-analysis  or Gene set analysis yourself, or make a heatmap of the differentially expressed genes.   
Heatmaps (hot(up)/cold(down)) are commonly used to visualize RNA-Seq results. In RNA-seq analysis, heatmaps visualize large, complex datasets of gene expression levels, showing patterns of high and low expression across samples using a color gradient. They typically feature samples (columns) and genes (rows) and often incorporate hierarchical clustering, which groups together genes or samples with similar expression patterns, making it easier to identify biological similarities and differences.  


 - To generate a heatmap of all 1390 genes, click **Haetmap(zscore)** from the list options presented on the right on your screen.  

It is also possible to generate a heatmap of a smaller group of differentially expressed genes. For example by changing (in the Adjustable settings window) the **P-value cutoff**, or by limiting the **Max number of results**.  


 - In the adjustable settings screen set **Max number of results** to 100 and click **submit**. And click gain on the **Heatmap(zscore)**. This generates the following heatmap (Figure 3).  



![](_static/images/vitiligo/vitiligo_heatmap.png "100 genes")

[**Figure 3: Figure 3: heatmap of the 100 most differentially expressed genes between lesional and non-lesional tissue**](_static/images/vitiligo/vitiligo.png )


The tissue samples lesional (red) and non-lesional (green) nicely cluster together. This shows that L and NL vitiligo RNAseq samples can be identified based on gene expression.  


 • Hovering over the heatmap reveals gene-names.

 • You can also look at the entire gene list shown in the heatmap by clicking on the **Sort order Listing** below the heatmap (click black triangle).  

## 1.4.1 Analyzing differential pathway expression between groups using the KEGG pathway finder  



 - Another way to look at differential expression is looking at pathways of biological processes other than looking for individual genes.
 
Let’s look which biological processes are differentially regulated between lesional and non-lesional samples.  

 - Go to the **main menu** again (click **Go to: R2 Main** in the left corner) and **From box 3** select **KEGG PathwayFinder by Groups**. Click **Next**.
 - In the adjustable setting window at **Track** select **tissue(2cat)**. Click **submit**. Which will generate this table:  


![](_static/images/vitiligo/KEGG_list.png "KEGG list")

[**table 1: Differentially regulated pathways between lesional and non-lesional vitiligo tissue, identified by KEGG PathwayFinder!**](_static/images/vitiligo/KEGG_list.png )


By clicking on the **red R** from a biological process you can find the genes from this pathway that were differentially regulated between L and NL tissue. If you subsequently click on Heatmap(zscore) a heatmap for these genes will be generated. E.g. the heatmap for Nucleotide_excision_repair is shown in figure 4 below.  

![](_static/images/vitiligo/bioproces_heatmap.png "heatmap")

[**Figure 5: Performing KEGG pathway analysis between lesional and non-lesional tissue reveals significant differential regulation of Nucleotide_excision_repair in lesional tissue, illustrated in this heatmap.**](_static/images/vitiligo/bioproces_heatmap.png)



**Question 5**: Does the differential regulation of processes like *Nucleotide_excision_repair* and *Homologous recombination* (Table 1) make sense in the context of vitiligo? Explain your answer. 


## 1.4.2 Finding genes that correlate with your gene of interest.  



If you are interest in a specific gene (Gene of interest, GOI), and you want to know what the potential biological function of this gene is, you can use the option **KEGG pathwayFinder by gene correlation**.  

- select this option from box 3 and click **Next**  
- Let’s look for functions for **MLANA** (type and select this gene from the **Gene / reporter window**.  
- Select genes that correlate (abbreviated by **r/R**) positively with this gene (in Corr R cutoff sign” select **positive**). Click **submit**.  
- 
From the table below you can see that genes correlating with MLANA expression do play a role in melanogenesis (among others). If you click on the red R you can see the correlating genes and then click on individual genes to see the correlation with MLANA. This *KEGG pathwayFinder by gene correlation* can thus help you better understand the biological function of your GOI.  

![](_static/images/vitiligo/KEGG_list2.png "KEGG")

[**Table 2:  biological pathways analysis of genes that positively correlate with MLANA**](_static/images/vitiligo/KEGG_list2.png)



## 1.5 Analyze differential expression using *Gene sets*

Other than looking at the most differentially regulated top genes in a specific tissue, it is also possible to specifically search for a biological process or pathway you are interested in. This can be done by looking at **genesets**.   


- From the main menu select again **differential expression between groups** (**tissue (2 cat)**). And click **Next**.
- In the adjustable settings window click on **select gene set** and type melanogenesis in the search field and click on the **magnifying glass** icon.
- From the **KEGG pathway** select after a few clicks the biological process **Melanogenesis**. The 100 in the count column indicates the number of genes in this specific genelist.
- Click **Confirm selection** and then **submit**.  
You can see that 16 of the 100 genes are significantly differentially expressed between the two groups. Again you can look at individual genes (via the **view** column). But you can also visualize all 16 genes in a single graph:  
- click on the **heatmap(zscore)** button on the right of your screen to generate a heatmap  
- or generate a volcano plot from the **adjustable settings** window select at **display** **Volcano plot** from the drop downlist. And click **submit**. This generates a volcano plot in which genes are displayed based on their upregulation in lesional (L) or non-lesional (NL) tissue, as well as their p-value. Hoover over the dots to identify the genes. With respect to the volcano plot:  

**Question 5**: Which gene from the melanogenesis pathway is most significantly down in Lesional tissue?  

**Question 6**: And which gene from the melanogenesis pathway is most strongly expressed in NL tissue?  

As expected, pathway related to melanocytes are downregulated (or absent) in lesional vitiligo.  

## 1.5.1 Analyzing T-cell presence in vitiligo using a Gene set

From the lectures you have learned that vitiligo is an auto-immune disease. 

**Question 7**: Do you expect to detect immune cells in vitiligo tissue using RNAseq? And if so, what kind of cells would you look for and in which tissue type (L / NL)?

Although the Natarajan dataset is a bulk RNAseq dataset we can use a gene set to get an idea whether e.g. T-cells are present in these vitiligo samples.

- From the R2 main page again select **Differential expression between two groups** in box 3, group by **tissue (2 cat)**, and click **Next**.  
- In the adjustable settings window new select at **display** select **Volcano plot** from the drop downlist. And click **submit**. This generates a volcano plot in which genes are displayed based on their upregulation in lesional (L) or non-lesional (NL) tissue, as well as their p-value.  












