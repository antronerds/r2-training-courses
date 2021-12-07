<a id="VAGABOND_interim_course_R2"> </a>

Finding causes in Neuroblastoma genomics data
=================================

*Introduction to bioinformatics tools using the web-based genomics analysis and visualization platform R2 and neuroblastoma data *

This resource is located online at http://r2-training-courses.readthedocs.io  
  
Introduction
------------

Cancer is a very complex disease. Much more complicated than originally anticipated when the first mutations were found to be causal for specific cancers. For instance, in colorectal cancer a well defined path of subsequently gained mutations leads to more aggressive tumorigenic cell types (the Vogelstein model).

  ![](_static/images/TumorHeterogeneity_CancerProgression.jpg "Figure 1: Mutation paths during cancer progression.")	
  
  [**Figure 1: Mutation paths during cancer progression**](_static/images/TumorHeterogeneity_CancerProgression.jpg)


##### Neuroblastoma 

Neuroblastoma is a childhood tumor of the peripheral sympathetic system. Primary tumors can arise in the adrenals and most patients are diagnosed between the age of 0 to 4 years.<br>
Neuroblastoma patients are classified by the INSS staging system. The increment in stages does not reflect progression of disease, as is the case for colon cancer, but represent different characteristics of the disease. Stage 1, 2 and 3 neuroblastomas have a very good prognosis. Stage 4 neuroblastomas usually go into complete remission upon therapy but often relapse as therapy-resistant disease. About 40% of stage 4 neuroblastoma have an amplification of the MYCN oncogene. This implies that instead of two DNA copies, each neuroblastoma cell has 30 to 100 copies of the MYCN gene. In addition to stage 1, 2, 3, and 4 neuroblastomas, there is the unusual stage 4S neuroblastoma, which is metastasized but goes into spontaneous regression. Over the last twenty years, the outcome for stage 4 neuroblastoma patients has not substantially improved.<br>
<br>
  ![](_static/images/Vagabond/Vagabond_lowvshighstages_neuroblastoma.png "Figure 2: Low stage versus high stage neuroblastoma")	
  
  [**Figure 2: Low stage versus high stage neuroblastoma**](_static/images/Vagabond/Vagabond_lowvshighstages_neuroblastoma.png)
  
Extensive research into mutation mechanisms in neuroblastoma has been done (also in the AMC Oncogenomics group). Unfortunately, such a mechanism has not been found for this often deadly childhood tumor.


##### Course day 1: Finding differences and biological processes

One of the technologies that can be used to study a disease or biological process is gene expression profiling. With this high throughput technology, we determine the mRNA expression of nearly all genes known in a single experiment. On this first day of the course, we will look for different subgroups in our data, find genes that make a difference and find cellular pathways that are activated in neuroblastoma patients with an unfavorable prognosis.<br>
<br>
The **grey buttons** in this course will bring you to the R2 platform, often with pre-set settings such that you can pick up an analysis easily. The **green buttons** in this document will open up a Google form, one per section, with which you can submit your answers. 
<br><br>

Research questions:
--------------------------------------  

During this practical course, we will use the R2 bioinformatics tool to study two research questions:
* Which molecular pathways are activated in neuroblastoma patients with an unfavorable prognosis?
* What is the function of the MYCN gene in neuroblastoma?



Finding prognostic factors in your data
---------------------------------------

R2 enables the analysis of the prognostic value of any annotated parameter of a tumor series. These parameters are available in R2 as so called ‘tracks’. The neuroblastoma series NB88 is annotated for a number of clinical and molecular parameters. To get some insight in the tumor and the NB88 series, we will analyze the prognostic value of stage, age at diagnosis and amplification of the MYCN oncogene. 

*Data used:*  
* 88 Human Neuroblastoma samples (Tumor Neuroblastoma public - Versteeg - 88 - MAS5.0 - u133p2)

*Techniques used:*   
* mRNA Microarray expression

*Analysis used* 
* Kaplan Meier by annotated parameter

<br>
<br>

##### Prognostic factors: 

R2 enables the analysis of the prognostic value of any annotated parameter of a tumor series. These parameters are available in R2 as so called ‘tracks’. The neuroblastoma series NB88 is annotated for a number of clinical and molecular parameters. To get some insight in the tumor and the NB88 series, we will analyze the prognostic value of stage, age at diagnosis and amplification of the MYCN oncogene. 
- start in the main menu
- verify that you use the ‘Tumor Neuroblastoma public - Versteeg - 88 - MAS5.0 - u133p2’ series
- select in field 3: "Kaplan Meier > Kaplan Meier by annotated parameter".  next
- We are going to separate the patients based on the INSS stating system. Within R2 grouping variables are referred to as tracks. Use the drop down menu of ‘use track’ under the Survival header, select ‘inss (cat 5)’,  next
- The Kaplan Meier curves appear.

---------

  ![](_static/images/R2d2_logo.png)**What can you say about the expression of this gene in the different tumor models?**

<br>
<br>
---------

##### Expression of key genes
* The button below brings you to the form in which you can submit your answers for section 1.2. 

<button class="course googleform" onclick="window.open('https://docs.google.com/forms/d/e/1FAIpQLSfo7ZeKEaVRflzEmXkFZsErDShYHs8PaZO1tBmVrnLeyobkyg/viewform?usp=sf_link','_blank');" type="button">Open the form for section 1.2</button> 
<br>
<br>


* Go to R2 by clicking on the button below:  


<form name="itcc_68_cell_lines" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_itcccellline86_u133p2">
  <button type="submit" class="course r2submit" >Go to R2</button>
</form>  
<br>
<br>

You're now on the R2 main page. This web based molecular biology data analysis platform contains a wealth of data and methods to analyze the datasets. Step by step, researchers are guided through a web of options for data analysis. R2's main page shows this principle: step through each of the numbered boxes to develop your analysis of choice.  
In this case we're first going to see if and how the mRNA expression of several genes changes through a single dataset. The proper dataset described above has been selected already. In this dataset 86 cell lines derived from 6 different childhood tumor types can be found (ewing sarcoma, medulloblastoma, neuroblastoma, osteosarcoma, acute lymphocytic leukemia and rhabdomyosarcoma).

---------

  ![](_static/images/R2d2_logo.png)**From knowledge acquired in previous lectures, or just from quick Googling on the web... Can you think of a gene that might show different expression between some of these 6 tumor models?**
<br><br>

---------

  * In field 4 type the name of the gene and click **Next**
  * Leave all settings at default and click **Next**  
  
A graph shows the expression of this gene's mRNA in the whole set of childhood tumor cell lines. Samples are along the x-axis, mRNA expression values of the gene in a sample are on the y-axis. Below the graph is the available annotation for the samples shown in colored tracks. In R2, samples can be annotated with e.g clinical data or biological information. Each group of annotated data is called a “Track” in R2. These tracks can be used to filter, color or split data in all types of R2 analyses.  
Sometimes you can see the categorical tracks displayed underneath a graph. But often more annotation is available for the samples. You can hover your mouse above dots in a graph or over the tracks underneath the graph to get more information per sample.  

  * Hover with your mouse over data points to show additional information.  

