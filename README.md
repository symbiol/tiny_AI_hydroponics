# tiny_AI_hydroponics

AI-Driven Hydroponic Biogeochemical Control Repository
This repository encapsulates Python-based workflows for implementing edge-based artificial intelligence (AI) in hydroponic systems, focusing on real-time monitoring and control of biogeochemical parameters to optimize nutrient dynamics and plant growth. Inspired by methodologies for low-power AI deployment (e.g., Sharma et al., 2025), the scripts leverage lightweight machine learning models on resource-constrained hardware, akin to ESP32 microcontrollers, to regulate pH and nutrient stoichiometry in hydroponic ecosystems.
Scripts

hydroponic_edge_ml.py: Implements a lightweight Linear Regression model for edge-based control of hydroponic systems, simulating real-time pH regulation via pump speed adjustments. Designed for low-power microcontrollers, it ensures rapid response to biogeochemical fluctuations critical for nutrient uptake and plant health.

hydroponic_data_preprocessing.py: Preprocesses sensor data (pH, nutrient concentration, temperature, humidity) with stoichiometric normalization and anomaly detection, ensuring robust inputs for AI-driven control systems.

hydroponic_visualization.py: Visualizes temporal dynamics and correlations of hydroponic parameters, facilitating insights into biogeochemical interactions and system performance.


Requirements

Python 3.8+
Libraries: numpy, pandas, scikit-learn, matplotlib, seaborn
Hardware (simulated): ESP32 or similar microcontroller with sensor interfaces

Usage

Clone the repository:git clone https://github.com/your-username/hydroponic-biogeochemical-ai.git


Install dependencies:pip install -r requirements.txt


Run the edge control script:python hydroponic_edge_ml.py


Preprocess and visualize data (replace paths as needed):python hydroponic_data_preprocessing.py hydroponic_sensor_data.csv
python hydroponic_visualization.py hydroponic_sensor_data_processed.csv



Notes

The scripts assume CSV-formatted sensor data with columns for pH, nutrient concentration (dS/m), seawater temperature, and humidity.
The edge-based ML model is designed for deployment on low-power devices, reflecting applications in real-time hydroponic control (Sharma et al., 2025).
The workflows are adaptable to other soilless cultivation systems, including those relevant to coral symbiosis studies, by modifying sensor inputs and control logic.
Future enhancements could integrate IoT for remote monitoring via a mobile application, as described in related hydroponic AI research.

License
MIT License
References

Sharma, A., Taherkhani, A., Orba, E., & Taherkhani, A. (2025). A Machine Learning Method on a Tiny Hardware for Monitoring and Controlling a Hydroponic System. AI, Computer Science and Robotics Technology.
