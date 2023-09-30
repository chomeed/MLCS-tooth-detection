import matplotlib.pyplot as plt

# Define the learning rate schedule
initial_lr = 0.05
epochs = list(range(5))
learning_rates = [0.025, 0.03125, 0.0375, 0.04375, 0.05]

# Lists to store learning rate and epoch values for plotting
epochs_all = list(range(50))

# Plotting the learning rate change
plt.step(epochs, learning_rates, where='post')
plt.xticks(range(max(epochs)+1))
plt.xlabel('Epochs')
plt.ylabel('Learning Rate')
plt.ylim(0, max(learning_rates) + 0.01)
plt.xlim(0, max(epochs))
plt.title('Learning Rate Change')
plt.grid(True)
plt.show()