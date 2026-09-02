<a id="Methylation_analysis"> </a>


Manual on R2 Platform for Methylation Analysis
=================================

*An Introduction on R2 Genomics Analysis and Visualization Platform Usage*

By Ji Sun (Klara) Kwon
Supervision: Dr. Antje Richter
Justus-Liebig University Giessen (JLU)
Institute for Genetics and Institute for Bioinformatics
Heinrich-Buff Ring 58, 35392 Giessen, Germany



Introduction
---

This manual is intended for scientists and students who wish to study DNA methylation, and its purpose is to provide instructions on how to analyze methylation data using the R2 Genomics Analysis and Visualization Platform, also known as the R2 Platform. Additionally, an online tutorial on the R2 Platform is available on the official website to learn about other features. The following mind map aids in understanding the structure of the manual and the relationships between its sections.

![](_static/images/Methylation/fig1-1.png)

[**Figure 1-1: Structure of the R2 Platform manual and the relationships between its section**](_static/images/Methylation/fig1-1.png)

## 2 Generating a Heatmap

For analysis of the human methylome in order to study the potential tumor suppressors, we are using the R2 platform and the methylome datasets available in R2. R2 hosts many methylome datasets generated on Illumina platforms, including the 450K, EPIC, and EPIC v2 arrays, which are bisulfite treatment based. It determines methylated versus unmethylated DNA target regions using probes (oligonucleotides). For each region, a Heatmap is a useful tool for observing the methylation status of individual probes and how isoforms cluster according to their degree of methylation.

As an example for this manual, the first exercise will show how to generate a Heatmap with an Illumina methylation array dataset on R2. This dataset belongs to a study that is called "A Landscape of Pharmacogenomic Interactions in Cancer" and can be found in R2 as a "cell line" dataset by the author name **Esteller**.  
Also, this dataset shows what the Heatmap looks like for highly proliferating cancer samples. Later, in *Section 3 Comparing Methylation Heatmaps*, the Heatmap from this example will be compared with two other examples from different datasets. The tutorial's scope will then be expanded to more complex use cases, such as a tutorial on the "Expression" dataset.

With the above dataset information, the platform user takes the following steps to create the Heatmap:

**1)** After login to the R2 Platform [1], click the text box under Field 2 "Select a dataset for analysis" (in Figure 2-1).

![](_static/images/Methylation/fig2-1a.png)

[**Figure 2-1: Click in box 2 to change the dataset**](_static/images/Methylation/fig1-1.jpg)



**2)** On the pop-up grid box (in Figure 2-2), click in Column {Category} on "Select Filter" to uncheck "Select all" and only select "cell line". In the text field of Column {Tissue/Tumor}, type "cancer pharmacogenomic"  or type "Esteller" in Column {Author}. One can confirm the right dataset by referring the description table below as shown in Figure 2-2. When the dataset is found, click anywhere on the row of the dataset and click "Confirm selection". (in Figure 2-3) Leave all other settings at their default and click "Next" on the main page to proceed. (in Figure 2-4)

![Change Dataset menu](_static/images/Methylation/fig2-2.jpg)

[**Figure 2-2: Search and select a dataset in the grid**](_static/images/Methylation/fig2-2.jpg)



![](_static/images/Methylation/fig2-3.jpg)

[**Figure 2-3: Select and confirm**](_static/images/Methylation/fig2-3.jpg)

![](_static/images/Methylation/fig2-4a.png)

[**Figure 2-4: Main menu (with selected dataset)**](_static/images/Methylation/fig2-4a.png)



**3)** The next page is "View a gene" that narrows down to the specific gene or methylation ID which to be shown in a Heatmap. (in Figure 2-5) As an example, "CLDN10" (Claudin 10) is written in Field {Gene / Met_id }, and the suggested Met_id that pops up is selected by a mouse click. CLDN10 is a candidate tumor suppressor currently being studied in our lab [4] and strongly hypermethylated across cancer types. For your purposes please use the name/abbreviation of your candidate gene of choice and select a Met_id by mouse that pops up. Click "Submit" to generate a YY-plot. 

![](_static/images/Methylation/fig2-5.png)

[**Figure 2-5: Adjustable settings menu on the dataset**](_static/images/Methylation/fig2-5.png)


In case that a gene name of interest is uncertain, one can find the exact gene name of interest by a methylation ID obtained from UCSC Genome Browser. This search process is described in *Appendix 12.1 Finding a Gene of Interest* of this manual.

A linear graph is generated as the following graph with an X-axis with samples (probes) and a Y-axis as CLDN10 methylation. (in Figure 2-6) Each sample (a.k.a. cell line type, on the X-axis) is ordered by its degree of CLDN10 methylation (on the Y-axis).

![](_static/images/Methylation/fig2-6.jpg)

[**Figure 2-6: Graph on the probes of the chosen CLDN10 dataset**](_static/images/Methylation/fig2-6.jpg)


Two additional features on this webpage come in handy: By clicking on the exclamation mark right in the graph title (marked in red in Figure 2-6), the user could see the description of the dataset as in Figure 2-7. Next, if the user wants to grasp the basic knowledge on biological or medical terminologies, one could click on the GeneID table link (marked in red in Figure 2-6) and read the definition of the terminologies on the National Library of Medicine (NIM) website. (in Figure 2-8)

![](_static/images/Methylation/fig2-7.jpg)

[**Figure 2-7: Description of the chosen dataset**](_static/images/Methylation/fig2-7.jpg)


![](_static/images/Methylation/fig2-8.jpg)

[**Figure 2-8: Definition of terminology "CLDN10" on the National Library of Medicine (NLM) website**](_static/images/Methylation/fig2-8.jpg)


**4)** As a next step, click on "View additional details" on the same page below the previous line graph. (in Figure 2-9) Then by clicking "view all" link as shown in Figure 2-10, the embedded Heatmap and R2 Genome Browser of the chosen dataset will open in a new screen.

![](_static/images/Methylation/fig2-9a.png)

[**Figure 2-9: View additional details" (clickable)**](_static/images/Methylation/fig2-9a.png)



![](_static/images/Methylation/fig2-10.jpg)

[**Figure 2-10: View all reporters details**](_static/images/Methylation/fig2-10.jpg)



**5)** Figure 2-11 shows the generated Heatmap. The **Heatmap** describes where each subset (probe) of the gene is methylated or not. The X-axis of the Heatmap indicates "primary histology" (or cell line type) and the Y-axis indicates all probes of the chosen gene of interest annotated within the dataset. The methylation score is colored by yellow (near to score 0, unmethylated), black in the middle (partially methylated, 50%), and blue (near to score 1, fully methylated). As shown in Figure 2-11, each probe per cell line type has a different tendency of methylation region.

