from xmlrpc.server import SimpleXMLRPCServer

# Function Get Ideal Weight
def my_ideal_weight(height, gender):
    if gender == "Male":
        ideal = (height - 100) - ((height - 100) * 0.1)
    elif gender == "Female":
        ideal = (height - 100) - ((height - 100) * 0.15)
    else:
        return "Invalid sexuality."
    return ideal



# Function Get BMI
def my_bmi(weight, height):
    height = height / 100
    bmi = weight / (height * height)
    return bmi

def category_bmi(bmi):
    if bmi < 18.5:
        return "Thin"
    elif bmi == 18.5 or bmi <= 22.9:
        return "Normal"
    elif bmi == 23 or bmi <= 29.9:
        return "Fat"
    else:
        return "Obese"

# Function Get Basal Metabolic Rate (BMR) 
def my_bmr(weight, height, age, gender):
    if gender == 'Male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 'Female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        return "Invalid sexuality."
    return bmr

#Function Get Heart Rate (Denyut Jantung)
def my_heart_rate(age):
    max_heart_rate = 220 - age
    target_heart_rate = {
        'minimum': 0.5 * max_heart_rate,
        'maximum': 0.85 * max_heart_rate
    }
    return target_heart_rate


# Function main
def main():
    server = SimpleXMLRPCServer(("localhost", 5000))
    print("Running XML-RPC server on localhost:5000...")
    server.register_function(my_ideal_weight, "my_ideal_weight")
    server.register_function(my_bmi, "my_bmi")
    server.register_function(category_bmi, "category_bmi")
    server.register_function(my_bmr, "my_bmr")
    server.register_function(my_heart_rate, "my_heart_rate")
    server.serve_forever()

if __name__ == "__main__":
    main()
