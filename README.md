# 🚗 Car Overtake Distance Calculator 🏁 </br></br></br>
• This project calculates the distance at which a second car, traveling faster than the first car, will overtake it.</br>
• Perfect for understanding relative motion in a fun and interactive way! 🎉 </br>

## 📋 Features</br>
• Dynamic Input: Users can input speeds and time differences.</br>
• Catch-Up Logic: Alerts when the second car cannot overtake the first car due to slower speed. ❌🚗💨</br>
• Real-Time Results: Calculates and displays the exact distance where the overtaking occurs. 📏</br>

## 🚀 How It Works</br>
• Input Speeds: Enter the speed of the first and second cars (in Km/h).</br>
• Time Difference: Enter the time difference between their starts (in hours).</br>
• Calculation: The program uses a mathematical formula to compute the distance. 🧮</br>
• Output: Displays the result or a warning if overtaking is not possible.</br>

## 📂 Code Overview</br>
• Function: care_takeover_distance</br>
• This function performs the following steps:</br>

1. Checks if the second car's speed is greater than the first car's speed.</br>
2. Calculates the time (t1) and distance (d1) for overtaking.</br>
3. Returns the distance or a warning message.</br>

## 🛠️Formula Used:</br>

For calculating the overtaking time:

$$
t_1 = \frac{V_2 \cdot \Delta t}{V_2 - V_1}
$$

For calculating the distance:

$$
d_1 = V_1 \cdot t_1
$$
 
## 🚀 How to Run:</br>

1. Make sure you have **Python** installed on your system.
2. Clone the repository:
    ```bash
   clone https://github.com/Oanekrif/Car-Overtake-Distance-Calculator.git
3. Navigate to the project directory:
    ```bash
   cd Car-Overtake-Distance-Calculator
4. Run the game script:
    ```bash
    python carTakeover
5. Enter the password length when prompted.

## 📝 Example Usage</br>
Input:

    Enter the speed of first car: 80
    Enter the speed of second car: 120
    Enter the time difference between them by hour: 0.5
Output:

    The distance at which car 2 will overtake car 1 is: 48.0 Km

## ✨ Future Enhancements</br>
• 🖼️ Add a graphical representation of the cars' movement.</br>
• 📊 Integrate with plotting libraries for visualizing the catch-up.</br>
• 🌍 Include real-world scenarios for different locations and road types.</br>

## 📜 License</br>
• This project is licensed under the MIT License. </br>
• Feel free to use, modify, and distribute! 📂</br>

## 📬 Contributions</br>
Contributions are welcome! Feel free to open an issue or submit a pull request. 🚀</br>

## ❤️ Thank You for Checking This Out! ❤️</br>
Made with Python 🐍 and a love for motion physics. 😊</br>

</br></br>
### Let me know if you'd like to customize any part further!</br>
