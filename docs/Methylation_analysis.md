<a id="molecular_genetics_crc"> </a>

Molecular Genetics Course - Colorectal Cancer
=================================

*Methylation Analysis*

This resource is located online at http://r2platform.com/mgcourse  
 
  
Introduction
------------

This manual is intended for scientists and students who wish to study DNA methylation and to its purpose is to provide instructions on how to analyze methylation data using the R2 Genomics Analysis and Visualization Platform, also known as the R2 Platform [1]. Additionally, an online tutorial on the R2 Platform is available on the official website to learn about other features. [2] The following mind map aids in understanding the structure of the manual and the relationships between its sections [2], [3].

![](_static/images/Methylation/image001.png "Figure 1: Mind map on this R2 methylation manual")

[**Figure 1: Mutation paths during cancer progression**](_static/images/Methylation/image001.png)



### Generating a Heatmap

For analysis of the human methylome in order to study the potentia

l tumor suppressors we are using the R2 platform and the methylome dataset available in R2. The methylome is analyzed by an EPIC array (details), which is bisulfite treatment based. It determines methylated vs. unmethylated DNA target regions between probes (oligonucleotides) and methylated region per each probe, a Heatmap is a useful tool to observe each (un)methylated probes and the clustered region of isoforms in relation to a degree of methylation. As an example for this manual, a Heatmap is generated under the following conditions: “cancer pharmacogenomic tissue”, “cell line” type from “Illumina” company by the author name “Esteller”. Also, this dataset shows how the Heatmap looks like from the highly proliferated cancer samples. Later in Section 3 Comparing Methylation Heatmaps of this manual, the Heatmap from this example will be compared with two other examples from different datasets. The tutorial scope will be then expanded to more complicated conditions such as a tutorial on “Expression” dataset. With the above conditions, the platform user takes the following steps to create the Heatmap:



![](_static/images/Methylation/image003.jpg "Figure 2:")

[**Figure 2: Main Menu**](_static/images/Methylation/image003.jpg)

Research is needed to understand the mechanisms underlying treatment resistance and to develop strategies to
overcome it. Better identification and characterization of multiple CRC subtypes could guide treatment decisions and
improve the outcomes for individuals with colorectal cancer. Furthermore, markers for early detection and prevention
might allow for interventions before advanced mutations occur. Clearly it is crucial to understand the diversity and
complexity of colorectal cancer in order to develop new and effective targeted treatment strategies. <br>

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
 

## Normal vs Colorectal Tumor Tissue: a first impression of genomic data

A fundamental query in cancer research consistently revolves around understanding the distinctions between normal 
and tumor tissues. Let's get acquainted with R2 and its large collection of omic datasets while imimediately exploring 
differences in gene expressions between normal tissue and adenoma tumor tissue.

**Datasets used:**
  
* Mixed Colon - Marra - 64 - MAS5.0 - u133p2
* Tumor Colon Adenocarcinoma (students) - tcga - 204 - tpm - gencode36

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

**A:225**

* How many sets has R2 when you only look for colon methylation sets.

**A:7**

This first dataset that we will use, can be found in R2 as "Mixed Colon - Marra - 64 - MAS5.0 - u133p2". In te main 
screen more background information is revealed bij clicking on the dataset name. In the rest of  R2 clicking on the exclamation marks next to the dataset name will also reveal additional information.

**An Introduction on R2 Genomics Analysis and Visualization Platform Usage**

By Ji Sun (Klara) Kwon
Supervision: Dr. Antje Richter
Justus-Liebig University Giessen (JLU)
Institute for Genetics and Institute for Bioinformatics
Heinrich-Buff Ring 58, 35392 Giessen, Germany

---

## 1 Introduction

This manual is intended for scientists and students who wish to study DNA methylation, and its purpose is to provide instructions on how to analyze methylation data using the R2 Genomics Analysis and Visualization Platform, also known as the R2 Platform [1]. Additionally, an online tutorial on the R2 Platform is available on the official website to learn about other features. [2] The following mind map aids in understanding the structure of the manual and the relationships between its sections [2], [3].

![Mind map on this R2 methylation manual](images/page-02.jpg)

**Figure 1-1:** Mind map on this R2 methylation manual

---

## 2 Generating a Heatmap

For analysis of the human methylome in order to study the potential tumor suppressors we are using the R2 platform and the methylome dataset available in R2. The methylome is analyzed by an EPIC array (details), which is bisulfite treatment based. It determines methylated vs. unmethylated DNA target regions between probes (oligonucleotides), and per methylated region per each probe, a Heatmap is a useful tool to observe each (un)methylated probes and the clustered region of isoforms in relation to a degree of methylation.

As an example for this manual, a Heatmap is generated under the following conditions: "cancer pharmacogenomic tissue", "cell line" type from "Illumina" company by the author name "Esteller". Also, this dataset shows how the Heatmap looks like from the highly proliferated cancer samples. Later in *Section 3 Comparing Methylation Heatmaps* of this manual, the Heatmap from this example will be compared with two other examples from different datasets. The tutorial scope will be then expanded to more complicated conditions such as a tutorial on "Expression" dataset.

With the above conditions, the platform user takes the following steps to create the Heatmap:

**1)** After login to the R2 Platform [1], click the checkbox under Field 2 "Select a dataset for analysis" (in Figure 2-1).

![Main menu](images/page-03.jpg)

**Figure 2-1:** Main menu

**2)** On the pop-up box (in Figure 2-2), select "cell line" by clicking Column {Category} "Select Filter", type "cancer pharmacogenomic" on Column {Tissue/Tumor} or type "Esteller" on Column {Author}. One can confirm the right dataset by referring the description table below as shown in Figure 2-2. When the dataset is found, click the found data and click "Confirm selection". (in Figure 2-3) Leave all other settings at their default and click "Next" on the main page to proceed. (in Figure 2-4)

![Change Dataset menu](images/page-04.jpg)

**Figure 2-2:** Change Dataset menu

**Figure 2-3:** Change Dataset menu (after filter)

![Main menu after selecting the dataset](images/page-05.jpg)

**Figure 2-4:** Main menu (after selecting the dataset)

