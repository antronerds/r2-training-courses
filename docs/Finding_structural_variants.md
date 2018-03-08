<a id="finding_structural_variants"> </a>

Investigating structural variants
===========================

*Not every cancer has determining somatic mutations. Using the full power of WGS data relevant structural variants can be traced also and linked to potential causes of disease*

In this course we'll introduce R2, the web based genomics analysis and visualization application. Throughout the course an integrative approach to genomics data will be used. By combining sequencing data with expression data and vice versa new insights can be derived. Throughout this course we'll focus on data of the childhood tumor Neuroblastoma.

We hope to show how R2 can be used to visualize and analyze your WGS data. 

This resource is located online at http://r2-training-courses.readthedocs.io

Introduction 
------------
Cancer is a very complex disease. Much more complicated than originally anticipated when the first mutations were found to be causal for specific cancers. At that time, for colorectal cancer, a well defined path of subsequently gained mutations was found to lead to more aggressive tumorigenic cell types (the Vogelstein model).

  ![Figure 1: Mutation paths during cancer progression.](_static/images/TumorHeterogeneity_CancerProgression.jpg "Figure 1: Mutation paths during cancer progression.")
	
  [**Figure 1: Mutation paths during cancer progression.**](_static/images/TumorHeterogeneity_CancerProgression.jpg)

Although there has been extensive research into similar mutation mechanisms in Neuroblastoma (also in the AMC Oncogenomics group), such a mechanism has not been found for this type of cancer. In this practical work session we will try to bring you to the cutting edge of research into this often deadly childhood tumor. Recent research suggests that Neuroblastoma consists of different cancer cell types. There is reason to believe that this heterogeneity causes the high percentage of relapses in the aggressive subtype of Neuroblastoma. Children developing a relapse almost always die. 
Fortunately new technologies have become available to molecular biology. These enable us to study not only mutations and RNA expression of genes but also study the epigenetic modifications of the DNA-associated histones. And in addition genes can now be manipulated in cell lines and living tissues. 
Using advanced data analysis, statistics and clustering methods, the field of bioinformatics tries to derive new insights from these experimental data and help molecular biologists to generate hypotheses that can be tested experimentally. Today you will use the web-based genomics analysis and visualization platform R2.  
R2 provides you with a set of bioinformatics tools to investigate recent patient and experimental data from Neuroblastoma tumors and cell lines. 

Despite decades of research high stage neuroblastoma still has a very poor prognosis. Since cancer is a disease of genomic aberrations we're going to investigate what aberrations are present and how these might relate to the onset of neuroblastoma. 


Exploring the dataset
---------------------

The oncogenomics department of the AMC has gathered a richly annotated set of neuroblastoma tumors. To easily explore this the R2 development team has devised the concept of Datascopes; a convenient view on the data with some pre-built analyses readily available.

 
* In the left menu click on **Change Data Scope** > **Neuroblastoma (AMC)**
* An additional choice step appears; click **Goto Neuroblastoma (AMC) home**
* For a quick impression of the data select the **Cohort Overview** R2 presents the tumor series with it's annotation, feel free to explore the distribution of the parameters.

---------
  ![](_static/images/R2d2_logo.png)**How many tumors have a MYCN amplification?**

<br>
<br>

---------
  
Until recently only several genomic aberrations were known:

<table>
<tr><th>  Gene  </th><th>Type        </th><th>Reference</th></tr>
<tr><td>MYCN</td><td>amplification 20%</td><td>(Schwab et al., 1983)</td></tr>
<tr><td>ALK</td><td>7%</td><td>(George/Mosse/Janoueix-Lerosey/Chen 2008)</td></tr>
<tr><td>CyclinD1</td><td>amplification 4%</td><td>(Molenaar et al., 2003)</td></tr>
<tr><td>PHOX2B</td><td>4%</td><td>(van Limpt et al., 2004)</td></tr>
<tr><td>PTPRD</td><td>4%</td><td>(Stallings et al. 2006)</td></tr>
<tr><td>NF1</td><td>3%</td><td>(Hölzel et al., 2010)</td></tr>
<tr><td>PTPN11</td><td>2%</td><td>(Merks et al., 2004, Bentires-Alj et al., 2004)</td></tr>
<tr><td>FOXR1</td><td>1%</td><td>(Santo et al., 2011)</td></tr>
<tr><td>LIN28B</td><td>1%</td><td>(Molenaar et al., 2012)</td></tr>
</table>