At the bottom of the page you can find a table with adjustable settings. Many settings of the graph can be adapted.  

* Try out a different view of the same data with the following changes to the settings:  
 The expression values on the y-axis are logarithmic by default, in the settings menu set the **Transform** option to *none* instead. Split the data in groups with the setting **use track** under Group separations: choose the *itcc_model* track that contains the information which sample belongs to which tumor type. Also sort the samples again on expression with **Extra Graph Option** set to *Track and Gene sort*. Finally, click **Adjust Settings** to obtain the graph with these adaptations.  
  
* Now try the gene MYCN (Type *MYCN* in the **Change Gene** box in the upper right corner to keep all your settings, but to change your gene).  
* Hover with your mouse over the track underneath the graph or over the data points, to find out which itcc_model belongs to which group of samples. 
  
---------

  ![](_static/images/R2d2_logo.png)**What can you say about the expression of this gene in the different tumor models?**

<br>
<br>

  ![](_static/images/R2d2_logo.png)**What might the expression level of this gene in neuroblastoma signify about the function of the gene in this cancer?**
<br>
<br>

---------

##### Clustering with tSNE maps

We've seen that the expression of genes differs among the samples and some types of tumors seem to specifically express certain genes. To further explore the type of data we're dealing with, an unbiased unsupervised type of clustering analysis is a good idea. One recently developed algorithm is the tSNE map. Similar cells will clump together on the map.   

* Click the button below to show the tSNE map in R2 

<button class="course" onclick="window.open('https://hgserver1.amc.nl/cgi-bin/r2/main.cgi?option=tsne_plot&tsne_id=3b64db2654de88efccac21ddeae73a8f','_blank');" type="button">Go to the t-SNE map</button> 
<br>
<br>



* Under the graph, a menu allows the user to adapt settings. Colors of the graph points are not set by default. To color the graph with a biologically meaningful annotation, find the **ColorMode** dropdown and select *Color by Track*. Now set the **Track for Color** dropdown to use the *itcc_model* track, and click **Next** to show the changes. 

* The t-SNE algorithm has a parameter called **perplexity**, which determines how much attraction points on a map have towards each other.  Set the perplexity value to *5* and click **next** again.  
  
------

![](_static/images/R2d2_logo.png)**What do you note about the clustering of the neuroblastoma samples?**

  ![](_static/images/R2d2_logo.png)**With which other tumor models do the neuroblastoma cell lines cluster?**

<br>
<br>

  ![](_static/images/R2d2_logo.png)**Based on the above, what would you do to further investigate your observations**
  
------


Urgency of research: patient material
----------------------------------------

In the former step we derived that neuroblastoma cell lines seem to group with cell lines of different developmental lineages. We have recently established new cell line pairs from neuroblastoma patients. In some cases multiple cell lines were obtained from the same biopsy. These cell lines share genetic defects and are therefore called *isogenic* cell line pairs. A microscopy image of each pair is provided below. 

  ![](_static/images/TumorHeterogeneity_IsoGenicPairsBF.png "Figure 2: Bright field image of isogenic cell line pairs.")
	
  [**Figure 2: Bright field image of isogenic cell line pairs.**](_static/images/TumorHeterogeneity_IsoGenicPairsBF.png)

* The button below brings you to the form in which you can submit your answers for section 1.3

<button class="course googleform" onclick="window.open('https://docs.google.com/forms/d/e/1FAIpQLSc0dGfEl9zDS7Yh-ZtrcKAn4IVgcwNxsZKNjQQtTj35JjgQng/viewform?usp=sf_link','_blank');" type="button">Open the form for section 1.3</button> 
<br>
<br>

---------

  ![](_static/images/R2d2_logo.png)**What do you note about the morphology of the cell lines?**
<br><br>

---------

We profiled the mRNA expression of genes using Affymetrix mRNA chips in three of these pairs and of a previously established neuroblastoma cell line that after culturing gave rise to two very divergent phenotypes. The resulting gene expression patterns can be used to perform a hierarchical clustering. An example of such clustering resulting in an ordered heatmap is provided below 

  ![](_static/images/TumorHeterogeneity_HeatmapClustering.png "Figure 3: Heatmap: unsupervised clustering of samples using the distribution of the expression data combined with the clustering of genes based on their expression through the samples.")
	
  [**Figure 3: Heatmap: unsupervised clustering of samples using the distribution of the expression data combined with the clustering of genes based on their expression through the samples.**](_static/images/TumorHeterogeneity_HeatmapClustering.png)



*Data used:*  
  * Cell lines recently derived from three different patients. Two morphologically different looking cells were taken per patient. This dataset is combined with two classical Neuroblastoma cell lines that clustered differently in the tSNE: SHEP and SY5Y (Mixed Neuroblastoma (MES-ADRN) - Versteeg - 8 - MAS5.0 - u133p2) 
  
*Techniques used:*  
* mRNA Microarray expression

*Analysis used*  
* Toplister: unsupervised gene selection
* Unsupervised hierarchical clustering
* Heatmap visualization

<br>
<br>

For this analysis we'll directly go to one of the analysis tools of R2: Toplister. The Toplister can assess which genes behave different throughout a dataset. It does so by selecting the genes whose expression values have the largest standard deviation within a given set of samples. This gives an unbiased view of the differences in gene expression.

* Go to R2 by clicking the button below. R2 will find the 100 genes that have the largest variation in gene expression among these 8 cell lines, three pairs from three tumors of a patient and two classical neuroblastoma cell lines. 

<form name="toplisterform" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
<input type='hidden' name='minpres' value='1'>
<input type='hidden' name='howmany' value='100'>
<input type='hidden' name='option' value='high_ana2'>
<input type='hidden' name='table' value='ps_avgpres_gse90803geo8_u133p2'>
<input type='hidden' name='hugoonce' value='yes'>
<input type='hidden' name='set' value='standard_deviation'>
<input type='hidden' name='cortype' value='transform_log2'>
<button type="submit" class="course r2submit" >Go to R2 Toplister</button>
</form>
<br>
<br>

* Click **Next**; a list of genes appears

---------

  ![](_static/images/R2d2_logo.png)**Do you recognize any genes that explain the difference in phenotype?**
<br><br>

---------

* Use the mousewheel to scroll to the bottom of the page (or click on the shoe-print at the top of the page). 

Here you can choose to perform an additional analysis. The heatmap vizualization produces a hierarchically clustered view of the expression values for the top 100 genes.  

---------

  ![](_static/images/R2d2_logo.png)**What number of groups do you expect?**
<br><br>

---------

* Click on **Heatmap (z-score)**
  
  
The cell line pairs from the patient were also investigated for the tumor stem cell marker gene CD133 and for their migration capability. See the results in the figure below:


  ![](_static/images/TumorHeterogeneity_PairsCD133Migrate.png "Figure 4: CD133 FACS analysis and transwell migration assay of isogenic pairs")
	
  [**Figure 4: CD133 FACS analysis and transwell migration assay of isogenic pairs**](_static/images/TumorHeterogeneity_PairsCD133Migrate.png)


