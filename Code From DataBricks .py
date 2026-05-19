# Databricks notebook source
# Create Variables 
student_name = "Amara"
age = 19
subject = "Math"
score = 72
passed = True

# Check data types
print(type(student_name))
print(type(age))
print(type(score))
print(type(passed))

# COMMAND ----------

#Task 1.2 
print(type(score))
print(type(passed))

# COMMAND ----------

#Task 1.3 
final_mark = (score / 100) * 150

print(final_mark)
print(type(final_mark))

# COMMAND ----------

#Task 2.1 
student_names = [
    "Amara",
    "Ben",
    "Chloe",
    "David",
    "Eva",
    "Farai",
    "Grace",
    "Hassan"
]

print(student_names[0])
print(student_names[-1])
print(student_names[2:5])
print(len(student_names))

# COMMAND ----------

#Task 2.2
scores = [72, 55, 88, 45, 91, 63, 50, 77]

print(scores[0])
print(scores[4])
print(scores[0] + scores[4])

# COMMAND ----------

#Task 2.3 
hassan = {
    "student_name": "Hassan",
    "age": 21,
    "subject": "Science",
    "score": 77,
    "passed": True
}

print(hassan["subject"])
print(hassan["score"] + 10)
print(type(hassan["passed"]))

# COMMAND ----------

#Task 2.4 
students = [
    {
        "student_name": "Amara",
        "age": 19,
        "subject": "Math",
        "score": 72,
        "passed": True
    },

    {
        "student_name": "Ben",
        "age": 21,
        "subject": "Science",
        "score": 55,
        "passed": False
    },

    {
        "student_name": "Chloe",
        "age": 20,
        "subject": "Math",
        "score": 88,
        "passed": True
    },

    {
        "student_name": "David",
        "age": 22,
        "subject": "English",
        "score": 45,
        "passed": False
    }
]

print(students[1]["score"])
print(students[0]["student_name"])
print(len(students))

# COMMAND ----------

#Task 3.1 
print(score > 60)
print(age == 20)
print(subject != "Science")
print(score >= 72)

# COMMAND ----------

#Task 3.2 
print(score > 60 and passed == True)
print(age < 18 or score > 70)
print(not passed)
print(score > 80 and subject == "Math")

# COMMAND ----------

#Task 3.3 
score = 72

if score >= 75:
    print("Distinction")
elif score >= 50:
    print("Pass")
else:
    print("Fail")

# COMMAND ----------

score = 45

if score >= 75:
    print("Distinction")
elif score >= 50:
    print("Pass")
else:
    print("Fail")

# COMMAND ----------

score = 91

if score >= 75:
    print("Distinction")
elif score >= 50:
    print("Pass")
else:
    print("Fail")

# COMMAND ----------

#Task 3.4 
score = 72
subject = "Math"

if score > 60 and subject == "Math":
    print("Math high achiever")
else:
    print("Does not meet criteria")

# COMMAND ----------

score = 55
subject = "Science"

if score > 60 and subject == "Math":
    print("Math high achiever")
else:
    print("Does not meet criteria")