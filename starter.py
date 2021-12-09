from config import *
from actions import *
from model import InputModel

input_params = InputModel(
    balance= 0.0,
    years= 0,
    price= 0.0,
    prediction= 0.0,
    commission= 0.0,
    stake_fee= 0.0,
    claim_fee= 0.0,
    ror= 0.0
)

@bot.message_handler(commands=['start'])
def start(msg):
    # import pdb; pdb.set_trace()
    

    bot.reply_to(
        msg,
        "zHi"
    )
        
    question = bot.send_message(
        msg.from_user.id,
        """
<b>Hello Folks, This is the GZIL Gainz Algorithm Bot</b>

Initial Number of Tokens Being Staked? (Number Only)

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
How many years are you planning to stake for? (Just number)

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
Current Price of the token(Prefilled)? 

        """,
        parse_mode='HTML',
    )

    bot.register_next_step_handler(question, add_current_price)
    

def add_current_price(msg):
    global input_params
    input_params.price = float(msg.text)

    question = bot.send_message(
        msg.from_user.id,
        f"""
Price Prediction of the token? 

        """,
        parse_mode='HTML',
    )

    bot.register_next_step_handler(question, add_prediction)
    

def add_prediction(msg):
    global input_params
    input_params.prediction = float(msg.text)

    question = bot.send_message(
        msg.from_user.id,
        f"""
Staking Node Commission? 

        """,
        parse_mode='HTML',
    )

    bot.register_next_step_handler(question, add_stake_commision)
    
    
def add_stake_commision(msg):
    global input_params
    input_params.commission = float(msg.text)

    question = bot.send_message(
        msg.from_user.id,
        f"""
Staking Fee? 

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
Claim Fee? 

        """,
        parse_mode='HTML',
    )

    bot.register_next_step_handler(question, add_claim_fee)
    

def add_claim_fee(msg):
    global input_params
    input_params.claim_fee = float(msg.text)

    question = bot.send_message(
        msg.from_user.id,
        f"""
Staking Fee Rate of Return? 

        """,
        parse_mode='HTML',
    )

    bot.register_next_step_handler(question, add_ror)
    
    

def add_ror(msg):
    global input_params
    input_params.ror = float(msg.text)

    question = bot.send_message(
        msg.from_user.id,
        f"""
<b>Form Input Complete!</b>
        """,
        parse_mode='HTML',
    )

    process_algorithm(msg.from_usere.id, input_params)