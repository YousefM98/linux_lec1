import numpy as np
from filterpy.kalman import KalmanFilter

# Initialize the Kalman filter
kf = KalmanFilter(dim_x=2, dim_z=1)
kf.x = np.array([0., 0.])  # initial state
kf.F = np.array([[1., 1.], [0., 1.]])  # state transition matrix
kf.H = np.array([[1., 0.]])  # observation matrix
kf.P = np.array([[1000., 0.], [0., 1000.]])  # initial covariance matrix
kf.R = np.array([[0.1]])  # measurement noise covariance

# Receive data from the user and store it in a dictionary
data = {}
data['time'] = []
data['measurement'] = []
data['Data'] = []
while True:
    time = input("Enter the time (in seconds), or 'q' to quit: ")
    if time == 'q':
        break
    measurement = float(input("Enter the measurement: "))
    data['time'].append(float(time))
    data['measurement'].append(measurement)

    # Apply Kalman filter on the measurement
    filtered = kf.predict()
    filtered = kf.update(measurement)
    data['Data'].append(kf.x)

# Print the filtered data
print("Time (s)\tMeasurement\tFiltered")
for i in range(len(data['time'])):
    print(f"{data['time'][i]}\t{data['measurement'][i]}\t{data['Data'][i]}")