For example, a kidney cell line is shown as green above the Heatmap. The vertical tendency from the green color (a kidney cell) on the X-axis extended towards the bottom shows how probes on the kidney cell are differently methylated. The user could see on this vertical tendency that probe "cg13733394" is unmethylated as in yellow, compared to probe "cg18470456" in blue which is methylated.

![](_static/images/Methylation/fig2-11a.png)

[**Figure 2-11:** The Heatmap of the chosen dataset**](_static/images/Methylation/fig2-11a.png)


If the user is interested in looking into a table of each sample (probe) and gene name of the dataset. Go to the page where the YY-plot is generated and click view datatable (in Figure 2-12)

![](_static/images/Methylation/fig2-12a.png)

[**Figure 2-12: The table of sample and reporter names of the chosen dataset**](_static/images/Methylation/fig2-12a.png)



**6)** Below the heatmap, the average ratio for each probe is depicted against their location on the genome. Clicking on the blue view....Genomebrowser link will open an interactive view of the same location on the genome as shown in Figure 2-13. The R2 Genome Browser relates the probes on the Y-axis of the Heatmap showing as two isoforms. The user could see Isoform A on the left side and Isoform B on the right side of the bar from R2 Genome Browser. The name of a certain probe could be seen or matched between the Heatmap and R2 Genome Browser by placing a cursor on that probe. Depending on the dataset, only one isoform or more isoforms can exist.

The colored vertical line just below the diagram title represents the chromosome of this database and shows the gene position in the chromosome by a small vertical line (marked in yellow in Figure 2-13).

Then R2 Genome Browser shows the average (mean) CpG by methylation score (on an Y-axis) and the gene (a.k.a. gene position number, on an X-axis). The dots in this diagram are CpG (or probe) and their according methylation degree. It is to be noted that the Y-axis of R2 Genome Browser is the methylation score per probe, whereas the X-axis of Heatmap is the methylation score (which is vice versa).

The standard deviation of methylation per CpG is shown with the vertical gray line in the diagram, which is located in the gene index around 96,160,000. The letter "q" (queue) from the X-axis label "q32.1" reveals that the gene is located on the chromosome's long arm. If it is located on the small arm of the chromosome it is labeled with "p" (petite).

Below the diagram, there are two green sticks called "CLDN10" labeled on the left and one red stick called "CLDN10-AS1" labeled on the right. The green sticks represent Isoform A and the red stick represents an antisense isoform. The B isoform is shown on the right side. Depending on the dataset, multiple isoforms more than two (A and B) could exist. More details regarding R2 Genome Browser could be found on R2 Platform online tutorial under Section 17. Using the R2-Genome browser. [2]

![](_static/images/Methylation/fig2-13b.png "Figure 2-13")

[**Figure 2-13: R2 Genome Browser with mean methylation score by gene index**](_static/images/Methylation/fig2-13b.png)

Now, if the user is interested in investigating certain probes from the dataset, the next steps could be done additionally. (marked in red in Figure 2-13)

**6-1)** When a cursor is placed on one of the probes, a pop-up message shows the information regarding the selected probe. ("ilmnhm450" in Figure 2-13).  Filtering by the information on pop-up messages, three CpGs within the promoter of the gene and isoform of interest are selected ("cg08418978", "cg22122715" at the left purple arrow, "cg25032595" at the blue arrow) by clicking the check-boxes on "Select reporters" table. As shown with marked color-arrows in Figure 2-13, the probes are observed both as a dot and as a block. Click "Next" to proceed.

**6-2)** Figure 2-14 shows the updated Heatmap and R2 Genome Browser after the previous step (Step 6-1). The user could investigate the methylation tendency of the three probes. Back to the example of "kidney" cell type (indicated in green on the X-axis "primary_histology" of Heatmap), the user sees two probes ("cg08418978", "cg22122715"; yellow in Heatmap) are unmethylated but Probe "cg25032595" (blue in Heatmap) is methylated.

![](_static/images/Methylation/fig2-14.jpg)

[**Figure 2-14: The updated Heatmap and R2 Genome Browser of the chosen dataset for a subset of CpG probes chosen**](_static/images/Methylation/fig2-14.jpg)



### Update: quick access to methylation heatmaps in R2

- click view a gene
- click view all Met_ids
- click next

![](_static/images/Methylation/fig-quickaccess-1.jpg)

[**Figure 2-15: Quick access step 1**](_static/images/Methylation/fig-quickaccess-1.jpg)



- chose your gene of interest in 'Gene' and click next

![](_static/images/Methylation/fig-quickaccess-2.jpg)

[**Figure 2-16: Quick access step 2**](_static/images/Methylation/fig-quickaccess-2.jpg)



- chose your gene of interest in 'Gene' and click next


- wait and heatmap is produced from all CpGs assigned to your Gene of interest

![](_static/images/Methylation/fig2-17.png)

[**Figure 2-17: Quick access step 3 - resulting heatmap**](_static/images/Methylation/fig2-17.png)





---

## 3 Comparing Methylation Heatmaps

To grasp a better idea how to interpret this Heatmap, two further methylation/Methylome datasets will be compared with the "Esteller" dataset. As mentioned earlier in *Section 2 Generating Heatmap* of this manual, this "Esteller" dataset is based on highly proliferating cancer cell lines. The second dataset is based on primary tumors ("tumor" type by the author name "Heyn" on R2 Platform). The third dataset is based on normal control tissue samples ("normal" type by the author name "Lokk" on R2 Platform). In this section, three Heatmaps generated from these three datasets are to be compared to show the difference in methylation tendency for a chosen gene of interest. These comparative methylome heatmaps were used to study another tumor suppressor ZAR1. [5]

To create the second ("Heyn") and the third ("Lokk") datasets, repeat the steps from 1) to 5) in *Section 2 Generating Heatmap* of this manual. The following Figure 3-1 is the generated Heatmaps of the three datasets ("Esteller" on the bottom, "Heyn" in the middle, "Lokk" on the top). As shown with colors in Figure 3-1, the "Lokk" Heatmap of CLDN10 is rather uniform with an CLDN10 CGI (or CpG-Island) that is unmethylated, whereas the CGI surrounding regions are methylated (for all samples).

When looking at the Heatmap from primary tumors "Heyn", some degree of methylation appears across the CLDN10 CGI (the entire black and blue colors throughout the Y-axis). This methylation shows/implies that the tumor samples started to inactivate the tumor suppressor.

Next, the "Esteller" Heatmap includes even more methylation for the CLDN10 CGI than the "Heyn" Heatmap. Much more blue colors are observed throughout the Y-axis, which makes sense that highly proliferative cancer cells have more CLDN10 inactivated than the less proliferative tumor cells. By comparing the later "Esteller" Heatmap with "Lokk" and "Heyn" Heatmaps, one could see the gradual changes in the methylation tendency for the gene of interest during carcinogenesis.

