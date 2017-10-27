<a id="investigating_tumor_heterogeneity"> </a>

Investigating Tumor Heterogeneity
=================================

*Learn how to use the R2 data analysis platform to analyse tumor heterogeneity in Neuroblastoma*

**NOTE:** This document is under construction.


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

For a start we'll investigate so called "classical" cell lines of Neuroblastoma tumors. Classical cell lines are cultured cell lines that can be grown and passaged indefinetely. A typical example is the classic HeLa cell line, taken from a cervical adenocarcinoma of Henrieta Lacks in 1951 that has been in culture since. How do these profiles relate to cell lines of other tumors? Additional data about classical cell lines from other childhood tumors is available in the resources of the scientific community. For each publication scientists are required to make their data available in public repositories. We can use these in a larger public dataset of other tumor cell lines and see how they relate. 

*Data used:*  
* 86 classical cell lines derived from 6 different childhood tumors (Cellline Childhood cancer - ITCC - 86 - MAS5.0 - u133p2)

*Techniques used:*   
* mRNA Microarray expression

*Analysis used*  
* t-SNE: t-distributed stochastic neighbor embedding statistics

##### A first impression of your data; expression of key genes

* Go to R2 by clicking on the button below:  


<form name="itcc_68_cell_lines" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_itcccellline86_u133p2">
  <button type="submit" >Go to R2</button>
</form>  


* You're now on the R2 main page. This web based molecular biology data analysis platform contains a wealth of data and methods to analyze these. Step by step researchers are guided through a web of data analysis possibilities. The portal of R2 shows this principle; step through each of the fields to your develop your analysis of choice. In this case we're first going to see if and how the mRNA expression of several genes changes through a single dataset. The proper dataset described above has been selected already. 

---------
  ![](_static/images/R2d2_logo.png)**Can you think of a gene that might mark differences between these tumor models?**

<br><br>

---------

  * In field 3 type the name of the gene and click next
  * Leave all settings to default and click **next**
  * A graph shows the expression of this gene's mRNA in the whole set of childhood tumor cell lines. Samples are along the x-axis, mRNA expression values along of the gene in a sample are on the y-axis. Below the graph is the available annotation for the samples shown in colored tracks. Hovering with your mouse over data points will show additional information.

---------
  ![](_static/images/R2d2_logo.png)**Do you observe a difference between different cell lines?**

<br>
<br>

---------
  

  * If you did not already choose this gene, now try the gene MYCN (Click the **Go to Main** link in the left upper corner)
  
---------
  ![](_static/images/R2d2_logo.png)**Can you say something about the role this gene can play in cancer?**

<br>
<br>

  ![](_static/images/R2d2_logo.png)**What do you observe from the data annotation track below?**

<br>
<br>

---------

##### A first impression of your data; tSNE maps

* We've seen that the expression of genes changes through the samples and some types of tumors seem to specifically express certain genes. To further explore the type of data we're dealing with, an unbiased unsupervised type of clustering analysis is a good idea. One recently developed algorithm is the tSNE map.  

* Go to the main screen in R2


<form name="itcc_68_cell_lines" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_itcccellline86_u133p2">
  <button type="submit" >Go to R2</button>
</form>  


* In the left menu bar select the **tSNE maps** option
* A selection of available tSNE maps appears; select *Cellline Childhood Cancer (public) - Versteeg - 86 - MAS5.0 - u133p2* 
* Click **Plot the t-SNE Default** result
* Colors are not set by default, under **ColorMode** select **Color by Track** and try different tracks, click next to show the changes 

---------
  ![](_static/images/R2d2_logo.png)**What kind of tumor models do you distinguish?**

<br>
<br>


  ![](_static/images/R2d2_logo.png)**What is their lineage, can you relate this to a type of tissue?**

<br>
<br>


  ![](_static/images/R2d2_logo.png)**What do you note about the Neuroblastoma cell lines?**

<br>
<br>


  ![](_static/images/R2d2_logo.png)**If you had to choose two cell lines for further investigation, which would you choose?**

<br>
<br>


---------


Urgency of research: patient material
----------------------------------------

In the former step we derived that Neuroblastoma cell lines seem to be less homogeneous than other childhood tumor classical cell lines. These so called classical cell lines have gone through thousands of cloning cycles and usually are pretty far off their original genomic composition. We’ve recently isolated from one patient from several tumor sites two biopsies per site. These are so called isogenic cell line pairs. A microscopic image is provided below. 

  ![Figure1: Bright field image of isogenic pairs.](_static/images/TumorHeterogeneity_IsoGenicPairsBF.png "Figure1: Bright field image of isogenic pairs.")
	
  [**Figure1: Bright field image of isogenic pairs.**](_static/images/TumorHeterogeneity_IsoGenicPairsBF.png)

---------
  ![](_static/images/R2d2_logo.png)**What do you note about the morphology of the cell lines?**

