from numpy import exp, sqrt, log
from scipy.stats import norm

## Black Scholes Logic
"""
Parameters:
S = Stock (or other underlying) Price
K = Exercise/Strike Price
t = Time to Maturity/Expiration in years
r = Risk-free Interest Rate
sigma = Standard deviation of log returns(volatility)
"""
class BlackScholes:
  def __init__(
    self, 
    S: float, 
    K: float, 
    t: float, 
    r: float, 
    sigma: float
  ):
    self.S = S
    self.K = K
    self.t = t
    self.r = r
    self.sigma = sigma
    
  ## Method to perform the Black Scholes calculation
  def calculatePrice(self):
    S = self.S
    K = self.K
    t = self.t
    r = self.r
    sigma = self.sigma
    
    ## Black Scholes formula
    d1 = (log(S/K) + (r + 0.5 * sigma**2) * t) / (sigma * sqrt(t))
    d2 = d1 - sigma * sqrt(t)
    
    call_price = S * norm.cdf(d1) - K * exp(-r * t) * norm.cdf(d2)
    put_price = K * exp(-r * t) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    # Store results as attributes for heatmaps
    self.call_price = call_price
    self.put_price = put_price

    return call_price, put_price
    
  ## Method for Greeks
  def greeks(self):
    S, K, t, r, sigma = self.S, self.K, self.t, self.r, self.sigma
    
    d1 = (log(S/K) + (r + 0.5 * sigma**2) * t) / (sigma * sqrt(t))
    d2 = d1 - sigma * sqrt(t)
  
    ## calculate the delta of the option
    call_delta = norm.cdf(d1)
    put_delta = call_delta-1

    ## calculate the gamma of the option
    call_gamma = (norm.pdf(d1) / (S * sigma * sqrt(t)))
    
    ## calculate the vega of the option   
    call_vega = S * norm.pdf(d1) * sqrt(t)

    ## calculate the theta of the option
    call_theta = -(S * norm.pdf(d1) * sigma) / (2 * sqrt(t)) - r * K * exp(-r * t) * norm.cdf(d2)
    put_theta = -(S * norm.pdf(d1) * sigma) / (2 * sqrt(t)) + r * K * exp(-r * t) * norm.cdf(-d2)
    
    ## calculate rho
    rho_call = K * t * exp(-r*t) * norm.cdf(d2)
    rho_put = -K * t * exp(-r*t) * norm.cdf(-d2)
    
    return {
      "call_delta": call_delta,
      "put_delta": put_delta,
      "call_gamma": call_gamma,
      "call_theta": call_theta,
      "put_theta": put_theta,
      "call_rho":rho_call,
      "put_rho":rho_put
    }
if __name__ == "__main__":
    S = 120
    K = 100
    t = 1
    r = 0.04
    sigma = 0.2

    # Black Scholes
    blackScholes = BlackScholes(
      S = S,
      K = K,
      t = t,
      r = r,
      sigma = sigma
      )
      
    blackScholes.calculatePrice()