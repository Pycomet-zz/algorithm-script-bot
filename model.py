from dataclasses import dataclass

@dataclass
class InputModel:
    balance: float
    years: int
    price: float
    prediction: float
    commission: float
    stake_fee: float
    claim_fee: float
    ror: float
    