<br><br>

---------

We’ve profiled the mRNA expression of genes using Affymetrix RNA chips in these samples and of two classical Neuroblastoma cell lines that behave very different. The resulting gene expression patterns can be used perform a hierarchical clustering. 

*Data used:*  
  * Cell lines recently derived from three tumors from one patient. Two biopsies per tumor were taken. This dataset is combined with two classical Neuroblastoma cell lines that clustered far apart: SHEP and SY5Y (Mixed Neuroblastoma (MES-ADRN) - Versteeg - 8 - MAS5.0 - u133p2) 
  
*Techniques used:*  
* mRNA Microarray expression

*Analysis used*  
* Unsupervised hierarchical clustering
* Heatmap visualization


* For this analysis we'll directly go to one of the analysis tools of R2; Toplister. The Toplister calculates which genes behave different through a dataset. It does so by calculating the genes whose expression values have the largest standard deviation within a given set of samples.
* Goto R2 by clicking the button below

<form name="toplisterform" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
<input type='hidden' name='minpres' value='1'>
<input type='hidden' name='howmany' value='100'>
<input type='hidden' name='option' value='high_ana2'>
<input type='hidden' name='table' value='ps_avgpres_gse90803geo8_u133p2'>
<input type='hidden' name='hugoonce' value='yes'>
<input type='hidden' name='set' value='standard_deviation'>
<input type='hidden' name='cortype' value='transform_2log'>
<button type="submit" >Go to R2 Toplister</button>
</form>

* Click **next**; a list of genes appears

---------
  ![](_static/images/R2d2_logo.png)**Do you recognize any genes?**

<br>
<br>

---------

* Use the mousewheel to scroll to the bottom of the page, here you can choose to perform an additional analysis. The heatmap vizualization produces a hierarchically clustered view of the expression values of the top 100 genes.  

---------
  ![](_static/images/R2d2_logo.png)**What number of groups do you expect?**

<br><br>

---------

* Click on **Heatmap(z-score)**
* The cell line pairs from the patient were also investigated for the tumor stem cell marker gene CD133 and for their migration capability. See the results in the figure below:


  ![Figure1: CD133 Facs analysis and transwell migration assay of isogenic pairs](_static/images/TumorHeterogeneity_PairsCD133Migrate.png "CD133 Facs analysis and transwell migration assay of isogenic pairs")
	
  [**Figure1: CD133 Facs analysis and transwell migration assay of isogenic pairs**](_static/images/TumorHeterogeneity_PairsCD133Migrate.png)


---------

  ![](_static/images/R2d2_logo.png)**Given these observations, what lineage can you assign to each group?**

<br>
<br>

---------



Which genes make a difference? Creating signatures
-----------------------------------------------------

We have identified two different types of cells that seem to be related in different tumor sites in the same patient. Neuroblastoma apparently has a heterogenous nature. What genes determine the difference between the two types? We’ll use RNA expression data again but now the other way around; based on a predefined classification in groups we look for genes that characterize this classification best, or in other words, that are differentially expressed between these two groups.

*Data used:*  
* Mixed Neuroblastoma (MES-ADRN) - Versteeg - 8 - MAS5.0 - u133p2 (same as above)
* Gene Ontology
* Broad curated hallmark datasets

*Techniques used:*   
* mRNA arrays

*Analysis used*  
* Overrepresentation calculation

*References*   

* Go to the main page of R2 by clicking the button below

<form name="main_4_pairs" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gse90803geo8_u133p2">
  <button type="submit" >Go to R2 main portal</button>
</form>  


* In Field 3 choose Find Differential expression between groups
* This dataset has been annotated with type information. Each sample was assigned to either the MESenchymal or the ADReNergic type, in R2 this is called a *track*. Choose the proper track in the **Select a track** dropdown. Since we have only 8 samples make sure that the multiple testing correction is set to **No correction**
* A list of differentially expressed genes appears; click on the hyperlinked name of your favorite gene to see its expression in the sample set; try an oppositely correlating gene also
* Now click on the **Heatmap(zscore)** button in the right menu panel; a heatmap showing the expression of all differentially expressed genes with correlation p-value < 0.01 in this dataset is shown.    

---------
  ![](_static/images/R2d2_logo.png)**How is this figure different from the former?**

<br>
<br>

---------

* For future use the genes that make the difference have been stored for you in R2 as signatures (aka genesets or categories). One set of genes that is highly expressed in the MES type of samples (r2_mesadrn_mes) and one set of genes highly expressed in the ADRN type of samples (r2_mesadrn_adrn) R2 provides additional analysis for sets of genes in the right panel of menu buttons. As a first analysis step we can check a data resource called the Gene Ontology that provides a tree of systematic ordered biological terms that is used to formally describe the biological role of each gene. R2 now calculates for each of the thousands of groups of genes that are annotated with a specific biological term whether your set of choice is over-represented in them. In the menu panel to the right select the **Gene Ontology Analysis** button 

