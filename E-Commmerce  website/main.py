from dto.catalogue_dto import Catalogue
from service.catalogue_service import CatalogueService
from util.validators import validate_boolean, validate_date, validate_int
from exceptions.exceptions import CatalogueNotFoundError, InvalidCatalogueInputError


service= CatalogueService()

def display_menu():
    print("----Catalogue Management Menu----")
    print("1. Create Catalogue")
    print("2. Get Catalogue by ID") 
    print("3. Update Catalogue by ID")  
    print("4. Delete Catalogue by ID")
    print("5. Get All Catalogues")  
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                catalogue_id = validate_int(input("Catalogue ID: "))
                name = input("Catalogue Name: ").strip()
                if not name:
                    raise InvalidCatalogueInputError("Catalogue name cannot be empty.")
                version = input("Version: ").strip()
                if not version:
                    raise InvalidCatalogueInputError("Version cannot be empty.")
                is_active = validate_boolean(int(input("Is Active (1 or 0): ")))
                start_date = validate_date(input("Start Date (YYYY-MM-DD): "))
                end_date = validate_date(input("End Date (YYYY-MM-DD): "))

                catalogue=Catalogue(catalogue_id, name, version,is_active, start_date, end_date)
                service.create_catalogue(catalogue)
                print(f"Successfully created a catalogue with ID: {catalogue_id}.")
            except InvalidCatalogueInputError as e:
                print(f"Invalid input error :{e}")  


        elif choice == "2":
            try:
                catalogue_id = validate_int(input("Catalogue ID: "))
                catalogue = service.get_catalogue_by_id(catalogue_id)
                if catalogue:
                    print(vars(catalogue))
                else:
                    raise CatalogueNotFoundError(f"Catalogue ID {catalogue_id} not found.")
            except CatalogueNotFoundError as e:
                print(f"Error in finding the catalogue :{e}")
            except ValueError as e:
                print(f"Value error: {e}. Please enter a valid integer ID.")

        elif choice == "3":
            try:
                catalogue_id = validate_int(input("Catalogue ID: "))
                name = input("New Catalogue Name: ").strip()
                if not name:
                    raise InvalidCatalogueInputError("Catalogue name cannot be empty.")
                version = input("New Version: ")
                if not version:
                    raise InvalidCatalogueInputError("Version cannot be empty.")
                is_active = validate_boolean((input("Is Active (1 or 0): ")))
                start_date = validate_date(input("Start Date (YYYY-MM-DD): "))
                end_date = validate_date(input("End Date (YYYY-MM-DD): "))

                update_catalogue= Catalogue(catalogue_id, name, version, is_active, start_date, end_date)
                service.update_catalogue_by_id(catalogue_id, update_catalogue)
                print(f"Catalogue with ID {catalogue_id} updated successfully.")
            except (CatalogueNotFoundError, InvalidCatalogueInputError, ValueError) as e:
                print(f"Error Occured: {e}")

        elif choice == "4":
            try:
                catalogue_id = validate_int(input("Catalogue ID: "))
                service.delete_catalogue_by_id(catalogue_id)
                print(f"Catalogue with ID {catalogue_id} deleted successfully.")
            except (CatalogueNotFoundError,ValueError) as e:
                print(f"Error Occured: {e}")

        elif choice == "5":
            catalogues = service.get_all_catalogues()
            if catalogues:
                for c in catalogues:
                    print(vars(c))
            else:
                print("No catalogues found.")

        elif choice == "6":
            print("Exiting.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

