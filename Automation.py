from pyrogram import Client
import time

# Telegram API credentials
API_ID = "24375346"  # Replace with your Telegram API ID
API_HASH = "5665fb80957aa951bc77fd4ed0ac20e9"  # Replace with your Telegram API Hash
BOT_USERNAME = "zoo_story_bot"  # Replace with the Zoo Story bot username

# Initialize Pyrogram client
app = Client("zoo_game_bot", api_id=API_ID, api_hash=API_HASH)

# Function to start the game and claim tokens
def play_game():
    with app:
        # Send a start command to the bot
        app.send_message(BOT_USERNAME, "/start")
        time.sleep(2)  # Wait for a response

        # Example: Collecting rewards
        app.send_message(BOT_USERNAME, "Collect Rewards")  # Adjust based on bot commands
        time.sleep(2)

        # Example: Upgrading enclosures
        app.send_message(BOT_USERNAME, "Upgrade Enclosures")  # Adjust based on bot commands
        time.sleep(2)

        # Example: Inviting friends (Replace with actual Telegram usernames)
        friends = ["@friend1", "@friend2"]
        for friend in friends:
            app.send_message(BOT_USERNAME, f"Invite {friend}")
            time.sleep(2)

        # Example: Joining alliances
        app.send_message(BOT_USERNAME, "Join Alliance")  # Adjust based on bot commands
        time.sleep(2)

        print("Automated tasks completed successfully!")

if __name__ == "__main__":
    play_game()