![](_static/images/Methylation/fig3-1.jpg)

[**Figure 3-1: The methylation Heatmaps from datasets "Lokk" (on the top), "Heyn" (in the middle) and "Esteller" (on the bottom)**](_static/images/Methylation/fig3-1.jpg)


A single Heatmap can be further categorized and compared by each cell type (by different tissues). With the example of "Lokk" Heatmap (normal cell), the following additional steps could be done after Step 5) to categorize per cell type:

Scroll down to the "Gene" table on the bottom of the Heatmap webpage. Select "a track" in Field "Order samples by" and "tissue (17 cat)" in Field "Ordering track" (in Figure 3-2). This allows the Heatmap to be organized by cell type.

![](_static/images/Methylation/fig3-2.jpg)
[**Figure 3-2: The table option on the Heatmap webpage**](_static/images/Methylation/fig3-2.jpg)


Figure 3-3 is a categorized Heatmap by cell type. If a cursor is placed on the "tissue" label on the X-axis (above), a pop-up message shows the information regarding the annotations/tracks such as tissue type and gender of each sample. For example, Sample "gsm1215434" came from bladder tissue of a male as shown in Figure 3-3.

![](_static/images/Methylation/fig3-3a1.png)
[**Figure 3-3a1: Categorized heatmap - Lokk normal tissues by tissue type**](_static/images/Methylation/fig3-3a1.png)


![](_static/images/Methylation/fig3-3b1.png)
[**Figure 3-3a2: Categorized heatmap - Heyn Tumor types**](_static/images/Methylation/fig3-3b1.png)

![](_static/images/Methylation/fig3-3c1.png)
[**Figure 3-3: Esteller cell line cancer**](_static/images/Methylation/fig3-3c1.png)


---

## 4 Shortcut of Generating a Heatmap

The user could take the following steps as a shortcut to generate a heatmap:

**1)** To select "Esteller" dataset, repeat the Step 1) to Figure 2-3 in Step 2) in *Section 2 Generating Heatmap* of this manual. After following the steps login to the R2 Platform [1], choose "View all Met_ids for a Gene (Heatmap)" under Field 3 checkbox. Leave all other settings at their default and click "Next" on the main page to proceed (in Figure 4-1).

![](_static/images/Methylation/fig4-1.png)
[***Figure 4-1:** Main menu**](_static/images/Methylation/fig4-1.png)


**2)** On the next webpage "View all reporters for a gene", the user could type a gene of interest to generate a Heatmap. As an example, "CLDN10" (Claudin 10) is written in Field {Gene} as shown in Figure 4-2. Click "Next" to execute a Heatmap.

![](_static/images/Methylation/fig4-2.jpg)

[**Figure 4-2: "View all reporters for a gene" menu**](_static/images/Methylation/fig4-2.jpg)


**3)** Figure 2-11 shows the generated Heatmap. One could notice that the Heatmap in Figure 4-3 looks the same as the Heatmap in *Section 2 Generating Heatmap*.

![](_static/images/Methylation/fig4-3.jpg)
[**Figure 4-3: The Heatmap of the chosen dataset**](_static/images/Methylation/fig4-3.jpg)


-The user could also generate a Heatmap by cell type from dataset "Esteller" like the Heatmap in *Section 3 Comparing Methylation Heatmaps*, with the following steps:

**4)** Repeat Step 1) as in Figure 4-1. On the website "View all reporters for a gene", type "CLDN10" (Claudin 10) in Field {Gene}. To create a Heatmap by cell type, select "a track" in the Field {Order samples by} and "primary_site (14 cat)" in the Field {Ordering track}. Click "Next" to execute a Heatmap by cell type (in Figure 4-4).

![](_static/images/Methylation/fig4-4.jpg)
[**Figure 4-4: "View all reporters for a gene" menu**](_static/images/Methylation/fig4-4.jpg)


Figure 4-5 is a categorized Heatmap by cell type. This Figure is the same as the Heatmap from the dataset "Esteller" in Figure 3-1 in *Section 3 Comparing Methylation Heatmaps*.

![](_static/images/Methylation/fig4-5.jpg)

[**Figure 4-5: Categorized Heatmaps by cell type from dataset "Esteller"**](_static/images/Methylation/fig4-5.jpg)



---

## 5 Comparing Methylation Scatter Plots

The user could also compare the methylation level of the same probe from multiple datasets. In this section, the same three datasets as *Section 3 Comparing Methylation Heatmaps* are used ("Lokk": normal cells, "Heyn": tumor cells, "Esteller": cancer cells). The user takes the following steps to create the scatter plots of the same probe methylation dataset:

**5)** After login to the R2 Platform [1], choose "Across Datasets" under Field 1 checkbox. Leave all other settings at their default and click "Next" on the main page to proceed (in Figure 5-1).

![Main menu](_static/images/Methylation/fig5-1.png)
[****Figure 5-1: Main menu**](_static/images/Methylation/fig5-1.png)



**6)** On the next webpage "MegaSampler", the user could change the settings in relation to the data type or preset/default (either in a global or in a group level) as shown in Figure 5-2. Select "hs, ilmnhm450, custom" on Field "Type of data" to see methylation datasets on the list of the next page. Leave other settings at their default and click "Next" to proceed.

![](_static/images/Methylation/fig5-2.jpg)
[**Figure 5-2: "MegaSampler" menu**](_static/images/Methylation/fig5-2.jpg)


**7)** On the next webpage, type "CLDN10" in the Field "Gene / Reporter" and click "Select Datasets" button. (in Figure 5-3)
[](_static/images/Methylation/fig5-3.jpg)
[**Figure 5-3:  "MegaSampler" menu**](_static/images/Methylation/fig5-3.jpg)



**8)** On the pop-up box, type the author name "Lokk" (normal cells) on Column {Author} and select the datasets by clicking "Select". Repeat the same steps for the datasets with the author names "Heyn" (tumor cells) and "Esteller" (cancer cells) respectively. Click "Confirm selection" button to proceed (as shown in Figure 5-4).

![](_static/images/Methylation/fig5-4.jpg)
[**Figure 5-4: Data selection menu**](_static/images/Methylation/fig5-4.jpg)



**9)** By previous Step 4), the user could see the data has reflected in the setting as shown in yellow in Figure 5-5. Type "CLDN10" in Field "Gene/Reporter" and choose "None" in Field "Transformation". Click "Next" button to proceed.

![](_static/images/Methylation/fig5-5.jpg)
[**Figure 5-5: "MegaSampler" menu reflected the selected datasets**](_static/images/Methylation/fig5-5.jpg)