---------
  ![](_static/images/R2d2_logo.png)**What can you say about the function of the group of genes that are upregulated in the MES type of cells?**

<br>
<br>

---------


* In R2 there are much more sets of genes that have been found to be implemented in specific processes. The Broad institute has compiled quite some of these sets of genes that characterize hallmark biological processes   
* Go back by clicking the back buttonn
* Select the **Gene set analysis** option from the right menu
* Select the *geneset_broad_2015_hallmark* geneset 

---------
  ![](_static/images/R2d2_logo.png)**Which hallmark category of genes pops up as most important? Can you explain this?**

<br>
<br>

---------

* Another type of sets of genes that can be used for over-representation calculations are pathways. KEGG is a database containing curated biological pathways. Perform the same analysis as above for the KEGG pathways database

---------
  ![](_static/images/R2d2_logo.png)**Which pathways do you consider interesting from a oncology point of view?**

<br>
<br>

---------


Identifying groups: using signatures to classify other datasets
------------------------------------------------------------------

We now have a signature that distinguishes between the two types of cells. We also obtained some hints about functional characteristics of these cells. How does this signature behave in other datasets? Does the same set of genes tell us something about other sets of tumors or cell lines? This is the next step in our analysis. We've assembled a more complex dataset by gathering the dataset of the 4 pairs of cell lines, additional classical cell lines from the first dataset and publicly available data of cell lines derived from normal neural crest tissue. This is the tissue where neuroblastoma tumors are known to initiate.

*Data used:*
* A combination of the 8 cell lines above, additional classical Neuroblastoma cell lines and cells from the neural crest lineage (Mixed Neuroblastoma (MES-ADRN-CREST) - Versteeg/Etchevers - 34 - MAS5.0 - u133p2)

*Techniques used:* 
* mRNA expression data

*Analysis used*
* Heatmap analysis

*References*
 
* Go to the main portal of R2 by clicking the button below; the dataset described above is automatically selected

<form name="main_34_pairs_and_crest" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gsenatgengeo34_u133p2">
  <button type="submit" >Go to R2</button>
</form>  


* In field 3 select **View Geneset**
* Click next and select *geneset_r2provided_genelists* 
* Click next, leave selection as is and click **next**
* Select both signatures that were derived before by CTRL click on the MES (*r2_mesadrn_mes*) and ADNR (*r2_mesadrn_mes*) signatures and click **next**

---------
  ![](_static/images/R2d2_logo.png)**Which samples group together?**

<br>
<br>

---------

---------
  ![](_static/images/R2d2_logo.png)**How does this relate to the above?**

<br>
<br>

---------

* When observing such clearcut patterns you immediately have to wonder whether something special is going on. We'll check the signature in another dataset, in this case a publicly available Colon Cancer dataset. Click on the button below to go there and perform the same analysis.


<form name="main_34_pairs_and_crest" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_colonmicrosat84_u133p2">
  <button type="submit" >Go to R2 colon data</button>
</form>  


---------
  ![](_static/images/R2d2_logo.png)**Do you observe similar patterns? Can you explain this?**

<br>
<br>

---------


* If you have time left you might want to check other datasets, some might show similar patterns of interest!

Using scores for further characterization
--------------------------------------------

The expression patterns of these specific signatures can be used to compare cell types. We can do this by summarizing the expression data of all genes in the signature in each cell type in one value; a signature score. R2 has calculated these scores for all samples in both signatures. We're going to find out how they relate.

*Data used:*
* Mixed Neuroblastoma (MES-ADRN-CREST) - Versteeg/Etchevers - 34 - MAS5.0 - u133p2

*Techniques used:* 
* mRNA expression data

*Analysis used*
* Signature scores 

*References*

* Go back to the main portal of R2 by clicking the button below.

<form name="main_34_pairs_and_crest" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gsenatgengeo34_u133p2">
  <button type="submit" >Go to R2</button>
</form>  


