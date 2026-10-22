Password Strength Checker



Project Overview



The Password Strength Checker is a beginner-level cybersecurity project developed using Python. The purpose of this program is to evaluate password strength, identify common security weaknesses, and provide recommendations for creating stronger passwords.



Project Objectives



Evaluate password length.



Identify uppercase and lowercase letters.



Detect numbers and special characters.



Identify commonly used passwords.



Detect predictable password patterns.



Calculate a password security score from 0 to 100.



Provide recommendations for improving password security.



Technologies Used



Python 3.15.1



Windows Command Prompt



Windows Notepad



Python getpass library



Python string library



Security Features



Password Length Analysis: Evaluates the number of characters in a password.



Character Variety: Checks for uppercase letters, lowercase letters, numbers, and special characters.



Common Password Detection: Identifies selected commonly used passwords.



Predictable Pattern Detection: Detects sequences such as 1234 and abcd.



Password Strength Rating: Classifies passwords as WEAK, MODERATE, or STRONG.



Password Security Score: Assigns an educational score from 0 to 100.



Password Privacy: Hides password input and does not intentionally save passwords to files or databases.



Testing Results



Test Password



Strength



Score



Result



123456



WEAK



17/100



PASSED



Hello123



MODERATE



67/100



PASSED



BlueRiver!Cloud27



STRONG



100/100



PASSED



Password1234!



WEAK



30/100



PASSED



How to Run the Program



Open Windows Command Prompt.



Navigate to the Password\_Strength\_Checker project folder.



Enter the command: py password\_checker.py



Enter a made-up test password.



Review the password strength, security score, and recommendations.



Security Limitations



This program is designed for educational purposes. Its numerical score does not represent a scientifically validated measure of password security. It uses a limited list of common passwords and does not check comprehensive breached-password databases. Passwords are processed temporarily in memory.



Future Improvements



Expand common-password detection.



Add advanced password-pattern analysis.



Develop a graphical user interface.



Implement automated testing.



Improve password-strength estimation.



Publish the completed project on GitHub.



Conclusion



This project demonstrates foundational Python programming, input validation, password security analysis, and secure coding concepts. It provides practical experience in developing a cybersecurity tool that identifies password weaknesses and recommends improvements.