**3)** The next page is "View a gene" that narrows down to the specific gene or methylation ID which to be shown in a Heatmap. (in Figure 2-5) As an example, "CLDN10" (Claudin 10) is written in Field {Gene / Met_id} as it is a candidate tumor suppressor currently being studied in our lab [4] and strongly hypermethylated across cancer types. For your purposes please use the name/abbreviation of your candidate gene of choice. Click "Submit" to execute a Heatmap.

**Figure 2-5:** Adjustable settings menu on the dataset

In case that a gene name of interest is uncertain, one can find the exact gene name of interest by a methylation ID obtained from UCSC Genome Browser. This search process is described in *Appendix 12.1 Finding a Gene of Interest* of this manual.

A linear graph is generated as the following graph with an X-axis with samples (probes) and a Y-axis as CLDN10 methylation. (in Figure 2-6) Each sample (a.k.a. cell line type, on the X-axis) is ordered by its degree of CLDN10 methylation (on the Y-axis).

![Graph on the probes of the chosen CLDN10 dataset](images/page-06.jpg)

**Figure 2-6:** Graph on the probes of the chosen CLDN10 dataset

**Figure 2-7:** Description of the chosen dataset

Two additional features on this webpage come in handy: By clicking on the checkbox right in the graph title (marked in red in Figure 2-6), the user could see the description of the dataset as in Figure 2-7. Next, if the user wants to grasp the basic knowledge on biological or medical terminologies, one could click on the GeneID table link (marked in red in Figure 2-6) and read the definition of the terminologies on the National Library of Medicine (NIM) website. (in Figure 2-8)

![Definition of terminology CLDN10 on the NLM website](images/page-07.jpg)

**Figure 2-8:** Definition of terminology "CLDN10" on the National Library of Medicine (NLM) website

**4)** As a next step, click on "View additional details" on the same page below the previous line graph. (in Figure 2-9) Then by clicking "view all" link as shown in Figure 2-10, the embedded Heatmap and R2 Genome Browser of the chosen dataset will open in a new screen.

**Figure 2-9:** "View additional details" (clickable)

![View additional details clickable](images/page-08.jpg)

**Figure 2-10:** "View additional details" (clickable)

**5)** Figure 2-11 shows the generated Heatmap. The **Heatmap** describes where each subset (probe) of the gene is methylated or not. The X-axis of the Heatmap indicates "primary histology" (or cell line type) and the Y-axis indicates all probes of the chosen gene of interest annotated within the dataset. The methylation score is colored by yellow (near to score 0, unmethylated), black in the middle (partially methylated, 50%), and blue (near to score 1, fully methylated). As shown in Figure 2-11, each probe per cell line type has a different tendency of methylation region.

For example, a kidney cell line is shown as green above the Heatmap. The vertical tendency from the green color (a kidney cell) on the X-axis extended towards the bottom shows how probes on the kidney cell are differently methylated. The user could see on this vertical tendency that probe "cg13733394" is unmethylated as in yellow, compared to probe "cg18470456" in blue which is methylated.

![The Heatmap of the chosen dataset](images/page-09.jpg)

**Figure 2-11:** The Heatmap of the chosen dataset

If the user is interested in looking into a table of each sample (probe) and gene name of the dataset, click on "Sort Order Listing" on the same webpage below the Heatmap. (in Figure 2-12)

**Figure 2-12:** The table of sample and gene names of the chosen dataset

**6)** By scrolling down, there is R2 Genome Browser as shown in Figure 2-13. The R2 Genome Browser relates the probes on the Y-axis of the Heatmap showing as two isoforms. The user could see Isoform A on the left side and Isoform B on the right side of the bar from R2 Genome Browser. The name of a certain probe could be seen or matched between the Heatmap and R2 Genome Browser by placing a cursor on that probe. Depending on the dataset, only one isoform or more isoforms can exist.

The colored vertical line just below the diagram title represents the chromosome of this database and shows the gene position in the chromosome by a small vertical line (marked in yellow in Figure 2-13).

Then R2 Genome Browser shows the average (mean) CpG by methylation score (on an Y-axis) and the gene (a.k.a. gene position number, on an X-axis). The dots in this diagram are CpG (or probe) and their according methylation degree. It is to be noted that the Y-axis of R2 Genome Browser is the methylation score per probe, whereas the X-axis of Heatmap is the methylation score (which is vice versa).

The standard deviation of methylation per CpG is shown with the vertical gray line in the diagram, which is located in the gene index around 96,160,000. The letter "q" (queue) from the X-axis label "q32.1" reveals that the gene is located on the chromosome's long arm. If it is located on the small arm of the chromosome it is labeled with "p" (petite).

Below the diagram, there are two green sticks called "CLDN10" labeled on the left and one red stick called "CLDN10-AS1" labeled on the right. The green sticks represent Isoform A and the red stick represents an antisense isoform. The B isoform is shown on the right side. Depending on the dataset, multiple isoforms more than two (A and B) could exist. More details regarding R2 Genome Browser could be found on R2 Platform online tutorial under Section 17. Using the R2-Genome browser. [2]

![R2 Genome Browser with mean methylation score by gene index](images/page-11.jpg)

**Figure 2-13:** R2 Genome Browser with mean methylation score by gene index

Now, if the user is interested in investigating certain probes from the dataset, the next steps could be done additionally. (marked in red in Figure 2-13)

**6-1)** When a cursor is placed on one of the probes, a pop-up message shows the information regarding the selected probe. ("ilmnhm450" in Figure 2-13) Filtering by the information on pop-up messages, three CpGs within the promoter of the gene and isoform of interest are selected ("cg08418978" in purple, "cg22122715" in red, "cg25032595" in blue) by clicking the check-boxes on "Select reporters" table. As shown with marked color-arrows in Figure 2-13, the probes are observed both as a dot and as a block. Click "Next" to proceed.

**6-2)** Figure 2-14 shows the updated Heatmap and R2 Genome Browser after the previous step (Step 6-1). The user could investigate the methylation tendency of the three probes. Back to the example of "kidney" cell type (indicated in green on the X-axis "primary_histology" of Heatmap), the user sees two probes ("cg08418978", "cg22122715"; yellow in Heatmap) are unmethylated but Probe "cg25032595" (blue in Heatmap) is methylated.

