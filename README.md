
# 🛡️ Manual & Automated Testing Report – PakCyberGuard Portal

This repository contains a comprehensive quality assurance report on the *PakCyberGuard* portal, developed for the course **SE-305T: Software Quality Engineering** under the **Department of Software Engineering**.

---

## 🔗 Target Application
**PakCyberGuard** is an AI-powered cybercrime reporting and awareness platform that enables Pakistani citizens to report digital offenses, receive real-time legal advice via chatbot, and access digital safety resources.

> 🔗 (Localhost Dev Used): `http://localhost:5173`

---

## 🎯 Objective
To test and validate the functionalities of the cybercrime portal, including:

- 🧩 Registration & Login forms (validation and field-level checks)
- 🗃️ Multi-step Crime Report form
- 🤖 AI Chatbot behavior and response consistency
- 🚫 Form submission constraints
- 🐞 Bug identification and documentation

---

## 🧪 Testing Summary

### ✔️ Manual Testing (JIRA-Based)
- Platform: **JIRA**
- Scope: Registration Form (Confirm Password validation bug)
- Issue Tracked: Submission without confirming password allowed
- Severity: **High**
- Priority: **High**

### 🧰 Automated Testing (Selenium)
- Tools: `Selenium WebDriver`, `Python`, `Unittest`
- Scripts:
  - `test_login.py`
  - `test_register.py`
  - `multipage_testing.py`
- Types: Frontend field validation, navigation flows, positive/negative test cases

---

## 🧪 Sample Test Case: Registration Form (Selenium)
**✅ Positive Scenario:**
- Fills all fields properly
- Accepts Terms & Conditions
- Confirms password
- Submits successfully

**❌ Negative Scenario:**
- Leaves email and phone blank
- Does not confirm password
- Expected: Validation errors block submission

---

## 🐞 Bug Report (JIRA Snapshot)
> **Issue:** Registration form does not enforce `Confirm Password` as required  
> **Consequence:** May lead to login/credential inconsistency  
> **Fix:** Update `validateForm()` to enforce confirm password validation

---

## 📸 Snapshots Included
- Homepage
- Login/Register
- Report Crime Form
- Awareness Content
- Warning Signs
- Unit test outputs
- JIRA Bug Reports

---

## 🧰 Tools Used For Testing

| Tool          | Purpose                         |
|---------------|----------------------------------|
| Selenium      | Automated form testing           |
| Python        | Test script development          |
| ChromeDriver  | Running browser automation       |
| JIRA          | Manual test case and bug tracking |

---

## 👨‍💻 Student Info

| Name             | Roll No          | Section |
|------------------|------------------|---------|
| Qudsia Omama     | 2022F-BSE-002    | B       |

- **Univeristy**: Sir Syed Univeristy Of Engineering & Technology
- **Program**: BS Software Engineering
- **Course**: SWE–305 – Software Quality Engineering
- **Instructor**: Miss Aiman Qasim
- **Date**: June 19, 2025  

---


## 📎 Submission Includes
✅ Selenium Test Scripts  
✅ JIRA Test Case & Bug Report  
✅ Unit Test Scripts  
✅ Screenshot Evidence  
✅ Word Report Document  
```

