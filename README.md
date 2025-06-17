# Veterinary Management System

This project provides a minimal command line interface for managing a small veterinary clinic. It allows you to store owners, pets and schedule appointments in a JSON file.

## Usage

Run commands with `python -m vet_manager.cli` followed by an action. Data is stored in `vet_manager/data.json` within this repository.

### Add an Owner

```bash
python -m vet_manager.cli add-owner "Owner Name" "Contact Info"
```

### Add a Pet

```bash
python -m vet_manager.cli add-pet OWNER_ID "Pet Name" "Species"
```

### Schedule an Appointment

```bash
python -m vet_manager.cli add-appointment PET_ID "YYYY-MM-DD" "Reason"
```

### List Data

```bash
python -m vet_manager.cli list owners
python -m vet_manager.cli list pets
python -m vet_manager.cli list appointments
```

## Development

The code is contained in the `vet_manager` package. No additional dependencies are required.