![The updated Heatmap and R2 Genome Browser for a subset of CpG probes chosen](images/page-12.jpg)

**Figure 2-14:** The updated Heatmap and R2 Genome Browser of the chosen dataset for a subset of CpG probes chosen

### Update: quick access to methylation heatmaps in R2

- click view a gene
- click view all Met_ids
- click next
- choose your gene of interest in 'Gene' and click next
- wait and heatmap is produced from all CpGs assigned to your Gene of interest

![Quick access flow to methylation heatmaps](images/page-13.jpg)

---

## 3 Comparing Methylation Heatmaps

To grasp a better idea how to interpret this Heatmap, two further methylation/Methylome datasets will be compared with the "Esteller" dataset. As mentioned earlier in *Section 2 Generating Heatmap* of this manual, this "Esteller" dataset is based on highly proliferating cancer cell lines. The second dataset is based on primary tumors ("tumor" type by the author name "Heyn" on R2 Platform). The third dataset is based on normal control tissue samples ("normal" type by the author name "Lokk" on R2 Platform). In this section, three Heatmaps generated from these three datasets are to be compared to show the difference in methylation tendency for a chosen gene of interest. These comparative methylome heatmaps were used to study another tumor suppressor ZAR1. [5]

To create the second ("Heyn") and the third ("Lokk") datasets, repeat the steps from 1) to 5) in *Section 2 Generating Heatmap* of this manual. The following Figure 3-1 is the generated Heatmaps of the three datasets ("Esteller" on the bottom, "Heyn" in the middle, "Lokk" on the top). As shown with colors in Figure 3-1, the "Lokk" Heatmap of CLDN10 is rather uniform with an CLDN10 CGI (or CpG-Island) that is unmethylated, whereas the CGI surrounding regions are methylated (for all samples).

When looking at the Heatmap from primary tumors "Heyn", some degree of methylation appears across the CLDN10 CGI (the entire black and blue colors throughout the Y-axis). This methylation shows/implies that the tumor samples started to inactivate the tumor suppressor.

Next, the "Esteller" Heatmap includes even more methylation for the CLDN10 CGI than the "Heyn" Heatmap. Much more blue colors are observed throughout the Y-axis, which makes sense that highly proliferative cancer cells have more CLDN10 inactivated than the less proliferative tumor cells. By comparing the later "Esteller" Heatmap with "Lokk" and "Heyn" Heatmaps, one could see the gradual changes in the methylation tendency for the gene of interest during carcinogenesis.

![Methylation Heatmaps from Lokk, Heyn, and Esteller datasets](images/page-14.jpg)

**Figure 3-1:** The methylation Heatmaps from datasets "Lokk" (on the top), "Heyn" (in the middle) and "Esteller" (on the bottom)

A single Heatmap can be further categorized and compared by each cell type (by different tissues). With the example of "Lokk" Heatmap (normal cell), the following additional steps could be done after Step 5) to categorize per cell type:

Scroll down to the "Gene" table on the bottom of the Heatmap webpage. Select "a track" in Field "Order samples by" and "tissue (17 cat)" in Field "Ordering track" (in Figure 3-2). This allows the Heatmap to be organized by cell type.

![The table option on the Heatmap webpage](images/page-15.jpg)

**Figure 3-2:** The table option on the Heatmap webpage

Figure 3-3 is a categorized Heatmap by cell type. If a cursor is placed on the "tissue" label on the X-axis (above), a pop-up message shows the information regarding the annotations/tracks such as tissue type and gender of each sample. For example, Sample "gsm1215434" came from bladder tissue of a male as shown in Figure 3-3.

![Categorized Heatmaps by cell type from Lokk, Heyn, and Esteller](images/page-16.jpg)

**Figure 3-3:** Categorized Heatmaps by cell type from datasets "Lokk" (on the top), "Heyn" (in the middle) and "Esteller" (on the bottom)

---

## 4 Shortcut of Generating a Heatmap

The user could take the following steps as a shortcut to generate a heatmap:

**1)** To select "Esteller" dataset, repeat the Step 1) to Figure 2-3 in Step 2) in *Section 2 Generating Heatmap* of this manual. After following the steps login to the R2 Platform [1], choose "View all Met_ids for a Gene (Heatmap)" under Field 3 checkbox. Leave all other settings at their default and click "Next" on the main page to proceed (in Figure 4-1).

![Main menu](images/page-17.jpg)

**Figure 4-1:** Main menu

**2)** On the next webpage "View all reporters for a gene", the user could type a gene of interest to generate a Heatmap. As an example, "CLDN10" (Claudin 10) is written in Field {Gene} as shown in Figure 4-2. Click "Next" to execute a Heatmap.

**Figure 4-2:** "View all reporters for a gene" menu

**3)** Figure 2-11 shows the generated Heatmap. One could notice that the Heatmap in Figure 4-3 looks the same as the Heatmap in *Section 2 Generating Heatmap*.

![The Heatmap of the chosen dataset](images/page-18.jpg)

**Figure 4-3:** The Heatmap of the chosen dataset

The user could also generate a Heatmap by cell type from dataset "Esteller" like the Heatmap in *Section 3 Comparing Methylation Heatmaps*, with the following steps:

**4)** Repeat Step 1) as in Figure 4-1. On the website "View all reporters for a gene", type "CLDN10" (Claudin 10) in Field {Gene}. To create a Heatmap by cell type, select "a track" in the Field {Order samples by} and "primary_site (14 cat)" in the Field {Ordering track}. Click "Next" to execute a Heatmap by cell type (in Figure 4-4).

**Figure 4-4:** "View all reporters for a gene" menu

Figure 4-5 is a categorized Heatmap by cell type. This Figure is the same as the Heatmap from the dataset "Esteller" in Figure 3-1 in *Section 3 Comparing Methylation Heatmaps*.

![Categorized Heatmaps by cell type from dataset Esteller](images/page-19.jpg)

**Figure 4-5:** Categorized Heatmaps by cell type from dataset "Esteller"

---

## 5 Comparing Methylation Scatter Plots

The user could also compare the methylation level of the same probe from multiple datasets. In this section, the same three datasets as *Section 3 Comparing Methylation Heatmaps* are used ("Lokk": normal cells, "Heyn": tumor cells, "Esteller": cancer cells). The user takes the following steps to create the scatter plots of the same probe methylation dataset:

