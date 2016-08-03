import pandas as pd
import glob
from methods import national_func,international_func

national_list=[]
international_list=[]

directory="/mnt/all/Python/purple/*"

get_file_list=glob.glob(directory)

# print get_file_list

for filename in get_file_list:

#national function calls
    national_traffic=national_func(filename)
    national_list.append(national_traffic)

#international function calls
    international_traffic=international_func(filename)
    international_list.append(international_traffic)


df_in = pd.DataFrame(national_list, columns=['fileName', 'BL_Total', 'Citycell_Total', 'airtel_total', 'robi_total', 'teletalk_total', 'gp_total', 'Total_minute'])
df_in.to_csv('National_traffic.csv', index=False)
print 'National Completed'

df_int = pd.DataFrame(international_list, columns=['filename', 'Btrac_in','Btrac_out','novo_in','novo_out','mir_in','mir_out',
                                                   'unique_in','unique_out','digicon_in','digicon_out','roots_in','roots_out',
                                                   'gvtel_in','gvtel_out','IOS_total_in', 'IOS_total_out'])

df_int.to_csv('International_traffic.csv', index=False)
print 'International Completed'
