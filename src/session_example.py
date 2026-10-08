#create a dictionary for the assessment_session
assessment_session = { 
  "session_id": "AS-001",
  "age_group": "adult",
  "completed": False,
  "answers_count": 0
  }

#create function to check if the answers_count is valid
def is_valid_answers_count(count):
  return True if count >= 0 else False

print(is_valid_answers_count(0))#true
print(is_valid_answers_count(-1))#false
print(is_valid_answers_count(5))#true