To extend these data the Oncogenomics department of the AMC set out to sequence 86 neuroblastoma tumors from this set.

Somatic mutations in Neuroblastoma
----------------------------------

For this the samples where sent to the Complete Genomics sequencing facility, now taken over by BGI. They provide a sequence as a service model.The R2 development team has processed the WGS data, through several filtering steps the somatic mutations were determined with respect to the reference genome.


  ![Figure 1: Comparing with the reference genome.](_static/images/structural_variants_reference_genome.png "Figure 1: Comparing with the reference genome.")
	
  [**Figure 1: Comparing with the reference genome.**](_static/images/structural_variants_reference_genome.png)


A comprehensive list of the mutations can be accessed through R2. 

  * Go back to the Neuroblastoma (AMC) datascope
  * Select the **somatic variants** tile
  * A table with all mutations in the 86 tumors appears. It is basically a view on a database table. Ordering on its columns is possible by clicking on the column header. Sort the column by gene name. 

---------
  ![](_static/images/R2d2_logo.png)**Can you spot recurring mutations?**

<br>
<br>

---------

  
* There are no mutations recurring more than a few times. Go to the ALK gene and select the **view** link (note: this is separate from the detail link). In a new tab this mutation is shown in the R2 genomebrowser zoomed in on the genome to the base level. All samples are drawn beneath this stretch. Annotation of the publicly available cosmic mutation database is provided as well.

---------
  ![](_static/images/R2d2_logo.png)**What type of aberrations does the ALK gene suffer?**

<br>
<br>

---------

* The buttons on top of the page can be used to zoom in and out. Zoom out 3 times with a factor 10. 

---------
  ![](_static/images/R2d2_logo.png)**Can you explain what changes occur? How many bases does the ALK gene span?**

<br>
<br>

---------

* The genomebrowser has a tremendous number of parameters that can be set. Scroll down to the bottom of the page. A form shows quite some parameter fields. These provide additional annotations and settings for the algorithms used. A useful annotation is provided by the NIH epigenome roadmap that annotates the genome with chromatin modification data based on methylation and acetylation patterns of the genome. This annotation however, is only provided on another Human Genome build. In the **Adjustable settings** form change the **GenomeBuild** to **HG19** (note that other builds as well as mouse data is available also). Click **redraw**
* An unannotated version of the reference genome is shown. Find and set the **Refseq(R2)** annotation on. Click **redraw**

---------
  ![](_static/images/R2d2_logo.png)**What has happened to the ALK gene?**

<br>
<br>

---------

* Locate the ALK gene (hint type in the gene name in the left upper **Find gene** field) 

* For clarity you can now switch off the cosmic annotation (in the Genome Variation box) and the Calldif Somatic Genome annotation (in the X:Complete Genomics => Variants box). Set the NIH Epigenome Roadmap annotation to all (in the TranscriptView annotation box). This annotation provides information on public datasets that have established whether chromatin regions are subject to active transcription (green), enhancer regions (yellow) or are part of a transcription start site (red).

* Select the front end of the gene by selecting a region; see image (hint the color of the transcript denotes the reading direction; green means the regular direction, red the opposite direction) Click redraw (Note: the NIH annotation only appears for regions under 200.000 bp)

  ![Figure 2: Selecting a region.](_static/images/structural_variants_selecting_region.png "Figure 2: Selecting a region.")
	
  [**Figure 2: Selecting a region.**](_static/images/structural_variants_selecting_region.png)

* The NIH Epigenome Roadmap annotation can be further detailed by selecting the detail view in the toolbox that appears when you click the tools icon, see image below. This box appears at more settings fields if available.


  ![Figure 3: Opening the NIH parameter settings toolbox.](_static/images/structural_variants_selecting_toolbox.png "Figure 3: Opening the NIH parameter settings toolbox.")
	
  [**Figure 3: Opening the NIH parameter settings toolbox.**](_static/images/structural_variants_selecting_toolbox.png)

