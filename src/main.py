from discord_runner import run_discord_bot

# Functional requirements Write a Discord bot in Python that
#     Constantly fetches spot K-line data for SOL/USDT pair from Bybit
#     Calculates RSI (relative strength index) for this symbol based on closing price
#     Sends a text message to Discord channel if the calculated RSI value is over 70 or below 30
#     Use the 1H (1 hour) time frame
#
# Non-functional requirements
#
#     The code should be readable and clean but is not expected to be production-ready nor fully covered with tests.
#     Delay between the bar close and notification should be less than 10 seconds
#     RSI should be calculated using a technical analysis library of your choice
#     Solution should run inside the Docker container and include corresponding Dockerfile
#     Solution is expected in form of github repository that includes readme instructions on how to run it


if __name__ == "__main__":
    run_discord_bot()