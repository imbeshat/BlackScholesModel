from numpy import exp, sqrt, log
from scipy.stats import norm

# Black Scholes Logic
  """
  Parameters:
  s = Stock Price
  x = Exercise/Strike Price
  t = Time to Maturity/Expiration in years
  r = Risk-free Interest Rate
  sigma = Standard deviation of log returns(volatility)
  """
class BlackScholes:
  def __init__(self, 
  s, 
  x, 
  t, 
  r, 
  sigma):