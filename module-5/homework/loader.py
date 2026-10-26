import pickle

lead = {
  "lead_source": "paid_ads",
  "industry": "technology",
  "employment_status": "employed",
  "location": "north_america",
  "number_of_courses_viewed": 2,
  "annual_income": 79276.0,
  "interaction_count": 4,
  "lead_score": 0.41
}

with open("pipeline.bin", "rb") as file:
    model = pickle.load(file)
    score = model.predict_proba(lead)[0][1].round(3)
    print(score)