**10)** Choose one probe ("cg25032595" and "cg16556145" respectively) from the CGI observed in yellow in the three Heatmaps produced from *Section 3 Comparing Methylation Heatmaps*. As shown in Figure 4-6, the two probes are found in the "Esteller" heatmap as "cg16275739" is marked in blue and "cg18393747" is marked in red.

![](_static/images/Methylation/fig5-61.png)
[**Figure 5-6: Probe location in the "Esteller" Heatmap**](_static/images/Methylation/fig5-61.png)




Select the first probe "cg25032595" as shown on the right in Figure 5-6. On "Adjustable settings" in Figure 5-8, the user could change the dataset order out of all selected datasets. Change the order the datasets: "Lokk" as "1", "Heyn" as "2" and "Esteller" as "3" (in Figure 5-8). This setting lets datasets be compared: "Lokk" as the first dataset, "Heyn" as the second dataset and "Esteller" as the third order. Click "Submit" button to proceed. Repeat the same process for the second probe "cg16556145" as shown on the right in Figure 5-7.


![](_static/images/Methylation/fig5-7c.png)
[**Figure 5-7: Selected probe (”cg25032595” on the left, “cg16556145” on the right)**](_static/images/Methylation/fig5-61.png)




![](_static/images/Methylation/fig5-8.jpg)
[**Figure 5-8: Probe location in the "Esteller" Heatmap**](_static/images/Methylation/fig5-8.jpg)



As a result, the first methylation scatter plot from Dataset "Lokk", "Heyn" and "Esteller" of Probe "cg25032595" are generated as shown in Figure 5-9. As expected, the methylation level of "Lokk" for normal tissues (with the average 0.025) is lower than the methylation level of "Heyn" tumor cell lines (with the average 0.08). The methylation level of "Heyn" for tumor tissues is also lower than the methylation level of "Esteller" tumor cell lines (with the average 0.4). It should be noted that the name of Y-axes of the scatter plots in Figure 5-9 and Figure 5-10 is false. The Y-axis of the scatter plot is not "Expression" but "Methylation".

On "One Way Analysis of variance (ANOVA)" table, it is also observed that the p-value is significant enough as shown in red (in Figure 5-9). In the gear box tick "add scatter"

![](_static/images/Methylation/fig5-9a.png)
[**Figure 5-9: ANOVA table and methylation graphs of the three datasets of Probe "cg25032595" (could be compared to expression plot Figure 7-5)**](_static/images/Methylation/fig5-9a.png)



The second methylation scatter plot from the three datasets of Probe "cg16556145" are generated as shown in Figure 5-9. As expected, the methylation tendency from the normal to cancer cells is increasing as observed in the scatter plot in Figure 5-9. The methylation level "Lokk" for normal tissues (with the average 0.1) is lower than the methylation level of "Heyn" tumor cell lines (with the average 0.25). The methylation level of "Heyn" for tumor tissues is also lower than the methylation level of "Esteller" tumor cell lines (with the average 0.65).

On "One Way Analysis of variance (ANOVA)" table, it is also observed that the p-value is significant enough as shown in red (in Figure 5-10).

![](_static/images/Methylation/fig5-10a.png)
[**Figure 5-10: ANOVA table and methylation graphs of the three datasets of Probe "cg16556145" (could be compared to expression plot Figure 7-5**](_static/images/Methylation/fig5-10a.png)



The mean methylation difference of the two probes is shown more simply in another online methylation analysis tool named "Wanderer". [6] There is a methylation difference to be seen between normal and tumor cells from Probe "cg25032595" (marked in blue in Figure 5-11) than the gap from Probe "cg16556145" (marked in red in Figure 5-11).

![](_static/images/Methylation/fig5-11.jpg)
[**Figure 5-11: Wanderer mean methylation graph**](_static/images/Methylation/fig5-11.jpg)


---

## 6 An Expression Box Plot

A box plot (a.k.a. Open High Low Close graph) of a single expression dataset could be drawn to see the expression level by a cell type and for your gene of interest. The user takes the following steps to create a scatter plot of a single gene within an expression dataset:

**1)** Repeat the steps from 1) to 3) in *Section 2 Generating Heatmap* of this manual. But instead, choose the expression dataset by typing "Tissues GTeX v8 Prot_Coding" on Column {Tissue/Tumor} as shown in Figure 6-1.

![](_static/images/Methylation/fig6-1a.png)

[**Figure 6-1: Change Dataset menu (after filter)**](_static/images/Methylation/fig6-1a.png)



**2)** Click on Link "CLDN10" under Field "CliniSnitch" which is located on the right of the webpage (in Figure 6-2).

![](_static/images/Methylation/fig6-2a.png)
[**Figure 6-2: "CliniSnitch" link**](_static/images/Methylation/fig6-2a.png)




**3)** A next webpage will be opened on a new internet tab. The user could see that the p-value is significant enough (where marked in red). Click on Link "tissue (View)" on Table "catvsnum" of the webpage (in Figure 6-3).

![](_static/images/Methylation/fig6-3a.png)

[**Figure 6-3: "View" link on Table "catvsnum"**](_static/images/Methylation/fig6-3a.png)



**4)** A next webpage will be opened on a new internet tab. To visualize and sort better, scroll down to Table "Adjustable settings". Select "Box plot" on Field "Graph type", "median (numeric Y)" on Field "Order Groups By" and "Color by Track" on Field "Color mode". Click "Submit" Button to update the scatter plot of a single expression data by a tissue type (in Figure 6-4).

![](_static/images/Methylation/fig6-4a.png)

[**Figure 6-4: Table "Adjustable settings"**](_static/images/Methylation/fig6-4a.png)



As a result, a scatter plot of the expression dataset "Tissues GTeX v8 Prot_Coding" shows the expression distribution of CLDN10 across primary tissues. The user can see tissue types like "salivary_gland", "pancreas" and "kidney" on the top right, which exhibit higher expression levels of Claudin10 on Figure 6-5.

![](_static/images/Methylation/fig6-5a.png)

[**Figure 6-5: Expression log2 Scatter plot of CLDN10 in normal tissues dataset "Tissues GTeX v8 Prot_Coding**](_static/images/Methylation/fig6-5a.png)



---

## 7 Comparing Expression Scatter Plots

Now that we have studied methylation graphs, our scope is extended to the next topic, which is "**expression**" of our gene of interest across tissues/cancer types. Methylation and expression have a reciprocal relationship to each other. From the previous *Section 3 Comparing Methylation Heatmaps*, it was observed that the methylation levels increase for certain genes during carcinogenesis. On the contrary, the expression levels decrease. A comparative expression graph is a good tool to observe the difference in expression from different datasets. Here, datasets with author name "Roth" and "Broad" are used to plot the expression graphs. The platform user takes the following steps to create the expression graph:

**1)** Repeat the steps from 1) to 5) in *Section 4 Comparing Methylation Scatter Plots* of this manual for two datasets with author names "Roth" (normal cells, in Figure 7-2) and "Broad" (cancer cells, in Figure 7-3). But skip the change from Step 2) in *Section 4* and leave the table as defaults as shown in Figure 7-1.

