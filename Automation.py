from pyrogram import Client
import time

# Replace with your Telegram API credentials
API_ID = '24375346'
API_HASH = '5665fb80957aa951bc77fd4ed0ac20e9'
BOT_USERNAME = 'zoo_story_bot'

# Initialize the Pyrogram client
app = Client("zoo_bot_session", api_id=API_ID, api_hash=API_HASH)

def start_game():
    """Starts interaction with the Zoo bot."""
    app.send_message(BOT_USERNAME, "/start")
    print("Game started")
    time.sleep(2)

def claim_daily_rewards():
    """Claims daily login rewards."""
    app.send_message(BOT_USERNAME, "Claim Rewards")  # Adjust the command based on bot's response
    print("Daily rewards claimed")
    time.sleep(2)

def invite_friends(friends):
    """Invites friends to earn rewards."""
    for friend in friends:
        app.send_message(BOT_USERNAME, f"Invite {friend}")
        print(f"Invited: {friend}")
        time.sleep(3)

def subscribe_to_channels():
    """Subscribes to channels for rewards."""
    app.send_message(BOT_USERNAME, "Subscribe Channels")  # Replace with the actual command
    print("Subscribed to required channels")
    time.sleep(3)

def solve_riddle(answer):
    """Submits the answer to a riddle."""
    app.send_message(BOT_USERNAME, f"Riddle Answer: {answer}")  # Replace with the actual command
    print(f"Riddle solved with answer: {answer}")
    time.sleep(2)

def add_emoji_to_story(emoji):
    """Adds an emoji to the Telegram story."""
    app.send_message(BOT_USERNAME, f"Add Emoji {emoji}")
    print(f"Emoji {emoji} added to story")
    time.sleep(2)

def join_or_create_alliance():
    """Joins or creates an alliance."""
    app.send_message(BOT_USERNAME, "Join Alliance")  # Replace with the actual command
    print("Alliance joined or created")
    time.sleep(2)

def upgrade_enclosures():
    """Upgrades enclosures to increase productivity."""
    app.send_message(BOT_USERNAME, "Upgrade Enclosures")  # Replace with the actual command
    print("Enclosures upgraded")
    time.sleep(2)

def complete_quests():
    """Completes daily quests for additional rewards."""
    app.send_message(BOT_USERNAME, "Complete Quests")  # Replace with the actual command
    print("Quests completed")
    time.sleep(2)

# Main function to execute tasks
def automate_zoo_bot():
    with app:
        start_game()
        claim_daily_rewards()
        invite_friends(["@friend1", "@friend2", "@friend3"])
        subscribe_to_channels()
        solve_riddle("Elephant")  # Replace with the actual riddle answer
        add_emoji_to_story("")
        join_or_create_alliance()
        upgrade_enclosures()
        complete_quests()
        print("All tasks completed successfully!")

if __name__ == "__main__":
    automate_zoo_bot()
