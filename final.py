import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from sklearn.linear_model import LogisticRegression

# Dummy function for predicting heart disease risk
def predict_heart_disease(name, age, sex, blood_pressure, cholesterol, family_history, st_depression, chest_pain, fasting_blood_sugar):
    # Dummy implementation
    # You should replace this with your actual prediction model
    return "High" if (blood_pressure > 140 or cholesterol > 200) else "Low"

# Function to provide suggestions based on prediction
def provide_suggestion(prediction):
    if prediction == "High":
        return "You may need to consult a doctor for further evaluation and follow a healthy lifestyle. If needed go for Ecg acording to the doctors advice"
    else:
        return "Your risk of heart disease is low. Keep up with a healthy lifestyle to maintain it. Please Maintain the normal ranges."

# GUI function
def predict():
    # Get input values from GUI
    name = name_entry.get()
    age = int(age_entry.get())
    sex = sex_combobox.get()
    blood_pressure = int(blood_pressure_entry.get())
    cholesterol = int(cholesterol_entry.get())
    family_history = family_history_combobox.get()
    st_depression = float(st_depression_entry.get())
    chest_pain = chest_pain_combobox.get()
    fasting_blood_sugar = int(fasting_blood_sugar_entry.get())

    # Perform prediction
    prediction = predict_heart_disease(name, age, sex, blood_pressure, cholesterol, family_history, st_depression, chest_pain, fasting_blood_sugar)

    # Display prediction result and suggestion
    result_label.config(text=f"Predicted heart disease risk for {name}: {prediction}")
    suggestion_label.config(text=provide_suggestion(prediction))

# Create main window
root = tk.Tk()
root.title("Heart Disease Prediction")

#set window size and position it in the center
window_width = 1500
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width/2) - (window_width/2))
y_coordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# Load and display background image
background_image = Image.open("heart.jpg")
background_image = background_image.resize((window_width, window_height), Image.LANCZOS)  # Use Image.LANCZOS for antialiasing
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1,relheight=1)

# Create and place input fields and labels
input_frame = ttk.Frame(root)
input_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

name_label = ttk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = ttk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

age_label = ttk.Label(input_frame, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=5)
age_entry = ttk.Entry(input_frame)
age_entry.grid(row=1, column=1, padx=10, pady=5)

sex_label = ttk.Label(input_frame, text="Sex:")
sex_label.grid(row=2, column=0, padx=10, pady=5)
sex_combobox = ttk.Combobox(input_frame, values=["Male", "Female", "others"])
sex_combobox.grid(row=2, column=1, padx=10, pady=5)

blood_pressure_label = ttk.Label(input_frame, text="Blood Pressure:")
blood_pressure_label.grid(row=3, column=0, padx=10, pady=5)
blood_pressure_entry = ttk.Entry(input_frame) 
blood_pressure_entry.grid(row=3, column=1, padx=10, pady=5)
blood_pressure_info = ttk.Label(input_frame, text="(Normal: 90-120 mmHg)")
blood_pressure_info.grid(row=3, column=2, padx=10, pady=5)

cholesterol_label = ttk.Label(input_frame, text="Cholesterol:")
cholesterol_label.grid(row=4, column=0, padx=10, pady=5)
cholesterol_entry = ttk.Entry(input_frame)
cholesterol_entry.grid(row=4, column=1, padx=10, pady=5)
cholesterol_info = ttk.Label(input_frame, text="(Normal: < 200 mg/dL)")
cholesterol_info.grid(row=4, column=2, padx=10, pady=5)

family_history_label = ttk.Label(input_frame, text="Family History:")
family_history_label.grid(row=5, column=0, padx=10, pady=5)
family_history_combobox = ttk.Combobox(input_frame, values=["Yes", "No"])
family_history_combobox.grid(row=5, column=1, padx=10, pady=5)

st_depression_label = ttk.Label(input_frame, text="ST Depression:")
st_depression_label.grid(row=6, column=0, padx=10, pady=5)
st_depression_entry = ttk.Entry(input_frame)
st_depression_entry.grid(row=6, column=1, padx=10, pady=5)
st_depression_info = ttk.Label(input_frame, text="(Normal: 0-0.5 mm)")
st_depression_info.grid(row=6, column=2, padx=10, pady=5)

chest_pain_label = ttk.Label(input_frame, text="Chest Pain:")
chest_pain_label.grid(row=7, column=0, padx=10, pady=5)
chest_pain_combobox = ttk.Combobox(input_frame, values=["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
chest_pain_combobox.grid(row=7, column=1, padx=10, pady=5)

fasting_blood_sugar_label = ttk.Label(input_frame, text="Fasting Blood Sugar:")
fasting_blood_sugar_label.grid(row=8, column=0, padx=10, pady=5)
fasting_blood_sugar_entry = ttk.Entry(input_frame)
fasting_blood_sugar_entry.grid(row=8, column=1, padx=10, pady=5)
fasting_blood_sugar_info = ttk.Label(input_frame, text="(Normal: <= 99 mg/dL)")
fasting_blood_sugar_info.grid(row=8, column=2, padx=10, pady=5)

# Team members' names
team_frame = ttk.Frame(root)
team_frame.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

team_members = ["Indu", "Almas", "Nirmala", "Poojitha"]

for idx, member in enumerate(team_members):
    ttk.Label(team_frame, text=member).grid(row=0, column=idx)

# Create predict button
predict_button = ttk.Button(root, text="Predict", command=predict)
predict_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Create label for displaying prediction result
result_label = ttk.Label(root, text="")
result_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

# Create label for displaying suggestion
suggestion_label = ttk.Label(root, text="")
suggestion_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

root.mainloop()