![](_static/images/Methylation/fig7-1.jpg)

[**Figure 7-1: MegaSampler menu"](_static/images/Methylation/fig7-1.jpg)



![](_static/images/Methylation/fig7-2.jpg)

[**Figure 7-2: Data selection menu with the author name "Roth"**](_static/images/Methylation/fig7-2.jpg)



**2)** On "Adjustable settings" in Figure 6-4, the user could change the dataset order out of two datasets. Change the order of the datasets: "Roth" as "1" and "Broad" as "2". This setting lets "Roth" as the first dataset compared to "Broad" as the second dataset. Click "Submit" button to proceed.

![Data selection menu with author name Broad](_static/images/Methylation/fig7-3a.jpg)

[**Figure 7-3: Data selection menu with the author name "Broad"**](_static/images/Methylation/fig7-3a.jpg)



![](_static/images/Methylation/fig7-4a.png)

[**Figure 7-4: Adjustable settings menu"**](_static/images/Methylation/fig7-4a.png)




As a result, two expression graphs from Dataset "Roth" and "Broad" are generated as shown in Figure 7-5. As expected, the expression level of "Roth" for normal tissues (with the average 7-5) is higher than the expression level of "Broad" cancer cell lines (with the average 3-4). This is in line with methylation level from the two datasets, because the cancer cells ("Broad") are highly methylated compared to the normal cells ("Roth").

On "One Way Analysis of variance (ANOVA)" table, it is also observed that the p-value is significant enough as shown in red (in Figure 7-5).

![](_static/images/Methylation/fig7-5a.png)

[**Figure 7-5: Expression comparison for CLDN10 in normal tissues and cancer cell lines as ANOVA table and expression graphs of the two datasets"**](_static/images/Methylation/fig7-5a.png)



---

## 8 Comparing Expression and Methylation Data

The user could also compare and correlate methylation and expression datasets by showing both in one plot. In this section, the datasets, "Garnett" (normal cells) and "Esteller" (cancer cells), are used. The user takes the following steps to create the dot plot of the methylation and the expression datasets:

**1)** After login to the R2 Platform [1], choose "Across Datasets" under Field 1 checkbox and "View a gene in two datatypes". Click "Next" on the main page to proceed (in Figure 8-1).

![](_static/images/Methylation/fig8-1.png)
[**Figure 8-1: Main menu**](_static/images/Methylation/fig8-1.png)



**2)** On Table "Select data sets to merge" of the next webpage, the user could set the data type and the X- and Y-axis of the dot plot. As shown in Figure 8-2, select "cellline_cancer_pharmaco" on Field "Data set collection", "Methylation data - Cell line Cancer Pharmacogenomic - Esteller - 1028 - custom - ilmnhm450" on Field "Source data" and "Expression data - Cell line Cancer Drug (Sanger) - Garnett - 1017 - RMA - u219" on Field "Target data". Click "Select data sets" to proceed.

![](_static/images/Methylation/fig8-2.png)

[**Figure 8-2: "Select data sets to merge" menu](_static/images/Methylation/fig8-2.png)



**3)** On Table "Adjustable settings" of the next webpage, type "CLDN10" in the left box of Field "Gene / Met_id" and "Gene / Reporter". The two probes from Step 6) on *Section 4 Comparing Methylation Scatter Plots* ("cg25032595", "cg16556145") are to be observed. To look at the dot plot of the first probe, type "cg25032595" in the right box of Field "Gene / Met_id" (in Figure 8-3).

![](_static/images/Methylation/fig8-3.jpg)

[**Figure 8-3: "Adjustable settings" menu (for Probe "cg25032595")](_static/images/Methylation/fig8-3.jpg)





As shown in Figure 8-4, the user can see the dot plot of the methylation dataset "Esteller" on the X-axis and the expression dataset "Garnett" on the Y-axis for the Probe "cg25032595". There is a significant correlation between the two axes (as p-value is marked in red under the table in Figure 8-4) supporting the idea of DNA hypermethylation decreasing gene expression.

![](_static/images/Methylation/fig8-4a.png)

[**Figure 8-4: The dot plot of Probe "cg25032595" (could be compared to Figure 8-6)**](_static/images/Methylation/fig8-4a.png)



**4)** Repeat the steps from 1) to 3) of this section for the second Probe by typing "cg16556145" in the right box of Field "Gene / Met_id" (in Figure 8-5).

![](_static/images/Methylation/fig8-5.jpg)

[**Figure 8-5: "Adjustable settings" menu (for Probe "cg16556145")**](_static/images/Methylation/fig8-5.jpg)



As shown in Figure 8-6, the dot plot for the Probe "cg16556145" is generated. With the significant correlation between the two axes, the concentration tendency of the most dots are the same as the tendency observed in Figure 8-4. One can observe a negative correlation between the methylation and the expression datasets.

![](_static/images/Methylation/fig8-6a.png)

[**Figure 8-6: Comparative log2 dot plot cg16556145**](_static/images/Methylation/fig8-6a.png)



---

## 9 In-Depth Study on Expression Dataset

Let's go back to Normal Tissues GTeX v8 Prot_Coding - GTeX - 17382 - tpm - gencode26 datasety. One could also take a closer look at expression of your gene of interest in certain tissues of the expression dataset on R2 Platform. From an expression box plot, a certain or several tissue types could be selected. In this section, the tissue type "skin" is further investigated with the following steps after the steps in *Section 6 An Expression Box Plot* [8].

**1)** Scroll down to "Adjustable settings" after the expression box plot is executed. Select "tissue (30 cat)" on Field "Subset track". On the pop-up window, click the tissue type "skin (1809)" checkbox and "OK". Click "Submit" to proceed. (In Figure 9-1)

![](_static/images/Methylation/fig9-1.jpg)

[**Figure 9-1: "Adjustable settings" menu**](_static/images/Methylation/fig9-1.jpg)



**2)** After the box plot on "skin" is executed, the user could further investigate expression level by skin types, such as differences in the expression between fibroblasts and normal skin types. On Table "Adjustable settings", select "tissue_detail (54 cat)" on Field "Track", "tissue_detail (54 cat)" on "Subset track", "Box/dot plot (dots)" on Field "Graph type" and "Color by Track" on Fields "Color mode/(groups)". "tissue_detail (54 cat)" is an in-depth category than the "tissue (30 cat)" category. (In Figure 9-2)

