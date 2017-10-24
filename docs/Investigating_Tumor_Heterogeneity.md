<a id="investigating_tumor_heterogeneity"> </a>

Investigating Tumor Heterogeneity
=================================

*Learn how to use the R2 data analysis platform to analyse tumor heterogeneity in Neuroblastoma*


Introduction
------------

Cancer is a very complex disease. Much more complicated than originally anticipated when the first mutations were found to be causal for specific cancers. During the lectures you’ve been shown how this works in colorectal cancer, where a well defined path of subsequently gained mutations leads to more aggressive tumorigenic cell types (the Vogelstein model).

  ![Figure1: Mutation paths during cancer progression.](_static/images/TumorHeterogeneity_CancerProgression.jpg "Figure1: Mutation paths during cancer progression.")
	
  [**Figure1: Mutation paths during cancer progression.**](_static/images/TumorHeterogeneity_CancerProgression.jpg)

Although there has been extensive research into similar mutation mechanisms in Neuroblastoma (also in the AMC Oncogenomics group), such a mechanism has not been found for this type of cancer. In this practical work session we will try to bring you to the cutting edge of research into this often deadly childhood tumor. From the lectures you should have learned already that this tumor seems to be heterogenic by nature. There is reason to believe that this heterogeneity causes the high percentage of relapses in the aggressive subtype of Neuroblastoma. Children experiencing a relapse almost always die. 
Fortunately new technologies have become available to molecular biology. These enable us to study not only the mutations and RNA expression of genes but also study the epigenetic modifications of the DNA and accompanied histones. And in addition genes can now be manipulated in cell lines and living tissues. 
Using advanced data analysis, statistics and clustering methods, the new field of bioinformatics tries to derive new insights from these experimental data and help molecular biologists to generate new hypotheses that can be tested experimentally.
Today you will use a web-based genomics analysis and visualization platform, R2, that provides you with a set of such bioinformatics tools to investigate recent patient and experimental data from Neuroblastoma tumors and cell lines. 
Neuroblastoma is a pediatric tumor of the peripheral adrenergic lineage, which is neural crest derived. During embryogenesis, cells delaminate from the neural crest, migrate ventrally and differentiate into adrenaline- or noradrenaline-producing cells. Neuroblastomas typically express enzymes for the adrenaline-synthesis route. High-stage neuroblastomas usually go into complete remission upon therapy but often relapse as therapy-resistant disease.
Using recent molecular biology data gathering techniques and advanced bioinformatic data analysis algorithms we set out to investigate this nasty characteristic of Neuroblastoma tumors. From single patients we obtained two biopsies that were cultured as separate cell lines.    


Tumors and lineages: clustering data
---------------------------------------

For a start we'll investigate so called "classical" cell lines of Neuroblastoma tumors. Classical cell lines are cultured cell lines that can be grown and passaged indefinetely. A typical example is the classic HeLa cell line, taken from a cervical adenocarcinoma of Henrieta Lacks in 1951 that has been in culture since.  
How do these profiles relate to cell lines of other tumors? Additional data about classical cell lines from other childhood tumors is available in the resources of the scientific community. For each publication scientists are required to make their data available in public repositories.  
We can use these in a larger public dataset of other tumor cell lines and see how they relate. 

*Dataset used:*  
* 86 classical cell lines derived from 6 different childhood tumors (Cellline Childhood cancer - ITCC - 86 - MAS5.0 - u133p2)

*Techniques used:*   
* mRNA Microarray expression

*Analysis used*  
* Principle Components Analysis

##### A first impression of your data; expression of key genes

* Go to R2 by clicking on the button below: TODO; this still has to point to the proper set  


<form name="main_4_pairs" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gse90803geo8_u133p2">
  <button type="submit" >Go to R2</button>
</form>  


* You're now on the R2 main page. This web based molecular biology data analysis platform contains a wealth of data and methods to analyze these. Step by step researchers are guided through a web of data analysis possibilities. The portal of R2 shows this principle; step through each of the fields to your analysis of choice. In this case we're first going to see if and how the mRNA expression of several genes changes through a single dataset. 

---------
  ![](_static/images/R2d2_logo.png)**Can you think of a gene that might mark differences between these tumors?**

> *----*

---------

  * In field 3 type the name of the gene and click next
  * Leave all settings to default and click next
  * A graph shows the expression of this gene's mRNA in the whole set of childhood tumor cell lines.

---------
  ![](_static/images/R2d2_logo.png)**Do you observe a difference between different cell lines?**

> *----*

---------
  

  * If you did not already choose this gene, now try the gen NMYC
  
---------
  ![](_static/images/R2d2_logo.png)**Can you say something about the role this gene can play in cancer?**

> *----*

  ![](_static/images/R2d2_logo.png)**What do you observe from the data annotation track below?**

> *----*

---------
  
##### A first impression of your data; Principle Components Analysis

* To get a first impression of the type of data we're dealing with, an unbiased unsupervised type of clustering analysis is a good idea. A suitable method is the Principle Components Analysis (PCA). 