**5)** After login to the R2 Platform [1], choose "Across Datasets" under Field 1 checkbox. Leave all other settings at their default and click "Next" on the main page to proceed (in Figure 5-1).

![MegaSampler main menu](images/page-20.jpg)

**Figure 5-1:** Main menu

**6)** On the next webpage "MegaSampler", the user could change the settings in relation to the data type or preset/default (either in a global or in a group level) as shown in Figure 5-2. Select "hs, ilmnhm450, custom" on Field "Type of data" to see methylation datasets on the list of the next page. Leave other settings at their default and click "Next" to proceed.

**Figure 5-2:** "MegaSampler" menu

**7)** On the next webpage, type "CLDN10" in the Field "Gene / Reporter" and click "Select Datasets" button. (in Figure 5-3)

**Figure 5-3:** "MegaSampler" menu

**8)** On the pop-up box, type the author name "Lokk" (normal cells) on Column {Author} and select the datasets by clicking "Select". Repeat the same steps for the datasets with the author names "Heyn" (tumor cells) and "Esteller" (cancer cells) respectively. Click "Confirm selection" button to proceed (as shown in Figure 5-4).

![Data selection menu with Lokk, Heyn, Esteller](images/page-21.jpg)

**Figure 5-4:** Data selection menu with the author names "Lokk", "Heyn", "Esteller"

**9)** By previous Step 4), the user could see the data has reflected in the setting as shown in yellow in Figure 5-5. Type "CLDN10" in Field "Gene/Reporter" and choose "None" in Field "Transformation". Click "Next" button to proceed.

**Figure 5-5:** "MegaSampler" menu reflected the selected datasets

**10)** Choose one probe ("cg25032595" and "cg16556145" respectively) from the CGI observed in yellow in the three Heatmaps produced from *Section 3 Comparing Methylation Heatmaps*. As shown in Figure 4-6, the two probes are found in the "Esteller" heatmap as "cg16275739" is marked in blue and "cg18393747" is marked in red.

![Probe location in the Esteller Heatmap](images/page-22.jpg)

**Figure 5-6:** Probe location in the "Esteller" Heatmap

Select the first probe "cg25032595" as shown on the left in Figure 5-7. On "Adjustable settings" in Figure 5-8, the user could change the dataset order out of all selected datasets. Change the order the datasets: "Lokk" as "1", "Heyn" as "2" and "Esteller" as "3" (in Figure 5-8). This setting lets datasets be compared: "Lokk" as the first dataset, "Heyn" as the second dataset and "Esteller" as the third order. Click "Submit" button to proceed. Repeat the same process for the second probe "cg16556145" as shown on the right in Figure 5-7.

![Selected probe in Gene CLDN10 table](images/page-23.jpg)

**Figure 5-7:** Selected probe ("cg25032595" on the left, "cg16556145" on the right) in "Gene: CLDN10" table

**Figure 5-8:** "Adjustable settings" menu

As a result, the first methylation scatter plot from Dataset "Lokk", "Heyn" and "Esteller" of Probe "cg25032595" are generated as shown in Figure 5-9. As expected, the methylation level of "Lokk" for normal tissues (with the average 0.025) is lower than the methylation level of "Heyn" tumor cell lines (with the average 0.08). The methylation level of "Heyn" for tumor tissues is also lower than the methylation level of "Esteller" tumor cell lines (with the average 0.4). It should be noted that the name of Y-axes of the scatter plots in Figure 5-9 and Figure 5-10 is false. The Y-axis of the scatter plot is not "Expression" but "Methylation".

On "One Way Analysis of variance (ANOVA)" table, it is also observed that the p-value is significant enough as shown in red (in Figure 5-9).

![ANOVA table and methylation graphs of probe cg25032595](images/page-24.jpg)

**Figure 5-9:** ANOVA table and methylation graphs of the three datasets of Probe "cg25032595" (could be compared to expression plot Figure 7-5)

The second methylation scatter plot from the three datasets of Probe "cg16556145" are generated as shown in Figure 5-9. As expected, the methylation tendency from the normal to cancer cells is increasing as observed in the scatter plot in Figure 5-9. The methylation level "Lokk" for normal tissues (with the average 0.1) is lower than the methylation level of "Heyn" tumor cell lines (with the average 0.25). The methylation level of "Heyn" for tumor tissues is also lower than the methylation level of "Esteller" tumor cell lines (with the average 0.65).

On "One Way Analysis of variance (ANOVA)" table, it is also observed that the p-value is significant enough as shown in red (in Figure 5-10).

![ANOVA table and methylation graphs of probe cg16556145](images/page-25.jpg)

**Figure 5-10:** ANOVA table and methylation graphs of the three datasets of Probe "cg16556145" (could be compared to expression plot Figure 7-5)

The mean methylation difference of the two probes is shown more simply in another online methylation analysis tool named "Wanderer". [6] There is a methylation difference to be seen between normal and tumor cells from Probe "cg25032595" (marked in blue in Figure 5-11) than the gap from Probe "cg16556145" (marked in red in Figure 5-11).

**Figure 5-11:** Wanderer mean methylation graph of CLDN10 (probe set) of the normal and primary breast tumor ("TCGA" dataset)

---

## 6 An Expression Box Plot

A box plot (a.k.a. Open High Low Close graph) of a single expression dataset could be drawn to see the expression level by a cell type and for your gene of interest. The user takes the following steps to create a scatter plot of a single gene within an expression dataset:

**1)** Repeat the steps from 1) to 3) in *Section 2 Generating Heatmap* of this manual. But instead, choose the expression dataset by typing "Tissues GTeX v8 Prot_Coding" on Column {Tissue/Tumor} as shown in Figure 6-1.

![Change Dataset menu after filter](images/page-26.jpg)

**Figure 6-1:** Change Dataset menu (after filter)

**2)** Click on Link "CLDN10" under Field "CliniSnitch" which is located on the right of the webpage (in Figure 6-2).

**3)** A next webpage will be opened on a new internet tab. The user could see that the p-value is significant enough (where marked in red). Click on Link "tissue (View)" on Table "catvsnum" of the webpage (in Figure 6-3).

