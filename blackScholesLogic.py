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
  def calculate(self):
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
    
    self.call_price = call_price
    self.put_price = put_price
    return call_price, put_price
  
  ## calculate the delta of the option
    call_delta = norm.cdf(d1)
    put_delta = 1 - norm.cdf(d1)
    
    self.call_delta = call_delta
    self.put_delta = put_delta
    ## return call_delta, put_delta
  
  ## calculate the gamma of the option
    call_gamma = (norm.pdf(d1) / (S * sigma * sqrt(t)))
    put_gamma = -call_gamma
    
    self.call_gamma = call_gamma
    self.put_gamma = put_gamma
    ## return call_gamma, put_gamma
  
  ## calculate the vega of the option   
    call_vega = S * norm.pdf(d1) * sqrt(t)
    put_vega = -call_vega
    
    self.call_vega = call_vega
    self.put_vega = put_vega
    ## return call_vega, put_vega
  
  ## calculate the theta of the option
    call_theta = -(S * norm.pdf(d1) * sigma) / (2 * sqrt(t)) - r * K * exp(-r * t) * norm.cdf(d2)
    put_theta = call_theta - r * K * exp(-r * t) * norm.cdf(-d2)
    
    self.call_theta = call_theta
    self.put_theta = put_theta
    ## return call_theta, put_theta
    
if __name__ == "__main__":
    t = 1
    K = 100
    S = 120
    sigma = 0.2
    r = 0.04

    # Black Scholes
    blackScholes = BlackScholes(
      S = S
      K = K
      t = t
      r = r
      sigma = sigma
    )
    blackScholes.run()