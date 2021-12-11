from dataclasses import dataclass

@dataclass
class InputModel:
    token: str("")
    balance: float(0.0)
    years: int(0)
    price: float(0.0)
    commission: float(0.0)
    stake_fee: float(0.0)
    claim_fee: float(0.0)
    ror: float(0.0)