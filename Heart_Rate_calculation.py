"""
(Target Heart-Rate Calculator) While exercising, you can use a heart-rate monitor to see that your heart rate stays
within a safe range suggested by your doctors and trainers. According to the American Heart Association (AHA) 
(http://bit.ly/AHATargetHeart- Rates), the formula for calculating your maximum heart rate in beats per minute is 220 minus your age in years. 
Your target heart rate is 50-85% of your maximum heart rate. Write a script that prompts for and inputs the user's age and calculates and 
displays the user's maximum heart rate and the range of the user's target heart rate. [These formulas are estimates provided by the AHA; 
maximum and target heart rates may vary based on the health, fitness and gender of the individual. Always consult a physician or qualified
healthcare professional before beginning or modifying an exercise program.]
"""
age = int(input("Enter your age: "))

# Calculate maximum heart rate
max_heart_rate = 220 - age

# Calculate target heart rate range (50% to 85% of maximum heart rate)
lower_target_rate = max_heart_rate * 0.50
upper_target_rate = max_heart_rate * 0.85

# Display results
print(f"\nMaximum Heart Rate: {max_heart_rate} beats per minute")
print(f"Target Heart Rate Range: {lower_target_rate:.1f} - {upper_target_rate:.1f} beats per minute")