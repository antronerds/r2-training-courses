<a id="molecular_genetics_crc"> </a>

Molecular Genetics Course - Colorectal Cancer
=================================

*Analyse Colorectal Cancer using the R2 data analysis platform*

This resource is located online at http://r2platform.com/mgcourse  
  
 
Introduction
------------

ToDo: Here we give in introduction into CRC CMS etc

  ![](_static/images/MolGenCRC/CMS_classification_characterization_pmc7511559.jpg "Figure 1: CMS classification")	
  
  [**Figure 1: CMS classification**](_static/images/MolGenCRC/CMS_classification_characterization_pmc7511559.jpg)


The <button class="course_permalink">grey buttons</button> in this course will bring you to the R2 platform, often with pre-set settings such that you can pick up an analysis easily. The <button class="course googleform">green buttons</button> in this document will open up a Google form, one per section, with which you can submit your answers.

We would like to ask you to fill in the evaluation form about this R2 course during or at the end of the course. To open the form, click the button below:




The R2 platform:
---------------------------------------
 *Maybe a small introduction*




## Normal vs Colon: 

**Datasets used:**
* Mixed Colon - Marra - 64 - MAS5.0 - u133p2
* Tumor Colon Adenocarcinoma (students) - tcga - 204 - tpm - gencode3


R2 is hosting a large collection of all types omic datasets.  Use the grid box to search and get some grips on the datasets R2 is hosting, just  to get some feeling with the large collections of the dateset in R2.

* In the main page in R2, click on dataset  name  in box 2. Using the grid box 'Tissue/Tumor/Disease/Misc' and find out how many colon related sets R2 is hosting.

**A:213**

* How many sets has R2 when you only look for methylation sets.

**A:6**

Cancer is very complex disease to investigated. With a hugh variety of cancers types. This course is focussing mainly on CRCs. So start with lets see if we can see we start to look  for genes which make the difference in normal anc cancer tissue.


Of course it is nice to have a lot of RNA expression datasets tot analyse and explore but without proper sample annotation your have very limited analysis options. Let's explore the annotation for the Marra dataset.

* Go to the cohort overview in box 2 and check  the samples annotation by using the pulldown menu, how many normal en tissue samples does the Marra set contain this set also contains the location such as tissue location etc etc.


The R2 platform support a large  set of analysis types to explore datasets. One of these modules is the "Find differential expression between groups.

* Check if you have selected the Marra set and select in the main menu box, "Find Differential expression between two groups. In the next screen, use the default select T-test and select "Tissue" in tjhe group by option, and click submit. Select Normal and Adenoma, make sure that log2 and p < 0.01 is selected  and click submit.

* R2 has generated a large list of differentially expressed genes, can you say something about the distribution of the genes how many are up and down regulated.


Next to many publicly available datasets, R2 is also hosting a lot of curated lists of genes which we call `gene categories` (gene sets). These gene categories can be used to restrict an analysis as well.  We can adapt our current search by scrolling down to the end of our gene list. In the Adjustable Settings Panel by hitting the "Search Select button" in the Gene Filters box you can now use a Gene Category to filter your list. Re-generate a list that is specifically associated with (colorectal) cancer (hint: look in the gene category or KEGG pathway list to identify an interesting gene set). You can look with keywords of inspect the KEGG pathway specific.

* check some genes with single gene view (AXIN2) by clicking the magnifying glass, in the green bar in the top you can easily go to list. Also note te coloured bars beneath plot, containing the sample annotation, these groupin variables are called tracks. Also note you hoover over the dots in the graph to get more information of the individual samples.


Pathway heatmap
---------------------------------------

The WNT pathway is an important signal transduction cascade in the development of colon cancer.

Generate a list of genes which are differentially expressed comparing normal and adenoma within the WNT pathway KEGG, use the False Discovery Rate for multiple testing correction, log 2 values and P <0.01. You can use the KEGG Pathway from the Gene Categories selection menu.

* How many genes are up / down regulated. 

* In the left menu generate a heatmap. Inspect the heatmap did you expect this pronounced clustering.




![](_static/images/MolGenCRC/marra_biased_wnt.png "Figure 2: heatmap")

Pathway Analysis:
---------------------------------------

Often, you do not immediately have an idea which pathways you could look for in your comparisons between groups (normal versus adenoma in our case). A module within R2 providing you with some suggestions is the so called KEGG Pathway Finder by Groups. It assesses whether the number of genes that show significant differential expression between normal and adenoma is significantly higher than you would expect compared to all genes that are mentioned in KEGG.


* Perform a KEGG pathway analysis from the ‘main’ page. Make sure that under Representation: all is selected (both under and overrepresentation) Are there KEGG pathways overrepresented in the differentially expressed genes between adenoma and normal tissue? If this is true which pathway (Set the p-value 0.01 for the analysis and select striking pathways).


*A: DNA replication and cell cycle are in the top off the list*



The previous task has shown that a number of WNT pathway genes were represented in the result list. Since we have generated a heatmap in the previous question  with the wnt pathway gene from th etest results. We can also  make a heatmap directly without any test.

* Go to the main screen select generate a heatmap and select the wnt path way from the text database.


![](_static/images/MolGenCRC/marra_unbiased_wnt.png "Figure 2: heatmap").

* The samples are clearly separeted in normal vs adenoma. It's different and less pronounced compared to the previous heatmap. Do you think this is special? , Why or Why not.