---------

  ![](_static/images/R2d2_logo.png)**Given these observations, what origin can you assign to each group?**
<br><br>

---------
<br>

Which genes make a difference? Creating signatures
-----------------------------------------------------

We have identified two different types of cells that occur within the same patient. Neuroblastoma apparently has a heterogenous nature. What genes determine the difference between the two types? We’ll use RNA expression data again but now we will use a predefined, supervised classification in groups to search for genes that characterize this classification best, or in other words, that are differentially expressed between these two groups.

*Data used:*  
* Mixed Neuroblastoma (MES-ADRN) - Versteeg - 8 - MAS5.0 - u133p2 (same as above)
* Gene Ontology
* Broad curated hallmark datasets

*Techniques used:*   
* mRNA arrays

*Analysis used*  
* Differential Expression: supervised gene selection
* Gene Ontology Analysis: Overrepresentation calculation
 
<br>
<br>

* The button below brings you to the form in which you can submit your answers for section 1.4

<button class="course googleform" onclick="window.open('https://docs.google.com/forms/d/e/1FAIpQLScesiEn-9mU9rGCIct4oHkplP6RxXNkccCCkVHBKzioYuczPg/viewform?usp=sf_link','_blank');" type="button">Open the form for section 1.4</button> 
<br>
<br>
  
* Go to the main page of R2 by clicking the button below

<form name="main_4_pairs" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gse90803geo8_u133p2">
  <button type="submit" class="course r2submit" >Go to R2 main portal</button>
</form>  
<br>
<br>


* In Field 3 choose *Find Differential expression between groups* and click **Next**

This dataset has been annotated with 'cell type' information. Each sample was assigned to either the MESenchymal or the ADReNergic cell type. The information is stored in R2 in a track. 
* Choose the proper track in the **Select a track** dropdown. Since we have only 8 samples make sure that the multiple testing correction is set to *No correction*.  Click **Next** twice. (More information on Correction for Multiple Testing can be found <a href="https://r2-tutorials.readthedocs.io/en/latest/Did_You_Know.html#multipletesting" target="_blank">here</a>).
* A list of differentially expressed genes appears with correlation p-value < 0.01 in this dataset is shown. Click on the hyperlinked name of your favorite gene to see its expression in the sample set; try an oppositely correlating gene as well
* Go back to the window with the differentially expressed genes. This is still open in one of your browser tabs. 
* Click on the **Heatmap(zscore)** button in the right menu panel; a heatmap shows the expression of the differentially expressed genes for each sample.    

---------

  ![](_static/images/R2d2_logo.png)**How is this figure different from the former?**
<br><br>

---------
<br>
For future use, this list of genes has been stored for you in R2 as signatures (aka genesets or categories). The list has been split into two categories: one set of genes that is highly expressed in the MES type of samples (r2_mesadrn_mes) and one set of genes highly expressed in the ADRN type of samples (r2_mesadrn_adrn).  

R2 provides additional analysis for sets of genes that can be accessed from the right panel of menu buttons. As a first analysis step we can check a data resource called the Gene Ontology that provides a tree of systematically ordered biological terms that is used to formally describe the biological role of each gene. The Gene Ontology Analysis tool in R2 calculates for each of the thousands of groups of genes that are annotated with a specific biological term whether your set of choice is over-represented in them. 

* On the page with the differentially expressed genes, select the **Gene Ontology Analysis** button in the menu on the right 

---------

  ![](_static/images/R2d2_logo.png)**What can you say about the function of the differentially expressed genes?**
<br><br>

---------
<br>

* Now scroll down to the end of the page (or click the filter button in the left upper corner of the page) and adapt the settings such that only the Biological Process branch of the Gene Ontology is selected, and select only the genes that are higher expressed in the MES type of cells 

---------

  ![](_static/images/R2d2_logo.png)**What can you say about the function of the group of genes that are upregulated in the MES type of cells?**
<br><br>

---------
<br>

In R2 there are many more sets of genes that have been found to be implemented in specific processes. The Broad Institute has compiled quite some of these sets of genes that characterize hallmark biological processes.  

* Go back to the window with the differentially expressed genes. 
* Select the **Gene set analysis** option from the right menu
* Select the *geneset_broad_2015_hallmark* geneset and click **Next**

---------

  ![](_static/images/R2d2_logo.png)**Which hallmark category of genes pops up as most important? Can you explain this?**
<br><br>

---------
<br>

Identifying groups: using signatures to classify other datasets
------------------------------------------------------------------

We now have a signature that distinguishes between the two types of cells. We also obtained some hints about functional characteristics of these cells. How does this signature behave in other datasets? Does the same set of genes tell us something about other sets of tumors or cell lines? This is the next step in our analysis.   
We've assembled a more complex dataset by gathering the dataset of the 4 pairs of cell lines, additional neuroblastoma cell lines from the first dataset and publicly available data of non-malignant human neural crest tissue. The neural crest undergoes a mesenchymal transition and gives rise to cell types from the adrenergic lineage.

*Data used:*
* A combination of the 8 cell lines above, additional neuroblastoma cell lines and cells from the neural crest lineage (Mixed Neuroblastoma (MES-ADRN-CREST) - Versteeg/Etchevers - 34 - MAS5.0 - u133p2)

*Techniques used:* 
* mRNA expression data

*Analysis used*
* Heatmap analysis

<br>
<br>
<br>

* The button below brings you to the form in which you can submit your answers for section 1.5

<button class="course googleform" onclick="window.open('https://docs.google.com/forms/d/e/1FAIpQLSephAsX9i-d_QUh7Gu7ZRWUKkL9XgtAuEzglGnBgBU4Nd3VrQ/viewform?usp=sf_link','_blank');" type="button">Open the form for section 1.5</button> 
<br>
<br>

* Go to the main portal of R2 by clicking the button below; the dataset described above is automatically selected

<form name="main_34_pairs_and_crest" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gsenatgengeo34_u133p2">
  <button type="submit" class="course r2submit" >Go to R2</button>
</form>  
<br>
<br>


* In field 3 select *View Geneset* that you can find under the red header *Meta-analysis*.
* Click **Next** and select *geneset_r2provided_genelists* 
* Click **Next**, leave selection as is and click **Next**
* Select both signatures that were derived before by CTRL click on the MES (*r2_mesadrn_mes*) and ADRN (*r2_mesadrn_adrn*) signatures and click **Next**

---------

  ![](_static/images/R2d2_logo.png)**Which cell types group together?**
<br>
<br>
  ![](_static/images/R2d2_logo.png)**How does this relate to the earlier observations on cell lineage?**
<br>
<br>

---------

When observing such clear-cut patterns it is good scientific practice to test this in additional datasets. The database of R2 contains an additional dataset consisting of neuroblastoma cell lines that were profiled by a French research team. 

