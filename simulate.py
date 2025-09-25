import pybullet as p
import time

# Connect to the physics server
p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)


# Simulation loop
for i in range(1000):
    p.stepSimulation()  # Step the physics simulation
    print(i)  # Print the loop variable
    # Sleep for 1/60th of a second to slow down the simulation
    time.sleep(1/60)

# Disconnect from the physics server
p.disconnect()