After selecting "tissue_detail (54 cat)" on Field "Subset track", the user sees the pop-up window. Click two skin types checkboxes ("cells_-_cultured_fibroblasts (504)" and "skin_-_not_sun_exposed_(suprapublic) (604)") and "OK" Button. Not-sun-exposed skin cells are chosen to reduce the impacting factor. Click "Submit" to proceed. (In Figure 9-3)

![Adjustable settings menu](_static/images/Methylation/fig9-2.jpg)

[**Figure 9-2: "Adjustable settings" menu**](_static/images/Methylation/fig9-2.jpg)





![](_static/images/Methylation/fig9-3.jpg)

[**Figure 9-3: Pop-up window on "tissue_detail (54 cat)" subset track**](_static/images/Methylation/fig9-3.jpg)



The box plot with dots shown in Figure 9-4 shows the difference of expression levels between fibroblasts and normal skin. Normal skin not exposed to the sun has a higher expression level, compared to the expression level of fibroblasts. (Be reminded that the Y-Axis name is log2 CLDN10 expression.)

![](_static/images/Methylation/fig9-4a.png)

[**Figure 9-4:Expression log2 Box/dot plot (dots) on fibroblasts and not-sun-exposed skin cells for CLDN10k**](_static/images/Methylation/fig9-4a.png)



---

## 10 Comparing Survival Probability

One could also investigate patient survival probability of a certain tumor type/entity in comparison to the expression for your gene of interest using the R2 Platform. In this section, the "TCGA" dataset is used as an example because it contains several general cancer types (including normal control tissues) and is relatively big.

**1)** Click "Survival (Kaplan-Meier/Cox)" on the left menu of the main page. On Table "Kaplan-Meier analysis using a data set", select Field "Data set" as shown in Figure 10-1.

![](_static/images/Methylation/fig10-1.jpg)

[**Figure 10-1: "Survival (Kaplan-Meier/Cox)" main page**](_static/images/Methylation/fig10-1.jpg)



**2)** On the pop-up box (in Figure 10-2), type "Kidney" on Column {Tissue/Tumor} and select "Kidney Renal Clear Cell Carcinoma" from "tcgars" on Column {Platform}. Click "Confirm selection" button as shown in Figure 10-2.

![](_static/images/Methylation/fig10-2.jpg)

[**Figure 10-2: Change Dataset menu (after filter)**](_static/images/Methylation/fig10-2.jpg)



**3)** Select "a single gene" on Field "Separated by" and click "Next" on the main page to proceed. (in Figure 10-3)

![](_static/images/Methylation/fig10-3.png)

[**Figure 10-3: "Kaplan-Meier analysis using a data set" Table on main page)**](_static/images/Methylation/fig10-3.png)



The result on the next page shows the overall survival probability between patients with high gene of interest expression and low expression (on the left in Figure 10-4) and expression levels with p-values (on the right in Figure 10-4).

When the automated separation of patients by expression level produced one big and one small cohort, it should be taken into account that results could be significant, but still not biologically relevant. Further studies should be performed, in order to better understand the contribution of your gene of interest in patient survival. Even though the p-values are significant (statistically valid), the dataset might not be biologically valid as well.

The left graph in Figure 10-4 shows the overall survival probability of two cohorts (on an Y-axis) that are high expression (a line marked in blue) and low expression (a line marked in red) groups, regarding the expression of the gene of interest. An X-axis is the follow-up in months. The total patient number of the cohorts are shown with colors on the right top of the graph ("n=430", "n=103" respectively). One could find out individual information of each sample by putting the cursor on the line (in Figure 10-5).

![](_static/images/Methylation/fig10-4a.png)

[**Figure 10-4:  "Overall survival probability graph" and "Expression graph"**](_static/images/Methylation/fig10-4a.png)




![Individual information pop-up in survival graph](_static/images/Methylation/fig10-5.png)

[**Figure 10-5: Individual information pop-up in "Overall survival probability graph"**](_static/images/Methylation/fig10-5.png)


The right graph in Figure 10-4 shows the expression level by "Events" groups. An Y-axis shows the expression level and an X-axis shows the p-values of each sample. The bar graph on the X-axis shows the p-value of each sample. The dots in green on the curve indicate the samples with the "Events" and the dots in red are the samples with no "Events". The definition of the "Events" is different by datasets. These "Events" could be for example relapse free or not (Relapse free means that the patients after primary treatment survived a certain period of time without any symptoms of the cancer). More information on the "Events" dataset label could be found on R2 Platform online tutorial under "Special sample annotation" in *Section 24. R2 Dataset Addition*. [2]

Some adjustments are to be made as the survival probability until 60 follow-up months (or 5 years) is more common (on the left graph in Figure 10-4). The expression graph (on the right graph in Figure 10-4) could be also shifted (or cut) by filtering the range with the significant p-values. This could be done by the following steps.

**4)** Scroll down to "Adjustable settings" after two graphs are executed. Type "60" months on Field "Only draw up to". Click "Redraw Graph" to proceed. (In Figure 10-6)

![](_static/images/Methylation/fig10-6a.png)

[**Figure 10-6:"Adjustable settings" Table**](_static/images/Methylation/fig10-6a.png)


Figure 10-7 shows the redrawn "Overall survival probability graph" and the range of the X-axis is adjusted to 60 months (marked in yellow in Figure 10-7). The graph became better to compare the difference between the normal people and cancer patients, as the tails of the two lines in the graph on the right are cut.

![](_static/images/Methylation/fig10-7.jpg)

[**Figure 10-7:** "Overall survival probability graph" (after adjustment)**](_static/images/Methylation/fig10-6a.png)





Next, a cutoff point on the "Expression graph" (the right graph in Figure 10-4) could be adjusted on Field "Cutoff" in "Adjustable settings" Table. The cutoff point is set with the highest p-value at default. To change the cutoff point, the following step is to be done.

**5)** Select any data sample which has the high local p-value ("387 - 819.7227: raw p: 0.015 (bonf: 1.000)" in Figure 10-8) on Field "Cutoff" in "Adjustable settings" Table. Type "60" months on Field "Only draw up to" in the same table. Click "Redraw Graph" to proceed. (In Figure 10-8)

![Adjustable settings table](_static/images/Methylation/fig10-8a.png)

[**Figure 10-8: "Adjustable settings" Table**](_static/images/Methylation/fig10-8a.png)



The result of Step 5 is described in Figure 10-9. The overall survival probability (on the left) has a smaller difference between the two lines compared to the previous graph that was drawn with the highest p-value.

![Overall survival probability and expression graph after adjustment](_static/images/Methylation/fig10-9a.png)

[**Figure 10-9:"Overall survival probability graph" and "Expression graph" (after adjustment)**](_static/images/Methylation/fig10-9a.png)





---

## 11 Hypermethylation Between Datasets (private data, not yet published)

