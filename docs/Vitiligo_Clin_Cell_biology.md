Clinical Cell biology – Vitiligo training course

Created by Walbert Bakker & R2

##3.1 Introduction
In this training course, designed as part of the UvA master course Clinical Cell Biology, you will use advanced bioinformatics tools to explore, analyze and visualize mRNA expression datasets centered around the pigment producing cells (melanocytes). Both datasets from vitiligo and melanoma are part of this R2 introduction course.

You will use the freely available and web-based genomics analysis and visualization platform R2, a Core Facility of the Amsterdam UMC. R2 provides the user with many experimental and clinical data sets coupled to a wide variety of clickable bioinformatics tools. Without any coding you will gain hands-on research experience with vitiligo and melanoma omics data and bioinformatics tools.

The green buttons in this document will open up a Google form, one per section, with which you can submit answers. Information from these forms will be used in the Q&A lecture (responsie college) to discuss questions that you encounter during this online training course.


##3.2 Selecting a dataset

Open a Chrome browser and use your R2 account to sign in in the collaborator’s server of the R2 platform: https://hgserver2.amc.nl (also accessible via https://r2platform.com/hg2)
Generally speaking, the R2 platform is easily accessible by the links https://r2.amc.nl | r2platform.com, but today we work from our collaborator’s server hgserver2.

You are now on the R2 main page. Step by step, users are guided through a web of options for data analysis. R2’s main page shows this principle: follow the 4 boxes to develop your analysis of choice. Let’s follow these steps to get a first look at gene expressions in one of the vitiligo datasets
•	Box 1: we leave box 1 as it is, because we will look only at a single datasets in this training course.
Currently the R2 platform houses a vast number of multi-omic datasets. Let’s find out which vitiligo datasets are present.
•	Box 2: click on the text
A grid pops up that shows all the datasets that are currently available to you. Each row is a dataset and each column contains a different searchable characteristic of the datasets. In the bottom right corner of the grid, you can find the exact number of rows, i.e. available datasets.


•	Under the header **Tissue/Tumor** on top of the grid type in the keyword ‘vitiligo’.

	**Question 1**: How many, and what kind of vitiligo datasets are currently in R2?

Datasets have a structured naming in R2, using the following rules: Category - Tissue/ Tumor - author - number of samples (N) - normalization - chiptype. When you click on a specific dataset, in the box below you will find a description of that dataset, including a link to Pubmed (if available). 
We will start analyzing the Natarajan dataset.
The grid tells us that this dataset (of which Natarajan is author) contains 30 samples (per patient 1 Lesional (vitiligo spot) and 1 non-lesional (normal skin vitiligo patient) sample), and was analyzed by bulk sequencing of RNA [Material says DNA but this is not correct?] .
•	Select any of the two **Natarajan** datasets and click on **Confirm selection**.[it looks like these two are identical is that ok?]
In Box 2 you will now see this dataset. We can now use this dataset for further analysis.

##3.3 Pathogenesis of vitiligo
As you know from the lectures, vitiligo is an cutaneous autoimmune disease in which the pigment-producing melanocytes are eliminated, resulting in patches of depigmented white spots. The pathogenesis of vitiligo is multifactorial in which genetic factors, environmental triggers (i.e. chemical compounds), oxidative stress, and autoimmune mechanisms play a part on the disease development. Figure 1 shows a schematic picture of lesional (left side) and non-lesional (right side) vitiligo skin.


