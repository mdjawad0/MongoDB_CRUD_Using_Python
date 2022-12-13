from DB import DB
from Classes import Pricing, SecurityGuard

def main():
    db = DB()

    while True:
        print("\n[1]: Add New Security Guard")
        print("[2]: Show All Security Guards")
        print("[3]: Update Existing Security Guard")
        print("[4]: Delete Existing Security Guard")
        print("[5]: Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            guard = SecurityGuard()
            guard.name = input("Enter Name of Security Guard: ")
            guard.phone = input("Enter Phone of Security Guard: ")
            guard.email = input("Enter Email of Security Guard: ")
            guard.gender = input("Enter Gender of Security Guard: ")
            guard.security_rating = float(input("Enter Ratings of Security Guard: "))

            pricing = Pricing()
            pricing.day = int(input("Enter Pricing for the Day: "))
            pricing.week = int(input("Enter Pricing for the Week: "))
            pricing.month = int(input("Enter Pricing for the Month: "))

            guard.pricing = vars(pricing)

            db.insert(document=vars(guard))

            print(guard.name, "Saved Successfully...")

        elif choice == "2":
            docs = db.query()
            for doc in docs:
                print(doc)

        elif choice == "3":
            guard = SecurityGuard()
            guard.phone = input("Enter Phone of Security Guard to update: ")
            query = {'phone': guard.phone}

            guard.name = input("Enter New Name of Security Guard: ")
            guard.email = input("Enter New Email of Security Guard: ")
            guard.gender = input("Enter New Gender of Security Guard: ")
            guard.security_rating = float(input("Enter New Ratings of Security Guard: "))

            pricing = Pricing()
            pricing.day = int(input("Enter New Pricing for the Day: "))
            pricing.week = int(input("Enter New Pricing for the Week: "))
            pricing.month = int(input("Enter New Pricing for the Month: "))

            guard.pricing = vars(pricing)

            db.update(document=vars(guard), query=query)

            print(guard.name, "Updated Successfully...")

        elif choice == "4":
            phone = input("Enter Phone of Security Guard to delete: ")
            query = {'phone': phone}

            db.delete(query=query)
            print("Guard with Phone Number", phone, "Deleted Successfully...")

        elif choice == "5":
            print("Thank You For Using the Application")
            break


if __name__ == "__main__":
    main()