As Hypermethylation is an indicator of tumor development, hypermethylated regions on Heatmaps could be compared between two datasets of normal and tumor patients. The dataset with the tumor type "renal cell carcinoma (PTM)" and the author name "Richter" is used for this analysis.

**1)** Click "Main" on the left menu of the main page. On Table, select "Differential expression between two groups" in Field 3. Click the option box in Field 2 for data selection. (In Figure 11-1)

![](_static/images/Methylation/fig11-1.png)

[**Figure 11-1: Main page**](_static/images/Methylation/fig11-1.png)



**2)** On the pop-up box, type the author name "Richter" on Column {Author} and select the dataset with "Renal cell carcinoma (PTM)" on Column {Tissue/Tumor} by clicking the row. Click "Confirm selection" button to proceed (In Figure 11-2). Click "Next" on main menu to proceed. (In Figure 11-3).

![](_static/images/Methylation/fig11-2.jpg)

[**Figure 11-2: Data selection menu with the author name "Richter" and the tumor type "Renal cell carcinoma (PTM)"**](_static/images/Methylation/fig11-2.jpg)



**3)** On "Select a test" Table, select "type (2 cat)" in Field "Group by" and "n10nvst (3 cat)" in Field "Subset track". Then on the pop-up menu, click the check buttons of "normal (5)" and "tumor (5)" samples except 2 outliers ("ND (2)"). Click "OK" button to finish the sample choice. Click "Submit" on the table to proceed. (In Figure 11-4)

**>>>>>>>>>>n10nvst not found contact Antje**

![](_static/images/Methylation/fig11-3.png)

[**Figure 11-3:** Main menu**](_static/images/Methylation/fig11-3.png)



![](_static/images/Methylation/fig11-4.png)

[**Figure 11-4: "Select a test" Table**](_static/images/Methylation/fig11-4.png)



**4)** On "Adjustable settings" Table, select "n (6)" as normal people in Field "Group 1" and "tm (6)" as tumor patients in Field "Group 2". Click "Submit" to proceed. (In Figure 11-5)

![](_static/images/Methylation/fig11-5.jpg)

[**Figure 11-5: "Adjustable settings" Table**](_static/images/Methylation/fig11-5.jpg)





**5)** At the right menu click "Heatmap(zscore)" to proceed. (In Figure 11-6)


![](_static/images/Methylation/fig11-6.jpg)

[**Figure 11-6: "Heatmap(zscore)" Button on the right menu**](_static/images/Methylation/fig11-6.jpg)





The next page shows the heatmap of hypermethylation between two datasets (normal people and tumor patients).

![](_static/images/Methylation/fig11-7.jpg)

[**Figure 11-7: "Heatmap(zscore)" Title**](_static/images/Methylation/fig11-7.jpg)



**>>>>heatmap plaatje vanuit DEG analysis werkt niet**

"zscore" or the standard score is "a statistical measure that represents the number of standard deviations an individual data point is from the mean of a dataset. It indicates how far a particular data point deviates from the average in terms of standard deviation units." [7] And "fdr" stands for False Discovery Rate and is "a statistical concept used in multiple hypothesis testing to control for the proportion of false discoveries or false positives." [7]

On the right of the heatmap, the colored block lines show the type of data points. The enlarged versions are shown in Figure 11-8. The red blocks of "n10nvst" are the data points of the tumor patients and the green blocks of "n10nvst" are the data points of the normal people. One could see the details of a certain data point by placing a cursor on the "n10nvst" block. On the pop-up message shows the type of the data point (marked in red) (in Figure 11-8).

![](_static/images/Methylation/fig11-8c.png)

[**Figure 11-8: "Enlarged heatmap zscore - Data points (in red) and normal data point (in green**](_static/images/Methylation/fig11-8c.png)



With this background knowledge, the positive score on the heatmap (in Figure 11-9) is colored in yellow and the negative score in blue. The positive score shows the data point above the mean and the negative below the mean of the datasets. All tumor patients have reciprocal behavior of all normal people, as observed in the color difference in the heatmap (yellow heatmap area for tumor patients are blue heatmap area for normal people).

![](_static/images/Methylation/fig11-9.jpg)

[**Figure 11-9: "Heatmap(zscore)" - rotated to horizontal for convenience**](_static/images/Methylation/fig11-9.jpg)



When the cursor is placed on Gene type axis, a pop-up message containing the gene name, the probe name and the order number (gene name="CLDN10", probe name="cg16275739", order number="581" on the pop-up message in Figure 11-10). The order number can be found from the table "Sort Order Listing" after clicking it as shown in Figure 11-10. One can investigate the difference in a certain gene's expression in this way.

![](_static/images/Methylation/fig11-10.jpg)

[**Figure 11-10: "Heatmap(zscore)" and "Sort Order Listing" Table**](_static/images/Methylation/fig11-10.jpg)




---

## 12 Appendix

### 12.1 Finding a Gene Name of Interest

If a gene name of Interest is uncertain, this could be found by using the methylation ID obtained via UCSC Genome Browser. A methylation ID represents a probe name.

For example, assume that a gene of interest is "Insulin". By following Step 3) under *Section 2. Generating a Heatmap* with a gene name as "INS", there are several choices listed below {Gene} Field on the Adjustable settings menu (in Figure 12.1-1). One could address the exact gene name of interest using a methylation ID (i.e. "Met-ID"; for example, "cg20278383" for a gene name "CLDN10") obtained from UCSC Genome Browser and select the right gene name of interest from the choices listed in Figure 12.1-1. The following describes the steps of search on UCSC Genome Browser for each solution, respectively.

Firstly, enter UCSC Genome Browser (https://genome.ucsc.edu/). Click "Human GRCh37/hg19" on the "Genomes" menu of the main page as shown in Figure 12.1-2.

![](_static/images/Methylation/fig12.1-1.jpg)

[**Figure 12.1-1: Choices for a gene of interest "Insulin"**](_static/images/Methylation/fig12.1-1.jpg)



![](_static/images/Methylation/fig12.1-2.jpg)

[**Figure 12.1-2: UCSC Genome Browser main page**](_static/images/Methylation/fig12.1-2.jpg)



#### (a) Search a Methylation ID using a sequence

If a sequence for a gene of interest is known, one may still use the sequence to begin the search as a guide. As an example, assume that "Insulin" is a gene of interest and a sequence for the certain region of this gene of interest is known as "TTAAGACTCTAATGACCCGCTGGTCCTGAGGAAGAG".

**1)** Click "Blat" on the "Tools" menu on the UCSC Genome Browser main page (in Figure 12.1-3).

![](_static/images/Methylation/fig12.1-3.jpg)

[**Figure 12.1-3: UCSC Genome Browser main page**](_static/images/Methylation/fig12.1-3.jpg)



