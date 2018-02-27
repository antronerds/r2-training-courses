<a id="finding_structural_variants"> </a>

Finding structural variants
===========================

*Somatic mutations are not always determining, using the full power of WGS data structural variants can be found also*

This resource is located online at http://r2-training-courses.readthedocs.io

Introduction 
------------
Despite decades of research high stage neuroblastoma still has a very poor prognosis. Since cancer is a disease of genomic aberrations 
To get a quick impression click on the link below to see this prognosis in a Kaplan-Meier scan.

TODO: create the click through link here directly to the kaplan meier of stage

You can explore other parameters for groupings that exhibit an effect on survival. Hint:  try the MYCN amp annotation.  
  
Historically only several genomic aberrations are known:


<table>
<tr><th>Gene</th><th>Type</th><th>Reference</th></tr>
<tr><td>MYCN</td><td>amplification 20%</td><td>(Schwab et al., 1983)</td></tr>
<tr><td>ALK</td><td>7%</td><td>(George/Mosse/Janoueix-Lerosey/Chen 2008)</td></tr>
<tr><td>Cyclin D1</td><td>amplification 4%</td><td>(Molenaar et al., 2003)</td></tr>
<tr><td>PHOX2B</td><td>4%</td><td>(van Limpt et al., 2004)</td></tr>
<tr><td>PTPRD</td><td>4%</td><td>(Stallings et al. 2006)</td></tr>
<tr><td>NF1</td><td>3%</td><td>(Hölzel et al., 2010)</td></tr>
<tr><td>PTPN11</td><td>2%</td><td>(Merks et al., 2004, Bentires-Alj et al., 2004)</td></tr>
<tr><td>FOXR1</td><td>1%</td><td>(Santo et al., 2011)</td></tr>
<tr><td>LIN28B</td><td>1%</td><td>(Molenaar et al., 2012)</td></tr>
</table>


R2 can be used to explore amplifications, we'll use R2 to show the MYCN amplicon.

TODO: create click through link to the MYCN amplicon  

To extend these data the Oncogenomics department of the AMC set out to sequence a set of 88 neuroblastoma tumors. After sequencing the read counts were processed as follows.
R2 enables the easy exploration of your WGS data. As an example we'll further explore the Neuroblastoma WGS data set.

Somatic mutations in Neuroblastoma
----------------------------------
Shortly explain what type of WGS was done

Show in R2; complete genomics data for all 

Let toy around with filtering for overrepresented categories

Zoom in to actual mutation

See all counts

Note that there is a low frequency of recurrent mutations

Further use of WGS data; structural variants
--------------------------------------------
WGS enables further analysis; especially the paired end technique that enables the discovery of structural variants

Structural variation affects single genes

Show in circos plot

Combined with somatic data; see which process might be overrepresented; hint to neuritogenesis

Chromothripsis
--------------
While investigating the WGS data an interesting phenomenon was observed.

Go to the specific tumor sample

Let zoom in on region

Locations with high frequency of structural variation.


Structural variations in relapsing tumors
-----------------------------------------
In the tumor series several relapsed tumor samples were gathered.  

Relapsed neuroblastoma landscape different from primary tumors and reveals new targets for therapy


Locations of structural variants, hotspots?
-------------------------------------------
TERT hint
