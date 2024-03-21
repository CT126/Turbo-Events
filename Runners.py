class Runner:
  def __init__(self, name, bib_number, age, gender):
    self.name = name
    self.bib_number = bib_number
    self.age = age
    self.gender = gender
    self.time = None

def validate_bib_number(bib_number):
  try:
    int(bib_number)
    return True
  except ValueError:
    return False

def register_runner(runners, name, bib_number, age, gender):
  if validate_bib_number(bib_number) and bib_number not in runners:
    runners.append(Runner(name, bib_number, age, gender))
  else:
    print("Invalid Bib Number (must be an integer and unique)")

def record_time(runners, bib_number, time):
  for runner in runners:
    if runner.bib_number == bib_number:
      runner.time = time
      return
  print("Bib Number not found")

runners = []

register_runner(runners, "John Doe", 123, 30, "Male")

record_time(runners, 123, "00:30:00")

for runner in runners:
   print(f"Name: {runner.name},\n"
        f"Bib Number: {runner.bib_number},\n"
        f"Age: {runner.age},\n"
        f"Gender: {runner.gender},\n"
        f"Time: {runner.time}")