* Click on the button below to go there and perform the same analysis.


<form name="main_34_pairs_and_crest" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gse90683geo48_gse90683r1">
  <button type="submit" class="course r2submit" >Go to R2 additional NB dataset</button>
</form>  
<br>
<br>


---------

  ![](_static/images/R2d2_logo.png)**Do you observe similar patterns?**
<br>
<br>

---------


Using scores for further characterization
--------------------------------------------

The expression patterns of these specific signatures can be used to compare cell types. We can do this by summarizing the expression data of all genes in the signature in each cell type in one value; a signature score. The figure below shows the signature score of the MES part of the signature in a specific sample.  

  ![](_static/images/TumorHeterogeneity_SignatureScores.png "Figure 5: The signature score as calculated for a specific sample in the MES signature.")
	
  [**Figure 5: The signature score as calculated for a specific ample in the MES signature.**](_static/images/TumorHeterogeneity_SignatureScores.png)


 R2 has calculated these scores for all samples in both signatures. We're going to find out how they relate.

*Data used:*
* Mixed Neuroblastoma (MES-ADRN-CREST) - Versteeg/Etchevers - 34 - MAS5.0 - u133p2

*Techniques used:* 
* mRNA expression data

*Analysis used*
* Signature scores 

<br>
<br>
<br>

* The button below brings you to the form in which you can submit your answers for section 1.6

<button class="course googleform" onclick="window.open('https://docs.google.com/forms/d/e/1FAIpQLSfeDhhvV2hQQ4erzjf18OX27jelvYxFVIyovPOxWin3GUxekg/viewform?usp=sf_link','_blank');" type="button">Open the form for section 1.6</button> 
<br>
<br>

* Go back to the main portal of R2 by clicking the button below.

<form name="main_34_pairs_and_crest" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gsenatgengeo34_u133p2">
  <button type="submit" class="course r2submit" >Go to R2</button>
</form>  
<br>
<br>


