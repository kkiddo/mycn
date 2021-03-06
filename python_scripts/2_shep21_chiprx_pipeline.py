#!/usr/bin/python


'''
The MIT License (MIT)

Copyright (c) 2016 Charles Lin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''


#Main method run script for processing of SHEP21 CHIPRX data

#See README for additional information on downloading and installing dependencies

#==========================================================================
#=============================DEPENDENCIES=================================
#==========================================================================


import sys, os
# Get the script's full local path
whereAmI = os.path.dirname(os.path.realpath(__file__))

pipeline_dir = '/storage/cylin/home/cl6/pipeline/'

sys.path.append(whereAmI)
sys.path.append(pipeline_dir)

import pipeline_dfci
import utils
import string
import numpy
import os
import re
from collections import defaultdict
import subprocess
#==========================================================================
#============================PARAMETERS====================================
#==========================================================================



projectName = 'mycn'
genome ='hg19'
annotFile = '%s/annotation/%s_refseq.ucsc' % (pipeline_dir,genome)

#project folders
projectFolder = '/storage/cylin/grail/projects/mycn_resub/%s/' % (projectName) #PATH TO YOUR PROJECT FOLDER

#standard folder names
gffFolder ='%sgff/' % (projectFolder)
macsFolder = '%smacsFolder/' % (projectFolder)
macsEnrichedFolder = '%smacsEnriched/' % (projectFolder)
mappedEnrichedFolder = '%smappedEnriched/' % (projectFolder)
mappedFolder = '%smappedFolder/' % (projectFolder)
wiggleFolder = '%swiggles/' % (projectFolder)
metaFolder = '%smeta/' % (projectFolder)
metaRoseFolder = '%smeta_rose/' % (projectFolder)
fastaFolder = '%sfasta/' % (projectFolder)
bedFolder = '%sbed/' % (projectFolder)
figureCodeFolder = '%sfigureCode/' % (projectFolder)
figuresFolder = '%sfigures/' % (projectFolder)
geneListFolder = '%sgeneListFolder/' % (projectFolder)
bedFolder = '%sbeds/' % (projectFolder)
signalFolder = '%ssignalTables/' % (projectFolder)
tableFolder = '%stables/' % (projectFolder)
maskFolder = '%smasks/' % (projectFolder)
#mask Files
maskFile ='%smasks/hg19_encode_blacklist.bed' % (projectFolder)

#genomeDirectory
genomeDirectory = '/storage/cylin/grail/genomes/Homo_sapiens/UCSC/hg19/Sequence/Chromosomes/'

#making folders
folderList = [gffFolder,macsFolder,macsEnrichedFolder,mappedEnrichedFolder,mappedFolder,wiggleFolder,metaFolder,metaRoseFolder,fastaFolder,figureCodeFolder,figuresFolder,geneListFolder,bedFolder,signalFolder,tableFolder,maskFolder]

for folder in folderList:
    pipeline_dfci.formatFolder(folder,True)



#==========================================================================
#============================LIST OF DATAFILES=============================
#==========================================================================

#this project will utilize multiple datatables
#data tables are organized largely by type/system
#some data tables overlap for ease of analysis

#ATAC-Seq
atac_dataFile = '%sdata_tables/ATAC_TABLE.txt' % (projectFolder)

#ChIP-Seq
be2c_dataFile = '%sdata_tables/BE2C_TABLE.txt' % (projectFolder)
mm1s_dataFile = '%sdata_tables/MM1S_TABLE.txt' % (projectFolder)
nb_all_chip_dataFile = '%sdata_tables/NB_ALL.txt' % (projectFolder)
p4936_young_dataFile = '%sdata_tables/P493-6_YOUNG_TABLE.txt' % (projectFolder)
sclc_dataFile = '%sdata_tables/SCLC_DATA_TABLE.txt' % (projectFolder)
shep21_dataFile = '%sdata_tables/SHEP21_TABLE.txt' % (projectFolder)
shep_on_dataFile = '%sdata_tables/SHEP_ON_TABLE.txt' % (projectFolder)

chip_data_list = [be2c_dataFile,mm1s_dataFile,nb_all_chip_dataFile,p4936_young_dataFile,sclc_dataFile,shep21_dataFile,shep_on_dataFile]
#note: all mouse analysis of THMYCN tumors are in a separate script

#CHIP-RX
shep21_chiprx_dataFile = '%sdata_tables/SHEP21_CHIPRX_TABLE.txt' % (projectFolder)

#RNA-Seq
be2c_rna_drug_dataFile = '%sdata_tables/BE2C_RNA_DRUG_TABLE.txt' % (projectFolder)
be2c_rna_twist_dataFile = '%sdata_tables/BE2C_RNA_TWIST_TABLE.txt' % (projectFolder)
shep21_rna_dataFile = '%sdata_tables/SHEP21_DOX_RNA_TABLE.txt' % (projectFolder)


#==========================================================================
#===========================MAIN METHOD====================================
#==========================================================================


def main():


    print('main analysis for MYCN project')

    print('changing directory to project folder')
    os.chdir(projectFolder)

    print('\n\n')
    print('#======================================================================')
    print('#======================I, LOADING DATA ANNOTATION======================')
    print('#======================================================================')
    print('\n\n')

    #This section sanity checks each data table and makes sure both bam and .bai files are accessible

    #for ChIP-Seq
    pipeline_dfci.summary(shep21_chiprx_dataFile)



    print('\n\n')
    print('#======================================================================')
    print('#==========================II. CALLING MACS============================')
    print('#======================================================================')
    print('\n\n')

    #running peak finding using macs 1.4.2 on all chip datasets
    #this usually takes ~2-3 hours on a reasonably fast machine
    #a 3 hour time out on this entire operation is set
    #if peak calling takes longer than 3 hours, simply run the script again after completion
    #run_macs(shep21_chiprx_dataFile)


    print('\n\n')
    print('#======================================================================')
    print('#================III. CALCULATING CHIPRX SCALE FACTORS=================')
    print('#======================================================================')
    print('\n\n')

    #scale_factor_path = '%sHG19_SHEP21_CHIPRX_SCALE_FACTORS.txt' % (tableFolder)
    #scale_factor_table = writeScaleFactors(shep21_chiprx_dataFile,namesList=[],output=scale_factor_path)


    print('\n\n')
    print('#======================================================================')
    print('#=========================IV. SCALING WIGGLES==========================')
    print('#======================================================================')
    print('\n\n')

    #scale_factor_table = '%sHG19_SHEP21_CHIPRX_SCALE_FACTORS.txt' % (tableFolder)
    #scaleWiggles(shep21_chiprx_dataFile,scale_factor_table,names_list=[])


    print('\n\n')
    print('#======================================================================')
    print('#========================V. FILTERING PEAKS============================')
    print('#======================================================================')
    print('\n\n')

    #filterPeaks(shep21_chiprx_dataFile,maskFolder,macsEnrichedFolder,namesList = [],repeatList = [],cutOff = 0.2)


    print('\n\n')
    print('#======================================================================')
    print('#=======================VI. MAKING REGION GFFS=========================')
    print('#======================================================================')
    print('\n\n')

    # #making the intersect and union sets of regions for CTCF and H3K4ME3
    # print('Making stitched intersect and union regions for SHEP21_CTXF_RX')
    # makeStitchedGFF(shep21_chiprx_dataFile,'SHEP21_CTCF_RX',['SHEP21_0HR_CTCF_RX','SHEP21_2HR_CTCF_RX','SHEP21_24HR_CTCF_RX'])

    # #print('Making stitched intersect and union regions for SHEP21_H3K4ME3_RX')
    # makeStitchedGFF(shep21_chiprx_dataFile,'SHEP21_H3K4ME3_RX',['SHEP21_0HR_H3K4ME3_RX','SHEP21_2HR_H3K4ME3_RX','SHEP21_24HR_H3K4ME3_RX'])

    # #making the +/- 1kb active TSS gff
    # print('Making active gene tss gff')
    # gene_list_path = '%sHG19_NB_H3K27AC_ACTIVE_UNION.txt' % (geneListFolder)
    # make_tss_gff(gene_list_path,'NB_H3K27AC_ACTIVE_UNION')

    #taking mycn sites and subdividing by promoters and enhancers and adding +/- 500 flank
    mycn_stats_path = '%sHG19_NB_MYCN_CONSERVED_STATS_TABLE.txt' % (tableFolder)
    make_mycn_gffs(mycn_stats_path,window=0)
    make_mycn_gffs(mycn_stats_path,window=500)
    make_mycn_gffs(mycn_stats_path,window=5000)

    sys.exit()
    print('\n\n')
    print('#======================================================================')
    print('#======================VII. MAPPING TO REGIONS=========================')
    print('#======================================================================')
    print('\n\n')

    # #mapping ctcf to ctcf regions
    # gffList = ['%sHG19_SHEP21_CTCF_RX_UNION_-0_+0.gff' % (gffFolder), '%sHG19_SHEP21_CTCF_RX_INTERSECT_-0_+0.gff' % (gffFolder)]
    # names_list = ['SHEP21_0HR_CTCF_RX','SHEP21_2HR_CTCF_RX','SHEP21_24HR_CTCF_RX','SHEP21_0HR_INPUT_RX_2','SHEP21_2HR_INPUT_RX_2','SHEP21_24HR_INPUT_RX_2']
    # map_regions(shep21_chiprx_dataFile,gffList,names_list)

    # #mapping h3k4me3 to h3k4me3 regions
    # gffList = ['%sHG19_SHEP21_H3K4ME3_RX_UNION_-0_+0.gff' % (gffFolder), '%sHG19_SHEP21_H3K4ME3_RX_INTERSECT_-0_+0.gff' % (gffFolder)]
    # names_list = ['SHEP21_0HR_H3K4ME3_RX','SHEP21_2HR_H3K4ME3_RX','SHEP21_24HR_H3K4ME3_RX','SHEP21_0HR_INPUT_RX_2','SHEP21_2HR_INPUT_RX_2','SHEP21_24HR_INPUT_RX_2']
    # map_regions(shep21_chiprx_dataFile,gffList,names_list)
    
    # #mapping everybody to active TSS locations
    # gffList = ['%sHG19_TSS_NB_H3K27AC_ACTIVE_UNION_-1000_+1000.gff' % (gffFolder)]
    # map_regions(shep21_chiprx_dataFile,gffList,names_list=[])


    # #mapping everybody to mycn peaks
    # gffList = ['%sHG19_TSS_NB_H3K27AC_ACTIVE_UNION_-1000_+1000.gff' % (gffFolder)]
    # gffList = ['%sHG19_NB_MYCN_CONSERVED_-0_+0.gff' % (gffFolder),
    #            '%sHG19_NB_MYCN_CONSERVED_-500_+500.gff' % (gffFolder),
    #            '%sHG19_NB_MYCN_CONSERVED_ENHANCER_-0_+0.gff' % (gffFolder),
    #            '%sHG19_NB_MYCN_CONSERVED_ENHANCER_-500_+500.gff' % (gffFolder),
    #            '%sHG19_NB_MYCN_CONSERVED_PROMOTER_-0_+0.gff' % (gffFolder),
    #            '%sHG19_NB_MYCN_CONSERVED_PROMOTER_-500_+500.gff' % (gffFolder),
    #            ]
    # map_regions(shep21_chiprx_dataFile,gffList,names_list=[])



    print('\n\n')
    print('#======================================================================')
    print('#==================VIII. MAKING CHIPRX BOX PLOTS=======================')
    print('#======================================================================')
    print('\n\n')

    #making boxplots
    boxplot_script_path = '%sr_scripts/4_chiprx_plots.R' % (projectFolder)
    scale_table_path = '%sHG19_SHEP21_CHIPRX_SCALE_FACTORS.txt' % (tableFolder)

    #=============================================================================
    #for ctcf intersect
    names_string = 'SHEP21_0HR_CTCF_RX,SHEP21_2HR_CTCF_RX,SHEP21_24HR_CTCF_RX'
    background_string = 'SHEP21_0HR_INPUT_RX_2,SHEP21_2HR_INPUT_RX_2,SHEP21_24HR_INPUT_RX_2'
    plot_name = 'SHEP21_CTCF_RX_INTERSECT'
    signal_table_path = '%sHG19_SHEP21_CTCF_RX_INTERSECT_-0_+0_SIGNAL.txt' % (signalFolder)
    
    r_cmd = 'Rscript %s %s %s %s %s %s %s' % (boxplot_script_path,signal_table_path,scale_table_path,names_string,background_string,plot_name,projectFolder)
    print(r_cmd)
    os.system(r_cmd)


    #=============================================================================
    #for ctcf union
    names_string = 'SHEP21_0HR_CTCF_RX,SHEP21_2HR_CTCF_RX,SHEP21_24HR_CTCF_RX'
    background_string = 'SHEP21_0HR_INPUT_RX_2,SHEP21_2HR_INPUT_RX_2,SHEP21_24HR_INPUT_RX_2'
    plot_name = 'SHEP21_CTCF_RX_UNION'
    signal_table_path = '%sHG19_SHEP21_CTCF_RX_UNION_-0_+0_SIGNAL.txt' % (signalFolder)
    
    r_cmd = 'Rscript %s %s %s %s %s %s %s' % (boxplot_script_path,signal_table_path,scale_table_path,names_string,background_string,plot_name,projectFolder)
    print(r_cmd)
    os.system(r_cmd)



    #=============================================================================
    #for h3k4me3 intersect
    names_string = 'SHEP21_0HR_H3K4ME3_RX,SHEP21_2HR_H3K4ME3_RX,SHEP21_24HR_H3K4ME3_RX'
    background_string = 'SHEP21_0HR_INPUT_RX_2,SHEP21_2HR_INPUT_RX_2,SHEP21_24HR_INPUT_RX_2'
    plot_name = 'SHEP21_H3K4ME3_RX_INTERSECT'
    signal_table_path = '%sHG19_SHEP21_H3K4ME3_RX_INTERSECT_-0_+0_SIGNAL.txt' % (signalFolder)
    
    r_cmd = 'Rscript %s %s %s %s %s %s %s' % (boxplot_script_path,signal_table_path,scale_table_path,names_string,background_string,plot_name,projectFolder)
    print(r_cmd)
    os.system(r_cmd)


    #=============================================================================
    #for h3k4me3 union
    names_string = 'SHEP21_0HR_H3K4ME3_RX,SHEP21_2HR_H3K4ME3_RX,SHEP21_24HR_H3K4ME3_RX'
    background_string = 'SHEP21_0HR_INPUT_RX_2,SHEP21_2HR_INPUT_RX_2,SHEP21_24HR_INPUT_RX_2'
    plot_name = 'SHEP21_H3K4ME3_RX_UNION'
    signal_table_path = '%sHG19_SHEP21_H3K4ME3_RX_UNION_-0_+0_SIGNAL.txt' % (signalFolder)
    
    r_cmd = 'Rscript %s %s %s %s %s %s %s' % (boxplot_script_path,signal_table_path,scale_table_path,names_string,background_string,plot_name,projectFolder)
    print(r_cmd)
    os.system(r_cmd)

    #=============================================================================
    #for nb mycn enhancers
    dataDict=  pipeline_dfci.loadDataTable(shep21_chiprx_dataFile)
    set_name = 'MYCN'
    names_list = [name for name in dataDict.keys() if name.count(set_name) > 0]
    names_list.sort()
    background_list = [ dataDict[name]['background'] for name in names_list]
    names_string = ','.join(names_list)
    background_string = ','.join(background_list)

    plot_name = 'NB_MYCN_CONSERVED_ENHANCER_-500_+500'
    signal_table_path = '%sHG19_%s_SIGNAL.txt' % (signalFolder,plot_name)
    
    r_cmd = 'Rscript %s %s %s %s %s %s %s' % (boxplot_script_path,signal_table_path,scale_table_path,names_string,background_string,plot_name,projectFolder)
    print(r_cmd)
    
    os.system(r_cmd)

    #=============================================================================
    #for nb mycn enhancers
    dataDict=  pipeline_dfci.loadDataTable(shep21_chiprx_dataFile)
    set_name = 'MYCN'
    names_list = [name for name in dataDict.keys() if name.count(set_name) > 0]
    names_list.sort()
    background_list = [ dataDict[name]['background'] for name in names_list]
    names_string = ','.join(names_list)
    background_string = ','.join(background_list)

    plot_name = 'NB_MYCN_CONSERVED_ENHANCER_-0_+0'
    signal_table_path = '%sHG19_%s_SIGNAL.txt' % (signalFolder,plot_name)
    
    r_cmd = 'Rscript %s %s %s %s %s %s %s' % (boxplot_script_path,signal_table_path,scale_table_path,names_string,background_string,plot_name,projectFolder)
    print(r_cmd)
    
    os.system(r_cmd)

    #=============================================================================
    #for nb mycn promoter +/- 500bp
    dataDict=  pipeline_dfci.loadDataTable(shep21_chiprx_dataFile)
    set_name = 'MYCN'
    names_list = [name for name in dataDict.keys() if name.count(set_name) > 0]
    names_list.sort()
    background_list = [ dataDict[name]['background'] for name in names_list]
    names_string = ','.join(names_list)
    background_string = ','.join(background_list)

    plot_name = 'NB_MYCN_CONSERVED_PROMOTER_-500_+500'
    signal_table_path = '%sHG19_%s_SIGNAL.txt' % (signalFolder,plot_name)
    
    r_cmd = 'Rscript %s %s %s %s %s %s %s' % (boxplot_script_path,signal_table_path,scale_table_path,names_string,background_string,plot_name,projectFolder)
    print(r_cmd)
    
    os.system(r_cmd)

    #=============================================================================
    #for nb mycn promoter +/- 0
    dataDict=  pipeline_dfci.loadDataTable(shep21_chiprx_dataFile)
    set_name = 'MYCN'
    names_list = [name for name in dataDict.keys() if name.count(set_name) > 0]
    names_list.sort()
    background_list = [ dataDict[name]['background'] for name in names_list]
    names_string = ','.join(names_list)
    background_string = ','.join(background_list)

    plot_name = 'NB_MYCN_CONSERVED_PROMOTER_-0_+0'
    signal_table_path = '%sHG19_%s_SIGNAL.txt' % (signalFolder,plot_name)
    
    r_cmd = 'Rscript %s %s %s %s %s %s %s' % (boxplot_script_path,signal_table_path,scale_table_path,names_string,background_string,plot_name,projectFolder)
    print(r_cmd)
    
    os.system(r_cmd)



#==========================================================================
#===================SPECIFIC FUNCTIONS FOR ANALYSIS========================
#==========================================================================


#specific functions written for this analysis


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RUNNING MACS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def run_macs(dataFile):
    dataDict = pipeline_dfci.loadDataTable(dataFile)
    namesList = [name for name in dataDict.keys() if name.upper().count('WCE') ==0 and name.upper().count('INPUT') == 0]
    namesList.sort()
    print(namesList)
    pipeline_dfci.callMacs(dataFile,macsFolder,namesList,overwrite=False,pvalue='1e-9')
    os.chdir(projectFolder) # the silly call macs script has to change into the output dir
    #so this takes us back to the project folder

    #to check for completeness, we will try to find all of the peak files
    peak_calling_done = False
    while not peak_calling_done:
        dataDict = pipeline_dfci.loadDataTable(dataFile)
        namesList = [name for name in dataDict.keys() if name.upper().count('WCE') ==0 and name.upper().count('INPUT') == 0]
        for name in namesList:
            peak_path = '%s%s/%s_summits.bed' % (macsFolder,name,name)
            print('searching for %s' % (peak_path))
            if utils.checkOutput(peak_path,1,180):
                peak_calling_done =True
                print('found %s' % (peak_path))
                continue
            else:
                print('Error: peak calling timed out')
                sys.exit()
    
    #now format the macs output
    print('formatting macs output')
    dataDict = pipeline_dfci.loadDataTable(dataFile)
    namesList = [name for name in dataDict.keys() if name.upper().count('WCE') ==0 and name.upper().count('INPUT') == 0]
    pipeline_dfci.formatMacsOutput(dataFile,macsFolder,macsEnrichedFolder,wiggleFolder,wigLink ='',useBackground=True)
    print('Finished running Macs 1.4.2')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~WRITING SCALE FACTORS~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def writeScaleFactors(dataFile,namesList=[],output=''):

    '''
    creates a table of scale factors based on the rx genome read depth
    '''
    
    #first set up the output folder
    #rpm scale factor is what the rpm/bp should be MULTIPLIED by
    #mouse mapped reads give the denominator for what raw r/bp should be divided by
    outputTable = [['NAME','HUMAN_MAPPED_READS','MOUSE_MAPPED_READS','RPM_SCALE_FACTOR']]

    
    dataDict=pipeline_dfci.loadDataTable(dataFile)
    if len(namesList) == 0:
        namesList = [name for name in dataDict.keys()]
    namesList.sort()
    print('scaling the following datasets')


    for name in namesList:
        
        print('WORKING ON %s' % (name))
        bam_path = dataDict[name]['bam']
        bam = utils.Bam(bam_path)
        bam_mmr = float(bam.getTotalReads())/1000000
        scale_path = string.replace(bam_path,'hg19','mm9')
        scaleBam = utils.Bam(scale_path)
        scale_mmr = float(scaleBam.getTotalReads())/1000000
        #print(bam_path)
        #print(scale_path)
        rpm_scale = bam_mmr/scale_mmr
        scale_line = [bam_mmr,scale_mmr,rpm_scale]
        scale_line = [round(x,4) for x in scale_line]
        outputTable.append([name] + scale_line)

    if len(output) == 0:
        return outputTable
    else:
        utils.unParseTable(outputTable,output,'\t')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~SCALING WIGGLES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def scaleWiggles(dataFile,scaleTableFile,names_list=[]):

    '''
    first unzips each wiggle
    then scales each line by the rpm
    and rounds to a reasonable number (2 decimal)
    '''

    dataDict=pipeline_dfci.loadDataTable(dataFile)
    if len(names_list) == 0:
        names_list = [name for name in dataDict.keys() if name.count('WCE') ==0 and name.count('INPUT') == 0]
    names_list.sort()
    print(names_list)

    print('loading scale factors')

    scale_table = utils.parseTable(scaleTableFile,'\t')
    scale_dict = {}
    for line in scale_table[1:]:
        scale_dict[line[0]] = float(line[2])
    os.chdir(wiggleFolder)
                   
    for name in names_list:

        print('scaling %s' % (name))
        scale_factor = scale_dict[name]
        wig_path_gz = '%swiggles/%s_treat_afterfiting_all.wig.gz' % (projectFolder,name)
        wig_path = '%swiggles/%s_treat_afterfiting_all.wig' % (projectFolder,name)
        

        wig_out = '%swiggles/%s_scaled.wig' % (projectFolder,name)
        wig_out_final ='%swiggles/%s_scaled.wig.gz' % (projectFolder,name)
        if utils.checkOutput(wig_out_final,0,0):
            print('Found scaled wiggle for %s at %s' % (name,wig_out_final))
            continue
        cmd = 'gunzip %s' % (wig_path_gz)
        print(cmd)

        #this should run to completion
        os.system(cmd)

        #now open up the new wig
        wig = open(wig_path,'r')
        wig_scaled = open(wig_out,'w')

        ticker = 0
        for line in wig:

            if ticker % 1000000 == 0:
                print(ticker)
            ticker+=1
            if line[0] == 't' or line[0] == 'v':
                wig_scaled.write(line)
            else:
                line = line.rstrip().split('\t')
                line[1] = str(round(float(line[1])/scale_factor,2))
                line_string = '\t'.join(line) + '\n'
                wig_scaled.write(line_string)


        wig.close()
        wig_scaled.close()
        cmd = 'gzip %s' % (wig_out)
        print(cmd)
        os.system(cmd)

        cmd = 'gzip %s' % (wig_path)
        print(cmd)
        os.system(cmd)
    os.chdir(projectFolder)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~FILTERING PEAKS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#CHIPRX peaks have some artifacts at repetitive regions introduced
#by the addition of mouse spike ins.
#these have been empirically determined to occur at regions with high
#LINE, LTR, and SIMPLE repeat density

#for the chiprx code
def filterPeaks(dataFile,maskFolder,macsEnrichedFolder,namesList = [],repeatList = [],cutOff = 0.2):

    '''                                            
    filters out regions where cumulative repeat seq exceeds cutoff fraction
    users selects the repeat classes to aggregate for filtering
    auto filters the 3 repeat classes LINE, LTR, Simple_repeat                                      
    outputs a filtered bed and edits the data file
    '''

    if len(repeatList) == 0:
        repeatList = ['LINE','LTR','Simple_repeat']
    
    repeatList = [x.lower() for x in repeatList]
    #set up a dictionary w/ paths to beds of repeats
    repeatDict = {}
    for repeatClass in repeatList:
        repeatDict[repeatClass] = '%shg19_%s_rmsk.bed.gz' % (maskFolder,repeatClass)

    dataDict = pipeline_dfci.loadDataTable(dataFile)
    if len(namesList) == 0:
        namesList = [name for name in dataDict.keys() if name.upper().count('WCE') == 0 and name.upper().count('INPUT') == 0]

    print('Filtering dataset:')
    for name in namesList:
        print(name)
        filter_count = 0
        ticker = 0
        peak_path = '%s%s' % (macsEnrichedFolder,dataDict[name]['enrichedMacs'])
        filtered_path = string.replace(peak_path,'.bed','_filtered.bed')
        if utils.checkOutput(filtered_path,0,0):
            print('Filtered output identified for %s at %s' % (name, filtered_path))
            continue
        filtered_bed = []
        peak_bed = utils.parseTable(peak_path,'\t')

        for bed_line in peak_bed:
            ticker+=1
            if ticker %1000 == 0:
                print(ticker)
            peak_ID = bed_line[3]
            chrom = bed_line[0]
            start = int(bed_line[1])
            stop = int(bed_line[2])
            enrichment = bed_line[4]
            length = stop - start
            locusString = '%s:%s-%s' % (chrom,start,stop)

            repeatFractions = []
            for repeatClass in repeatList:

                tabixCmd = 'tabix %s %s' % (repeatDict[repeatClass],locusString)
                tabix = subprocess.Popen(tabixCmd,stdin = subprocess.PIPE,stderr = subprocess.PIPE,stdout = subprocess.PIPE,shell = True)
                tabixLines = tabix.stdout.readlines()
                tabixLines = [x.rstrip().split('\t') for x in tabixLines]
                overlapFraction = 0.0
                for repeat_line in tabixLines:
                    lineStart = int(repeat_line[1])
                    lineStop = int(repeat_line[2])
                    lineStart = max(start,lineStart)
                    lineStop = min(stop,lineStop)
                    overlapLength = lineStop - lineStart
                    overlapFraction += float(overlapLength)/float(length)
                repeatFractions.append(round(overlapFraction,4))
                    
            if numpy.sum(repeatFractions) < cutOff:
                filtered_bed.append(bed_line)
            else:
                filter_count +=1
        print('filtered out %s of %s regions for %s' % (filter_count,len(peak_bed),name))

        utils.unParseTable(filtered_bed,filtered_path,'\t')



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~MAKING REGION GFFS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def makeStitchedGFF(dataFile,set_name,names_list):

    '''
    makes a stitched gff and dumps it into the gff folder
    '''

    dataDict = pipeline_dfci.loadDataTable(dataFile)
    
    loci = []
    collection_dict = {}
    for name in names_list:
        print(name)
        macsEnrichedFile = '%s%s_peaks_filtered.bed' % (macsEnrichedFolder,name)
        collection = utils.importBoundRegion(macsEnrichedFile,name)
        collection_dict[name]=collection
        loci+= collection.getLoci()

    all_collection = utils.LocusCollection(loci,50)
    stitched_collection = all_collection.stitchCollection()

    gff = utils.locusCollectionToGFF(stitched_collection)

    out_path = '%sHG19_%s_UNION_-0_+0.gff' % (gffFolder,set_name)
    print(out_path)
    utils.unParseTable(gff,out_path,'\t')


    #now get the intersect gff
    print('getting intersection gff')
    stitched_loci = stitched_collection.getLoci()
    intersect_loci = []
    ticker = 0
    for locus in stitched_loci:
        if ticker%1000==0:
            print(ticker)
        ticker+=1
        overlap = True
        for name in names_list:
            if len(collection_dict[name].getOverlap(locus,'both')) == 0:
                overlap = False

        if overlap == True:
            intersect_loci.append(locus)

            
    print('identified %s stitched loci' % (len(stitched_loci)))
    print('identified %s intersect loci' % (len(intersect_loci)))

    intersect_collection = utils.LocusCollection(intersect_loci,50)

    intersect_gff = utils.locusCollectionToGFF(intersect_collection)

    intersect_path = '%sHG19_%s_INTERSECT_-0_+0.gff' % (gffFolder,set_name)
    print(intersect_path)
    utils.unParseTable(intersect_gff,intersect_path,'\t')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~MAKING ACTIVS TSS GFFS~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def make_tss_gff(gene_list_path,name):

    '''
    makes a +/- 1kb tss gff from the provided gene list
    '''

    tss_gff = utils.parseTable('%sHG19_TSS_ALL_-1000_+1000.gff' % (gffFolder),'\t')

    gene_list_table = utils.parseTable(gene_list_path,'\t')

    gene_rows = [int(line[0]) - 1 for line in gene_list_table]

    row_gff =[tss_gff[row] for row in gene_rows]

    row_gff_path = '%sHG19_TSS_%s_-1000_+1000.gff' % (gffFolder,name)

    utils.unParseTable(row_gff,row_gff_path,'\t')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~MAKING MYCN PROMOTER AND ENHANCER REGIONS~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def make_mycn_gffs(mycn_stats_path,window=0):

    '''
    makes promoter and enhancer gffs from the mycn stats table
    with an appropriate flanking window
    returns paths
    '''

    window = int(window)

    mycn_stats_table = utils.parseTable(mycn_stats_path,'\t')
    
    enhancer_gff = []
    promoter_gff = []
    for line in mycn_stats_table[1:]:
        
        gff_line = [line[1],line[0],'',int(line[2]) - window,int(line[3]) + window,'','.','',line[0]]

        if int(line[5]) == 1:
            promoter_gff.append(gff_line)
        
        if int(line[6]) == 1:
            enhancer_gff.append(gff_line)

    enhancer_gff_path = '%sHG19_NB_MYCN_CONSERVED_ENHANCER_-%s_+%s.gff' % (gffFolder,window,window)
    promoter_gff_path = '%sHG19_NB_MYCN_CONSERVED_PROMOTER_-%s_+%s.gff' % (gffFolder,window,window)
    utils.unParseTable(promoter_gff,promoter_gff_path,'\t')
    utils.unParseTable(enhancer_gff,enhancer_gff_path,'\t')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~MAPPING CHIPRX TO REGIONS~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def map_regions(nb_all_chip_dataFile,gffList,names_list=[]):

    '''
    making a normalized binding signal table at all regions
    '''

    #since each bam has different read lengths, important to carefully normalize quantification
    dataDict = pipeline_dfci.loadDataTable(nb_all_chip_dataFile)

    if len(names_list) == 0:
        names_list = dataDict.keys()
    names_list.sort()

    
    for name in names_list:
        bam = utils.Bam(dataDict[name]['bam'])
        read_length = bam.getReadLengths()[0]
        bam_extension = 200-read_length
        print('For dataset %s using an extension of %s' % (name,bam_extension))
        pipeline_dfci.mapBamsBatch(nb_all_chip_dataFile,gffList,mappedFolder,overWrite =False,namesList = [name],extension=bam_extension,rpm=True)

        

    #want a signal table of all datasets to each gff
    print('Writing signal tables for each gff:')
    for gffFile in gffList:
        gffName = gffFile.split('/')[-1].split('.')[0]
        signal_table_path = '%s%s_SIGNAL.txt' % (signalFolder,gffName)
        print(signal_table_path)
        pipeline_dfci.makeSignalTable(nb_all_chip_dataFile,gffFile,mappedFolder,namesList = names_list,medianNorm=False,output =signal_table_path)



#==========================================================================
#==================================THE END=================================
#==========================================================================

    
if __name__=="__main__":
    main()
