authors:
      Kishore K G 22BRS1095 kishore.kg2022@vitstudent.ac.in , Naga Rithesh 22BRS1006 naga.rithesh2022@vitstudent.ac.in

eKYC-simulation
We simulated the whole eKCY process with a website, PostgreSQL online database , C and HTML programs .

ARCHITECTURE:

HTML Website: The user interface of the e-KYC system is built on HTML websites, which provide a user-friendly platform for customers to engage in the identity verification process. These websites are frontend of this project and point of contact for users and guide them through the various steps of the verification process. Users are prompted to upload photo of their Aadhar card and use the website to take a photo of their face while also providing user instructions.

Aadhar Card Scanning: The e-KYC process commences with users uploading photographs of the front and back of their Aadhar cards to the website. The information is extracted using Json , open CV ,regular expression and pytesseract libraries. Then it is verified with customer information stored in PostgreSQL . The extract key information includes customer’s name, Aadhar number, gender and date of birth . This step automates the extraction process, ensuring accuracy, consistency and greatly reduces time .

PostgreSQL Database: PostgreSQL is an object-relational database management system. PostgreSQL is an open-source descendant of this original Berkeley code. PostgreSQL comes with many features aimed to help developers build applications, administrators to protect data integrity and build fault-tolerant environments. The heart of the system's backend operations is the PostgreSQL database, responsible for the secure storage and retrieval of customer data i.e., customer’s name, Aadhar number, gender and date of birth. This information is done from bank’s side when they receive application form of customer. Each customer's record is associated with a unique identifier, ensuring data integrity and retrieval efficiency.

OTP Verification: Following successful data verification, the system requests that the user input an OTP (One-Time Password) sent to the mobile number associated with their Aadhar card. This step adds an extra layer of security and verifies that the user has control over the provided mobile number . Only when the OTP is verified , the website moves to face recognition step .

Data Retrieval: The data retrieval process in the e-KYC system begins by establishing a secure connection to the PostgreSQL database using the database name, username, password, host name, and port number. These parameters play a crucial role in ensuring a protected and authenticated connection to the database.
Verification Against the Database: Subsequently, the retrieved customer data is compared to the information provided during the e-KYC process to verify the authenticity of the customer's identity. Data retrieval is a pivotal operation, ensuring the accuracy and consistency of customer data in the e-KYC system. Specifically, the system matches the information uploaded during the customer's initial application. A successful match indicates that the customer's details are accurate and consistent.

Photograph Capture: The system captures a live photograph of the user and prompts user to send their application number. which is then compared to the photograph submitted with their original application. Facial recognition algorithms are used to verify the likeness between the two images.

Facial Recognition: In addition to image processing, the C code also incorporates facial recognition technology. This allows the system to compare a live photograph of the user with the photograph submitted with their original application. The facial recognition algorithms verify the likeness between the two images, ensuring that the user's identity matches the information previously provided.