---------
  ![](_static/images/R2d2_logo.png)**What chromatin modification patterns are visible at the start of the ALK gene?**

<br>
<br>

---------


* Now go back to the AMC datascope, select the Somatic mutations tile and now click the  **detail** link. R2 now shows additional information on the expression of the gene and its location on the genome. 

---------
  ![](_static/images/R2d2_logo.png)**What is remarkable about the expression of the ALK gene?**

<br>
<br>

---------
 
* From this detail view other analysis tools within R2 can be approached by clicking on the links below.

Further use of WGS data; structural variants
--------------------------------------------
WGS enables further analysis; especially the paired end technique that enables the discovery of structural variants.

  ![Figure 4: Paired end sequencing makes discovery of structural variants possible.](_static/images/structural_variants_paired_end.png "Figure 4: Paired end sequencing makes discovery of structural variants possible.")
	
  [**Figure 4: Paired end sequencing makes discovery of structural variants possible.**](_static/images/structural_variants_paired_end.png)

* These structural variations are best visualized as so called _circosplots_. To access these in R2 go to the Neuroblastoma (AMC) datascope and click the **circos archive** tile.
* An overview of all sequences appears displayed as circos plots. These give an immediate comprensive view on the state of the genome. Click on one of the circos plots.
* In a new tab a detailed view of this specific tumor genome is shown. When hovering over the plot the mouse opens a magnifier window.

---------
  ![](_static/images/R2d2_logo.png)**What do the green and red areas mean? And the lines crossing the circle?**

<br>
<br>

---------

* In the tabbed panel to the right of the circos plot all information is detailed. Open the _sample annotation_ tab.

---------
  ![](_static/images/R2d2_logo.png)**What are the patient characteristics?**

<br>
<br>

---------

* Now open the _Gene affecting structural variants_ panel.  

---------
  ![](_static/images/R2d2_logo.png)**Can you locate a structural variant that involves a gene and spans over two chromosomes?**

<br>
<br>

---------


Chromothripsis
--------------
While investigating the WGS data an interesting phenomenon was observed. In some tumor samples parts of the genome appeared to be riddled with structural variants, resulting in a shredded chromosomal structure.

* Go to the overview page with circos plots.

---------
  ![](_static/images/R2d2_logo.png)**Can you spot an example of chromothripsis from the circos overview?**

<br>
<br>

---------

To see how chromothripsis relates to clinical data we can investigate survival data in R2. 

* From  the left menu select Kaplan Meier > By annotated parameter
* A selection menu appears, select the track cg_chromothripsis and click next 

---------
  ![](_static/images/R2d2_logo.png)**How does chromothripsis affect survival?**

<br>
<br>

---------

* Filtering for subsets allows you to further isolate specific survival characteristics. If you like you can toy around with different parameters.



Locations of structural variants, hotspots?
-------------------------------------------
Chromothripsis can be seen as an extreme case of concentration of structural variants in one sample. The question arises whether there are other hotspots of structural variation on the genome that are found in multiple samples. These might point to functional interactions.

* One of the genes that exhibited such a hotspot is the TERT gene. Go back to the startpage of the Neuroblastoma datascope and select the GenomeBrowser tile. This brings you to the TERT gene on the genome with some preset annotations. 

---------
  ![](_static/images/R2d2_logo.png)**How does this region qualify as a hotspot?**

<br>
<br>

---------
 
 * As is obvious from the high number of peaks around the TERT gene there is a hotspot of structural variants in that area. The types of variants are annotated below the stretch on the genome.   

---------
  ![](_static/images/R2d2_logo.png)**What do the arrows and colored tracks mean? (Hint: hovering with the mouse provides additional information)**

<br>
<br>

---------

* Red arrows depict translocations to other loactions in the genome. Locate the translocation to chromosome 11 (hint; sample 724) and click on the arrow.
* R2 brings you to the other side of the translocation. In the TranscriptView panel switch on the SuperEnhancers NB annotation and click redraw.
 
---------
  ![](_static/images/R2d2_logo.png)**What advantage would a tumor have from this translocation?**

<br>
<br>

---------


Remarks
---------------------------------

We hope that this course has been helpful. If you want to have your genomics data visualized and analyzed using the R2 platform you can always consult r2-support@amc.nl

The R2 support team.

