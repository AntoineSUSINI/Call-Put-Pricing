# Black-Scholes Option Calculator

A web-based calculator for pricing European options using the Black-Scholes model. This application calculates option prices and Greeks (Delta, Gamma, Vega, and Theta) to help traders and analysts in their decision-making process.

## Features

- Calculate Call and Put option prices using the Black-Scholes model
- Compute important option Greeks:
  - Delta (Δ): Measures the rate of change in option value with respect to the underlying asset's price
  - Gamma (Γ): Measures the rate of change in Delta with respect to the underlying asset's price
  - Vega (ν): Measures sensitivity to volatility
  - Theta (Θ): Measures the rate of time decay

## Prerequisites

- Python 3.x
- Flask
- SciPy

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Call-Put-Pricing
```

2. Install the required dependencies:
```bash
pip install flask scipy
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Enter the following parameters:
   - S0: Current price of the underlying asset
   - K: Strike price of the option
   - r: Risk-free interest rate (as a decimal, e.g., 0.05 for 5%)
   - σ (sigma): Volatility of the underlying asset (as a decimal)
   - T: Time to expiration (in years)

## Mathematical Background

The Black-Scholes model uses the following formulas:

### Option Prices
- Call Option Price = S₀N(d₁) - Ke^(-rT)N(d₂)
- Put Option Price = Ke^(-rT)N(-d₂) - S₀N(-d₁)

Where:
- d₁ = (ln(S₀/K) + (r + σ²/2)T) / (σ√T)
- d₂ = d₁ - σ√T
- N(x) is the cumulative distribution function of the standard normal distribution

### Greeks
- Delta (Call) = N(d₁)
- Delta (Put) = N(d₁) - 1
- Gamma = N'(d₁) / (S₀σ√T)
- Vega = S₀N'(d₁)√T
- Theta (Call) = -S₀N'(d₁)σ/(2√T) - rKe^(-rT)N(d₂)
- Theta (Put) = -S₀N'(d₁)σ/(2√T) + rKe^(-rT)N(-d₂)

## Project Structure

- `app.py`: Main Flask application with Black-Scholes calculations
- `templates/index.html`: Web interface for the calculator
- `call-put-pricing.ipynb`: Jupyter notebook with example calculations

## License

This project is open source and available under the MIT License.