**4)** A next webpage will be opened on a new internet tab. To visualize and sort better, scroll down to Table "Adjustable settings". Select "Box plot" on Field "Graph type", "median (numeric Y)" on Field "Order Groups By" and "Color by Track" on Field "Color mode". Click "Submit" Button to update the scatter plot of a single expression data by a tissue type (in Figure 6-4).

![Adjustable settings table](images/page-27.jpg)

**Figure 6-4:** Table "Adjustable settings"

As a result, a scatter plot of the expression dataset "Tissues GTeX v8 Prot_Coding" shows the expression distribution of CLDN10 across primary tissues. The user can see tissue types like "salivary_gland", "pancreas" and "kidney" on the top right, which exhibit higher expression levels of Claudin10 on Figure 6-5.

![Expression log2 scatter plot of CLDN10 in normal tissues](images/page-28.jpg)

**Figure 6-5:** Expression log2 Scatter plot of CLDN10 in normal tissues dataset "Tissues GTeX v8 Prot_Coding"

---

## 7 Comparing Expression Scatter Plots

Now that we have studied methylation graphs, our scope is extended to the next topic, which is "**expression**" of our gene of interest across tissues/cancer types. Methylation and expression have a reciprocal relationship to each other. From the previous *Section 3 Comparing Methylation Heatmaps*, it was observed that the methylation levels increase for certain genes during carcinogenesis. On the contrary, the expression levels decrease. A comparative expression graph is a good tool to observe the difference in expression from different datasets. Here, datasets with author name "Roth" and "Broad" are used to plot the expression graphs. The platform user takes the following steps to create the expression graph:

**1)** Repeat the steps from 1) to 5) in *Section 4 Comparing Methylation Scatter Plots* of this manual for two datasets with author names "Roth" (normal cells, in Figure 7-2) and "Broad" (cancer cells, in Figure 7-3). But skip the change from Step 2) in *Section 4* and leave the table as defaults as shown in Figure 7-1.

![MegaSampler menu and data selection with Roth](images/page-29.jpg)

**Figure 7-1:** "MegaSampler" menu

**Figure 7-2:** Data selection menu with the author name "Roth"

![Data selection menu with Broad and adjustable settings](images/page-30.jpg)

**Figure 7-3:** Data selection menu with the author name "Broad"

**2)** On "Adjustable settings" in Figure 6-4, the user could change the dataset order out of two datasets. Change the order of the datasets: "Roth" as "1" and "Broad" as "2". This setting lets "Roth" as the first dataset compared to "Broad" as the second dataset. Click "Submit" button to proceed.

**Figure 7-4:** "Adjustable settings" menu

As a result, two expression graphs from Dataset "Roth" and "Broad" are generated as shown in Figure 7-5. As expected, the expression level of "Roth" for normal tissues (with the average 7-5) is higher than the expression level of "Broad" cancer cell lines (with the average 3-4). This is in line with methylation level from the two datasets, because the cancer cells ("Broad") are highly methylated compared to the normal cells ("Roth").

On "One Way Analysis of variance (ANOVA)" table, it is also observed that the p-value is significant enough as shown in red (in Figure 7-5).

![Expression comparison ANOVA table and graphs](images/page-31.jpg)

**Figure 7-5:** Expression comparison for CLDN10 in normal tissues and cancer cell lines as ANOVA table and expression graphs of the two datasets

---

## 8 Comparing Expression and Methylation Data

The user could also compare and correlate methylation and expression datasets by showing both in one plot. In this section, the datasets, "Garnett" (normal cells) and "Esteller" (cancer cells), are used. The user takes the following steps to create the dot plot of the methylation and the expression datasets:

**1)** After login to the R2 Platform [1], choose "Across Datasets" under Field 1 checkbox and "View a gene in two datatypes". Click "Next" on the main page to proceed (in Figure 8-1).

**2)** On Table "Select data sets to merge" of the next webpage, the user could set the data type and the X- and Y-axis of the dot plot. As shown in Figure 8-2, select "cellline_cancer_pharmaco" on Field "Data set collection", "Methylation data - Cell line Cancer Pharmacogenomic - Esteller - 1028 - custom - ilmnhm450" on Field "Source data" and "Expression data - Cell line Cancer Drug (Sanger) - Garnett - 1017 - RMA - u219" on Field "Target data". Click "Select data sets" to proceed.

![Main menu and select data sets to merge](images/page-32.jpg)

**Figure 8-1:** Main menu

**Figure 8-2:** "Select data sets to merge" menu

**3)** On Table "Adjustable settings" of the next webpage, type "CLDN10" in the left box of Field "Gene / Met_id" and "Gene / Reporter". The two probes from Step 6) on *Section 4 Comparing Methylation Scatter Plots* ("cg25032595", "cg16556145") are to be observed. To look at the dot plot of the first probe, type "cg25032595" in the right box of Field "Gene / Met_id" (in Figure 8-3).

![Adjustable settings menu for probe cg25032595](images/page-33.jpg)

**Figure 8-3:** "Adjustable settings" menu (for Probe "cg25032595")

As shown in Figure 8-4, the user can see the dot plot of the methylation dataset "Esteller" on the X-axis and the expression dataset "Garnett" on the Y-axis for the Probe "cg25032595". There is a significant correlation between the two axes (as p-value is marked in red under the table in Figure 8-4) supporting the idea of DNA hypermethylation decreasing gene expression.

**Figure 8-4:** The dot plot of Probe "cg25032595" (could be compared to Figure 8-6)

**4)** Repeat the steps from 1) to 3) of this section for the second Probe by typing "cg16556145" in the right box of Field "Gene / Met_id" (in Figure 8-5).

![Adjustable settings menu for probe cg16556145 and dot plot](images/page-34.jpg)

**Figure 8-5:** "Adjustable settings" menu (for Probe "cg16556145")

As shown in Figure 8-6, the dot plot for the Probe "cg16556145" is generated. With the significant correlation between the two axes, the concentration tendency of the most dots are the same as the tendency observed in Figure 8-4. One can observe a negative correlation between the methylation and the expression datasets.

**Figure 8-6:** Comparative log2 dot plot of CLDN10 methylation for probe "cg16556145" vs. CLDN10 expression