* In what way is the heatmap your generated different compared to the previous one.


### MSI / MSS in CRC





Clicking on the Marra dataset name also reveals some background information if available in R2 of the selected dataset. In what year is the Marra datasets listed. Howly cow thats an old set. lets quickly look for a newer set. Select a mixed the mixed tcga set










### Genes Affected by Mutations: 







## CMS
ToDo: Intro to CMS now in the words of the Guinney paper:

"Thanks to collaborative bioinformatics work on the largest collection of CRC cohorts with molecular annotation to date, 
and building upon previous efforts by the independent researchers, the consortium resulted in a consensus molecular 
classification system that allows the categorization of most tumors into one of four robust subtypes. Marked differences 
in the intrinsic biological underpinnings of each subtype support the new taxonomy of this disease (Fig. 5) that will 
facilitate future research in this field and should be adopted by the community for CRC stratification: CMS1 (MSI Immune), 
CMS2 (Canonical), CMS3 (Metabolic), and CMS4 (Mesenchymal)." (Guinney 2015et al., Nat Med. 2015 Nov; 21(11): 1350–1356. )


##### Clustering with t-SNE maps

We've seen that the expression of genes differs among the samples and the CRC subtypes seem to specifically express certain genes. 
To further explore the type of data we're dealing with, an unbiased unsupervised type of clustering analysis is a good idea. 
The t-SNE algorithm is an algorithm that was developed in recent years. It finds similarity in expression profiles of samples 
and will clump similar cells together on a map.   

* Click the button below to show the t-SNE map in R2: 

![](_static/images/MolGenCRC/temp/tSNE204_create_permalink_later.png "Figure 2: temp image, todo make permalink tSNE with CMS coloring")

[**Figure 2: temp image, todo make permalink tSNE with CMS coloring**](_static/images/MolGenCRC/temp/tSNE204_create_permalink_later.png)

ToDo make permalink to tSNE instead of image above  
<a class="course_permalink" href="https://hgserver2.amc.nl/cgi-bin/r2/main.cgi?permalink=course_molgen_tsne_86_6tumortypes" target="_blank">Go to the t-SNE map</a>
<br>
<br>

Under the graph, a menu allows the user to adapt settings.
Colors of the graph points are not set by default.  
* Find the **Color mode** dropdown and select *Color by Track*. Now set the **Color track** dropdown to use the *cms_predicted* track 
again, and click **Submit** to show the changes.
* The different maps can be found under de setting Versions. Set **Versions** to the value *all* and click **Submit** again. 

  
  
------

  ![](_static/images/R2d2_logo.png)**What insight did you obtain when you colored the plot with annotation?**

  ![](_static/images/R2d2_logo.png)**Why do you think it is good practice to check different values for a parameter?**

<br>
<br>


------

### Differences between the various CMS types

Previously we looked into CMS subtype 1. We would like to understand what sets CMS 4 apart from the subtypes 2 and 3. 

* From the main page choose the analysis Differential Expression Between Two Groups. 
* ToDo: how to Choose the track cms4vs3
* Look in the list of genes if you see anything familiar and hover over the magnifying glass icon of a few genes

Gene set analysis helps researchers interpret the biological relevance of a group of genes. Instead of looking at individual 
genes, it allows you to understand the collective functions or pathway involvements genes in your list. This can provide more 
meaningful insights into the underlying biology of a particular condition or experiment.

* Click on the top most button on the right that is labeled Gene set analysis.
* Select the Gene set Collection Broad 2020 09 h hallmark
* Switch the Representation setting to all 
* Click Next


ToDo: Remove picture
![](_static/images/MolGenCRC/temp/GeneSetAnalysis_create_permalink_later.png "Figure 3: temp image of result Gene set analysis, todo remove")

[**Figure 3: temp image of result Gene set analysis, todo remove**](_static/images/MolGenCRC/temp/GeneSetAnalysis_create_permalink_later.png)

------

![](_static/images/R2d2_logo.png)**Which gene sets do you see pop up and are they over or under expressed in CMS 4?**

![](_static/images/R2d2_logo.png)**Explain the biological relevance for the CMS4 subtype for these over- or/and underexpression of these gene sets for CMS4 subtype CRC tumors**

<br>
<br>


------



## Experiment in cell lines
ToDo: Now that we have discovered interesting mecanisms that influence teh development of CRC, can we influence the mechanisms by targeting a gene? 

## Trial in patiënts
Is a drug or treatment effective?

### Single cell? 


## Evaluation
Please don't forget to fill in the evaluation form about this R2 course, if you haven't done so yet:

<button class="course googleform" onclick="window.open('https://docs.google.com/forms/d/e/1FAIpQLSflNJpsTcLIhwEC0ZlHksfnE0VwBay1I2KOGPArYu4Q_QhtrA/viewform?usp=sf_link','_blank');" type="button">Open the Evaluation form</button>

---------

Final remarks / future directions
---------------------------------
In the March 1st 2018 issue of Nature a paper was published describing a landscape of genomic alterations across childhood cancers. The data is accessible in R2 also as a Datascope. This is another example of how R2 can visualize your genomics data. 
<br><br>
This ends the course. Feel free to further explore the course materials or our tutorials.
<br><br>
We hope that this course has been helpful. If you want to have your genomics data visualized and analyzed using the R2 platform you can always consult r2-support@amc.nl
<br><br>
The R2 support team.