* In field 3 choose **Relate 2 tracks** and click next
* First we'll explore the scores in each signature separately; on the X-axis (**Select X track**) we'll use the unique sample id (lab\_id) and on the Y-axis the signature score track that R2 has generated for the MES signature (u-34\_mesadrn\_mes(#)). Click next.
* A graph is generated for each sample the signature score for the mesadrn\_mes signature is shown, select **Color by Track** for ColorMode and try different tracks. Click **Adjust Settings** to view the result.
* Now select for the Y-axis the ADRN part of the signature, click Adjust Settings to view the result.
* Now we're going to compare the signature scores; select the MES signature for the X track
* If you have time you can also try the **Color by Gene ColorMode**, choose a gene of interest (Note: the dropdown selection is linked to the database, wait for the proper selections to popup...)

---------
  ![](_static/images/R2d2_logo.png)**What conclusion would you draw from these figures?**

<br>
<br>

---------


Finding causes; homing in on transcription factors
-----------------------------------------------------

Apparently there are two types of cells in Neuroblastoma tumors. Neuroblastoma seems to be a heterogenous tumor. Transcription factors are known to determine gene expression programs in cells. These gene expression programs determine the development of the cell. Can we determine which TF’s might determine the difference between both of these cell lines?

*Data used:*
* Mixed Neuroblastoma (MES-ADRN-CREST) - Versteeg/Etchevers - 34 - MAS5.0 - u133p2
* Transcription factor annotation from Gene Ontology
* NCBI (National Center for Biotechnology Information - USA) Gene information database 

*Techniques used:* 
* mRNA expression data

*Analysis used*
* Differential expression

* Go back to the main portal of R2 by clicking the button below.

<form name="main_34_pairs_and_crest" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gsenatgengeo34_u133p2">
  <button type="submit" >Go to R2 main</button>
</form>  


* Again we're going to find out which genes make a difference, but now in a specific subset that has been annotated to have Transcription Factor activity. This is gathered from databases that collect that information from peer reviewed publications. In field 3 select **Find Differential expression between groups** Click **next**
* Make sure to select the proper track **Select a track** We're now also going to filter for a specific **GeneCategory**; select the Transcription factors (*TF(945)*). Click **Next**. 
* In the next screen we're asked to further filter for a specific type of samples to compare, we're focusing on the difference between ADRN and MES; select these. Click **Next**. 
* A list of genes appears. Investigate the top 4 by clicking on the hyperlinked gene symbols. This brings you to the expression view of the gene. From here you can also access the NCBI gene database containing additional information on the function of the gene and related scientific publications. Do this by clicking on the hyperlinked **GeneID** number in the top table.

---------
  ![](_static/images/R2d2_logo.png)**Armed with this information, which gene would you choose for further research? Why?**

<br>
<br>

---------


Proving causes; manipulating cell lines
------------------------------------------

From experiments it is known that cells can change their nature, some cells exhibit a certain plasticity.

---------
  ![](_static/images/R2d2_logo.png)**Can you think of any such processes that are of relevance to cancer?**

<br>
<br>

---------

From experiments in our lab it became evident that the two cell types found in Neuroblastoma were able to switch. After a given period of time cells is dishes changed their nature as became evident from the expression of certain marker proteins on their surface.
Now that we have a candidate Transcription Factor we can try to investigate its relevance in this plasticity by manipulating the gene in cell lines we grow in the lab. 

---------
  ![](_static/images/R2d2_logo.png)**Can you think of ways to manipulate genes in cell lines?**

<br>
<br>

---------

The TF was inducibly expressed in the SKNBE cell line and this was monitored through time for their gene expression using Affymetrix mRNA arrays. The resulting data was added to the dataset we used above for comparison. 


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

* Go to the R2 main page by clicking the button below, the correct dataset will be selected.  

<form name="52_pairs_crest_exp" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gsenatgen2017geo52_u133p2">
  <button type="submit" >Go to R2 main, inducible TF set</button>
</form>  

* Select in field 3 the **Relate 2 tracks** option. R2 has calculated signature scores for all samples in both signatures; in this dataset these tracks are called *adrn_score* and *mes_score*. Relate the two tracks, adapt the ColorMode to Color by Track and try appropriate tracks.

---------
  ![](_static/images/R2d2_logo.png)**What is your conclusion from this experiment?**

<br>
<br>

---------


Creating hypotheses; relating to chromatin modification data
---------------------------------------------------------------

Apparently this TF is capable of shifting cells from state to the other. How can we further determine causal relations and probably targetable processes in these cancer cells? How is a switch dynamically possible? A growing body of evidence implicates enhancers as key elements defining cell identity but the relationship of these enhancers to intratumoral heterogeneity is unknown. We measured the enhancer marks. We'll investigate this for a couple of genes that are part of the signatures to discover patterns

Epigenetic versus genetic; the concept of re-programming

*Data used:*
*

*Techniques used:* 
*

*Analysis used*
*

*References*
*

* Directly link to the chromatin modification data from TF's that were found to be specific (MEOX)
* Try different TF's and have them explain the difference

Suggesting therapy
---------------------


* With the current new knowledge you derived above, can you think of a way to use the fact that neuroblastoma is a heterogenous tumor consisting of a mesenchymal, motile cell type and a adrenergic, differentiated cell type for therapeutic options?
* Use the tools available 
* SKNSH; upon chemotherapy (drugs) mesenchymal shift; drugable are for example kinases; 
* Hints: 
* Figures:

*Data used:*
* 

*Techniques used:* 
* 

*Analysis used*
* 

*References*
* 