---

## 9 In-Depth Study on Expression Dataset

One could also take a closer look at expression of your gene of interest in certain tissues of the expression dataset on R2 Platform. From an expression box plot, a certain or several tissue types could be selected. In this section, the tissue type "skin" is further investigated with the following steps after the steps in *Section 6 An Expression Box Plot*.

**1)** Scroll down to "Adjustable settings" after the expression box plot is executed. Select "tissue (30 cat)" on Field "Subset track". On the pop-up window, click the tissue type "skin (1809)" checkbox and "OK". Click "Submit" to proceed. (In Figure 9-1)

![Adjustable settings menu with skin subset](images/page-35.jpg)

**Figure 9-1:** "Adjustable settings" menu

**2)** After the box plot on "skin" is executed, the user could further investigate expression level by skin types, such as differences in the expression between fibroblasts and normal skin types. On Table "Adjustable settings", select "tissue_detail (54 cat)" on Field "Track", "tissue_detail (54 cat)" on "Subset track", "Box/dot plot (dots)" on Field "Graph type" and "Color by Track" on Fields "Color mode/(groups)". "tissue_detail (54 cat)" is an in-depth category than the "tissue (30 cat)" category. (In Figure 9-2)

After selecting "tissue_detail (54 cat)" on Field "Subset track", the user sees the pop-up window. Click two skin types checkboxes ("cells_-_cultured_fibroblasts (504)" and "skin_-_not_sun_exposed_(suprapublic) (604)") and "OK" Button. Not-sun-exposed skin cells are chosen to reduce the impacting factor. Click "Submit" to proceed. (In Figure 9-3)

![Adjustable settings and pop-up window for tissue detail](images/page-36.jpg)

**Figure 9-2:** "Adjustable settings" menu

**Figure 9-3:** Pop-up window on "tissue_detail (54 cat)" subset track

The box plot with dots shown in Figure 9-4 shows the difference of expression levels between fibroblasts and normal skin. Normal skin not exposed to the sun has a higher expression level, compared to the expression level of fibroblasts. (Be reminded that the Y-Axis name is log2 CLDN10 expression.)

![Expression box dot plot fibroblasts vs skin](images/page-37.jpg)

**Figure 9-4:** Expression log2 Box/dot plot (dots) on fibroblasts and not-sun-exposed skin cells for CLDN10

---

## 10 Comparing Survival Probability

One could also investigate patient survival probability of a certain tumor type/entity in comparison to the expression for your gene of interest using the R2 Platform. In this section, the "TCGA" dataset is used as an example because it contains several general cancer types (including normal control tissues) and is relatively big.

**1)** Click "Survival (Kaplan-Meier/Cox)" on the left menu of the main page. On Table "Kaplan-Meier analysis using a data set", select Field "Data set" as shown in Figure 10-1.

**2)** On the pop-up box (in Figure 10-2), type "Kidney" on Column {Tissue/Tumor} and select "Kidney Renal Clear Cell Carcinoma" from "tcgars" on Column {Platform}. Click "Confirm selection" button as shown in Figure 10-2.

![Survival main page and change dataset menu](images/page-38.jpg)

**Figure 10-1:** "Survival (Kaplan-Meier/Cox)" main page

**Figure 10-2:** Change Dataset menu (after filter)

**3)** Select "a single gene" on Field "Separated by" and click "Next" on the main page to proceed. (in Figure 10-3)

The result on the next page shows the overall survival probability between patients with high gene of interest expression and low expression (on the left in Figure 10-4) and expression levels with p-values (on the right in Figure 10-4).

When the automated separation of patients by expression level produced one big and one small cohort, it should be taken into account that results could be significant, but still not biologically relevant. Further studies should be performed, in order to better understand the contribution of your gene of interest in patient survival. Even though the p-values are significant (statistically valid), the dataset might not be biologically valid as well.

The left graph in Figure 10-4 shows the overall survival probability of two cohorts (on an Y-axis) that are high expression (a line marked in blue) and low expression (a line marked in red) groups, regarding the expression of the gene of interest. An X-axis is the follow-up in months. The total patient number of the cohorts are shown with colors on the right top of the graph ("n=430", "n=103" respectively). One could find out individual information of each sample by putting the cursor on the line (in Figure 10-5).

![Kaplan-Meier table and overall survival probability graph](images/page-39.jpg)

**Figure 10-3:** "Kaplan-Meier analysis using a data set" Table on main page

**Figure 10-4:** "Overall survival probability graph" and "Expression graph"

![Individual information pop-up in survival graph](images/page-40.jpg)

**Figure 10-5:** Individual information pop-up in "Overall survival probability graph"

The right graph in Figure 10-4 shows the expression level by "Events" groups. An Y-axis shows the expression level and an X-axis shows the p-values of each sample. The bar graph on the X-axis shows the p-value of each sample. The dots in green on the curve indicate the samples with the "Events" and the dots in red are the samples with no "Events". The definition of the "Events" is different by datasets. These "Events" could be for example relapse free or not (Relapse free means that the patients after primary treatment survived a certain period of time without any symptoms of the cancer). More information on the "Events" dataset label could be found on R2 Platform online tutorial under "Special sample annotation" in *Section 24. R2 Dataset Addition*. [2]

Some adjustments are to be made as the survival probability until 60 follow-up months (or 5 years) is more common (on the left graph in Figure 10-4). The expression graph (on the right graph in Figure 10-4) could be also shifted (or cut) by filtering the range with the significant p-values. This could be done by the following steps.

**4)** Scroll down to "Adjustable settings" after two graphs are executed. Type "60" months on Field "Only draw up to". Click "Redraw Graph" to proceed. (In Figure 10-6)

![Adjustable settings table for survival graph](images/page-41.jpg)

**Figure 10-6:** "Adjustable settings" Table

Figure 10-7 shows the redrawn "Overall survival probability graph" and the range of the X-axis is adjusted to 60 months (marked in yellow in Figure 10-7). The graph became better to compare the difference between the normal people and cancer patients, as the tails of the two lines in the graph on the right are cut.

**Figure 10-7:** "Overall survival probability graph" (after adjustment)