* Go to the main screen in R2


<form name="main_4_pairs" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gse90803geo8_u133p2">
  <button type="submit" >Go to main page R2</button>
</form>  

* In field 3 select Principle Components analysis (TODO; make this available)
* In the next screen leave all as is and click

---------
  ![](_static/images/R2d2_logo.png)**What kinds of tumors do you distinguish?**

> *----*

  ![](_static/images/R2d2_logo.png)**What is their lineage, can you relate this to a type of tissue?**

> *----*

  ![](_static/images/R2d2_logo.png)**What do you note about the Neuroblastoma cell lines?**

> *----*

---------


Urgency of research: patient material
----------------------------------------

In the former step we derived that Neuroblastoma cell lines seem to be less homogeneous than other childhood tumor classical cell lines. These so called classical cell lines have gone through thousands of cloning cycles and usually are pretty far off their original genomic composition. We’ve recently isolated from one patient from several tumor sites two biopsies per site. These are so called isogenic cell line pairs, see below. 

  ![Figure1: Bright field image of isogenic pairs.](_static/images/TumorHeterogeneity_IsoGenicPairsBF.png "Figure1: Bright field image of isogenic pairs.")
	
  [**Figure1: Bright field image of isogenic pairs.**](_static/images/TumorHeterogeneity_IsoGenicPairsBF.png)

---------
  ![](_static/images/R2d2_logo.png)**What do you note about the morphology of the cell lines?**

> *----*

---------

We’ve profiled the mRNA expression of these samples and of a so called classical cell line. To investigate the relations between these samples we’ve profiled them using Affymetrix RNA chips. The resulting gene expression patterns can be used perform a hierarchical clustering. 

*Dataset used:*  
  * Cell lines recently derived from three tumors from one patient. Two biopsies per tumor were taken. This dataset is combined with two classical Neuroblastoma cell lines that clustered far apart: SHEP and SY5Y (Mixed Neuroblastoma (MES-ADRN) - Versteeg - 8 - MAS5.0 - u133p2) 
  
*Techniques used:*  
* mRNA Microarray expression

*Analysis used*  
* Unsupervised hierarchical clustering
* Heatmap visualization

*References*  
*

* For this analysis we'll directly go to one of the analysis tools of R2; Toplister. The Toplister calculates which genes behave different through a dataset. It does so by calculating the genes whose expression values have the largest standard deviation within a given set of samples.
* Goto R2 by clicking the button below

<form name="toplisterform" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
<input type='hidden' name='minpres' value='1'>
<input type='hidden' name='howmany' value='300'>
<input type='hidden' name='option' value='high_ana2'>
<input type='hidden' name='table' value='ps_avgpres_gse90803geo8_u133p2'>
<input type='hidden' name='hugoonce' value='yes'>
<input type='hidden' name='set' value='highest'>
<input type='hidden' name='cortype' value='transform_2log'>
<button type="submit" >Go to R2</button>
</form>

* Check that the settings are as follows
* Click next; a list of genes appears

---------
  ![](_static/images/R2d2_logo.png)**Do you recognize any genes?**

> *----*

---------

* Use the mousewheel to scroll to the bottom of the page, here you can choose to perform an additional analysis. The Heatmap(z-score) produces a hierarchically clustered view of the expression values of the top 100 genes.  
* Click on Heatmap(z-score)

---------
  ![](_static/images/R2d2_logo.png)**What number of groups do you expect?**

> *----*

  ![](_static/images/R2d2_logo.png)**Given the former observations, what type of lineage can you assign to each group?**

> *----*

---------



Which genes make a difference? Creating signatures
-----------------------------------------------------

We have identified two different types of cells that seem to be related in different tumor sites in the same patient. What genes determine the difference between the two types? We’ll use RNA expression data again but now the other way around; based on a predefined classification in groups we look for genes that characterize this classification best, or in other words, that are differentially expressed between these two groups.

*Dataset used:*  
* Mixed Neuroblastoma (MES-ADRN) - Versteeg - 8 - MAS5.0 - u133p2 (same as above)
* Gene Ontology
* Broad curated hallmark datasets

*Techniques used:*   
* mRNA arrays

*Analysis used*  
* Overrepresentation calculation

*References*  
* 

* Go to the main page of R2

<form name="main_4_pairs" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gse90803geo8_u133p2">
  <button type="submit" >Go to R2</button>
</form>  


* In Field 3 choose Find Differential expression between groups
* This dataset has been annotated with type informations. Each sample was assigned to either the mesenchymal or the adrenergic type, in R2 this is called a *track*. Choose the proper track.

---------
  ![](_static/images/R2d2_logo.png)**How is this figure different from the former?**

> *----*

---------

* For future use the genes that make the difference have been stored for you as so called signatures. R2 provides additional analyses for this set of genes in the right panel of menu buttons. As a first analysis step we can check a data resource called the Gene Ontology that provides a tree of systematic ordered biological terms that is used to formally describe the biological role of each gene. R2 now calculates for each of the thousands of groups of genes that are annotated with a specific biological term whether your set of choice is over-represented in them.  

