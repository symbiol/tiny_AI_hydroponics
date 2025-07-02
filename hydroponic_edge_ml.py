import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import time
from random import uniform  # Simulate sensor data for demo purposes

# Simulated script for edge-based AI monitoring and control of hydroponic system
# Implements lightweight ML model on ESP32-like hardware for real-time pH and nutrient regulation
# Inspired by Sharma et al. (2025) for low-power, high-accuracy control

class HydroponicEdgeController:
    def __init__(self, optimal_ph=6.0, ph_tolerance=0.5):
        """Initialize hydroponic controller with target pH and tolerance."""
        self.optimal_ph = optimal_ph
        self.ph_tolerance = ph_tolerance
        self.model = LinearRegression()  # Lightweight model for edge deployment
        self.is_trained = False
        self.pump_speed = 0.0  # Simulated pump speed (0-100%)

    def simulate_sensor_data(self):
        """Simulate sensor readings for pH, nutrient concentration, and temperature."""
        # Mock data simulating real-time sensor inputs
        ph = uniform(5.0, 7.0)
        nutrient_conc = uniform(1.0, 2.0)  # dS/m (electrical conductivity proxy)
        temp = uniform(20.0, 25.0)  # Celsius
        return {"ph": ph, "nutrient_conc": nutrient_conc, "temp": temp}

    def train_model(self, data):
        """Train lightweight regression model to predict pump speed for pH regulation."""
        # Simulated historical data: [pH, nutrient_conc, temp] -> pump_speed
        X = np.array([[d["ph"], d["nutrient_conc"], d["temp"]] for d in data])
        y = np.array([self.calculate_ideal_pump_speed(d["ph"]) for d in data])
        self.model.fit(X, y)
        self.is_trained = True
        print("Edge ML model trained for pH regulation.")

    def calculate_ideal_pump_speed(self, ph):
        """Calculate ideal pump speed based on pH deviation (simulated logic)."""
        deviation = abs(ph - self.optimal_ph)
        if deviation <= self.ph_tolerance:
            return 0.0  # No adjustment needed
        return min(100.0, 50.0 * deviation)  # Linear scaling for demo

    def regulate_ph(self, sensor_data):
        """Predict and adjust pump speed to maintain optimal pH."""
        if not self.is_trained:
            raise ValueError("Model not trained.")
        
        # Prepare input for model
        X = np.array([[sensor_data["ph"], sensor_data["nutrient_conc"], sensor_data["temp"]]])
        predicted_speed = self.model.predict(X)[0]
        self.pump_speed = max(0.0, min(100.0, predicted_speed))
        
        # Simulate actuator response
        print(f"Current pH: {sensor_data['ph']:.2f}, Predicted pump speed: {self.pump_speed:.2f}%")
        return self.pump_speed

    def monitor_system(self, duration_seconds=60, interval_seconds=5):
        """Simulate real-time monitoring and control loop."""
        start_time = time.time()
        sensor_history = []
        
        while time.time() - start_time < duration_seconds:
            sensor_data = self.simulate_sensor_data()
            sensor_history.append(sensor_data)
            
            # Train model initially with simulated data
            if not self.is_trained and len(sensor_history) >= 10:
                self.train_model(sensor_history)
            
            # Regulate pH if model is trained
            if self.is_trained:
                self.regulate_ph(sensor_data)
            
            time.sleep(interval_seconds)
        
        return pd.DataFrame(sensor_history)

def main():
    """Main function to simulate hydroponic system control."""
    controller = HydroponicEdgeController(optimal_ph=6.0, ph_tolerance=0.5)
    print("Starting hydroponic system monitoring...")
    sensor_data = controller.monitor_system(duration_seconds=30)
    print("Sensor data collected:")
    print(sensor_data)

if __name__ == "__main__":
    main()
