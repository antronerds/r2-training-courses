<a id="rna_seq_data_analysis_-_using_rheumatoid_arthritis_data"> </a>

Gene expression in Rheumatoid Arthritis
=======

Introduction
---
Rheumatoid arthritis (RA) is a common autoimmune disorder characterised by inflammatory cell infiltration, such as T cells, B cells, macrophages and plasma cells. Production of cytokines and proteases lead to chronic inflammation of the synovial tissues and progressive joint disability. RA affects as much as 1% of the worldwide population. Although the exact causes are unknown, decades of research has led to increasingly detailed understanding of multiple disease mechanisms. Different treatments for RA have been proposed, e.g. infliximab (IFX), methotrexate (MTX), tocilizumab (TCZ). However, a significant proportion of patients do not respond to initial treatment or reach remission. Others experience recurrence or deterioration of their disease.   
   
This has led to extensive efforts to find more specific diagnostic markers. The complexity of the disease mechanisms have spurred unbiased searches using genetics, transcriptomics or proteomics. Because of difficulties in measuring markers in the inflamed joints, efforts have, to a large extent focused on analyses of peripheral blood. However, as Lee et al. point out ([Cytokine, March 2020](https://doi.org/10.1016/j.cyto.2019.154960)), clinical translation has proven difficult. Lee et al. hypothesize that inflammatory responses in peripheral blood are different from those in the arthritic joint.   
 
 ![](_static/images/KIT_rheumatoid-arthritis-drug-targets.jpg "Figure 1:  Cell types, cytokines, and chemokine receptors as rheumatoid arthritis drug targets (Source DOI: 10.1211/PJ.2016.20201090)")
   
   [**Figure 1:  Cell types, cytokines, and chemokine receptors as rheumatoid arthritis drug targets (Source DOI: 10.1211/PJ.2016.20201090)**](_static/images/KIT_rheumatoid-arthritis-drug-targets.jpg)

 Immune response in blood and synovial fluid  
---
 Today you will use the web-based genomics analysis and visualization platform R2. R2 provides you with a set of bioinformatics tools to investigate patient and experimental data.  
   
 Takeshita and Okuzono et al. (2019) and Lauwerys et al. (2014) have collected a large number of samples from clinically well-defined cohorts of patients with RA and age-matched healthy controls (HCs). This data and other similar studies have been uploaded into our platform R2. We will make use of these datasets to explore the  differences and similarities between peripheral blood and synovial fluid, to study the characteristics of T cells, and to look for possible effects of treatments. 
  
##### A first look at T cell gene expression with the R2 platform

 *Data used:*  
 * R2 dataset: Disease Rheumatoid arthritis subset (drugs) - Okuzono - 75 - deseq2 - gpl17303
 * Description: 75 blood and synovial T cell samples of RA patients with rheumatoid arthritis 
 
 *Techniques used:*   
 * RNA Seq
 
 *References*
 * Paper: [Multi-dimensional analysis identified rheumatoid arthritis-driving pathway in human T cell](https://ard.bmj.com/content/78/10/1346.long)
 
 *Analysis used*
 * One Gene View 
 
<br><br>

 Let's take a first glance at the platform. Click on the following button to go to R2:  
  
<form name="accessing_r2" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gse118829subsgeo75_gpl17303">
  <button type="submit" >Go to R2</button>
</form>  
<br>
<br>

* Log on to the R2 platform with your credentials that were provided (or apply for a login using the link).  

The five numbered boxes or steps in the middle of the R2 main page allow you to choose a dataset and a type of analysis. In box 2 you can see that the dataset of Okuzono has already been selected. In box 3 you can select an analysis to perform on this dataset. 

* The default analysis is View a gene. Type in the textbox of step 4 *Gene / Probeset:* **CD4**.   
* Click the **Next** button. To read a description of your provided gene, hover your mouse over the bold **CD4** letters next to the radiobutton.  Leave all settings as is and click **Next** again to get a result.   

 The dots in the graph show the expression value of each sample of the dataset for the gene CD4. Under the graph you can see different types of *annotation*. 
 In R2 the samples of a dataset can be annotated with extra information, such as clinical data of the patients the sample were taken from, or biological characteristics of the cells that were observed in the lab.  
   
 Each group of annotated data is called a *Track* in R2. You will see the annotation often displayed underneath a plot, or if you hover your mouse of the dots in a plot. 
 * Try it out with your mouse in the graph that you have generated to view the expression of the gene CD4.  
 
 Furthermore, these tracks can be used in most of the analyses in R2 to add a layer of complexity. Tracks will allow you for instance to filter datasets, to compare groups of samples, to color scatter plots of samples with meta information, or to correlate genomics patterns in your data to lets say different phenotypes or demographic characteristics.
 
---------

   ![](_static/images/R2d2_logo.png)**Look at the *t-cell* track underneath the graph. The two colors represent two different cell types. Hover with your mouse over the two different colors of this cell type annotation row. Which cell types are present in the dataset?**
       
   
   ![](_static/images/R2d2_logo.png)**Do you notice anything different about the expression levels between the two cell types?**
 <br>
 
 ---------   
Tumor necrosis factor‐alpha (TNF‐α) is a proinflammatory cytokine that plays a pivotal role in regulating the inflammatory response in rheumatoid arthritis (RA). 

* In the upper left corner, click the link *Go to:*  **Main**  to go back to the main page.
 
To understand better how this cytokine relates to different tissue and cell types, we do the same process but now we take a look at the gene TNF

* Type in the textbox **Gene / Probeset: TNF**.   
* Click the **Next** button and click **Next** again in the following page.    

We can make use of the annotations to view the results of our samples in groups.

* Scroll down in the page to make some adjustments in the *Adjustable settings* menu under the graph. Under *Group Separations* change *use track:* **tissue (2cat)** to separate the samples of the tissue blood from those of synovial fluid.
* Under *Graphics* adjust *Graphtype:* **Boxplot with circles** and *ColorMode:* **Color by Track**.
* After you selected your preferred adjustments, click **Adjust Settings**.  
  
 Often you use a boxplot to assess whether the expression values between groups of samples differ for a particular gene and to quickly identify average values, outliers, the dispersion of the data set, and signs of skewness.  
 
 * Next to the visual representation, R2 also provides the five number summary in textual format. Hover your mouse over each box to compare the summarizing values of the two groups. 
 
The circles on top of the boxplot show the individual value of each sample, which is a good way to stay aware of the raw data and the distribution behind the summary.
 We can see that the two groups show different values for the boxplots. But how certain are we that the group means vary by more than that random chance allows? To answer that question R2 shows you the results of an analysis of variance (ANOVA): you can find the F-value, the test statistic of the ANOVA test, and the p-value of the ANOVA test in the table above the plot.  
---------  
  
   ![](_static/images/R2d2_logo.png)**What can you conclude about the expression of the gene TNF in blood tissue versus synovial fluid?**
 <br>
---------  

The immune system is a complex system of different cell types that interact with each other with chemokines and other cytokines. T cells are one of two primary types of white blood cells — B cells being the second type — that determine the specificity of immune response to antigens (foreign substances) in the body. T cells originate in the bone marrow and mature in the thymus.  
  
  ![](_static/images/KIT_Tcelldifferentiation.png "Figure 2: Differentiation of T-cells, each subtype having its specific role in the immune system.")
  
  
  [**Figure 2: Differentiation of T-cells, each subtype having its specific role in the immune system.**](_static/images/KIT_Tcelldifferentiation.png)
  
  By *developmental stage*, peripheral blood (PB) CD4+ T cells are classified into four stages: naïve (Tn), stem cell memory (Tscm), central memory (Tcm) and effector memory (Tem), whereas CD8+ T cells are classified into five stages: Tn, Tscm, Tcm, Tem and CD45RA-positive effector memory (Temra).  
    
 Each subset has its own markers as can be seen in the table below. This heterogeneity among Tcells has made it challenging to identify the specific cell subsets and states that drive RA pathogenesis.

<table>
<tr><th>  T-cell  </th><th>Developmental stage</th><th>Markers</th></tr>
<tr><td>CD4</td><td>tn</td><td></td></tr>
<tr><td>CD4</td><td>tcm</td><td>(George/Mosse/Janoueix-Lerosey/Chen 2008)</td></tr>
<tr><td>CD4</td><td>tem</td><td>(Molenaar et al., 2003)</td></tr>
<tr><td>CD8</td><td>tn</td><td>(van Limpt et al., 2004)</td></tr>
<tr><td>CD8</td><td>tcm</td><td>(Stallings et al. 2006)</td></tr>
<tr><td>CD8</td><td>tem</td><td>(Hölzel et al., 2010)</td></tr>

</table>

  
---------

 **Under your latest graph, change "use track" to "t-cell-stage-type".**   
   
 ![](_static/images/R2d2_logo.png)**What can you conclude about the expression of TNF in the different T-cell subtypes?**
 
 ---------
 
##### Exploring relevant annotation of a dataset

*Analysis used*
* Cohort Overview

<br>  

We have seen before that the samples of a dataset can be annotated with extra annotation, or tracks. 
To get a better overview of the available annotation of a dataset, we can use the tool **Cohort Overview** in R2. 

* Go back to the main page and select **Cohort Overview** as type of analysis in box 3.

R2 presents the Okuzo dataset samples with its available annotation in a table at the bottom of the page. Each pie chart above the table shows a different available track. 
* Hover your mouse over the different slices of the **gender** annotation pie chart.  Which percentage is male and which is female?
* Explore the other pie charts as well: hover with your mouse over the slices and double click on a slice to select that group of the samples (you can click on the button **Clear Filters** to undo your selection). Above the main pie chart you can read the number of samples in your current selection (the "n= " number). Also note how the table at the bottom adapts the overview based on your selection.  
  
   
---------

![](_static/images/R2d2_logo.png)**How many synovial fluid samples are present in this dataset?** <br><br>
![](_static/images/R2d2_logo.png)**And how many samples are CD4 Effector Memory T cells (Tem) in the blood tissue? (Hint: you will have to apply 3 different filters)**  
  
---------

 Based on the expression profiles of each sample, we would like to know which samples behave much alike and which show different patterns? Before we used the analysis of *One Gene View* to plot the gene expression of a single gene. Often a dataset contains expression values of about 20.000 genes for each sample. We cannot check all these genes one by one to find out which samples show similar expression profiles. Let's see if we can find out more information with a so called t-SNE analysis.  

##### An unbiased look at sample similarity

*Analysis used* 
* t-SNE

A **t-SNE** analysis (t-Distributed Stochastic Neighbor Embedding) can summarize the characteristics of many genes in new, more abstract variables. t-SNE will plot the samples that show similarity in their expression profiles closer together. This type of analysis is useful to find interesting groups of samples that show similar expression profiles or if there are outliers that we might want to exclude from our dataset. 

* Click the button below to show a 2D t-SNE plot of the Okuzono dataset in R2

<form name="pca_form" target="_blank" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" method="POST">
<input type="hidden" name="option" value="tsne_plot">
<input type="hidden" name="tsne_id" value="45159a5e2c4c234999cb70b745fbc72b">
<input type="hidden" name="perplexity" value="20">
<input type="hidden" name="dotsize" value="6">
<input type="hidden" name="table" value="ps_avgpres_gse118829subsgeo75_gpl17303">
<input type="hidden" name="cortype" value="transform_zscore">
<input type="hidden" name="subset" value="">
<button type="submit" >Go to t-SNE Analysis</button>
</form>  
<br>
<br>  

Each dot is a sample and the axes are the more abstract t-SNE variables (v1 and v2).  
  
 So far the black dots do not give us much insight. To see whether any biological process might determine the similarity in expression profiles, we can color the dots with a track. Sometimes, biological or clinical annotation groups correspond with the t-SNE ordering of the samples in the plot. 
 
* Colors are not set by default. Under the graph, first adjust *ColorMode:* **Color by Track** and *Track for color:* **tissue (2 cat)**; click next for the changes to take effect.  

*  Now try the **tcell-stage (4cat)** track as **Track for Color**. Click next to show the changes. Also try the other tracks for coloring.
  
  
---------

  ![](_static/images/R2d2_logo.png)**What biological information corresponds with a similarity in expression profiles according to this t-SNE analysis?**
  
 ---------

##### Finding pathways that make a difference

*Analyses used* 
* Differential Expression between groups
* Gene set analysis
* KEGG mapping

We have seen that the expression profiles of the same cell types can show differences in peripheral blood and synovial fluid. It would be interesting to have a better understanding which genes and pathways cause the biggest differences and whether they are relevant to RA pathogenesis. 

* From the main page, select the analysis **Find Differential expression between groups** in box 3; click **Next**.  
* In the next page with selection criteria, choose *Select a track:* **tissue (2cat)**.   
* The rest of the settings we leave as is. Note that by default the *anova test* is selected with a p-value treshold of 0.01. Click **Next** and click **Next** in the group selection where both blood and synovial fluid are selected.

 R2 now performs a one-way Anova statistical test on the fly with a correction for multiple testing. The result is a list of genes that is ordered by the most significant differential expression between the groups that we chose before (PB and SF). 
  
    
 ---------
 
   ![](_static/images/R2d2_logo.png)**Do you recognize any genes related to the immune system?**
   
   **Hover your mouse over the names of the genes to read a summary of information about its function and alternative names.  
   Click on a gene name to see the gene expression per sample in a *One Gene View* graph.**  
   
  ---------
    
 * To find the biological processes that are affected by the genes in this list, we can use the Gene Set Analysis. On the menu to the right of your list of genes click the button **Gene Set Analysis** and click **Next** in the following window.  
 
 The returned table shows you the processes in which the genes are involved as defined by the [KEGG (Kyoto Encyclopedia of Genes and Genomes) database](https://www.genome.jp/kegg/).  
 
 * To understand the respective roles that T cells play in peripheral blood and synovial fluid of patients with RA, which pathways seem relevant? You can click on the little green **K icon** in front of a gene set to see the genes projected in a KEGG pathway map. 
 
 * Above the result table, you can read the meaning of the color coding. Which tissue has a larger expression of most of the genes. What does that mean biologically? 
   
   
 ---------  
 
  
![](_static/images/R2d2_logo.png)**What are your thoughts on RA treatment based on peripheral blood samples?**  
  
 ---------  
 
   
 Effects of treatment
---
 Now that we have a better understanding of gene expression of T-cells, let's have a look if we can find any effect of rheumatoid arthritis treatments on a genomic scale.    
 
*Data used:*  
* R2 dataset: Disease Rheumatoid arthritis (drugs) - Lauwerys - 40 - MAS5.0 - u133p2
* Description: Paired synovial biopsy samples were obtained from the affected knee of early RA patients before and 12 weeks after initiation of Tocilizumab (n=12) or Methotrexate (n=8) therapy 

*Techniques used:*   
* Affymetrix DNA Microarray 

*References*
* Paper: [Global Molecular Effects of Tocilizumab Therapy in Rheumatoid Arthritis Synovium](https://onlinelibrary.wiley.com/doi/full/10.1002/art.38202)
     
*Analyses used*
* Cohort Overview
* One Gene View
* PCA

##### Explore the provided information

How does treatment effect gene expression? Let's have a look at a dataset of Lauwerys et al. In the dataset we can find samples taken from the synovial fluid in the knee of 20 early RA patients, both before and after treatment.  
  
Click the button below to go to R2 with the correct dataset selected.   

<form name="accessing_r2" action="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi" enctype="multipart/form-data" target="R2" method="post">
  <input type="hidden" name="table" value="ps_avgpres_gse45867geo40_u133p2">
  <button type="submit" >Go to R2</button>
</form>  
<br>
<br>

First, we take a look at the information that was provided. Let's start with the dataset Cohort Overview.  

* In box 3, select the **Cohort Overview**, click **next** and explore the available annotation.
* To understand what the study is about, click on the **i information balloon** behind the dataset title. Which genes are important according to the description?     

Since this set is treatment related, let's plot some data to see if treatment has any result.

* Go back to the main page. Choose the analysis **Correlate gene with track** and type in box 4 any of the genes that in the description is mentioned to be down regulated by treatment. Click **Next**.
* Choose *Select a track:* **therapy (2cat)** and click **Next**.
* Every patient had a sample taken before the start (no) and after 12 weeks (yes) of therapy, it is a paired test. It would be nice to see which dots belong to the same patient. With Sample Paths we can connect the two samples of each patient. Because it is a bit labour intensive to get the correct syntax, we did this for you. Copy paste the following information in the textbox of **Sample Paths**: GSM1116933,GSM1116934;GSM1116935,GSM1116936;GSM1116937,GSM1116938;GSM1116939,GSM1116940;GSM1116941,GSM1116942;GSM1116943,GSM1116944;GSM1116945,GSM1116946;GSM1116947,GSM1116948;GSM1116949,GSM1116950;GSM1116951,GSM1116952;GSM1116953,GSM1116954;GSM1116955,GSM1116956;GSM1116957,GSM1116958;GSM1116959,GSM1116960;GSM1116961,GSM1116962;GSM1116963,GSM1116964;GSM1116965,GSM1116966;GSM1116967,GSM1116968;GSM1116969,GSM1116970;GSM1116971,GSM1116972
* Click on **Adjust Settings**
* Change **Colormode:  Color by Track** and **Track for Color: therapy (2 cat)**    
  
  
---


![](_static/images/R2d2_logo.png)**What can you tell about the effect of treatment on the expression of this gene?**  
 
---

* In the upper right corner is a text box **Change gene**. Change the gene to a different gene that you can find in the description of the study, or that you yourself wonder about. Click the Change Gene button under the textbox. 
* By a slight adjustment of the graph, sometimes we can get different insights. Change under Group Separations **use track: pid_drug**. Which drug works best to downregulate this gene? Do any of the patients have remarkable results?  
<br><br>  
  

##### An unbiased look into the dataset

Also in this set, we take a look at an unbiased view of expression profile sample similarity. This time, we will use **PCA** (Principle Component Analysis ). Like t-SNE, PCA analysis can summarize the characteristics of many genes in new abstract variables. The new variables are called principle components (PCs). PCA will plot the samples that behave similarly in their expression profiles closer together as well.

* Return to the main page from the Cohort Overview, using the top left link **Go to: Main** 
* Select **Principle Component Analysis (PCA)** in box 3 and click **Next**. Also on the following page, click **next**, then click **Plot the PCA result**
* R2 also allows you to color t-SNE and PCA with the expression of a gene. Under the plot select **ColorMode: Color by Gene** and type **Gene for Color: IL6**, select the first option IL6 (Reporter: 205207_at HO:1). Don't forget to click **next** in order for your changes to take effect. 

The PCA calculation creates many principle components. The first PC explains most of the variation found between the samples. Every following PC explains less and less of the variation of the dataset, R2 allows you to view the first 3 PCs in 3D.
* Under the graph, select **PCA Projection: PC1:PC2:PC3-3D** and click **next** to see the effect. You can play with the 3D cube by holding your right mouse button down while dragging your mouse around. 
 

##### Showing pathways in heatmaps

We now want to know which pathways are affected by treatment with tocilizumab.
* From the main page, select the analysis **Differential Expression between groups**, click **Next** 
* Choose *Select a track:* **therapy (2 cat)**
* Because we won't have many samples, we will not correct for multiple testing. Change *Corr. multiple testing:* **No correction** 
* Under *Sample Filter* we want to select the subset of samples involved in the tocilizumab study, both before and after treatment. Therefore, select *Select a track (subset):* **drug (3 cat)** and check both **tocilizumab (12)** and **untreated (20)**, click **ok**. Click **Next**. Click **Next** again on the following page. 

The list shows the genes that are differentially expressed before and after treatment. 
* To see in which pathways these genes play a role, this time we click on **Gene Ontology Analysis**. What pathways show a difference before and after therapy? Look at the color scheme, therapy: no >= yes means that the genes where higher expressed before than after treatment. Is this what you would exprect?
* The page with the list of differentiating genes is still opened. This time click the button Heatmap(zscore).
---


![](_static/images/R2d2_logo.png)**Do you see any patients that did not respond?**  
 
--- 


