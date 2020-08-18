import finnhub
import os

finnhub_client = finnhub.Client(api_key=os.environ["STONK_API_KEY"])
