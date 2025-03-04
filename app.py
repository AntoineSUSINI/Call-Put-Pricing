from flask import Flask, render_template, request, jsonify
from math import exp, log, sqrt
from scipy.stats import norm

app = Flask(__name__)

def d1 (S0,K,r,sigma,T):
    return (log(S0/K)+(r+sigma**2/2)*T)/(sigma*sqrt(T))

def d0 (S0,K,r,sigma,T):
    return (log(S0/K)+(r-sigma**2/2)*T)/(sigma*sqrt(T))

def call_price(S0,K,r,sigma,T):
    return S0*norm.cdf(d1(S0,K,r,sigma,T))-K*exp(-r*T)*norm.cdf(d0(S0,K,r,sigma,T))

def put_price(S0, K, r, sigma, T):
    return -S0*norm.cdf(-d1(S0,K,r,sigma,T)) + K*exp(-r*T)*norm.cdf(-d0(S0,K,r,sigma,T))

def delta_call(S0, K, r, sigma, T):
    return norm.cdf(d1(S0,K,r,sigma,T))

def delta_put(S0, K, r, sigma, T):
    return norm.cdf(d1(S0,K,r,sigma,T)) - 1

def gamma(S0, K, r, sigma, T):
    return norm.pdf(d1(S0,K,r,sigma,T))/(S0*sigma*sqrt(T))

def vega(S0, K, r, sigma, T):
    return S0*norm.pdf(d1(S0,K,r,sigma,T))*sqrt(T)

def theta_call(S0, K, r, sigma, T):
    return -S0*norm.pdf(d1(S0,K,r,sigma,T))*sigma/(2*sqrt(T)) - r*K*exp(-r*T)*norm.cdf(d0(S0,K,r,sigma,T))

def theta_put(S0, K, r, sigma, T):
    return -S0*norm.pdf(d1(S0,K,r,sigma,T))*sigma/(2*sqrt(T)) + r*K*exp(-r*T)*norm.cdf(-d0(S0,K,r,sigma,T))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greeks')
def greeks():
    return render_template('greeks.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    S0 = float(data['S0'])
    K = float(data['K'])
    r = float(data['r'])
    sigma = float(data['sigma'])
    T = float(data['T'])
    
    call = call_price(S0, K, r, sigma, T)
    put = put_price(S0, K, r, sigma, T)
    
    delta_call_value = delta_call(S0, K, r, sigma, T)
    delta_put_value = delta_put(S0, K, r, sigma, T)
    gamma_value = gamma(S0, K, r, sigma, T)
    vega_value = vega(S0, K, r, sigma, T)
    theta_call_value = theta_call(S0, K, r, sigma, T)
    theta_put_value = theta_put(S0, K, r, sigma, T)
    
    return jsonify({
        'call': round(call, 6),
        'put': round(put, 6),
        'delta_call': round(delta_call_value, 6),
        'delta_put': round(delta_put_value, 6),
        'gamma': round(gamma_value, 6),
        'vega': round(vega_value, 6),
        'theta_call': round(theta_call_value, 6),
        'theta_put': round(theta_put_value, 6)
    })

if __name__ == '__main__':
    app.run(debug=True)