* In field 3 choose **Relate 2 tracks** and click **Next**
* First we'll explore the scores in each signature separately; on the X-axis (**Select X track**) we'll use the unique sample id (*lab\_id*) and on the Y-axis the signature score track that R2 has generated for the ADRN signature (s\_mesadrn\_adrn(#)). Click **Next**.
* A graph is generated. For each sample the signature score for the mesadrn\_adrn signature is shown. Select **Color by Track** for ColorMode and try different tracks. Click **Adjust Settings** to view the result.
* Now select for the Y-axis the MES part of the signature, click **Adjust Settings** to view the result.
* To compare the signature scores, select the ADRN signature for the X track
* If you have time you can also try the **Color by Gene ColorMode**, choose a gene of interest (Note: the dropdown selection is linked to the database, wait for the proper selections to popup...)

---------

  ![](_static/images/R2d2_logo.png)**What conclusion would you draw from these figures?**
<br>
<br>

---------


Finding causes: homing in on transcription factors
-----------------------------------------------------

Apparently there are two types of cells in Neuroblastoma tumors. Neuroblastoma seems to be a heterogenous tumor. Transcription factors (TF's) are known to determine gene expression programs in cells. These gene expression programs determine the development of the cell. Can we find out which TF's might influence the difference between both of these cell lines?

*Data used:*
* Mixed Neuroblastoma (MES-ADRN-CREST) - Versteeg/Etchevers - 34 - MAS5.0 - u133p2
* Transcription factor annotation from Gene Ontology
* NCBI (National Center for Biotechnology Information - USA) Gene information database 

*Techniques used:* 
* mRNA expression data

*Analysis used*
* Differential expression: supervised gene selection  

<br>
<br>
<br>

* The button below brings you to the form in which you can submit your answers for section 1.7

<button button class="course googleform" onclick="window.open('https://docs.google.com/forms/d/e/1FAIpQLSfbXuvePyJg5CKj_mE1UygJwrI-GJD39FrM16nY2Uh7YrtsHw/viewform?usp=sf_link','_blank');" type="button">Open the form for section 1.7</button> 
<br>
<br>

* Go back to the main portal of R2 by clicking the button below.

<form name="main_34_pairs_and_crest" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gsenatgengeo34_u133p2">
  <button type="submit" class="course r2submit" >Go to R2 main</button>
</form>  
<br>
<br>


Again we're going to find out which genes make a difference, but now in a specific subset of genes that has been annotated to have Transcription Factor activity. This is gathered from databases that collect that information from peer reviewed publications. 
* In field 3 select **Find Differential expression between groups** Click **Next**
* Like before, select the track that contains information about the cell types*.
* We're now also going to filter for a specific gene filter. In the **Gene Filters** section, choose from the bottom dropdown the category *C: geneannot* as **Gene set**. Now click again on the **same dropdown**, and you will see that the dropdown list has expanded with different subcategories. Select the subcategory transcription factors, *SC: TF (945)*. Click **Next**. 
* In the next screen we're asked to further filter for the specific types of samples to compare. Here we're focusing on the difference between ADRN and MES; select these (i.e. uncheck neural\_crest). Click **Next**. 
* A list of genes appears. Investigate the top 4 by clicking on the hyperlinked gene symbols. This brings you to the expression view of the gene. 
* From here you can also access the NCBI gene database containing additional information on the function of the gene and related scientific publications. Do this by clicking on the hyperlinked **GeneID** number in the top table. You'll arrive at a website that gathers all known information on genes. A useful section is the **Bibliography** containing short summaries of relevant scientific papers.

---------

  ![](_static/images/R2d2_logo.png)**Armed with this information, which gene would you choose for further research? Why?**
<br>
<br>

---------


Proving causes: manipulating cell lines
------------------------------------------

From experiments it is known that cells can change their nature, some cells exhibit a certain plasticity.  

* The button below brings you to the form in which you can submit your answers for section 1.8

<button class="course googleform" onclick="window.open('https://docs.google.com/forms/d/e/1FAIpQLScdjNTEfcu5vuyskvWbKASj3xani-_eMwvN26N1_-F5gYF0tw/viewform?usp=sf_link','_blank');" type="button">Open the form for section 1.8</button> 
<br>
<br>

---------

  ![](_static/images/R2d2_logo.png)**From your own biomedical knowledge, can you explain why this is of relevance to cancer?**
<br>
<br>

---------

From experiments in our lab it became evident that the two cell types found in Neuroblastoma were able to switch. After a given period of time cells in dishes changed their nature as was proven by the expression of certain marker proteins on their surface.  
Now that we have a candidate Transcription Factor we can try to investigate its relevance in this plasticity by manipulating the gene in cell lines we grow in the lab. 

---------

  ![](_static/images/R2d2_logo.png)**Can you think of ways to manipulate genes in cell lines?**
<br>
<br>

---------

The TF was inducibly expressed in the SKNBE cell line and this was monitored through time for its gene expression using Affymetrix mRNA arrays. The resulting data was added to the dataset we used above for comparison. 


---------

  ![](_static/images/R2d2_logo.png)**To which of the cell types does SKNBE belong?**
<br>
<br>

---------

*Data used:*
* A combination of the 4 cell line pairs, additional classical Neuroblastoma cell lines, cells from the neural crest lineage and lines that had the TF inducible expressed for increasing periods (Mixed Neuroblastoma (MES-ADRN-Crest-Exp) - Versteeg - 52 - MAS5.0 - u133p2)


*Techniques used:* 
* Inducible gene expression
* mRNA expression data

*Analysis used*
* Signature score comparison

<br>
<br>
  
* Go to the R2 main page by clicking the button below, the correct dataset will be selected.  

<form name="52_pairs_crest_exp" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gsenatgen2017geo52_u133p2">
  <button type="submit" class="course r2submit" >Go to R2 main, inducible TF set</button>
</form>  
<br>
<br>

* Select in field 3 the **Relate 2 tracks** option. R2 has calculated signature scores for all samples in both signatures; in this dataset these tracks are called *adrn_score* and *mes_score*. Relate the two tracks, adapt the **ColorMode** to **Color by Track** and try the *mes_adrn_time* track. This track contains information on the time that the PRRX1 gene expression was induced in the SKNBE cell line.

---------

  ![](_static/images/R2d2_logo.png)**What is your conclusion from this experiment?**
<br>
<br>

---------

* This conclusion is even more obvious when the sequence of events is highlighted, as can be done in R2. The relations between the isogenic pairs are also illustrated. Click the button below to view the graph annotated in this way, a figure that can be incorporated in a publication right away. 

<form name="timepath" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gsenatgen2017geo52_u133p2">
<input type="hidden" name="species" value="hs">
<input type="hidden" name="selectedtrack" value="adrn_score">
<input type="hidden" name="selectedtracky" value="mes_score">
<input type="hidden" name="subsettracksubset" value="experiment-group">
<input type="hidden" name="graphtype" value="XY">
<input type="hidden" name="colormode" value="colorbytrack">
<input type="hidden" name="trackforcolor" value="mes_adrn_time">
<input type="hidden" name="option" value="display2">
<input type="hidden" name="exageratemark" value="no">
<input type="hidden" name="chainedsams" value="gsm2413241,gsm2413246:#eeeeee;gsm2413239,gsm2413243:#eeeeee;gsm2413242,gsm2413245:#eeeeee;gsm2413240,gsm2413244:#eeeeee;gsm2413257,gsm2413247,gsm2413248,gsm2413249:#222222:2;gsm2413249,gsm2413250,gsm2413251,gsm2413252,gsm2413253,gsm2413254:#222222:3;gsm2413254,gsm2413255,gsm2413256:#222222:4">
<input type="hidden" name="fontsize_ruler" value="25">
<input type="hidden" name="fontsize_y" value="30">
<input type="hidden" name="dotsize" value="5">
<button type="submit" class="course r2submit" >Show time path annotation in R2</button>
</form>  
<br>
<br>


Creating hypotheses: relating to chromatin modification data
---------------------------------------------------------------

Apparently this TF is capable of shifting cells from one state to the other. How can we further determine causal relations and ideally targetable processes in these cancer cells? How is a switch dynamically possible? A growing body of evidence implicates enhancers as key elements defining cell identity but the relationship of these enhancers to intratumoral heterogeneity is unknown. We performed ChIP-Seq analysis of the H3K27ac histone modifications for the isogenic cell line pairs. 

*Data used:*
* Four MES and five ADRN neuroblastoma cell lines, including three isogenic cell line pairs. 

*Techniques used:* 
* ChIP-Seq analysis

*Analysis*
* Genome Browser: analyzing histone modifications marking active enhancers
* Differential Expression
<br>
<br>
<br>

* The button below brings you to the form in which you can submit your answers for section 1.9

<button class="course googleform" onclick="window.open('https://docs.google.com/forms/d/e/1FAIpQLScQC2N5QsLOOUJULFuooscO4gAKzxyE_0nk-OM1n5MLvlslRw/viewform?usp=sf_link','_blank');" type="button">Open the form for section 1.9</button> 
<br>
<br>

---------

  ![](_static/images/R2d2_logo.png)**Can you explain what the goal of this experiment was?**
<br>
<br>

---------


First we'll check one of the HAND genes, known to play a role in the development of the sympatho-adrenal lineage from the neural crest.  

---------

  ![](_static/images/R2d2_logo.png)**What do you expect for the H3K27ac signals?**
<br>
<br>

---------

* Click on the button below to show the ChIP-Seq data for HAND1 in the four mesenchymal and five adrenergic neuroblastoma cell lines. For your convenience the signals are colored according to the type (MES or ADRN) of cell line.  

<form name='genomebrowser_tf' action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" method='POST' target='_gv'>
<input type='hidden' name='option' value='gbv2_base'>
<input type='hidden' name='|a01giemsa' value='on'>
<input type='hidden' name='a02bsequence' value='off'>
<input type='hidden' name='a02csequence' value='off'>
<input type='hidden' name='a04cons' value='off'>
<input type='hidden' name='a10refseq' value='on'>
<input type='hidden' name='a10refseq_cds' value='off'>
<input type='hidden' name='a10refseq_features' value='off'>
<input type='hidden' name='a15ensgene' value='off'>
<input type='hidden' name='arrayreporters' value='off'>
<input type='hidden' name='breadcrumbs' value=''>
<input type='hidden' name='breast_basis_fisher_v1' value='off'>
<input type='hidden' name='cg_annotvars' value='off'>
<input type='hidden' name='cg_calldifso' value='off'>
<input type='hidden' name='cg_calldifso_v25_18' value='off'>
<input type='hidden' name='cg_cgh1k_seg' value='off'>
<input type='hidden' name='cg_cgh1k_segv2' value='off'>
<input type='hidden' name='cg_cgh1k_segv2_v2' value='off'>
<input type='hidden' name='cg_evidence_bc' value='off'>
<input type='hidden' name='cg_junction' value='off'>
<input type='hidden' name='cg_junctiondif' value='off'>
<input type='hidden' name='cg_mei_v1' value='off'>
<input type='hidden' name='cg_varfileb_25' value='off'>
<input type='hidden' name='cgh_acgh_kdp_v1' value='off'>
<input type='hidden' name='cgh_cgcgh_pmc_v1' value='off'>
<input type='hidden' name='cgh_mixed_seg' value='off'>
<input type='hidden' name='cgh_public_ccle' value='off'>
<input type='hidden' name='cgh_v4' value='off'>
<input type='hidden' name='chip_col_v2' value='20150468:#c1c1c1,20150469:#129944,20150470:#366092,20150471:#c1c1c1,20150472:#129944,20150473:#366092,20150755:#c1c1c1,20150756:#366092,20150757:#c1c1c1,20150758:#E46D0A,20150759:#c1c1c1,20150760:#aa0000,20150761:#c1c1c1,20150762:#aa0000,20150763:#c1c1c1,20150764:#129944,20150765:#c1c1c1,20150766:#E46D0A,20150767:#c1c1c1,20150768:#366092,20150769:#c1c1c1,20150770:#aa0000,20150771:#129944,20150772:#129944,20150773:#129944,20150774:#129944,20150775:#366092,20150776:#129944,20150777:#129944,20150778:#129944,20160425:#0000AA,20160427:#0000AA,20160428:#0000AA,20160520:#0000aa,20160521:#129944,20160522:#129944,20160523:#aa0000,20160524:#aa0000,20161175:#c1c1c1,20161176:#0000aa,20161177:#c1c1c1,20161178:#129944,20161179:#aa0000,20161183:#c1c1c1,20161184:#129944,20161185:#E46D0A,20161202:#c1c1c1,20161203:#129944,20161204:#aa0000,20161205:#c1c1c1,20161206:#129944,20161207:#0,29160113:#0000aa,29160114:#129944,29160115:#129944,29160116:#aa0000,29160117:#aa0000,20150473_e200:#aa0000,20161178-e200:#129944,20161179-e200:#aa0000,C0018:#aa0000,C0018-et200:#aa0000,C0019:#aa0000,C0019-et200:#aa0000,C0020:#c1c1c1,C0021:#aa0000,C0021-et200:#aa0000,C0022:#aa0000,C0022-et200:#aa0000,ENCFF000KID:#aa0000,ENCFF000KIE:#aa0000,ENCFF000KIG:#aa0000,ENCFF000KIH:#aa0000,ENCFF001GFL:#aa0000,ENCFF001GFN:#aa0000,GSE71072:#aa0000,GSM1532401:#aa0000,GSM1532402:#aa0000,GSM1532405:#aa0000,GSM1532408:#aa0000,GSM1532409:#aa0000,GSM1532411:#aa0000,GSM1532414:#aa0000,GSM1532415:#aa0000,GSM1532417:#aa0000,GSM1602665:#aa0000,GSM1602665OG:#aa0000,GSM1602666:#0000aa,GSM1602667:#0000aa,GSM1602668:#0000aa,GSM1680101:#aa0000,GSM1680102:#0000aa,GSM1680104:#aa0000,GSM1680105:#0000aa,GSM1680107:#aa0000,GSM1693097:#0000aa,GSM1693098:#0000aa,GSM1693101:#0000AA,GSM1693102:#0000AA,GSM1693105:#c1c1c1,GSM1693117:#222222,GSM1693118:#222222,GSM1867061:#0000AA,GSM2027301:#222222,GSM2066632:#0000AA,GSM2113517:#aa0000,GSM2113518:#aa0000,GSM2113519:#129944,GSM2113521:#0000aa,GSM2113522:#aa0000,GSM2113523:#0000aa,GSM2113524:#aa0000,GSM2113526:#0000aa,GSM2113527:#aa0000,GSM2113529:#0000aa,GSM2113530:#aa0000,GSM2113532:#0000aa,GSM2113533:#0000aa,GSM2120699:#129944,GSM2120700:#aa0000,GSM2120701:#aa0000,GSM2120702:#aa0000,GSM2120703:#c1c1c1,GSM2120704:#129944,GSM2120705:#aa0000,GSM2120706:#aa0000,GSM2120707:#aa0000,GSM2120708:#c1c1c1,GSM2120709:#aa0000,GSM2120710:#c1c1c1,GSM2120711:#129944,GSM2120712:#aa0000,GSM2120713:#aa0000,GSM2120714:#aa0000,GSM2120715:#c1c1c1,GSM2120716:#aa0000,GSM2120717:#c1c1c1,og00001:#0000aa,zr1010_2:#aa0000,zr96905:#c1c1c1,zr96906:#aa0000,zr969_12:#aa0000,zr969_2:#aa0000,zr969_4:#aa0000,zr969_7:#aa0000,20150470-et200:#366092,20150473-et200:#366092,20150756-et200:#366092,20150768-et200:#366092,20150775-et200:#366092,20161185-et200:#E46D0A,20161207-et200:#E46D0A,20150766-et200:#E46D0A,20150758-et200:#E46D0A,'>
<input type='hidden' name='chip_exp_v2' value='20150470-et200,20150473-et200,20150756-et200,20150758-et200,20150766-et200,20150768-et200,20150775-et200,20161185-et200,20161207-et200'>
<input type='hidden' name='chip_height' value='45'>
<input type='hidden' name='chip_label_size' value='12'>
<input type='hidden' name='chip_libscale' value='20000000'>
<input type='hidden' name='chip_max' value='10'>
<input type='hidden' name='chip_min' value='a'>
<input type='hidden' name='chip_ord_v2' value='undefined:,20161207-et200:a,20161185-et200:b,20150775-et200:e,20150766-et200:c,20150758-et200:d,20150756-et200:g,20150768-et200:f,20150473-et200:h,20150470-et200:i,'>
<input type='hidden' name='chip_signif' value='false'>
<input type='hidden' name='chip_slider' value='no'>
<input type='hidden' name='chip_slider_value' value='3'>
<input type='hidden' name='chip_table' value='chip_raw'>
<input type='hidden' name='chrom' value='chr5'>
<input type='hidden' name='clinvar' value='off'>
<input type='hidden' name='combiset' value='ps_amc_ticcellcheck43_u133p2'>
<input type='hidden' name='cosmic' value='off'>
<input type='hidden' name='cosmic_mutascape' value='off'>
<input type='hidden' name='cpct_bc' value='off'>
<input type='hidden' name='cpct_design' value='off'>
<input type='hidden' name='cpct_variants' value='off'>
<input type='hidden' name='cpgisland' value='off'>
<input type='hidden' name='custom_id' value='20150756,20150758,20150775,20161207,20161185,20150470,20150473,20150766,20150768'>
<input type='hidden' name='custom_id_not' value=''>
<input type='hidden' name='custom_jscan_dz' value='off'>
<input type='hidden' name='dbsuper' value='off'>
<input type='hidden' name='dbtss' value='off'>
<input type='hidden' name='dkfz_cg_calldifso_v20_16' value='off'>
<input type='hidden' name='dkfz_cg_cgh1k_seg' value='off'>
<input type='hidden' name='dkfz_cg_evidence_bc' value='off'>
<input type='hidden' name='dkfz_cg_testvar_v2e' value='off'>
<input type='hidden' name='dkfz_cg_varfileb_20' value='off'>
<input type='hidden' name='dkfz_junctiondif' value='off'>
<input type='hidden' name='dkfzpdx1_450k_cn' value='off'>
<input type='hidden' name='dkfzpdx2_450k_cn' value='off'>
<input type='hidden' name='elmer_nm_1kg_e5' value='off'>
<input type='hidden' name='elmer_nm_1kg_e5e5' value='off'>
<input type='hidden' name='elmer_nm_rs_mac1_2' value='off'>
<input type='hidden' name='elmer_nm_var_all' value='off'>
<input type='hidden' name='encode_bed_data_v1' value='off'>
<input type='hidden' name='encode_tf_v1' value='off'>
<input type='hidden' name='end' value='154120827'>
<input type='hidden' name='epi_roadmap' value='off'>
<input type='hidden' name='exomevarserver' value='off'>
<input type='hidden' name='express_background' value=''>
<input type='hidden' name='express_drawtype' value=''>
<input type='hidden' name='express_ext' value='yes'>
<input type='hidden' name='express_height' value='60'>
<input type='hidden' name='express_max' value='a'>
<input type='hidden' name='express_min' value='a'>
<input type='hidden' name='express_minpres' value='1'>
<input type='hidden' name='express_selectedtrack' value='u-mesne_2016_c'>
<input type='hidden' name='express_slider' value='no'>
<input type='hidden' name='express_slider_value' value='3'>
<input type='hidden' name='express_transform' value='transform_zscore'>
<input type='hidden' name='fantom5_cage_test' value='off'>
<input type='hidden' name='fantom5_enhancer_premissive' value='off'>
<input type='hidden' name='fantom5_enhancer_robust' value='off'>
<input type='hidden' name='fantom5_enhancer_tss_fdr' value='off'>
<input type='hidden' name='filterfilein' value=''>
<input type='hidden' name='fw_se_overlap_v1' value='off'>
<input type='hidden' name='fw_se_overlap_v2' value='off'>
<input type='hidden' name='g_position' value=''>
<input type='hidden' name='genesets_v1' value='off'>
<input type='hidden' name='genome_build' value='hg19'>
<input type='hidden' name='gwascatalog' value='off'>
<input type='hidden' name='hic_domains_lit' value='off'>
<input type='hidden' name='hugoonce' value='yes'>
<input type='hidden' name='icgc_snv_pbca' value='off'>
<input type='hidden' name='imagewidth' value='1000'>
<input type='hidden' name='inform_450k_baf' value='off'>
<input type='hidden' name='inform_450k_cn' value='off'>
<input type='hidden' name='inform_cg_cgh10k_segv2' value='off'>
<input type='hidden' name='inform_cg_somatic_coding_v1' value='off'>
<input type='hidden' name='ither_450k_cn' value='off'>
<input type='hidden' name='ither_cgh10k_segv2' value='off'>
<input type='hidden' name='ither_somatic_coding_v1' value='off'>
<input type='hidden' name='lincipedia' value='off'>
<input type='hidden' name='liver_enhancer_cell201501' value='off'>
<input type='hidden' name='macs14_amc_og_v1' value='off'>
<input type='hidden' name='macs14_geo_og_v1' value='off'>
<input type='hidden' name='macs2_amc_og_v1' value='off'>
<input type='hidden' name='macs2_broad_fw_v1' value='off'>
<input type='hidden' name='macs2_broad_og_v1' value='off'>
<input type='hidden' name='modus' value='complex:chip:ps'>
<input type='hidden' name='mook_cgcgh' value='off'>
<input type='hidden' name='nc_enhancer_prescott_2015' value='off'>
<input type='hidden' name='newgene' value=''>
<input type='hidden' name='ngs_cgcgh_mb_v1' value='off'>
<input type='hidden' name='ngs_cgcgh_pdx1_v1' value='off'>
<input type='hidden' name='ngs_cgcgh_ped_v1' value='off'>
<input type='hidden' name='og_motif_b_gata3peaks' value='off'>
<input type='hidden' name='og_motif_b_transfac' value='off'>
<input type='hidden' name='og_motif_c' value='off'>
<input type='hidden' name='og_se_overlap_v1' value='composition10'>
<input type='hidden' name='og_se_overlap_v2' value='off'>
<input type='hidden' name='pluginopt:a01giemsa:height' value='11'>
<input type='hidden' name='pluginopt:a01giemsa:style' value='standard'>
<input type='hidden' name='pluginopt:a10refseq:class' value='protein_coding'>
<input type='hidden' name='pluginopt:a10refseq:detail_modes_full' value='10000'>
<input type='hidden' name='pluginopt:a10refseq:height' value='18'>
<input type='hidden' name='pluginopt:a10refseq:hilite' value=''>
<input type='hidden' name='pluginopt:a10refseq:represent' value='merge_by_symbol'>
<input type='hidden' name='pluginopt:og_se_overlap_v1:height' value='10'>
<input type='hidden' name='pluginopt:og_se_overlap_v1:modus' value='default'>
<input type='hidden' name='pluginopt:og_se_overlap_v1:overlap' value='0'>
<input type='hidden' name='pluginopt:rose_se_r0_s0_t0_v1:height' value='9'>
<input type='hidden' name='pluginopt:rose_se_r0_s0_t0_v1:is_super' value='1'>
<input type='hidden' name='pluginopt:rose_se_r0_s0_t0_v1:modus' value='by_factor'>
<input type='hidden' name='pluginopt:rose_se_r0_s0_t0_v1:rose_bam' value='0'>
<input type='hidden' name='pluginopt:rose_se_r0_s0_t0_v1:rose_conf_size' value='0'>
<input type='hidden' name='profilename' value='171010_wwtr1_mes_se'>
<input type='hidden' name='rmsk' value='off'>
<input type='hidden' name='rose_se_pub_rseg_m2_s0_t0_v1' value='off'>
<input type='hidden' name='rose_se_r0_s0_t0_v1' value='off'>
<input type='hidden' name='rose_se_r0_s0_t2500_v1' value='off'>
<input type='hidden' name='rose_se_test' value='off'>
<input type='hidden' name='rose_se_v1' value='off'>
<input type='hidden' name='rseg_ac_me3_v1' value='off'>
<input type='hidden' name='rseg_pub_og_v1' value='off'>
<input type='hidden' name='rseg_v1' value='off'>
<input type='hidden' name='rsegdiff_test' value='off'>
<input type='hidden' name='rsegdiff_v1' value='off'>
<input type='hidden' name='sample' value='dataset_track'>
<input type='hidden' name='snp138' value='off'>
<input type='hidden' name='snp_array' value='off'>
<input type='hidden' name='start' value='153591527'>
<input type='hidden' name='superenhancer_nb_george' value='off'>
<input type='hidden' name='sv_delly_pedcan1' value='off'>
<input type='hidden' name='sv_ivo_mb500' value='off'>
<input type='hidden' name='svg' value='false'>
<input type='hidden' name='switch' value='add'>
<input type='hidden' name='target_ilmn_cgh_seg' value='off'>
<input type='hidden' name='target_wxs_cgh_seg' value='off'>
<input type='hidden' name='thiesen_cg_calldifso_v20_18' value='off'>
<input type='hidden' name='thiesen_cg_cgh1k_segv2' value='off'>
<input type='hidden' name='thiesen_cg_evidence_bc' value='off'>
<input type='hidden' name='thiesen_cg_varfileb_20' value='off'>
<input type='hidden' name='thiesen_junction' value='off'>
<input type='hidden' name='thiesen_junctiondif' value='off'>
<input type='hidden' name='tmp_bed' value='off'>
<input type='hidden' name='tmp_bed2' value='off'>
<input type='hidden' name='usergroup' value='personal'>
<input type='hidden' name='vcfe_dkfz_som_mb500_v1' value='off'>
<input type='hidden' name='vcfe_dkfz_som_pdx1_v1' value='off'>
<input type='hidden' name='vcfe_dkfz_som_suz_v1' value='off'>
<input type='hidden' name='vcfe_msk_impact_nat_med_17' value='off'>
<input type='hidden' name='vista_enhancers' value='off'>
<input type='hidden' name='vucghseq_mixed_seg' value='off'>
<input type='hidden' name='vumc_cg_calldifso_v20_18' value='off'>
<input type='hidden' name='vumc_cg_cgh1k_segv2' value='off'>
<input type='hidden' name='vumc_cg_evidence_bc' value='off'>
<input type='hidden' name='vumc_cg_mei_v1' value='off'>
<input type='hidden' name='vumc_cg_varfileb_20' value='off'>
<input type='hidden' name='vumc_junction' value='off'>
<input type='hidden' name='vumc_junctiondif' value='off'>
<input type='hidden' name='wgencoderegdnaseclusteredv2' value='off'>
<input type='hidden' name='wgs_cgh1k_curie_seg' value='off'>
<input type='hidden' name='wgs_cgh1k_nbrel_seg' value='off'>
<input type='hidden' name='wgs_cgh1k_nbrel_segsqza' value='off'>
<input type='hidden' name='wgs_cgh1k_nbrel_segsqza_pn' value='off'>
<input type='hidden' name='wgs_cgh1k_seg' value='off'>
<input type='hidden' name='wgs_curie_junction' value='off'>
<input type='hidden' name='wgs_dcgh10k_curie_seg' value='off'>
<input type='hidden' name='wgs_dcgh10k_nbrelsqza_seg' value='off'>
<input type='hidden' name='wgs_junction' value='off'>
<input type='hidden' name='wgs_maris_calldifso_v20_18' value='off'>
<input type='hidden' name='wgs_maris_cgh1k_seg' value='off'>
<input type='hidden' name='wgs_maris_junctiondif' value='off'>
<input type='hidden' name='wgs_ploidy1k_curie_seg' value='off'>
<input type='hidden' name='wgs_ploidy1k_seg' value='off'>
<input type='hidden' name='wgs_sequenza1k_nbrel_seg' value='off'>
<input type='hidden' name='wgs_somatic_snpsift' value='off'>
<input type='hidden' name='wgs_somatic_snpsift_missense' value='off'>
<input type='hidden' name='wgs_somatic_strelka' value='off'>
<input type='hidden' name='wgs_somatic_varscan2' value='off'>
<input type='hidden' name='wgs_varfileb_maris_20' value='off'>
<button type="submit" class="course r2submit" >Go to R2 GenomeBrowser for HAND1</button>
</form>
<br>
<br>

Regions encoding genes are drawn at the bottom of the graph. When in red they're encoded in the reverse direction, coding exons are darker.  

---------

  ![](_static/images/R2d2_logo.png)**Can you explain this graph? What do you expect for the expression of this gene?**
<br>
<br>

---------


* At the top of the page click on the **zoom out 10X** button. Look at the differences between the cell lines 


The chromatin state is especially important for transcription factors; we'll re-visit the list of transcription factors that are differentially expressed between the MES and ADRN cell lines.

---------

  ![](_static/images/R2d2_logo.png)**Why are Transcription Factors of interest in this setting?**
<br>
<br>

---------

* Perform the differential expression analysis again by clicking on the button below

<form name="tfdifexprform" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
<input type='hidden' name='minpres' value='1'>
<input type='hidden' name='option' value='display'>
<input type='hidden' name='table' value='ps_avgpres_gsenatgengeo34_u133p2'>
<input type='hidden' name='hugoonce' value='yes'>
<input type='hidden' name='cortype' value='transform_log2'>
<input type='hidden' id="geneset0-geneset-select" name="geneset" value="geneannot::TF::transcription factor">
<input type='hidden' name='selectedtrack' value='cell_type'>
<input type='hidden' name='test' value='anova'>
<input type='hidden' name='factor' value='NG_mes_adrn_nc'>
<input type='hidden' name='subset' value='TRACKER:,0,1,2,3,4,5,6,7,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33'>
<button type="submit" class="course r2submit" >Go to R2 differential expression of TF's</button>
</form>
<br>
<br>

* Use both expression analysis and the enhancer data in the genomebrowser to decide which transcription factors would be worthwhile to further investigate. In the genomebrowser that was still open from the previous question, type the name of the gene in the left upper corner textfield. To further explore the larger region around the gene you can use the zoom buttons at the top of the page.  


---------

  ![](_static/images/R2d2_logo.png)**Which Transcription Factor would you consider for further study?**
<br>
<br>

---------



Suggesting therapy
---------------------

* With the current new knowledge that you derived above, can you think of a strategy to use the fact that neuroblastoma is a heterogenous tumor consisting of a mesenchymal, motile cell type and a adrenergic, differentiated cell type for therapeutic options? This is an open question, so be creative, you might find something interesting! If you want, you can follow the suggestions below.  
  
* Use the button of 1.9 to perform a differential expression analysis. This time explore other gene categories that could be interesting for drug development. Look at the expression profiles of some genes of your choice. 
  * Hint: There is a category "drugtargets" in R2 to select druggable proteins; you can select this in the same dropdown where the TF selection was done.  
  * Another very interesting gene category is the "kinase" category, this contains known kinases that have active roles in pathways.
* The first button in 1.9 takes you to the Genome Browser at the position of the HAND1 gene. In the upper left corner of that page, you can fill in other genes of interest to look at the ChIP-Seq profiles of the samples at these locations of the genome. Do this for the genes whose expression profiles you just have studied. Try to find genes that show consistent chromatin modification profiles for the one type of neuroblastoma cell lines and a different consistent profile for the other type. 
* Knowledge about pathways can be exploited as well.
* The NCBI database can provide additional information from literature about the genes of interest.
 
 <br>
 <br>
 <br>
 
 * The button below brings you to the form in which you can submit your answers for section 1.10

 <button class="course googleform" onclick="window.open('https://docs.google.com/forms/d/e/1FAIpQLSd7iB8d2ozHEsYx4KidGxLdhQRefUw2-03gGGnmpJ6eoqhdlA/viewform?usp=sf_link','_blank');" type="button">Open the form for section 1.10</button> 
 <br>
 <br>
  
---------

  ![](_static/images/R2d2_logo.png)**Which strategy do you suggest?**
<br>
<br>

---------

Final remarks / future directions
---------------------------------
In the March 1st 2018 issue of Nature a paper was published describing a landscape of genomic alterations across childhood cancers. The data is accessible in R2 also as a Datascope. This is another example of how R2 can visualize your genomics data. 

This ends the course. Feel free to further explore the course materials or our tutorials.

We hope that this course has been helpful. If you want to have your genomics data visualized and analyzed using the R2 platform you can always consult r2-support@amc.nl

The R2 support team.


