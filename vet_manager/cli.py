import argparse
import uuid
from typing import Any, Dict
from .data import load_data, save_data
from .models import Owner, Pet, Appointment


def add_owner(args: argparse.Namespace) -> None:
    data = load_data()
    owner = Owner(id=str(uuid.uuid4()), name=args.name, contact=args.contact)
    data["owners"].append(owner.__dict__)
    save_data(data)
    print(f"Owner added: {owner}")


def add_pet(args: argparse.Namespace) -> None:
    data = load_data()
    pet = Pet(id=str(uuid.uuid4()), owner_id=args.owner_id, name=args.name, species=args.species)
    data["pets"].append(pet.__dict__)
    save_data(data)
    print(f"Pet added: {pet}")


def add_appointment(args: argparse.Namespace) -> None:
    data = load_data()
    appt = Appointment(id=str(uuid.uuid4()), pet_id=args.pet_id, date=args.date, reason=args.reason)
    data["appointments"].append(appt.__dict__)
    save_data(data)
    print(f"Appointment scheduled: {appt}")


def list_data(args: argparse.Namespace) -> None:
    data = load_data()
    for item in data.get(args.category, []):
        print(item)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Veterinary Management System")
    subparsers = parser.add_subparsers(dest="command")

    owner_parser = subparsers.add_parser("add-owner", help="Add a new owner")
    owner_parser.add_argument("name")
    owner_parser.add_argument("contact")
    owner_parser.set_defaults(func=add_owner)

    pet_parser = subparsers.add_parser("add-pet", help="Add a new pet")
    pet_parser.add_argument("owner_id")
    pet_parser.add_argument("name")
    pet_parser.add_argument("species")
    pet_parser.set_defaults(func=add_pet)

    appt_parser = subparsers.add_parser("add-appointment", help="Schedule an appointment")
    appt_parser.add_argument("pet_id")
    appt_parser.add_argument("date")
    appt_parser.add_argument("reason")
    appt_parser.set_defaults(func=add_appointment)

    list_parser = subparsers.add_parser("list", help="List data")
    list_parser.add_argument("category", choices=["owners", "pets", "appointments"])
    list_parser.set_defaults(func=list_data)

    return parser


def main(argv=None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
