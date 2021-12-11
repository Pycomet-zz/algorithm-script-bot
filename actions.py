from config import *
from app import send_response


def process_algorithm(user_id, params):
    today = date.today()
    Final_Balance = []
    Initial_Balance = params.balance
    Years = params.years
    Investment_Lenght = Years*365
    N_Range = Investment_Lenght+1
    Price = params.price
    Commission = 0

    for n in range(1, N_Range):
        Balance = Initial_Balance
        ROR = params.ror
        N_ROR = ROR*Years
        Staking_Amount = (N_ROR / n) * Balance
        Total_Days = 0
        Sfee = params.stake_fee
        Cfee = params.claim_fee
        while Total_Days < Investment_Lenght:
            Staking_Amount = (N_ROR / n) * Balance
            Days_Taken = ((Staking_Amount*Investment_Lenght)/(Balance*N_ROR))
            Total_Days = Total_Days + Days_Taken
            Balance = Balance + (Staking_Amount*(1-Commission) - Sfee - Cfee)
        if Total_Days == Investment_Lenght:
            Final_Balance.append(Balance)
            # print(Total_Days)
        elif Total_Days > Investment_Lenght:
            Remaining_Time = Investment_Lenght-(Total_Days-Days_Taken)
            Final_Reward = (Remaining_Time/Investment_Lenght)*N_ROR*Balance
            #print("The remaining time after the last payment is",Remaining_Time,"days")
            #print("The final reward is ",Final_Reward)
            Final_Balance.append(Balance+Final_Reward-Staking_Amount)
    MB = max(Final_Balance)
    Max_n = Final_Balance.index(MB)+1
    Staking_Amount_Max = Initial_Balance*N_ROR/Max_n
    Total_Days = 0
    Balance_Vector = [Initial_Balance]
    Days = [0]
    Balance = Initial_Balance
    while Total_Days < Investment_Lenght:
        Days_Taken = (Staking_Amount_Max*Investment_Lenght)/(Balance*N_ROR)
        Total_Days = Total_Days+Days_Taken
        Balance = Balance + Staking_Amount_Max - Sfee - Cfee
        Balance_Vector.append(Balance)
        Days.append(Total_Days)
    x = np.linspace(0, Investment_Lenght, len(Days))
    # x_2 = np.linspace(0,Investment_Lenght, Investment_Lenght)
    # print (x)
    plt.plot(x, (ROR)*(x/365)*Initial_Balance+Initial_Balance)
    plt.plot(Days, Balance_Vector)
    # plt.plot(x_2,Initial_Balance*(1+ROR)**(x_2/Investment_Lenght));
    y = (ROR)*(x/365)*Initial_Balance+Initial_Balance
    # print('x',len(x),x)
    #print('y',len(y), y)
    # print('days',len(Days),Days)
    #print('vwctor',len(Balance_Vector), Balance_Vector)
    years_tracker = 1

    Percentage_Increase_2 = (
        ((max(Final_Balance)-Initial_Balance))-(Initial_Balance*N_ROR))/Initial_Balance
    Percentage_Increase = (
        (max(Final_Balance) - Initial_Balance * (1 + N_ROR)) / Initial_Balance) * 100
    MB = max(Final_Balance)
    New_ROR = ((MB/Initial_Balance)**(1/Years))-1
    Profit_over_yearly = (MB-Initial_Balance*(1+ROR)**(Years))
    # GZil Section, this just takes the amount of zil gained and divides it by 1000 to get the gzil, however this only works if you set the years to be around a third
    # of a year because thats when GZil minting stops around October. Ideally I would want to end up coding this to be automatic
    GZil_Gained = (MB-Initial_Balance)/1000
    ROR_simple = ROR*(1-Commission)
    Balance_without_reinvesting = Initial_Balance*(1+ROR*Years)
    Bonus_Return_on_Capital = (
        (MB-Balance_without_reinvesting)/Initial_Balance)
    Balance_Reinvest_Yearly = Initial_Balance*(1+ROR)**(Years)
    Profit_over_yearly = MB - Balance_Reinvest_Yearly
    Return_over_yearly = (1+New_ROR)**Years-(1+ROR)**Years
    Reinvest_Amount = Balance_Vector[1]-Initial_Balance
    Reinvest_Times = len(Balance_Vector)

    while years_tracker < Years + 1:
        res = Initial_Balance*(1+New_ROR*(1-Commission))**years_tracker - \
            Initial_Balance*(1+ROR_simple*(1-Commission)*years_tracker)
        message = f"Your bonus profit at year {years_tracker} is {res}"
        send_response(user_id, message)
        years_tracker = years_tracker+1

    bonus = Bonus_Return_on_Capital*100
    message = f"This leads to a Bonus Return on your Initial Stake of {bonus}%"
    send_response(user_id, message)

    res = Initial_Balance*(1+ROR*Years)
    message = f"Your Balance without the calculator over {Years} years would be {res}"
    send_response(user_id, message)

    send_response(
        user_id, f"Your balance {Years} years from now using the calculator is {MB}")
    send_response(
        user_id, f"You should withdraw every {Reinvest_Amount} coins")
    send_response(
        user_id, f"In total over {Years} Years you will have to reinvest {Reinvest_Times} times")

    # print(Final_Balance.index(max(Final_Balance))+1)
    res = Investment_Lenght/(Final_Balance.index(MB) + 1)
    send_response(user_id, f"This is rougly every {res} days")
    # print(Final_Balance.index(max(Final_Balance))+1))

    res = MB - Initial_Balance * (1 + Years*ROR)
    send_response(user_id, f"Profit using calculator is {res} coins")

    res = 100*ROR*(1-Commission)
    send_response(
        user_id, f"Your rate of return after the staking node commission is {res}%")

    res = New_ROR*100
    send_response(
        user_id, f"This means the new effective rate of return is {res}%")

    res = (New_ROR-ROR_simple)*100
    send_response(
        user_id, f"This is a {res}% increase in effective ROR year over year")
    send_response(
        user_id, "This means that with current token prices you would be ")