Next, a cutoff point on the "Expression graph" (the right graph in Figure 10-4) could be adjusted on Field "Cutoff" in "Adjustable settings" Table. The cutoff point is set with the highest p-value at default. To change the cutoff point, the following step is to be done.

**5)** Select any data sample which has the high local p-value ("387 - 819.7227: raw p: 0.015 (bonf: 1.000)" in Figure 10-8) on Field "Cutoff" in "Adjustable settings" Table. Type "60" months on Field "Only draw up to" in the same table. Click "Redraw Graph" to proceed. (In Figure 10-8)

![Adjustable settings and adjusted survival probability graph](images/page-42.jpg)

**Figure 10-8:** "Adjustable settings" Table

The result of Step 5 is described in Figure 10-9. The overall survival probability (on the left) has a smaller difference between the two lines compared to the previous graph that was drawn with the highest p-value.

**Figure 10-9:** "Overall survival probability graph" and "Expression graph" (after adjustment)

---

## 11 Hypermethylation Between Datasets (private data, not yet published)

As Hypermethylation is an indicator of tumor development, hypermethylated regions on Heatmaps could be compared between two datasets of normal and tumor patients. The dataset with the tumor type "renal cell carcinoma (PTM)" and the author name "Richter" is used for this analysis.

**1)** Click "Main" on the left menu of the main page. On Table, select "Differential expression between two groups" in Field 3. Click the option box in Field 2 for data selection. (In Figure 11-1)

**2)** On the pop-up box, type the author name "Richter" on Column {Author} and select the dataset with "Renal cell carcinoma (PTM)" on Column {Tissue/Tumor} by clicking the row. Click "Confirm selection" button to proceed (In Figure 11-2). Click "Next" on main menu to proceed. (In Figure 11-3).

![Main page and data selection menu with Richter](images/page-43.jpg)

**Figure 11-1:** Main page

**Figure 11-2:** Data selection menu with the author name "Richter" and the tumor type "Renal cell carcinoma (PTM)"

**3)** On "Select a test" Table, select "type (2 cat)" in Field "Group by" and "n10nvst (3 cat)" in Field "Subset track". Then on the pop-up menu, click the check buttons of "normal (5)" and "tumor (5)" samples except 2 outliers ("ND (2)"). Click "OK" button to finish the sample choice. Click "Submit" on the table to proceed. (In Figure 11-4)

**4)** On "Adjustable settings" Table, select "n (6)" as normal people in Field "Group 1" and "tm (6)" as tumor patients in Field "Group 2". Click "Submit" to proceed. (In Figure 11-5)

![Main menu, select a test table, and adjustable settings](images/page-44.jpg)

**Figure 11-3:** Main menu

**Figure 11-4:** "Select a test" Table

**5)** At the right menu click "Heatmap(zscore)" to proceed. (In Figure 11-6)

![Adjustable settings and heatmap zscore button](images/page-45.jpg)

**Figure 11-5:** "Adjustable settings" Table

**Figure 11-6:** "Heatmap(zscore)" Button on the right menu

The next page shows the heatmap of hypermethylation between two datasets (normal people and tumor patients).

![Heatmap zscore title](images/page-46.jpg)

**Figure 11-7:** "Heatmap(zscore)" Title

"zscore" or the standard score is "a statistical measure that represents the number of standard deviations an individual data point is from the mean of a dataset. It indicates how far a particular data point deviates from the average in terms of standard deviation units." [7] And "fdr" stands for False Discovery Rate and is "a statistical concept used in multiple hypothesis testing to control for the proportion of false discoveries or false positives." [7]

On the right of the heatmap, the colored block lines show the type of data points. The enlarged versions are shown in Figure 11-8. The red blocks of "n10nvst" are the data points of the tumor patients and the green blocks of "n10nvst" are the data points of the normal people. One could see the details of a certain data point by placing a cursor on the "n10nvst" block. On the pop-up message shows the type of the data point (marked in red) (in Figure 11-8).

With this background knowledge, the positive score on the heatmap (in Figure 11-9) is colored in yellow and the negative score in blue. The positive score shows the data point above the mean and the negative below the mean of the datasets. All tumor patients have reciprocal behavior of all normal people, as observed in the color difference in the heatmap (yellow heatmap area for tumor patients are blue heatmap area for normal people).

![Enlarged heatmap zscore with tumor and normal data points](images/page-47.jpg)

**Figure 11-8:** Enlarged "Heatmap(zscore)": tumor patient data point (in red) and normal data point (in green)

![Heatmap zscore rotated to horizontal](images/page-48.jpg)

**Figure 11-9:** "Heatmap(zscore)" - rotated to horizontal for convenience

When the cursor is placed on Gene type axis, a pop-up message containing the gene name, the probe name and the order number (gene name="CLDN10", probe name="cg16275739", order number="581" on the pop-up message in Figure 11-10). The order number can be found from the table "Sort Order Listing" after clicking it as shown in Figure 11-10. One can investigate the difference in a certain gene's expression in this way.

![Heatmap zscore and sort order listing table](images/page-49.jpg)

**Figure 11-10:** "Heatmap(zscore)" and "Sort Order Listing" Table

---

## 12 Appendix

### 12.1 Finding a Gene Name of Interest

If a gene name of Interest is uncertain, this could be found by using the methylation ID obtained via UCSC Genome Browser. A methylation ID represents a probe name.

For example, assume that a gene of interest is "Insulin". By following Step 3) under *Section 2. Generating a Heatmap* with a gene name as "INS", there are several choices listed below {Gene} Field on the Adjustable settings menu (in Figure 12.1-1). One could address the exact gene name of interest using a methylation ID (i.e. "Met-ID"; for example, "cg20278383" for a gene name "CLDN10") obtained from UCSC Genome Browser and select the right gene name of interest from the choices listed in Figure 12.1-1. The following describes the steps of search on UCSC Genome Browser for each solution, respectively.

