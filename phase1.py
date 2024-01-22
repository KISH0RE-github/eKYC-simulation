import cv2
import dlib
import pytesseract
import json
import re
import os
from datetime import datetime
#import psycopg2
import matplotlib.pyplot as plt
import numpy as np

def extract_aadhar_info(image_path):
    img = cv2.imread(image_path,-1)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray_img, lang='eng')
    text_lines = text.split('\n')
    text_lines = [line for line in text_lines if line.strip()]  
    cleaned_text = '\n'.join(text_lines)
    print(cleaned_text)
    
    aadhar_number_pattern = r'\d{4}\s?\d{4}\s?\d{4}'
    aadhar_number_match = re.search(aadhar_number_pattern, cleaned_text)
    aadhar_number = aadhar_number_match.group().replace(" ", "") if aadhar_number_match else None
    
    name_pattern = r'(.+)(?=\n\s*DOB:)'
    name_match = re.search(name_pattern, cleaned_text, re.MULTILINE)
    x = name_match.group(1).strip() if name_match else None
    if(x):
        name=x
        print("\n\n",1)
    else:
        name_pattern1 = r'(.+)(?=\s+[(\[].+?DOB:)'
        name_match1 = re.search(name_pattern1, cleaned_text, re.MULTILINE)
        y = name_match1.group(1).strip() if name_match1 else None
        print("\n\n",2)
        name=y
        if(y):
            name=y
        else:
            name_pattern2 = r'\n(.*\n)*.*DOB.*\n(.*\n)*'
            name_match2 = re.search(name_pattern2, cleaned_text, re.MULTILINE)
            z = name_match2.group(1).strip() if name_match2 else None
            print("\n\n",3)
            name=z
         
    dob_pattern = r'DOB:\s*(\d{2}/\d{2}/\d{4})'
    dob_match = re.search(dob_pattern, cleaned_text)
    dob = dob_match.group(1) if dob_match else None
    
    gender_pattern = r'(Male|Female|Transgender)'
    gender_match = re.search(gender_pattern, cleaned_text)
    gender = gender_match.group() if gender_match else None
    
    extracted_info = {
        "Name": name,
        "Aadhar Number": aadhar_number,
        "Date of Birth": dob,
        "Gender": gender,
    }

    return extracted_info

def extract_address_info(image_path_address):
    img = cv2.imread(image_path_address,-1)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray_img, lang='eng')
    print(text)
    address_pattern = r'Address:[\s\n]+((?:[^\n]+?\n){1,10})'
    address_match = re.search(address_pattern, text)
    address = address_match.group(1) if address_match else None
    cleaned_address = address.replace("\n", " ")
    return cleaned_address

def check(extracted_info):
    db_params = {
    "database": "database_name",
    "user": "username",
    "password": "password",
    "host": "host",
    "port": "port_number"
    }
    try:
    
        conn = psycopg2.connect(**db_params)
    
    
        if conn.closed == 0:
            print("Database connection is open.")
        else:
            print("Database connection is closed.")

        cursor = conn.cursor()
        
        query = "SELECT name,date_of_birth,address,gender FROM aadhar_details WHERE aadhar_number = %s"
        cursor.execute(query, (extracted_info["Aadhar Number"],))
        matching_record = cursor.fetchone()
        parts = matching_record[1].strftime("%Y-%m-%d").split("-")
        formatted_date = f"{parts[2]}/{parts[1]}/{parts[0]}"
        print(matching_record[0])
        print(formatted_date)
        print(matching_record[2])
        print(matching_record[3])
        if matching_record:
            
            if (matching_record[0] == extracted_info["Name"].strip() and
                formatted_date == extracted_info["Date of Birth"].strip() and
                matching_record[2] == extracted_info["Address"].strip() and
                matching_record[3] == extracted_info["Gender"].strip()):
                return True
        return False
            
    except Exception as e:
        print("Error:", e)
def face_match(click,appli):
    


    return 0; 


if __name__ == "__main__":
    file_name1 = os.path.join(os.path.dirname(__file__), "frontpicture.jpeg")
    assert os.path.exists(file_name1)
    file_name2 = os.path.join(os.path.dirname(__file__), "backpicture.png")
    assert os.path.exists(file_name2)
    extracted_info = extract_aadhar_info(file_name1)
    extracted_address = extract_address_info(file_name2)
    extracted_info["Address"] = extracted_address
    
    print("Extracted Aadhar Information:")
    print(json.dumps(extracted_info, indent=4))
    
    verification_result = check(extracted_info)
    
    if verification_result:
       print("Match: The details are verified.")
    else:
       print("Not a match: The details do not match the database.")

    print("Please look into Camera and click camera icon.\n")
    
    clicked_photo = os.path.join(os.path.dirname(__file__), "xxx.jepg")
    assert os.path.exists(clicked_photo)
    applic_photo = os.path.join(os.path.dirname(__file__), "yyy.jepg")
    assert os.path.exists(applic_photo)
    face_match(clicked_photo,applic_photo)
