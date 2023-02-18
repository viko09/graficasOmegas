import matplotlib.pyplot as plt
import numpy as np


# Para Ω_r(z) con Ω_{r0} = 0.1 y Ω_{m0} = 0.9 y k = 0
# z va de 10^-3 a 10^5
def omega_r(z):
    a = 0.1 * ((z + 1) ** 4)
    b = (0.1 * ((z + 1) ** 3)) + (0.1 * ((z + 1) ** 4)) - ((0.9 + 0.1 - 1) * ((1 + z) ** 2))
    return a / b


inicio = 10 ** (-3)
fin = 10 ** 5
z = np.arange(inicio, fin, 0.1)

omega_r(z)

plt.plot(z, omega_r(z), color='purple', alpha=0.65, label='Radiación')
# Add this line to change the x-axis scale to logarithmic
plt.xscale('log')
# Graphic settings
plt.title(r'Gráfica de radicación para $\Omega_r(z)$')
plt.xlabel('$z$')
plt.ylabel('$\Omega_r(z)$')
plt.legend()
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Save as png
# plt.savefig("figuraR.png")

# Show the plot
plt.show()
