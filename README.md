# Black-Scholes Option Calculator

A web-based calculator for pricing European options using the Black-Scholes model. This application provides an intuitive interface for calculating option prices and visualizing the Greeks (Delta, Gamma, Vega, and Theta) to assist traders and analysts in their decision-making process.

## Features

- Interactive web interface for option pricing calculations
- Real-time calculation of Call and Put option prices
- Visualization of important option Greeks:
  - Delta (Δ): Measures the rate of change in option value with respect to the underlying asset's price
  - Gamma (Γ): Measures the rate of change in Delta with respect to the underlying asset's price
  - Vega (ν): Measures sensitivity to volatility
  - Theta (Θ): Measures the rate of time decay
- Interactive graphs with adjustable volatility parameters
- Modern, responsive design with intuitive controls

## Prerequisites

- Python 3.x
- Flask
- SciPy
- Plotly.js (included via CDN)
- Bootstrap 5 (included via CDN)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd black-scholes-calculator
```

2. Install the required Python packages:
```bash
pip install flask scipy numpy
```

3. Run the application:
```bash
python app.py
```

4. Open your web browser and navigate to `http://localhost:5000`

## Usage

### Option Price Calculator
1. Enter the following parameters:
   - Stock Price (S₀)
   - Strike Price (K)
   - Time to Maturity (T)
   - Risk-free Rate (r)
   - Volatility (σ)
2. The calculator will instantly display:
   - Call Option Price
   - Put Option Price
   - Greeks values (Delta, Gamma, Vega, Theta)

### Greeks Visualization
1. Navigate to the Greeks page
2. Use the interactive sliders to adjust volatility
3. Observe how the Greeks change with respect to the stock price

## Mathematical Background

### Black-Scholes Formula
The Black-Scholes model calculates the theoretical price of European-style options using the following variables:
- S: Current stock price
- K: Strike price
- r: Risk-free interest rate
- T: Time to maturity
- σ: Volatility of the stock

The formulas for call (C) and put (P) options are:
```
d1 = (ln(S/K) + (r + σ²/2)T) / (σ√T)
d2 = d1 - σ√T

C = SN(d1) - Ke^(-rT)N(d2)
P = Ke^(-rT)N(-d2) - SN(-d1)
```
where N(x) is the cumulative distribution function of the standard normal distribution.

## Project Structure

- `app.py`: Main Flask application with Black-Scholes calculations
- `templates/`
  - `index.html`: Main calculator interface
  - `greeks.html`: Greeks visualization interface
  - `navbar.html`: Navigation component
- `call-put-pricing.ipynb`: Jupyter notebook with example calculations

## License

This project is open source and available under the MIT License.