Firstly, enter UCSC Genome Browser (https://genome.ucsc.edu/). Click "Human GRCh37/hg19" on the "Genomes" menu of the main page as shown in Figure 12.1-2.

![Choices for gene of interest Insulin and UCSC main page](images/page-48.jpg)

**Figure 12.1-1:** Choices for a gene of interest "Insulin"

**Figure 12.1-2:** UCSC Genome Browser main page

#### (a) Search a Methylation ID using a sequence

If a sequence for a gene of interest is known, one may still use the sequence to begin the search as a guide. As an example, assume that "Insulin" is a gene of interest and a sequence for the certain region of this gene of interest is known as "TTAAGACTCTAATGACCCGCTGGTCCTGAGGAAGAG".

**1)** Click "Blat" on the "Tools" menu on the UCSC Genome Browser main page (in Figure 12.1-3).

**2)** Write the sequence "TTAAGACTCTAATGACCCGCTGGTCCTGAGGAAGAG" in the input box and click "submit" to proceed (in Figure 12.1-4).

**3)** On the next page, the sequence candidates are listed as the search results. Click one of the most relevant "browser" links to one's interest from the listed results (in Figure 12.1-5).

![UCSC tools menu and BLAT search](images/page-49.jpg)

**Figure 12.1-3:** UCSC Genome Browser main page

**Figure 12.1-4:** Human Blat Search page

**4)** The next page is Genome Browser page that one could observe the genome region. Scroll down and select "show" for "CpG Islands" and for "ENC DNA Methyl" Options in "Regulation" Field. Click "refresh" to apply the modifications on the Genome Browser (in Figure 12.1-6).

**5)** One could now see the corresponding methylation IDs on the Genome Browser page. If the methylation IDs are not observed on the page, adjust the genome region using "zoom in" or "zoom out" buttons on the top of the page (in Figure 12.1-7).

![BLAT search results and regulation field](images/page-50.jpg)

**Figure 12.1-5:** Blat Search Results page

**Figure 12.1-6:** "Regulation" Field

![Methylation IDs on UCSC Genome Browser page](images/page-51.jpg)

**Figure 12.1-7:** Methylation IDs on UCSC Genome Browser page

**6)** Now, return to the Adjustable settings menu on R2 Genomics Analysis and Visualization Platform (https://r2.amc.nl/) (in Figure 12.1-1). Write the observed methylation ID "cg03366382" observed from the previous Step 5) in {Met_id} Field on Adjustable settings menu. Click the listed option below {Met_id} Field (in Figure 12.1-8). The exact gene name of interest is automatically written in {Gene} Field (in Figure 12.1-9).

**Figure 12.1-8:** Adjustable settings menu on R2 Platform

![Adjustable settings menu on R2 Platform](images/page-52.jpg)

**Figure 12.1-9:** Adjustable settings menu on R2 Platform

#### (b) Search a Methylation ID using an uncertain gene name of interest

Now that a search for a methylation ID using a sequence is possible from the Steps in *(a) Search a Methylation ID using a sequence*. On the other hand, if a sequence is also unknown for a gene of interest, one could begin the search using an uncertain gene name of interest on UCSC Genome Browser.

**1)** Write "INS" as a guess for this gene name of interest in {Gene} Field on UCSC Human GRCh37/hg19 Genome Browser. Click the relevant one from the listed choices below {Gene} Field to proceed (in Figure 12.1-10). If one is uncertain what is relevant, press "Enter".

**Figure 12.1-10:** UCSC Human GRCh37/hg19 Genome Browser page

**2)** If you just pressed "Enter" on the previous Step 1), all search results of a gene "Insulin" are listed with more information. Click the relevant gene option (or just the first option "INS-IGF2 (uc001lvm.3)" as a tryout) to proceed (in Figure 12.1-11).

![UCSC genome browser search page results](images/page-53.jpg)

**Figure 12.1-11:** Search Results on hg19 for "Insulin"

**3)** On the next page, all methylation IDs for "INS-IGF2 (uc001lvm.3)" are listed on the Genome Browser page. If the methylation IDs are not shown at first glance, scroll down or adjust the options below the page as described in Figure 12.1-6. Click the relevant methylation ID (or just the spotted methylation ID "cg02343602" as a tryout) (in Figure 12.1-12).

![Methylation IDs on genome browser page](images/page-54.jpg)

**Figure 12.1-12:** Methylation IDs on UCSC Genome Browser page

If one wishes to double-check its choice by looking at the DNA sequence for this methylation ID, the following steps could be done.

**4)** On the next page, the information on the spotted methylation ID "cg02343602" is provided. Click "View DNA for this feature" link (in Figure 12.1-13).

**5)** As an example, click "One FASTA record per region" Option under "Sequence Retrieval Region Options". Define a range as "20" for an up- and a downstream (in Figure 12.1-14).

![Methylation ID info page and DNA sequence extraction page](images/page-55.jpg)

**Figure 12.1-13:** Information page on the methylation ID

**Figure 12.1-14:** DNA sequence extraction page

**6)** The corresponding DNA sequences on the defined region are shown as Figure 12.1-15. One could check if the sequence is aligned with known information.

![DNA sequences on the defined region](images/page-56.jpg)

**Figure 12.1-15:** DNA sequences on the define region

---

## 13 References

[1] J. Koster, Amsterdam University Medical Centers (AUMC), Center for Experimental and Molecular Medicine (CEMM) - R2 Genomics Analysis and Visualization Platform, https://r2.amc.nl. retrieved on 24.04.2023

[2] R2 support team - R2 Tutorials, https://r2-tutorials.readthedocs.io/en/latest/. updated on 13.04.2023

[3] Mind map on the "Manual on R2 Platform for Methylation Analysis (by Ji Sun Kwon)" - Miro, https://miro.com/app/board/uXjVMMBYyDQ=/. updated on 04.05.2023

[4] Groll/Nitaj et al., in prep. - Epigenetic inactivation of CLDN10 in Malignant melanoma and its epigenetic reactivation counteracts tumor progression; Manuscript in preparation.

[5] V. Deutschmeyer/J. Breuer et al. - Epigenetic therapy of novel tumour suppressor ZAR1 and its cancer biomarker function, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6894338/. published on 04.12.2019

[6] I. Mallona. - Wanderer, an interactive viewer to explore DNA methylation and gene expression data in human cancer, http://maplab.imppc.org/wanderer/. published on 2015

[7] Chat GPT, keywords as "what is zscore?" and "what is fdr in statistics?", https://chat.openai.com/. retrieved on 27.06.2023
