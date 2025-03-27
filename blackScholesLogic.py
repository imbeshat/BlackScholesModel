from numpy import exp, sqrt, log
from scipy.stats import norm

# Black Scholes Logic
  """
  Parameters:
  S = Stock (or other underlying) Price
  K = Exercise/Strike Price
  t = Time to Maturity/Expiration in years
  r = Risk-free Interest Rate
  sigma = Standard deviation of log returns(volatility)
  """
class BlackScholes:
  def __init__(self, 
  S: float, 
  K: float, 
  t: float, 
  r: float, 
  sigma: float):