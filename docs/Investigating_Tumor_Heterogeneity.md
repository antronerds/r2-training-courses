<a id="investigating_tumor_heterogeneity"> </a>

Investigating Tumor Heterogeneity
=================================

*Learn how to use the R2 data analysis platform to analyse tumor heterogeneity in Neuroblastoma*


Introduction
------------

Cancer is a very complex disease. Much more complicated than originally anticipated when the first mutations were found to be causal for specific cancers. During the lectures you’ve been shown how this works in colorectal cancer, where a well defined path of subsequent gained mutations leads to more aggressive tumorigenic cell types. 
Although there has been extensive research into similar mutation mechanisms in Neuroblastoma (also in our group), there has been no such mechanism found for this cancer type. In this practical work we want to try to bring you to the cutting edge of research into this dangerous childhood tumor. From the lectures you should have learned already that this tumor seems to be heterogenic by nature. There is reason to believe that this heterogeneity causes the high percentage of relapses in the aggressive subtype of Neuroblastoma. Children experiencing a relapse almost always die. 
Fortunately new technologies have become available to molecular biology. These enable us to study not only the mutations and RNA expression of genes but also study the epigenetic modifications of the DNA. And not only that but genes can now be manipulated in cell lines and living tissues. 
Using advanced data analysis, statistics and clustering methods, the new field of bioinformatics tries to derive new insights from these experimental data and help molecular biologists to generate new hypotheses that can be tested experimentally.
Today you’ll use a web-based platform, R2, that provides you with a set of such bioinformatics tools to investigate recent patient and experimental data from Neuroblastoma tumors and cell lines. 
Neuroblastoma is a pediatric tumor of the peripheral adrenergic lineage, which is derived from the neural crest. During embryogenesis, cells delaminate from the neural crest, migrate ventrally and differentiate into adrenaline- or noradrenaline-producing cells. Neuroblastomas typically express enzymes for the adrenaline-synthesis route. High-stage neuroblastomas usually go into complete remission upon therapy but often relapse as therapy-resistant disease.
Figures:


Tumors and lineages: clustering data
---------------------------------------

1.  <a href="https://hgserver1.amc.nl/cgi-bin/r2/main.cgi?&dscope=TRAIN001&option=about_dscope" target="_blank">Go to the R2 website</a> 
2.  Click tSNE maps in the left menu
	
How can we further characterize the groups? Use additional data available in the scientific community resources. Since we profiled the two additional classical cell lines we can use these in a larger public dataset of other tumor cell lines and see where they cluster. 
The other datasets used are
What  
This is not isogenic, we 
Figures:
Explain tSNE map; figure Jan presentation?
Show figures of mesenchymal and neuroectodermal tumors (2.7 and 2.9)


------------------
  ![](_static/images/R2d2_logo.png)**Sample did you know box?**
  
>  *Text goes here*

------------------



Urgency of research: patient material
----------------------------------------

These so called classical cell lines have gone through thousands of cloning cycles and usually are pretty far off their original genomic composition. We’ve recently isolated from on patient from several tumor sites two biopsies per site. These are so called isogenic cell line pairs. We’ve profiled the mRNA expression of these samples and of a so called classical cell line. To investigate the relations between these samples we’ve profiled them using Affymetrix RNA chips. The resulting gene expression patterns can be used perform a hierarchical clustering. 
What number of groups do you expect?

Figures:
 * the cell line images from the Nat Gen paper, supplemental fig 1a

  ![Figure1: Bright field image of isogenic pairs.](_static/images/TumorHeterogeneity_IsoGenicPairsBF.png "Figure1: Bright field image of isogenic pairs.")
	
  [**Figure1: Bright field image of isogenic pairs.**](_static/images/TumorHeterogeneity_IsoGenicPairsBF.png)

Explain RNA analysis; differential expression picture from the book; fig 1.17
Explaining clustering techniques


Which genes make a difference? Creating signatures
-----------------------------------------------------

We have identified two different types of cells that seem to be related independent from patients. What genes determine the difference between the two types? We’ll use RNA expression data again but now the other way around; based on the classification in groups we look for genes that characterize this classification best, or in other words, that are differentially expressed between these two groups.
For future use we’ll store the genes that make the difference as a so called signature. We’ll make two sets, each specific for a type of cells. Name them according to the hints we got from the previous analysis: MES and ADRN
Try Broad geneset EMT
As a first analysis step we can check a data resource called the Gene Ontology that provides a tree of systematic ordered biological terms that is used to formally describe the biological role of each gene. What can you say about the function of the group of genes that are upregulated in the MES type of cells?
Figures:


Identifying groups: using signatures to classify other datasets
------------------------------------------------------------------

Now that we have a clue as to what character the two types of cell lines have, we can use the gene expression data to create an expression based definition of each type.   
Figures:


Using scores for further characterization
--------------------------------------------

The expression patterns of these specific signature can be used to investigate the relative behaviour of cell types. We can do this by summarizing the expression data of all genes in the signature in each cell type in one number; a signature score. These scores can be compared in more dimensions, in this case signature dimensions. First we
Figures:


Finding causes; homing in on transcription factors
-----------------------------------------------------

Apparently there are two types of cells in Neuroblastoma tumors. Neuroblastoma seems to be a heterogenous tumor. Transcription factors are known to determine gene expression programs in cells. These gene expression programs determine the development of the cell. Can we determine which TF’s might determine the difference between both of these cell lines?
Figures:


Proving causes; manipulating cell lines
------------------------------------------

From experiments we know that both cell types can switch
Now that we found the TF PRRX1 to be highly expressed in the MES type of cell lines we can try to investigate this relation by manipulating the gene in cell lines we grow in the lab. The gene was inducibly expressed in the cell lines and these were monitored through time for their gene expression. The PRRX1 gene was also silenced by using a CRISPR/Cas9 system.
Keyword: reprogramming
Figures:


Creating hypotheses; relating to chromatin modification data
---------------------------------------------------------------

So the TF PRRX1 is capable of shifting cells from a MES state to an ADRN state. How can we further determine causal relations and probably targetable processes in these cancer cells? How is a switch dynamically possible? A growing body of evidence implicates enhancers as key elements defining cell identity but the relationship of these enhancers to intratumoral heterogeneity is unknown. We measured enhancer mark. We view a couple of genes from the signatures to discover patterns
Epigentisch versus genetisch

Figures:



Suggesting therapy
---------------------


Armed with the current new knowledge, can you think of a way to use the fact that neuroblastoma is a heterogenous tumor consisting of a mesenchymal, motile cell type and a adrenergic, differentiated cell type for therapeutic options?
Related 
SKNSH; upon chemotherapy (drugs) mesenchymal shift; drugable are for example kinases; 
Hints: 
Figures:







