from actions import *
from model import *
from api import *

input_params = InputModel

@bot.message_handler(commands=['start'])
def start(msg):
    # import pdb; pdb.set_trace()
        
    question = bot.send_message(
        msg.from_user.id,
        """
<b>Welcome To Staked Token Compounding Reminder Bot</b>

Please input the name of the token to be compounded? (E.g ethereum)

        """,
        parse_mode='HTML',
    )

    bot.register_next_step_handler(question, fetch_token)
    
def fetch_token(msg):
    global input_params
    text = msg.text.lower()
    
    token, _ = fetch_current_price(
        slug= text
    )
    
    if token is None:
        bot.send_message(
            msg.from_user.id,
            f"{_}",
            parse_mode='HTML'
        )
    else:
        # import pdb; pdb.set_trace()

        input_params.token = text
        input_params.ror = float(token['reward'] / 100)
        input_params.price = token['price']
        
        question = bot.send_message(
            msg.from_user.id,
            f"""
    Initial Number of Tokens Being Staked? (E.g 1000000)

            """,
            parse_mode='HTML',
        )

        bot.register_next_step_handler(question, add_initial_balance)
        
        
def add_initial_balance(msg):
    global input_params
    input_params.balance = float(msg.text)
    
    question = bot.send_message(
        msg.from_user.id,
        f"""
How many years are you planning to stake for? (E.g 5)

        """,
        parse_mode='HTML',
    )

    bot.register_next_step_handler(question, add_stake_years)
    


def add_stake_years(msg):
    global input_params
    input_params.years = int(msg.text)

    question = bot.send_message(
        msg.from_user.id,
        f"""
Staking Fee? (E.g 0.16)
        """,
        parse_mode='HTML',
    )

    bot.register_next_step_handler(question, add_stake_fee)


def add_stake_fee(msg):
    global input_params
    input_params.stake_fee = float(msg.text)

    question = bot.send_message(
        msg.from_user.id,
        f"""
Claim Fee? (E.g 0.16)
        """,
        parse_mode='HTML',
    )

    bot.register_next_step_handler(question, add_claim_fee)
    

def add_claim_fee(msg):
    global input_params
    input_params.claim_fee = float(msg.text)

    bot.send_message(
        msg.from_user.id,
        f"""
<b>Form Input Complete!</b>
        """,
        parse_mode='HTML',
    )
    process_algorithm(msg.from_user.id, input_params)