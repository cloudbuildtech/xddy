from constants import ABORT_ALL_POSITIONS
from func_connections import connect_dydx
from func_private import abort_all_positions

# MAIN FUNCTION
if __name__ == "__main__":

  # Connect to client
  try:
    client = connect_dydx()
  except Exception as e:
    print(e)
    print("Error connecting to client: ", e)
    exit(1)

#Abort all open positions
if ABORT_ALL_POSITIIONS
  try:
    print("Closing all positions...")
    close-orders = abort_all_positions(client)
  except Exception as e:
    print("Error closing all positions to client: ", e)
    exit(1)





 