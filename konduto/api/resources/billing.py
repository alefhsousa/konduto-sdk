from dataclasses import dataclass, asdict

from konduto.api.resources.address import Address


@dataclass
class Billing:
    address: Address

    @property
    def to_dict(self) -> dict:
        return asdict(self)
