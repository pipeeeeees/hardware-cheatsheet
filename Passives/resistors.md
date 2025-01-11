# Resistors

Below are my notes and cheat sheet material on resistors for circuit board design.

### Typical Manufacturers

- TE Connectivity Passive Product
- YAGEO
- Samsung Electro-Mechanics
- Panasonic Electronic Components
- Stackpole Electronics

### Useful tools

- [Nearest standard resistor finder](https://www.fodey.com/r)
- [Voltage Divider Calculator](https://www.fodey.com/voltage-divider)
- [Parallel Resistance Calculator](https://www.fodey.com/electronics/parallel-resistance-calculator)

## Common *YAGEO* Thick Film 0402 1% 1/16W 100ppm/°C Resistors
- Preset Digi-Key Parametric Search Link: https://www.digikey.com/short/w3ntd7r8
- YAGEO is known for being cost-effective, having high availability, and having reliable performance in general-purpose applications. For standard thick film resistors, they do a great job. 

| Resistance (Ω) | YAGEO Part Numeber |
|----------------|--------------------|
| 10             | RC0402FR-0710RL    |
| 33             | RC0402FR-0733RL    |
| 100            | RC0402FR-07100RL   |
| 1k             | RC0402FR-071KL     |
| 10k            | RC0402FR-0710KL    |
| 47k            | RC0402FR-0747KL    |
| 100k           | RC0402FR-07100KL   |
| 220k           | RC0402FR-07220KL   |
| 470k           | RC0402FR-07470KL   |
| 1M             | RC0402FR-071ML     |
| 10M            | RC0402FR-1310ML    |

### PPM/°C

PPM/°C (Parts Per Million per Degree Celsius) measures how much a resistor's value changes as the temperature changes. The term "parts per million" means the number of parts (or changes) for every one million parts of the resistor's original value. For example, if a resistor has a rating of 100 ppm/°C, it means that for every degree Celsius the temperature increases, the resistor's value could change by 100 parts for every million parts of its original value. **So, if the resistor's value is 1,000 Ω, at 100 ppm/°C, it could change by 0.1 Ω for every 1°C change in temperature**. This is important because resistors can heat up during use, and the more stable a resistor is with temperature changes, the better it is for precise electronics.

### Thick Film vs. Thin Film

The main difference between thick film and thin film resistors is how they're made and their performance. Thick film resistors are created by printing a thick layer of resistive material (like a paste) onto a ceramic base and then firing it at high temperatures. This process is cheaper, but the resistors are less precise and have higher temperature changes. On the other hand, thin film resistors are made by depositing a very thin layer of resistive material onto a ceramic or glass base through a vacuum process. This makes thin film more precise, stable, and accurate, but they are also more expensive. So, **thick film resistors are commonly used in general-purpose applications where cost is a factor**, while **thin film resistors are preferred for high-precision or sensitive circuits where accuracy and stability are more important**.