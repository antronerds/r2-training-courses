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
* Mixed Colon - Marra - 64 - MAS5.0 - u133p
* Tumor Colon Adenocarcinoma (students) - tcga - 204 - tpm - gencode3


Use the grid box to search and get some grips on the datasets R2 is hosting, just  to get some feeling with the database (How many of them are me


### Genes Affected by Mutations: 



### MSI / MSS in CRC



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

