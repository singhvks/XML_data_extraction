# Import all modules
import xml.etree.ElementTree as ET
import csv
import os

# List to hold all file addresses
file_list = []

# Logger requirements
logFile = open("Debug_Log.txt","r+") 

# Output Folder
output_folder = os.getcwd().split('S')[0] + 'Output\\'
input_folder = os.getcwd().split('S')[0] + '\\'

# Getting all xml files available in the current directory
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith(".xml"):
             file_list.append(os.path.join(root, file))

# Returns values from the intended menu
def return_all(ET):
    temp_list = [] # field variable to store the list and is destroyed after function
    for i in range(0,len(ET)):
        temp_list.append(ET[i].text)
    return temp_list

#New Writer function
def write_value(file_name,header,column,data):
    with open(output_folder + file_name + '.csv', 'a',newline ='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(header)
            for i in range(0,len(column)):
                writer.writerow(list(str(column[i]).split("  "))+list(str(data[i]).split("  ")))
            writeFile.close()

# Reading function for Prod1
def read_Prod1(root):
    # Level Reading columns
    po_level = list((root[3][0].text).split(" "))  # First column name
    po_level_main = return_all(root[3][1]) # Level Properties
    po_level_value = return_all(root[4][0][0]) # level values
    cl_name = return_all(root[3][2][0][1]) # properties name
    value =[]
    for i in range(0,len(root[4][0][1][0][0])):
    	value.append(return_all(root[4][0][1][0][0][i][0]))

    file_name = str(root[4][0][0][0].text).replace(':','_')
    logFile.write("Output file: "+file_name + '\n')
    
    write_value(file_name,po_level,po_level_main,po_level_value)
    for i in range(0,len(value)):
    	write_value(file_name,['Cl'] + [i+1],name,value[i])
    logFile.write("Status OK \n")

# Reading function for Prod2
def read_Prod2(root):
    # details column readout to be called only once

    main_gp = list((root[0][0][0].text).split(" "))
    po_detail = return_all(root[0][0][1]) # Prints details # 17 th index will give the header value

    # details column readout to be called only once

    ve_main = list((root[0][0][2][0][0].text).split(" "))
    ve_details = return_all(root[0][0][2][0][1])

    # details column readout to be called only once
    dri_main = list((root[0][0][2][0][2][0][0].text).split(" "))
    dri_details = return_all(root[0][0][2][0][2][0][1])

    # Cl Details column readout to be called only once
    cl_main = list((root[0][0][2][0][2][0][2][0][0].text).split(" "))
    cl_details = return_all(root[0][0][2][0][2][0][2][0][1])

    # Conv details column readout to be called only once
    conv_main = list((root[0][0][2][0][2][0][2][1][0].text).split(" "))
    conv_details = return_all(root[0][0][2][0][2][0][2][1][1])

    try:
        cl_value = return_all(root[0][1][0][1][0][0][0][1][0][0][0][1][0][0][0][0])
    except:
        cl_details_value = "None"    
    try:
        conv_details_value = return_all(root[0][1][0][1][0][0][0][1][0][0][0][1][1][0][0][0])
    except:
        conv_details_value = "None"

    # The section that reads values for attributes
    po_detail_value = return_all(root[0][1][0][0])
    ve_details_value = return_all(root[0][1][0][1][0][0][0][0])
    dri_details_value = return_all(root[0][1][0][1][0][0][0][1][0][0][0][0])
    
    file_name = str(policy_detail_value[16]).replace(':',"_") # Replace the : from file name
    logFile.write("Output file: "+ file_name +'\n')

    write_value(file_name,main_gp,po_detail,po_detail_value)
    write_value(file_name,ve_main,ve_details,ve_details_value)
    write_value(file_name,dri_main,dri_details,dri_details_value)
    write_value(file_name,conv_main,conv_details,conv_details_value )
    write_value(file_name,cla_main,cla_details,cla_details_value )
    logFile.write("Status OK \n")

# Read input file one by one in a loop ranging the number of XML in root directory
for i in range(0,len(file_list)):
    logFile.write("Input : "+file_list[i].split('\\')[-1]+'\n')
    try:
        tree = ET.parse(file_list[i])
    except:
        logFile.write("Not a valid XML \n")
        logFile.write("Status FAIL \n")
    root = tree.getroot()
    
    #Logic to verify which type of file is it
    try:
        root[4][0][0]
        read_prod1(root)
    except:
        try:
            root[0][0][2][0][2][0][0].text
            read_prod2(root)
        except:
            logFile.write(file_list[i].split('\\')[-1] + " is Not a valid Prod1 or Prod2 XML file \n")
            logFile.write("Status FAIL \n")

logFile.close()
