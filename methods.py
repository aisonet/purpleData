import pandas as pd

def national_func(fileName):
    National_traffic=pd.read_excel(fileName,0,skiprows=7)
# National Traffic calculation

    BL_Total = National_traffic.iloc[5][1]
    Citycell_Total=National_traffic.iloc[6][1]
    airtel_total=National_traffic.iloc[10][1]
    robi_total=National_traffic.iloc[16][1]
    teletalk_total=National_traffic.iloc[19][1]
    gp_total=National_traffic.iloc[25][1]
    Total_minute=National_traffic.iloc[26][1]

    return (fileName,BL_Total,Citycell_Total,airtel_total,robi_total,teletalk_total,gp_total,Total_minute)
    # print (fileName,BL_Total,Citycell_Total,airtel_total,robi_total,teletalk_total,gp_total,Total_minute)

#International Traffic Calculation

def international_func(filename_int):
    international_traffic=pd.read_excel(filename_int,1,skiprows=7)
#ANS report


# IOS report incoming
    Btrac=international_traffic.iloc[19][1]
    novo=international_traffic.iloc[22][1]
    mir=international_traffic.iloc[25][1]
    unique=international_traffic.iloc[28][1]
    digicon=international_traffic.iloc[31][1]
    roots=international_traffic.iloc[34][1]
    gvtel=international_traffic.iloc[37][1]
    IOS_total=international_traffic.iloc[38][1]


# IOS report outgoing
    Btrac_out=international_traffic.iloc[19][5]
    novo_out=international_traffic.iloc[22][5]
    mir_out=international_traffic.iloc[25][5]
    unique_out=international_traffic.iloc[28][5]
    digicon_out=international_traffic.iloc[31][5]
    roots_out=international_traffic.iloc[34][5]
    gvtel_out=international_traffic.iloc[37][5]
    IOS_total_out=international_traffic.iloc[38][5]



    return (filename_int, Btrac,Btrac_out,novo,novo_out,mir,mir_out,unique,unique_out,digicon,digicon_out,roots,roots_out,gvtel,gvtel_out,IOS_total, IOS_total_out)




