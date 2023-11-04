<a id="molecular_genetics_crc"> </a>

Molecular Genetics Course - Colorectal Cancer
=================================

*Analyse Colorectal Cancer using the R2 data analysis platform*

This resource is located online at http://r2platform.com/mgcourse  
 
  
Introduction
------------

In the late 1980s the Vogelstein model was proposed. It introduced the concept of a stepwise accumulation of genetic
mutations leading to the development of colorectal cancer (CRC).  

![](_static/images/MolOncCRC/santos_ijms241311023_TumorProgression.png "Figure 1: Mutation paths during cancer progression")

[**Figure 1: Mutation paths during cancer progression**](_static/images/MolOncCRC/santos_ijms241311023_TumorProgression.png)

<span class="citation_txt">(source: https://doi.org/10.3390/ijms241311023)</span>

Similar to the picture above, the model highlights the importance of key genetic mutations during CRC progression, 
including mutations in APC, KRAS, and TP53. While the Vogelstein model has provided a valuable foundation for 
understanding colorectal cancer, subsequent research has revealed that the disease is more complex and heterogeneous 
than initially described. Colorectal cancer can involve various genetic and epigenetic changes. Additional 
factors, such as the tumor microenvironment, inflammation, and the immune system, also play significant roles in the 
progression of the disease. <br>
Colorectal cancer is the third most common cancer worldwide, according to the World Health Organization, accounting 
for approximately 10% of all cancer cases, and it is the second leading cause of cancer-related deaths worldwide. 

![](_static/images/MolOncCRC/CMS_classification_characterization_pmc7511559.jpg "Figure 2: Subtypes in colorectal 
 cancer: CMS classification (Guinney et al., 2015)")

[**Figure 2: Subtypes in colorectal cancer: CMS classification (Guinney et al., 2015)**](_static/images/MolOncCRC/CMS_classification_characterization_pmc7511559.jpg)

Research is needed to understand the mechanisms underlying treatment resistance and to develop strategies to
overcome it. Better identification and characterization of multiple CRC subtypes could guide treatment decisions and
improve the outcomes for individuals with colorectal cancer. Furthermore, markers for early detection and prevention
might allow for interventions before advanced mutations occur. Clearly it is crucial to understand the diversity and
complexity of colorectal cancer in order to develop new and effective targeted treatment strategies. <br><br>
Bioinformatics tools enable the analysis of vast amounts of omic and clinical data, helping researchers identify 
genetic mutations, epigenetic aberrations, biomarkers, and potential therapeutic targets in order to better understand 
and combat cancer.<br>
Today you will use advanced bioinformatics tools to explore, analyze and visualize colorectal cancer data in
search for a deeper understanding. You will use the freely available and web-based genomics analysis and 
visualization platform R2, a Core Facility of the Amsterdam UMC. R2 provides the user with many experimental and 
clinical data sets coupled to a wide variety of clickable bioinformatics tools. Without any coding you will gain
hands-on research experience with colorectal cancer omics data and bioinformatics tools.

The <button class="course_permalink">grey buttons</button> in this course will bring you to the R2 platform, often with
pre-set settings such that you can pick up an analysis easily. The <button class="course googleform">green
buttons</button> in this document will open up a Google form, one per section, with which you can submit your answers.

We would like to ask you to fill in the evaluation form about this R2 course during or at the end of the course. To open
the form, click the button below:

<button class="course googleform" onclick="window.open('https://forms.gle/kfiE5vQiDmhJVS1f8','_blank');" type="button">Open the Evaluation form</button>
<br>
<br>

## Normal colonic epithelium vs colorectal tumor tissue: a first impression of genomic data

Colorectal cancers are believed to arise predominantly from adenomas. A fundamental query in cancer research 
consistently revolves around understanding the distinctions between the transcriptomic profiles of normal tissue and 
tumor tissues. Let's get acquainted with R2 and its large collection of omic datasets while immediately exploring 
differences in gene expressions between normal colonic mucosa and colorectal adenomatous tissue. 

**Datasets used:**
  
* Mixed Colon - Marra - 64 - MAS5.0 - u133p2

### Filtering and exploring

* The button below brings you to the form in which you can submit your answers for section 1.2.

<button class="course googleform" onclick="window.open('https://docs.google.com/forms/d/1ZGSmm3oMSJKHBHosCJsDUuGbQDhUX-_JSesBLizcDwQ/','_blank');" type="button">Open the form for section 1.2</button>
<br>
<br>

* Open a Chrome browser and go to the R2 platform
  address: <a href="http://r2.amc.nl" target="_blank">http://r2.amc.nl</a> and choose the button **Use R2 without an
  account** under the sign in fields.

You're now on the R2 main page. This web based molecular biology data analysis platform contains a wealth of data and
methods to analyze the datasets. Step by step, researchers are guided through a web of options for data analysis. R2's
main page shows this principle: step through each of the numbered boxes to develop your analysis of choice.<br><br>
In this case we're first going to see if and how the mRNA expression of several genes changes through a single dataset.
We use the dataset that is described above. In this dataset, 64 samples of   .

* In order to find the dataset in R2, click on the text of the currently selected dataset in box 2. A grid pops up in
  which you can find all the datasets of R2 that are available to you.
* Each row is a dataset and each column contains the different searchable characteristics of a dataset. Under the header
  **Tissue/Tumor** type the keyword *colon* in the white textfield to find out how many colon related sets R2 is 
  hosting.


* How many sets has R2 when you only look for colon methylation sets.


This first dataset that we will use, can be found in R2 as "Mixed Colon - Marra - 64 - MAS5.0 - u133p2". In te main 
screen more background information is revealed bij clicking on the dataset name. In the rest of  R2 clicking on the exclamation marks next to the dataset name will also reveal additional information.

Of course it is nice to have a lot of RNA expression datasets to analyse and explore but without proper sample annotation your have very limited analysis options. Let's explore the annotation for the Marra dataset.



![](_static/images/MolOncCRC/CRCprogression_highres.jpg "Figure 2: CRC progression from normal tissue to metastatic 
cancer")

[**Figure 2: CRC progression from normal tissue to metastatic cancer**](_static/images/MolOncCRC/CRCprogression_highres.jpg)
<span class="citation_txt">(source: https://www.sciencedirect.com/science/article/pii/S1936523321001236#fig0001)</<span>

* Find  and select the RNA expression dataset from Author Marra and select the one with 64 samples. *Note: Click the blue box with confirm selection*.

* Go to the cohort overview in box 3 and check the samples annotation by using the pulldown menu. In the annotation section, check *cohort overview* how many normal en tissue samples does the **Marra** set contain this set also contains the location such as tissue location etc etc.

The R2 platform support a large  set of analysis types to explore datasets. One of these modules is the "Find differential expression between groups". The differential expression analysis aims to identify genes which are significant different between two groups. R2 offers a couple of statistical test in this case we use the T-test which is selected by default.

* Check if you have selected the **Marra** set and select in the main menu box, "Find Differential expression between two groups. In the next screen, use the default select T-test and select "Tissue" in **the group by:** option, and click submit in the next screen,  Select Normal and Adenoma for subsequently group 1 and group 2, make sure that log2 and p < 0.01 is selected  and click submit.

* R2 has generated a large list of differentially expressed genes, can you say something about the distribution of the genes, how many are up and down regulated.


Next to many publicly available datasets, R2 is also hosting a lot of curated lists of genes which we call `gene sets` (gene categories). These gene categories can be used to restrict or filter as well.  We can adapt our current search by scrolling down to the end of our gene list. In the Adjustable Settings Panel by hitting the **"Search GS"** in the Gene Filters box you can now use a Gene Set to filter your list. Re-generate a list that is specifically associated with (colorectal) cancer (hint: look in the gene category or KEGG pathway list to identify an interesting gene set). You can look with keywords of inspect the KEGG pathway specific.

* Check some genes with single gene view (AXIN2 etc etc) by clicking the magnifying glass, in the green bar in the top you can easily go to list. Note the coloured bars beneath plot, containing the sample annotation, these grouping variables are called tracks. Also note you hoover over the dots in the graph and the tracks to get more information of the individual samples.


## A song of heatmaps and pathways


The WNT pathway is an important signal transduction cascade which plays an important role in many biological processes. The dysregulation of the Wnt pathway has been observed in many different cancers including colon cancer. 

### The WNT pathway

Generate a list of genes which are differentially expressed comparing normal and adenoma within the WNT pathway KEGG, use the False Discovery Rate for multiple testing correction, log 2 values and P <0.01. Find the **Wnt pathway** by clicking again the GS (Gene set button) and search by key word for Wnt or go through the KEGG pathways. 

* How many genes are up / down regulated. 

* In the left menu generate a heatmap. Play a little bit with the color scheme, select e.g: the green-black-red scheme,  Inspect the heatmap did you expect this pronounced clustering?.


### Find relevant pathways


Often, you do not immediately have an idea which pathways you could look at for in your comparisons between groups (normal versus adenoma in our case). A module within R2 providing you with some suggestions is the so called KEGG Pathway Finder by Groups. It assesses whether the number of genes that show significant differential expression between Normal and Adenoma is significantly higher than you would expect compared to all genes that are mentioned in KEGG. In other words are the genes you found regulated between the groups enriched in the KEGG pathway database. 

[Info: The KEGG pathway Database]( https://www.genome.jp/kegg/pathway.html).


* Perform a KEGG pathway analysis from the ‘main’ page. leave the re-presentation on **"over"** again with the Normal vs Adenoma group. Are there KEGG pathways over-represented in the differentially expressed genes  (Set the p-value 0.01 for the analysis and select striking pathways). And does it make sense that these are in the list ?.


* Perform the same task with the under-representation selected in de drop down menu. Do you see interesting 
  pathways popping up?

In this test the WNT pathway was not really significant but still in the list at the bottom. One of the reasons why this is the case, is that in this case not all the genes  are assigned to the KEGG WNT pathway. Or that the pathway genes are in this case not sufficient to access pathway activity. However, visualizing the gene expression still hints you towards WNT pathway involvment. 

* Go to the main screen select generate a heatmap and select the wnt path way from the text database.


* The samples are clearly seperated in Normal vs Adenoma. It's different and less pronounced compared to the previous heatmap you generated.  Do you think this is special? , Why or Why not.

* In what way is the heatmap your generated different compared to the previous one.  



## Identifying groups and their characteristics: CMS

Let us now move past the precancerous stage of adenomas and look at colorectal cancer. Colorectal cancer is a complex 
and heterogeneous disease, characterized by a multitude of variations in its genetic, molecular, and clinical 
attributes. This heterogeneity manifests in diverse ways, influencing the tumor's behavior, response to treatments, and patient outcomes. Understanding this heterogeneity is critical for tailoring effective therapies and improving patient care. In this context, we will explore the various dimensions of heterogeneity in colorectal cancer and its implications for diagnosis, treatment, and research.  
  
In 2015, Guinney et al. (Nat Med. 2015 Nov; 21(11):1350–1356) published a bioinformatics study on a vast collection 
of colorectal cancer cohorts with detailed molecular annotation. The consortium developed a now widely accepted 
molecular classification system that allows researchers to categorize most colorectal tumors into one of four 
distinct and robust subtypes, each characterized by its unique biological features. These subtypes are: CMS1 (MSI 
Immune), CMS2 (Canonical), CMS3 (Metabolic), and CMS4 (Mesenchymal), see Figure 2. 

### Clustering with t-SNE maps

An unbiased unsupervised type of clustering analysis is a good starting point to familiarize yourself with a new
dataset. The t-SNE algorithm is an algorithm that was developed in recent years. It finds similarity in expression profiles of
samples and will clump cells with similar expression profiles together on a map.

* Click the button below to show the t-SNE map in R2:


ToDo make permalink to tSNE 
<a class="course_permalink" href="https://hgserver2.amc.nl/cgi-bin/r2/main.cgi?permalink=course_molgen_tsne_86_6tumortypes" target="_blank">
Go to the t-SNE map</a>
<br>
<br>

Under the graph, a menu allows the user to adapt settings.
Colors of the graph points are not set by default.

* Find the **Color mode** dropdown and select *Color by Track*. Now set the **Color track** dropdown to use the
  *cms_predicted* track
  again, and click **Submit** to show the changes.
* The different maps can be found under de setting Versions. Set **Versions** to the value *all* and click **Submit**
  again.  



------  


![](_static/images/R2d2_logo.png)**What insight did you obtain when you colored the plot with annotation?**

![](_static/images/R2d2_logo.png)**Why do you think it is good practice to check different values for a parameter?**

<br>
<br>


------  

CRC contains subtypes, of which we already looked at one subtype more in depth. We will study differences among
the subtypes further. To start, lets see if there is any difference in survival chances among the subtypes


### Different survival chances for different CMS CRC subtypes? 

* In the left side menu on the main page, click on Survival (Kaplan-Meier / Cox)
* In the menu at the center of the page, click at the Dataset setting on the current Dataset name, and find the
  dataset with *Author* is **Guinney** and the amount of samples *N* is **3232**
* Click on the row to read its description in the information box underneath the dataset selection grid

ToDo: Fill in the information about the dataset Summary Design etc

* Leave *Separate by* at **categorical track (Kaplan-Meier)** and click **Next**
* Choose *type of Survival* **overall* and *Track* **lv_cms_final**


* Now perform the same analysis, but choose **relapse-free** in stead of overall for the setting *type of Survival*  



------  


![](_static/images/R2d2_logo.png)**What does the first Kaplan Meier plot tell you?**

![](_static/images/R2d2_logo.png)**And what is your conclusion from the second Kaplan Meier graph?**
<br>
<br>

------


### Mutations

Optionally   
* From the main page, select the Guinney choose a **relate 2 tracks** analysis to show the different ratios of 
  mutations per CMS subtype.
* For the *y axis* choose **lv_braf_mut** mutations and for the *X axis* choose **lv_cms_final**.
* Select the **stacked barplot (%)** *graph type* and click **Submit**
* The Guinney dataset contains several datasets put together. To only look at the samples that looked at the 
  mutational information, scroll down underneath the graph to Adjustable settings menu. Use the Sample Filter with 
  the setting *Subset track*, select **lv_braf_mut** and in teh pop up check the boxes of **0 (776) and 1(87)**, click 
  **ok**
* For the changes to take effect click **Submit**

------  


![](_static/images/R2d2_logo.png)**Which CMS group shows the highest amount of Braf mutations?**

<br>
<br>

------

Now we will look at the KRAS mutations
* Underneath the graph in Adjustable settings menu, change the *y-axis* to **lv_kras_mut**. 
* Use the red cross behind the setting *Subset track* to eliminate the braf mutation subset and click on the 
  dropdown to now select **lv_kras_mut**. In the pop up check the boxes of **0 (560) and 1(336)**, click **ok**
* Click **Submit** to see the result

------  


![](_static/images/R2d2_logo.png)**Which CMS group shows the highest amount of KRAS mutations?**

<br>
<br>

------


### A dive into CMS1: MSI / MSS in CRC

In one the previous tasks we have introduced the R2 platform and looked at differences between Normal and Colon tissue by looking at differentially expressed genes. For many cancers types it is important to focus on subtyping meaning identifying subgroups within CRC datasets R2 is hosting. As already discussed, CRC has 4 CMS subtypes, one of the characteristics of CMS I, is MSI instability.

The genomic instability in colon cancer can be divided into at least two major types, microsatellite instability (MSI) or chromosomal instability (CIN). Microsatellite instability (MSI) is caused by mutations in DNA mismatch repair genes such as MLH1, MSH2, MSH6, and PMS2, and it is found in 10% to 15% of sporadic colorectal cancers (CRCs). The presence of MSI predicts a good outcome in colorectal cancer.

In MSI colon cancer, genes of the DNA mismatch repair system play an important role. Germline mutations in these genes are a major cause of the inherited form of colon cancer, namely HNPCC (hereditary nonpolyposis colon cancer).  In sporadic forms of colon cancer however, these genes are frequently inactivated. Inactivation is often achieved via hypermethylation, switching the gene off. Hypermethylation of genes in colon cancer is most common in colon tumors with a proximal location in the colon and much less in colon tumors with a distal location.

Dataset used: The next section we will use another dataset. * "Colon Tumor - Watanabe - 84 - MAS5.0 - u133p2"*

This dataset consists of Microsatellite stable (MSS) tumors and microsatellite instable (MSI) tumors.

#### Watanabe dataset

* **Select "Colon Tumor - Watanabe - 84 - MAS5.0 - u133p2"**


Use the “Find Differential expressed genes between groups” module to generate a list of genes that differentially expressed between MSI and MSS characterized tumors. Because we know that DNA repair genes play an important role in microsatellite (in) stability, we can use a set of DNA repair genes to examine whether these genes are differentially expressed between MSI and MSS tumors. Go back to the previous settings for "Finding differentially expressed genes" and then select from 'GeneCategory' the ‘DNA repair’ genes. There are 247 genes annotated as DNA repair genes.

* Which one is in top list.



*  One of the genes differentially expressed clearly is MLH1 (does this gene sounds familiar). Look at the expression pattern of MLH1 in colon tumors, both sets (MSI vs. MSS). What do you notice ?. The MHL1 expression came significant out our test as a down regulated gene. What did you expect and what do you see?. 



MSI tumors give a very heterogeneous picture. This could be an indication that within the MSI tumor group also a subgroup could be identified. Which one do you think ??. (note: Inspect the tracks or hoover)



Taking a close look at te other tracks below the graph you already get an idea what might be the case. R2 has an analysis tool called *relate two tracks* where you investigate the relation between dataset annotations. Go back to the main menu and select **relate two tracks** and click next.  Select for the X-track the MS_status  and for the Y_track MS_Orientation and click next. 

Here the relation between Orientation and MSI is plotted and for the statistics a Fisher Exact test has been performed.

* In the previous question we saw the MLH1 expression was not equally distributed within the MSI group, select in Color mode,  Color by Gene and enter MLH1 and click submit.  

q: What do you see?

In many cases of proximal colon cancer with MSI, the high level of microsatellite instability is caused by the loss of MLH1 expression. MLH1 inactivation can occur due to mutations in the MLH1 gene or through epigenetic changes, such as promoter methylation. In summary, the loss of MLH1 expression is a common mechanism leading to MSI in proximal colon cancer. Understanding the relationship between MLH1 expression and MSI is crucial for diagnosing MMR deficiency, predicting prognosis, and guiding targeted therapies for patients with colorectal cancer.


So we have identified an important player as discussed in college. You have just selected the Watanabe set. Inspect the background information and look at the data this dataset has been generated. This is very old set, of course this set still of biological relevance we will also try to find we can find out we can validate this other sets. Not only because this is an old set, but it is always common practice in Research practice to validate your results with other sources


ToDo (small info  about tcga ?)

#### MSI in tcga set

Select **Tumor Colon Adenocarcinoma (students) - tcga - 204 - tpm - gencode36**

* Perform the **Find Differential Expression** for **Microsatellite_instability**, select in the GS button filter > Broad 2020, oncogenic and click again the MHL1 gene.

![](_static/images/MolOncCRC/filter_broad_oncogenic.png "204 set: MLH1")

[**don't forget to use the filter option**](_static/images/MolOncCRC/chrommap.png)


So clearly it seems that MLH1 plays is a key role and is possible affecting other genes also in other independent generated datasets, 

* One way to find out which genes are possibly regulated by the MLH1 gene is to find genes which are (inverse) correlated with this gene.


#### Find genes correlating with a single gene

* Run the Find correlated genes with a single gene module for the MLH1 gene do not forget to use the filter option for Broad 2020: Oncogenics further use.  the default settings. 


* Then click on the best correlating gene to plot both genes together, in a two gene view. Inspect the correlation. Can you think of reasons why the gene expression is highly correlated/


* Click on **view additional details**, on which chromosomes are both genes located


* Click T-view and zoom out 2 or 5 times, what can you say about their location of the two genes. 

![](_static/images/MolOncCRC/viewadddetails.png "Genome Browser")



Todo: (hier een klein text bruggetje waarom we de volgende stap doen?).

The MLH1 gene expression affects clearly some important pathways. In case you want to find genes which 

* Go back to your genelist of correlating genes and select only **neg corr** genes and click chrom map, do not use a filter this take some seconds.



![](_static/images/MolOncCRC/loading_page.png "Loading Page")



* A lot of genes are clearly over-represented on a number of chromosome, especially chrom 18 with a high p-value.



#### DNA repair system


Because we know that DNA repair genes play an important role in microsatellite (in) stability, we can use a set of DNA repair genes to examine whether these genes are differentially expressed between MSI and MSS tumors. Go back to the previous settings for "Finding differentially expressed genes" and then select from 'GeneCategory' the ‘DNA repair’ genes. There are 247 genes annotated as DNA repair genes.


* Go back to the MLH1 correlating genelist make sure you have preselected the DNA-repair genes. CLick submit. Click on generated a heatmap. And do you see a clear associated with a CMS subgroup ?, and which one.


* and take look at the CMS classification !!! what do you see ?? are you surprised
CMS4, MSI had been associated with CM1 and CMS4

In one of the first questions in this course we have seen there is an association with the genomic location. We have seen that a low MLH1 expression is associated with CRC subtypes. As briefly touched, the R2 platform has many types not only gene expression but also methylation arrays. Go to the main menu and select

*Tumor Colon adenocarcinoma - tcga - 296 - custom - ilmnhm450*

* Plot the one gene view for MLH1, do you see something special ?


* In the Alternative box, unfold additional details,  click on the view all link below MLH, here a nice heatmap is plotted of the methylation ratios's what do you see.


* A lot of samples are unfortunately not all the samples are annotated for Microsatelite instability, filter for those samples only and click submit. The MLH1 reporters for this gene (only 4), seem all methylated however, most likely these are not well designed and can maybe not distinguish for the proper MLH1 reporters. However look at the other reporters on the same location, we also see a gene name we encountered before. Do you see an association with MSI/MSS.



### What pathways drive subtype CMS4?

Previously we looked into CMS subtype 1. We would like to understand what sets CMS 4 apart from the subtypes 2 and 3.

* From the main page choose the *analysis* **Differential Expression Between Two Groups**.
* ToDo: how to Choose the track **cms4vs3**
* Look in the list of genes if you see anything familiar and hover over the magnifying glass icon of a few genes

Gene set analysis helps researchers interpret the biological relevance of a group of genes. Instead of looking at individual
genes, it allows you to understand the collective functions or pathway involvements genes in your list. This can provide more
meaningful insights into the underlying biology of a particular condition or experiment.

* Click on the top most button on the right that is labeled **Gene set analysis**.
* Select the *Gene set Collection* **Broad 2020 09 h hallmark**
* Switch the *Representation* setting to **all** to look at both over- and under-representation
* Click Next


------

![](_static/images/R2d2_logo.png)**Which gene sets do you see pop up and are they over or under expressed in CMS 4?**

![](_static/images/R2d2_logo.png)**Explain the biological relevance for the CMS4 subtype for these over- or/and underexpression of these gene sets for CMS4 subtype CRC tumors**

<br>
<br>


------

## Experiments TP53; Molecule of the year 1994


The well-described tumor suppressor function of p53 primarily relies on transcriptional activation of these target 
genes and their ability to mitigate the consequences of damaged DNA.

Nearly half of human malignancies harbor mutations in p53  that facilitate and promote metastasis, tumorigenesis, and resistance to apoptosis.



These mutations generally lead to loss of DNA binding and an inability to transactivate
canonical anti proliferative p53 target genes.5 Genotoxic chemotherapeutics, like doxorubicin
and etoposide, are clinically relevant activators of wild-type p53, but the potential
risk of resistance and secondary malignancies due to increased mutational burden
remains a significant concern.Given the powerful tumor suppression abilities of p53,
restoration of the p53-regulated transcriptome without inducing additional DNA damage
represents an intriguing approach for development of anticancer strategies and
therapeutics.
Nongenotoxic, small molecule activation of the p53 pathway has been proposed as
a potential solution.

TP53 mutations were found in 60% of the CRCs. However, gene set enrichment analyses indicated that their transcriptional consequences varied among the CMSs and were most pronounced in CMS1-immune and CMS4-mesenchymal.

Dataset being used:<br>
**Exp Colon Cell Lines (TP53 +/-) Nutlin-3A-etoposide - Sammons - 30 - DESeq2_rlog - tpm109geo**.

4 drugs are used:

The four drugs can be diveded in two types.


### TP53 activation

Etoposide:  Clinically relevant activators of wild-type p53, Activates p53 via induction of  DNA double strand breaks. Initiation double strand breaks but leads of course to resitance and secondary malignancies. 
Nutlin-3A:  MDM2 inhibitor nutlin-3A to activate wild-type p53 in a non-genotoxic, considered a proto-oncogene.



**Integrated stress response pathway:**

Effector of anti-proliferative and cell death expression programs

Tunicamycin: Activates the ISR (integrated stress response pathway), via ER stress of accumulating 
Histidinol: Activates the ISR (integrated stress response pathway), via histinide depletion.



* ATF3 mRNA and protein levels increased under both p53 and ISR stimulating treatments
in HCT116 WT cells
* A second approach uses compounds like the MDM2 inhibitor nutlin-3A to activate wild-type p53 in a nongenotoxic
* TP53 is mayor player of one of the tumor supressor mechanisms. 
* Both the p53-dependent and the ATF4-driven ISR gene networks are antiproliferative,
  either through induction of apoptosis or cell cycle control




* Check the TP53 level in this dataset. Is the dataset grouped by a different p53 expression

* Analyse which genes are affected by the compounds

Let's start with drugs known to interact with tp53. In college also MDM2 has been mentioned as negative P53 regulator. 
If you want to  find diffentially expressed genes in Tp53 dependent background which subgroups do you have to select.

* Do you see the MDM2 gene ?.

* Inspect the MDM2 level in a one gene view  are your surprised ?
![](_static/images/MolOncCRC/MDM2-gene_sammons.png "MDM2")

* Also check the relation with TP53
  ![](_static/images/MolOncCRC/sammons_tp53MDM2.png "TP53/MDM2")


*  A very significant correlation. Can you think of a reason? Hint:you are looking at RNA expression levels, how does nutlin3a inhibits MDM2 ???


* And why is also TP53 increased ?


* Check of there is an overlap between affected genes


Exp Colon Cell Lines (TP53 +/-) Nutlin-3A-etoposide - Sammons - 30 - DESeq2_rlog - tpm109geo

![](_static/images/MolOncCRC/atf3_sammons.png "Figure 2: heatmap")

![](_static/images/MolOncCRC/venn_drugsp53.png "Figure 2: heatmap")

 

## Effects of imatinib: shifts of signature profiles and molecular subtypes

Mesenchymal Consensus Molecular Subtype 4 (CMS4) colon cancer is associated with poor prognosis and therapy resistance.
MES signature is strongly correlated with CMS4 some MES genes  
"In the ImPACCT trial, informed consent was obtained for molecular subtyping at initial diagnosis of colon cancer using
a validated RT-qPCR CMS4-test on three biopsies per tumor (Phase-1, n=69 patients), and for neoadjuvant CMS4-targeting
therapy with imatinib (Phase-2, n=5). Pre- and post-treatment tumor biopsies were analyzed by RNA-sequencing and
immunohistochemistry. Imatinib-induced gene expression changes were associated with molecular subtypes and survival in
an independent cohort of 3232 primary colon cancer."

"The mesenchymal-to-epithelial phenotype shift following imatinib therapy coincided with increased expression of WNT- and
MYC-target genes and signatures reflecting proliferation. Accelerated proliferation may – at first sight – not be
considered a desired effect of any anti-cancer therapy. However, high expression of proliferation signatures and WNT
target genes are associated with good prognosis and reduced metastatic capacity in CRC (36–38). Proliferation and
invasion are often inversely regulated in tumor biology, supporting the notion that proliferating tumor cells have to
switch their transcriptional state (through EMT) in order to acquire invasive and metastatic properties (40, 44, 45).
Proliferating tumor cells require high expression of mTORC1 and its target genes to meet their anabolic demand (46). The
high expression of mTORC1 in imatinib-treated tumors may therefore simply reflect the MET phenotype switch."

We want to see how the expression changes between the pre and post treatment samples expression of specific 
mesenchymal genes such as ZEB1, PDGFRA, PDGFRB, and CD36 :
(ToDo: or Wnt pathway etc uit Supplementary materials)
* On the main page in the center menu, select the dataset **Tumor ImPACCT - Kranenburg - 30 - custom - ensh37e75**  
* Choose the analysis **View Multiple Genes** and click Next
* In the *Genes/Reporters to include* textbox, type **Zeb1,PDGFRA,PDGFRB,CD36**
* Set Track to **imatinib** to divide the samples in the pretreatment and the posttreatment group and *Handle groups 
  by* **lump by gene plot group** to show this per gene. 
* Set *color by* to **Track** in order to make the box plots visually more dictinct.  
* Click next


------

  ![](_static/images/R2d2_logo.png)**What can you say about the level of expression of these genes post treatment?**

  ![](_static/images/R2d2_logo.png)**What is the role of ZEB1 in EMT?**
  



------

### Proliferation vs metastases 

ToDo: optional analysis - I have not made all the steps. If we want these three analyses in, I will write the actual 
steps down.  

Mesenchymal tumor phenotypes are generally accompanied by reduced proliferation. Indeed, high expression of
proliferation signatures and Wnt target genes are associated with good prognosis and reduced metastatic capacity in CRC

ToDo: Remove picture
![](_static/images/MolOncCRC/wnt_up_post_imatinib_relate2tracks_optionalanalysis_impacct.png "Figure 4: View  
multiple genes 4 gene signature, todo remove")

[**Figure 4: View multiple genes 4 gene signature, todo remove**](_static/images/MolOncCRC/wnt_up_post_imatinib_relate2tracks_optionalanalysis_impacct.png)


ToDo: Remove picture
![](_static/images/MolOncCRC/myc_up_post_imatinib_relate2tracks_optionalanalysis_impacct.png "Figure 4: View  
multiple genes 4 gene signature, todo remove")

[**Figure 4: View multiple genes 4 gene signature, todo remove**](_static/images/MolOncCRC/myc_up_post_imatinib_relate2tracks_optionalanalysis_impacct.png)

ToDo: Remove picture
![](_static/images/MolOncCRC/mtorc1_up_post_imatinib_relate2tracks_optionalanalysis_impacct.png "Figure 4: View  
multiple genes 4 gene signature, todo remove")

[**Figure 4: View multiple genes 4 gene signature, todo remove**](_static/images/MolOncCRC/mtorc1_up_post_imatinib_relate2tracks_optionalanalysis_impacct.png)

"The mesenchymal-to-epithelial phenotype shift following imatinib therapy coincided with increased expression of WNT- and
MYC-target genes and signatures reflecting proliferation. Accelerated proliferation may – at first sight – not be
considered a desired effect of any anti-cancer therapy. However, high expression of proliferation signatures and WNT
target genes are associated with good prognosis and reduced metastatic capacity in CRC (36–38). Proliferation and
invasion are often inversely regulated in tumor biology, supporting the notion that proliferating tumor cells have to
switch their transcriptional state (through EMT) in order to acquire invasive and metastatic properties (40, 44, 45).
Proliferating tumor cells require high expression of mTORC1 and its target genes to meet their anabolic demand (46). The
high expression of mTORC1 in imatinib-treated tumors may therefore simply reflect the MET phenotype switch"

* On the main page, make sure that the selected dataset is **Tumor ImPACCT - Kranenburg - 30 - custom - ensh37e75**
* Select the analysis **View Geneset (Heatmap)
* Select *Gene set Collection* **Broad 2020 09 h hallmark** and click **next**
* Click **next** again
* Click one time on *Gene set* **HALLMARK_MYC_TARGETS_V1 (200)** and click **Next**

The heatmap for the z-scores of the expression values of the MYC targets geneset is shown. Underneath the heatmap 
you find the geneset average z-value per sample, also known as the signature score. With an account you can save 
such scores to use later in R2. For this course we added these scores to the public information.

* Go back to the main page
* Click **Relate 2 tracks**, click **Next**
* Select *x-axis* **imatinib (2cat)** and *y-axis* **hallmark_myc_targets_v1_signsc**
* Select *Graph type* **Box/dot plot (bands)**
* Change *Color mode* to **Color by Track** and click **Submit**

* In the Adjustable settings menu underneath the plot, change the *y track* to **wnt_impacct_signsc**
* Optionally change the *Graph type* to one that you want to try out
* Click **Submit**

ToDo: check that this has been added in R2
------

![](_static/images/R2d2_logo.png)**What happened with the expression of WNT- and MYC-target genes post treatment?**

![](_static/images/R2d2_logo.png)**Even though it is counterintuitive, can you think of a reason why this actually 
could be good news?**

<br>
<br>


------


### Assess the prognostic value of imatinib treatment
To assess the potential prognostic value of the treatment, we will make a signature of the genes that were changed 
after treatment. 

* On the main page, make sure that the selected dataset is **Tumor ImPACCT - Kranenburg - 30 - custom - ensh37e75**
* Select the analysis **Differential expression between two groups**
* Switch the *Group by* setting to **imatinib (2cat)** and click Submit
* Extra settings appear. We can now fill in the groups for which we want to find the differentially expressed genes: 
  *Group 1* **pre-imatinib (15)** and *Group 2* **post-imatinib (15)**
* Set the *P-value cutoff* to a stricter value: **0.001** and click Submit

A table shows the differentially expressed genes. On the right underneath buttons with followup analyses, you can 
find a small table that shows how many genes were downregulated by the imatinib treatment (imatinib: pre-imatinib >= 
post-imatinib) and how many genes were upregulated (imatinib: pre-imatinib < post-imatinib). 


------

![](_static/images/R2d2_logo.png)**How many upregulated and how many downregulated genes were found?** 

______

* To use this genelist in other analyses within R2, click on the lowest button on the right side that is labeled 
  *Store result as custom gene set*
* As a name, type **impacct_imatinib_treatment_up**
* In the *Included groups* check only the upregulated genes
* Click on **Save gene set**
  
The treatment resulted in a shift in gene expressions. To find out what the effect is of this shift, we will make 
use of geneset of upregulated genes that we just saved, now in combination with the Guinney dataset, the 
cohort dataset with annotated CMS status and survival data. We use the unsupervised k-means algoritm to find groups 
in our cohort that sow similar expression patterns for our geneset. 

* On the main page, select the Guinney dataset again
* Select the **K-means analysis** in *box 3* and click Next
* In the *Subset track* dropdown, select **lv_stage**, and in the pop up window check the boxes **2** and **3** , 
  click **Ok**
* Behind the setting *Gene set*, you find the button **Search GS**. Click on the button and find your previously 
  stored gene set under **User gene sets > - > impacct_imatinib_treatment_up** and hit the green button on the left 
  to use the selected gene set
* We leave the number of groups at 2 
* Set the *Cell* width to **1** and click on next

The Kmeans algorithm looks at the expression of the samples for the selected genes and makes two groups of samples 
that show most similar expression patterns. Then for each gene it shows the expression by a color code


------

  ![](_static/images/R2d2_logo.png)**Which group would you say shows high expression and which group shows low 
expression of the geneset?**

______

Again this group division can be stored in R2 to use in a next analysis. 
* To do so, hit the button **Store as track** that you can find on the left
* On the following page, just click the button Next
* To save the results in a way in which we will easily remember what the track was for and whic group showed wich
  expression, change the name of *Group 'cluster 1'* into **high** and of *Group 'cluster 2'* into **low**. Also 
  change *Track name* into **kmeans_imatinib_induced**
* Click on Build set and go back to the main page

Let's see which cms subtypes are represented in the two k-means sample clusters
* On the main page, select the analysis **Relate 2 tracks**
* For the *X track* scroll all the way down and select **kmeans_imatinib_induced**
* For the *Y track* choose **lv_cms_final**
* In the *Subset track* dropdown, select **lv_stage**, and in the pop up window check the boxes **2** and **3** ,
  click **Ok**
* Change the *Graph type* into **Stacked bar plot (%)**
* *Order Groups by* **group size** and hit **Submit**


------

![](_static/images/R2d2_logo.png)**If the impact of imatinib shows a shift of the geneset from low expression to 
high expression values, what shift in CMS subtypes do we expect to see?**

![](_static/images/R2d2_logo.png)**What is known about the treatability of subtype 4 and cms 2 respectively?**

______
  
ToDo: not sure we want to include this analysis
  
* From the main page in the left menu click the **Survival (Kaplan Meier/Cox)** analysis
* Check that the Guinney set is selected and that the separation is made by **a categorical track**. Click **Next**
* Choose *overall* survival type and *Track* **kmeans_stage23_imatinib_induced**. Click Next


* In the left menu click again the **Survival (Kaplan Meier/Cox)** analysis
* Repeat the process but select the **relapse free** in stead of *overall* survival type. 


------

![](_static/images/R2d2_logo.png)**What is your conclusion?**

______

## Identifying key drivers of CRC: superenhancers controlling gene expression

An enhancer is a short (50-1500 bp) region of DNA that can be bound by proteins (activators) to increase the 
likelihood transcription will occur at a gene. They can be located up to 1 Mbp (1,000,000 bp) away from the gene, 
either upstream or downstream from the start site, and either in the forward or backward direction. A super-enhancer 
is a region of the mammalian genome comprising multiple of these enhancers, collectively bound by an array of 
transcription factor proteins to drive transcription of genes, often involved in regulation of cell identity. They 
can be up to 20 times the size of an enhancer. <br>
In chapter [Integrative analysis: ChIP-seq data](https://r2-tutorials.readthedocs.io/en/latest/Integrative_analysis_ChIP-Seq_data.html) of the R2 Tutorial, you can find a more detailed description 
of Chipseq data analysis. 
<br><br>

![](_static/images/MolOncCRC/IntAnalysis_ChIPSeq_ModificationTypes.png "Figure 4:Survival chances that are linked to the gene shift, todo remove")

[**Survival chances that are linked to the gene shift, todo remove**](_static/images/MolOncCRC/IntAnalysis_ChIPSeq_ModificationTypes.png)

(Fig source: https://www.nature.com/articles/s12276-020-0428-7)


Enhanced enhancer activity can lead to the overexpression of oncogenes, which promote cancer growth. Super-enhancers 
often play a central role in determining cell identity and tumor initiation and progression. Identifying these active enhancers can help pinpoint key drivers of colorectal cancer, potentially revealing new therapeutic targets.  
Different patients may have colorectal tumors with distinct enhancer landscapes. By characterizing enhancer activity, researchers can potentially classify patients into subgroups with different treatment responses or prognosis, enabling personalized medicine approaches.

With Chromatine Immuno Precipitation binding of elements to the genome can be studied. Transcription of DNA to RNA
is regulated by the binding of these elements. These can be Transcription Factors, that bind temporarily to start
transcription, but also chemical modification of the histones (molecular structures that coil the DNA) by methylation, acetylation, etc. These modifications change the accessibility of the DNA for transcription.
<br><br>
When a specific antibody is used in the pulldown that recognizes these chemically modified regions, these specific regions can be studied. Regions with H3K27Ac acetylation mark active enhancers and active transcription, H3K4Me3 methylation marks active and poised transcription (Figure 2). Studying the relative contributions of both types of modifications allows a researcher to discern enhancer regions from active transcription sites.


* Click on the button below to show the ChIP-Seq data for VEGFA in the four mesenchymal and five adrenergic neuroblastoma cell lines. For your convenience the signals are colored according to the type (MES or ADRN) of cell line.

ToDo: create new button to go to VEGFA

<a class="course_permalink" href="https://hgserver2.amc.nl/cgi-bin/r2/main.cgi?permalink=course_molgen_chipseq_gb_hand1_9_mes_adrn" target="_blank">Go to R2 GenomeBrowser for HAND1</a>
<br>
<br>

Regions encoding genes are drawn at the bottom of the graph. When in red they're encoded in the reverse direction, coding exons are darker.


## Evaluation

Please don't forget to fill in the evaluation form about this R2 course, if you haven't done so yet:

<button class="course googleform" onclick="window.open('https://docs.google.com/forms/d/e/1FAIpQLSflNJpsTcLIhwEC0ZlHksfnE0VwBay1I2KOGPArYu4Q_QhtrA/viewform?usp=sf_link','_blank');" type="button">
Open the Evaluation form</button>

---------

# Final remarks / future directions

In the March 1st 2018 issue of Nature a paper was published describing a landscape of genomic alterations across
childhood cancers. The data is accessible in R2 also as a Datascope. This is another example of how R2 can visualize
your genomics data.
<br><br>
This ends the course. Feel free to further explore the course materials or our tutorials.
<br><br>
We hope that this course has been helpful. If you want to have your genomics data visualized and analyzed using the R2
platform you can always consult r2-support@amc.nl
<br><br>
The R2 support team.

