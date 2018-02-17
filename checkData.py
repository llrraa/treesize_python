import os
import csv
import sys
import re
import time

CSV_HEADER = ['volume','abs_path','drive','directory','filename','extension','is_file','is_dir','is_link','size_in_bytes','creation_time','modify_time']

def create_csv_line(myFileName):

    volume = sys.argv[3]
    abs_path = myFileName
    drive = os.path.splitdrive(myFileName)[0]
    directory = os.path.split(myFileName)[0] 
    filename = os.path.basename(myFileName)
    extension = os.path.splitext(myFileName)[1].lower()
    is_file = str(os.path.isfile(myFileName))
    is_dir = str(os.path.isdir(myFileName))
    is_link = str(os.path.isdir(myFileName))
    size_in_bytes = str(os.path.getsize(myFileName))
    creation_time = "-".join([str(time.gmtime(os.path.getctime(myFileName)).tm_year), str(time.gmtime(os.path.getctime(myFileName)).tm_mon), str(time.gmtime(os.path.getctime(myFileName)).tm_mday)])
    modify_time = "-".join([str(time.gmtime(os.path.getmtime(myFileName)).tm_year),str(time.gmtime(os.path.getmtime(myFileName)).tm_mon),str(time.gmtime(os.path.getmtime(myFileName)).tm_mday)])
    
    csv_line = [volume,abs_path,drive,directory,filename,extension,is_file,is_dir,is_link,size_in_bytes,creation_time,modify_time]
    csv_line_clean = []

    for element in csv_line:
        csv_line_clean.append(element.encode('ascii','ignore').decode('UTF-8'))

    return csv_line_clean

def main():

    writer = csv.writer(open(sys.argv[2],"w"), delimiter=';', lineterminator = "\n")
    writer.writerow(CSV_HEADER)
    
    for dirname, dirnames, filenames in os.walk(sys.argv[1]):
    # print path to all subdirectories first.
        for subdirname in dirnames:
            myFileName = os.path.join(dirname, subdirname)
            csv_line = create_csv_line(myFileName)
            writer.writerow(csv_line)
            print(csv_line)

    # print path to all filenames.
        for filename in filenames:
            myFileName = os.path.join(dirname, filename)
            csv_line = create_csv_line(myFileName)
            writer.writerow(csv_line)
            print(csv_line)

if __name__ == "__main__":
    main()