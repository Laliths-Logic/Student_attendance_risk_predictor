        STUDENT ATTENDANCE RISK PREDICTOR

Project Overview
--------------------------------------------------
Student Attendance Risk Predictor is a machine
learning–based project that predicts whether a
student is at risk of low attendance based on
academic and behavioral data.

The system uses Logistic Regression to analyze
student activity patterns and provide early risk
detection. This project demonstrates the practical
application of supervised machine learning in the
education domain.


Objective
--------------------------------------------------
• Identify students who may be at risk of poor attendance
• Enable early intervention by educators
• Apply machine learning to a real-world problem


Machine Learning Approach
--------------------------------------------------
Algorithm Used   : Logistic Regression
Problem Type    : Binary Classification
Output Classes  :
    0 → Not At Risk
    1 → At Risk


Dataset Description
--------------------------------------------------
The dataset contains the following features:

Avg_Login_Time   : Average login time of the student
Missed_Classes   : Number of classes missed
Assignment_Rate  : Percentage of assignments completed
Internet_Issue   : Internet issues (0 = No, 1 = Yes)
Participation    : Student participation score
At_Risk          : Target variable (0 or 1)


Project Workflow
--------------------------------------------------
1. Load student attendance data from CSV file
2. Preprocess the dataset
3. Split data into training and testing sets
4. Train Logistic Regression model
5. Evaluate model performance
6. Predict attendance risk for new students


Technologies Used
--------------------------------------------------
• Python
• Pandas
• Scikit-learn
• Command Line Interface


How to Run the Project
--------------------------------------------------
1. Download or clone the repository
2. Ensure attendance.csv and main.py are in the same folder
3. Install required libraries:

   pip install pandas scikit-learn

4. Run the program:

   python main.py


Sample Output
--------------------------------------------------
Student is AT RISK of low attendance


Note
--------------------------------------------------
The dataset used is small and intended for learning
purposes only. For real-world applications, a
larger dataset is recommended.


Future Enhancements
--------------------------------------------------
• Increase dataset size
• Add more student behavior features
• Build a web interface using Streamlit or Flask
• Save and reuse trained models
• Visualize feature importance


Author
--------------------------------------------------
Lalith


License
--------------------------------------------------
This project is for educational purposes only.
==================================================
