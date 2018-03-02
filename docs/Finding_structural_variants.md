<a id="finding_structural_variants"> </a>

Finding structural variants
===========================

*Somatic mutations are not always determining, using the full power of WGS data structural variants can be found also*

In this tutorial we hope to show how R2 can be used to visualize and analyze your WGS data. As an example datasets from childhood tumors will be used. 

This resource is located online at http://r2-training-courses.readthedocs.io

Introduction 
------------
Despite decades of research high stage neuroblastoma still has a very poor prognosis. Since cancer is a disease of genomic aberrations we're going to investigate what aberrations are present and how these might relate to the onset of neuroblastoma. 


Exploring the dataset
---------------------

The oncogenomics department of the AMC has gathered a richly annotated set of neuroblastoma tumors. To easily explore this the R2 development team has devised the concept of Datascopes; a convenient view on the data with some pre-built analyses readily available.

*Data used:*  
* Tumor Neuroblastoma (combat) - Versteeg - 122 - MAS5.0(bc) - u133p2

*Techniques used:*   
* -

*Analysis used*  
* -

 
* In the left menu click on **Change Data Scope** > **Neuroblastoma (AMC)**
* An additional choice step appears; click **Goto Neuroblastoma (AMC) home**
* For a quick impression of the data select the **Cohort Overview** R2 presents the tumor series with it's annotation, feel free to explore the distribution of the parameters.

---------
  ![](_static/images/R2d2_logo.png)**How many tumors have a MYCN amplification?**

<br>
<br>

---------
  
Historically only several genomic aberrations are known:

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


This can of course be seen in the 


TODO: create click through link to the MYCN amplicon  

To extend these data the Oncogenomics department of the AMC set out to sequence 86 neuroblastoma tumors from this set.

Somatic mutations in Neuroblastoma
----------------------------------

For this the samples where sent The R2 development team has processed the WGS data, through several filtering steps the somatic mutations were determined with respect to the reference genome.

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

  
  * There are no mutations recurring more than a few times. Go to one of them, (e.g. TIAM or ALK) and select the **view** link (note: this is separate from the detail link). In a new tab this mutation is shown in the genomebrowser. Explore the view. 
  * Now go back using the back button in your browser, select the **detail** link. R2 now shows additional information on the expression of the gene and its location on the genome. 
  

Further use of WGS data; structural variants
--------------------------------------------
WGS enables further analysis; especially the paired end technique that enables the discovery of structural variants.

  ![Figure 2: Paired end sequencing makes discovery of structural variants possible.](_static/images/structural_variants_paired_end.png "Figure 2: Paired end sequencing makes discovery of structural variants possible.")
	
  [**Figure 2: Paired end sequencing makes discovery of structural variants possible.**](_static/images/structural_variants_paired_end.png)

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
While investigating the WGS data an interesting phenomenon was observed. In some tumor samples parts of the genome appered to be riddled with structural variants, resulting in a shredded chromosomal structure.

---------
  ![](_static/images/R2d2_logo.png)**Can you spot an example of chromothripsis from the circos overview?**

<br>
<br>

---------



Locations of structural variants, hotspots?
-------------------------------------------
TODO: how to locate TERT?

Final remarks / future directions
---------------------------------
In the March 1st 2018 issue of Nature a paper was published describing a landscape of genomic alterations across childhood cancers. The data is accessible in R2 also as a Datascope. Click the button below to access this.

<form name="itcc_68_cell_lines" action="http://hgserver1.amc.nl/cgi-bin/r2/main.cgi?&dscope=DKFZ_PED&option=about_dscope" enctype="multipart/form-data" target="R2" method="post">
  <button type="submit" >Go to R2</button>
</form>  


We hope that this course has been helpful. If you want to have your genomics data visualized and analyzed using the R2 platform you can always consult r2-support@amc.nl

The R2 support team.