**2)** Write the sequence "TTAAGACTCTAATGACCCGCTGGTCCTGAGGAAGAG" in the input box and click "submit" to proceed (in Figure 12.1-4).

![](_static/images/Methylation/fig12.1-4.png)

[**Figure 12.1-4: Human Blat Search page**](_static/images/Methylation/fig12.1-4.png)



**3)** On the next page, the sequence candidates are listed as the search results. Click one of the most relevant "browser" links to one's interest from the listed results (in Figure 12.1-5).

![](_static/images/Methylation/fig12.1-5.png)

[**Figure 12.1-5: Blat Search Results page**](_static/images/Methylation/fig12.1-5.png)



**4)** The next page is Genome Browser page that one could observe the genome region. Scroll down and select "show" for "CpG Islands" and for "ENC DNA Methyl" Options in "Regulation" Field. Click "refresh" to apply the modifications on the Genome Browser (in Figure 12.1-6).

![](_static/images/Methylation/fig12.1-6.png)

[
**Figure 12.1-6: "Regulation" Field**](_static/images/Methylation/fig12.1-6.png)



**5)** One could now see the corresponding methylation IDs on the Genome Browser page. If the methylation IDs are not observed on the page, adjust the genome region using "zoom in" or "zoom out" buttons on the top of the page (in Figure 12.1-7).

![](_static/images/Methylation/fig12.1-7.jpg)

[**Figure 12.1-7: Methylation IDs on UCSC Genome Browser page**](_static/images/Methylation/fig12.1-7.jpg)





**6)** Now, return to the Adjustable settings menu on R2 Genomics Analysis and Visualization Platform (https://r2.amc.nl/) (in Figure 12.1-1). Write the observed methylation ID "cg03366382" observed from the previous Step 5) in {Met_id} Field on Adjustable settings menu. Click the listed option below {Met_id} Field (in Figure 12.1-8). The exact gene name of interest is automatically written in {Gene} Field (in Figure 12.1-9).

![](_static/images/Methylation/fig12.1-8.jpg)

[**Figure 12.1-8: Adjustable settings menu on R2 Platform**](_static/images/Methylation/fig12.1-8.jpg)


![](_static/images/Methylation/fig12.1-9.jpg)

![Adjustable settings menu on R2 Platform with gene name filled](_static/images/Methylation/fig12.1-9.jpg)



#### (b) Search a Methylation ID using an uncertain gene name of interest

Now that a search for a methylation ID using a sequence is possible from the Steps in *(a) Search a Methylation ID using a sequence*. On the other hand, if a sequence is also unknown for a gene of interest, one could begin the search using an uncertain gene name of interest on UCSC Genome Browser.

**1)** Write "INS" as a guess for this gene name of interest in {Gene} Field on UCSC Human GRCh37/hg19 Genome Browser. Click the relevant one from the listed choices below {Gene} Field to proceed (in Figure 12.1-10). If one is uncertain what is relevant, press "Enter".

![](_static/images/Methylation/fig12.1-10.jpg)

![**Figure 12.1-10: UCSC Human GRCh37/hg19 Genome Browser page**](_static/images/Methylation/fig12.1-10.jpg)


**2)** If you just pressed "Enter" on the previous Step 1), all search results of a gene "Insulin" are listed with more information. Click the relevant gene option (or just the first option "INS-IGF2 (uc001lvm.3)" as a tryout) to proceed (in Figure 12.1-11).

![](_static/images/Methylation/fig12.1-11.jpg)

![**Figure 12.1-11: Search Results on hg19 for "Insulin"**](_static/images/Methylation/fig12.1-11.jpg)



**3)** On the next page, all methylation IDs for "INS-IGF2 (uc001lvm.3)" are listed on the Genome Browser page. If the methylation IDs are not shown at first glance, scroll down or adjust the options below the page as described in Figure 12.1-6. Click the relevant methylation ID (or just the spotted methylation ID "cg02343602" as a tryout) (in Figure 12.1-12).

![](_static/images/Methylation/fig12.1-12.jpg)

![**Figure 12.1-12: Methylation IDs on UCSC Genome Browser page**](_static/images/Methylation/fig12.1-12.jpg)



If one wishes to double-check its choice by looking at the DNA sequence for this methylation ID, the following steps could be done.

**4)** On the next page, the information on the spotted methylation ID "cg02343602" is provided. Click "View DNA for this feature" link (in Figure 12.1-13).

![](_static/images/Methylation/fig12.1-13.png)

![**Figure 12.1-13: Information page on the methylation IDe**](_static/images/Methylation/fig12.1-13.png)



**5)** As an example, click "One FASTA record per region" Option under "Sequence Retrieval Region Options". Define a range as "20" for an up- and a downstream (in Figure 12.1-14).

![](_static/images/Methylation/fig12.1-14.png)

![**Figure 12.1-14: DNA sequence extraction page**](_static/images/Methylation/fig12.1-14.png)



**6)** The corresponding DNA sequences on the defined region are shown as Figure 12.1-15. One could check if the sequence is aligned with known information.

![](_static/images/Methylation/fig12.1-15.png)

![**Figure 12.1-15: DNA sequences on the define region**](_static/images/Methylation/fig12.1-15.png)



---

## 13 References

[1] J. Koster, Amsterdam University Medical Centers (AUMC), Center for Experimental and Molecular Medicine (CEMM) - R2 Genomics Analysis and Visualization Platform, https://r2.amc.nl. retrieved on 24.04.2023

[2] R2 support team - R2 Tutorials, https://r2-tutorials.readthedocs.io/en/latest/. updated on 2026-06-24

[3] Mind map on the "Manual on R2 Platform for Methylation Analysis (by Ji Sun Kwon)" - Miro, https://miro.com/app/board/uXjVMMBYyDQ=/. updated on 04.05.2023

[4] Arroyo et al., 2025 Clinical Epigenetics .Epigenetic silencing and CRISPR-mediated
reactivation of tight junction protein claudin10b
(CLDN10B) in renal cancer. 
https://pubmed.ncbi.nlm.nih.gov/40524239/

[5] J. Breuer et al., - Epigenetic therapy of novel tumour suppressor ZAR1 and its cancer biomarker function, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6894338/. published on 04.12.2019

[6] I. Mallona., - Wanderer, an interactive viewer to explore DNA methylation and gene expression data in human cancer, http://maplab.imppc.org/wanderer/. published on 2015

[7] Chat GPT, keywords as "what is zscore?" and "what is fdr in statistics?", https://chat.openai.com/. retrieved on 27.06.2023

[8] Arroyo et al., 2026 - A Bioinformatics and Wet-Lab-Based Pipeline Identifies CLDN10 and GJB2 as Epigenetically Silenced Tumor Suppressor Genes in Cutaneous Melanoma https://pmc.ncbi.nlm.nih.gov/articles/PMC12986398/