---------
  ![](_static/images/R2d2_logo.png)**What can you say about the function of the group of genes that are upregulated in the MES type of cells?**

> *----*

---------


* Now select the Geneset option Try Broad geneset EMT

---------
  ![](_static/images/R2d2_logo.png)**Which hallmark category of genes pops up as most important?**

> *----*

---------


Identifying groups: using signatures to classify other datasets
------------------------------------------------------------------

So we now have a signature that distinguishes between the two types of cells. How does this signature behave in other datasets? Does the same set of genes tell us something about other sets of tumors or cell lines?

*Dataset used:*
* A combination of the 8 cell lines above, additional classical Neuroblastoma cell lines and cells from the neural crest lineage (Mixed Neuroblastoma (MES-ADRN-CREST) - Versteeg/Etchevers - 34 - MAS5.0 - u133p2)

*Techniques used:* 
* mRNA expression data

*Analysis used*
* Heatmap analysis

*References*
* 
* Go to the main portal of R2 by clicking the button below; the dataset described above is automatically selected

<form name="main_34_pairs_and_crest" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gsenatgengeo34_u133p2">
  <button type="submit" >Go to R2</button>
</form>  


* In field 3 select View Geneset
* 
* View geneset with the combined signature and observe the high and low portions are similar   

---------
  ![](_static/images/R2d2_logo.png)**Which samples group together?**

> *----*

---------

---------
  ![](_static/images/R2d2_logo.png)**How does this relate to the above?**

> *----*

---------


Using scores for further characterization
--------------------------------------------

The expression patterns of these specific signature can be used to investigate the relative behavior of cell types. We can do this by summarizing the expression data of all genes in the signature in each cell type in one number; a signature score. These scores can be compared in more dimensions, in this case signature dimensions. First we'll analyze the scores separately.

*Dataset used:*
* Mixed Neuroblastoma (MES-ADRN-CREST) - Versteeg/Etchevers - 34 - MAS5.0 - u133p2

*Techniques used:* 
* 

*Analysis used*
* 

*References*

* Go back to the main portal of R2 by clicking the button below.

<form name="main_34_pairs_and_crest" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gsenatgengeo34_u133p2">
  <button type="submit" >Go to R2</button>
</form>  

* 
* First show each track, with boxplots  
* Next relate two tracks  



Finding causes; homing in on transcription factors
-----------------------------------------------------

Apparently there are two types of cells in Neuroblastoma tumors. Neuroblastoma seems to be a heterogenous tumor. Transcription factors are known to determine gene expression programs in cells. These gene expression programs determine the development of the cell. Can we determine which TF’s might determine the difference between both of these cell lines?

*Dataset used:*
* 

*Techniques used:* 
* 

*Analysis used*
* 

*References*
* 

* Differential expression between groups  
* select only MES and ADRN, select TF as category  
* Investigate top 4 high in MES in Entrez; which to choose?  



Proving causes; manipulating cell lines
------------------------------------------

From experiments we know that both cell types can switch
Now that we found the TF PRRX1 to be highly expressed in the MES type of cell lines we can try to investigate this relation by manipulating the gene in cell lines we grow in the lab. The gene was inducibly expressed in the cell lines and these were monitored through time for their gene expression. The PRRX1 gene was also silenced by using a CRISPR/Cas9 system.
Keyword: reprogramming

*Dataset used:*
* 

*Techniques used:* 
* 

*Analysis used*
* 

*References*
* 

* Show that experimental manipulation of one of them can move cell lines along the MES/ADRN axis
* Directly link to the dataset
* Toy around with colors till the one that explains most shows   


Creating hypotheses; relating to chromatin modification data
---------------------------------------------------------------

So the TF PRRX1 is capable of shifting cells from a MES state to an ADRN state. How can we further determine causal relations and probably targetable processes in these cancer cells? How is a switch dynamically possible? A growing body of evidence implicates enhancers as key elements defining cell identity but the relationship of these enhancers to intratumoral heterogeneity is unknown. We measured enhancer mark. We view a couple of genes from the signatures to discover patterns

Epigenetic versus genetic; the concept of re-programming

*Dataset used:*
*

*Techniques used:* 
*

*Analysis used*
*

*References*
*

* Directly link to the chromatin modification data from TF's that were found to be specific (MEOX?)
* Try different TF's and have them explain the difference

Suggesting therapy
---------------------


* Armed with the current new knowledge, can you think of a way to use the fact that neuroblastoma is a heterogenous tumor consisting of a mesenchymal, motile cell type and a adrenergic, differentiated cell type for therapeutic options?
* SKNSH; upon chemotherapy (drugs) mesenchymal shift; drugable are for example kinases; 
* Hints: 
* Figures:

*Dataset used:*
* 

*Techniques used:* 
* 

*Analysis used*
* 

*References*
* 


