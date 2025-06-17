from dataclasses import dataclass, field
from typing import List
import uuid

@dataclass
class Owner:
    id: str
    name: str
    contact: str

@dataclass
class Pet:
    id: str
    owner_id: str
    name: str
    species: str

@dataclass
class Appointment:
    id: str
    pet_id: str
    date: str
    reason: str
