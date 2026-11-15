from flask import Flask, render_template, request, redirect, flash, session
from database import (
    create_table,
    add_donor,
    get_all_donors,
    get_donor_by_id,
    update_donor,
    delete_donor,
    get_donor_count
)

app = Flask(__name__)
app.secret_key = "bloodcare-secret-key"
ADMIN_PASSWORD = "change-this-password"

# Create database table
create_table()


# Home Page
@app.route("/")
def home():
    total_donors = get_donor_count()
    return render_template("index.html", total_donors=total_donors)


# Registration Page
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"].strip()
        age = request.form["age"]
        gender = request.form["gender"]
        blood_group = request.form["blood_group"]
        phone = request.form["phone"].strip()
        city = request.form["city"].strip()
        address = request.form["address"].strip()

        try:
            age = int(age)

            if age < 18 or not all([
                name, gender, blood_group,
                phone, city, address
            ]):
                raise ValueError

        except ValueError:
            flash("Please enter valid donor details.")
            return redirect("/register")

        add_donor(
            name, age, gender, blood_group,
            phone, city, address
        )

        flash("Donor registered successfully!")
        return redirect("/register")

    return render_template("register.html")



# Find Donors Page
@app.route("/donors")
def donors():

    all_donors = get_all_donors()

    blood_group = request.args.get("blood_group", "")
    city = request.args.get("city", "").strip()

    if blood_group:
        all_donors = [
            donor for donor in all_donors
            if donor[4] == blood_group
        ]

    if city:
        all_donors = [
            donor for donor in all_donors
            if city.casefold() in donor[6].casefold()
        ]

    return render_template(
        "donors.html",
        donors=all_donors,
        selected_group=blood_group,
        selected_city=city
    )


# Admin Login
@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":
        password = request.form.get("password", "")

        if password == ADMIN_PASSWORD:
            session["admin_logged_in"] = True
            return redirect("/admin")

        flash("Incorrect password. Please try again.")

    return render_template("admin_login.html")


# Admin Dashboard
@app.route("/admin")
def admin_dashboard():

    if not session.get("admin_logged_in"):
        return redirect("/admin-login")

    all_donors = get_all_donors()

    return render_template(
        "admin.html",
        donors=all_donors
    )


# Edit Donor
@app.route("/edit-donor/<int:donor_id>", methods=["GET", "POST"])
def edit_donor(donor_id):

    if not session.get("admin_logged_in"):
        return redirect("/admin-login")

    donor = get_donor_by_id(donor_id)

    if donor is None:
        flash("Donor not found.")
        return redirect("/admin")

    if request.method == "POST":

        name = request.form["name"].strip()
        age = request.form["age"]
        gender = request.form["gender"]
        blood_group = request.form["blood_group"]
        phone = request.form["phone"].strip()
        city = request.form["city"].strip()
        address = request.form["address"].strip()

        try:
            age = int(age)

            if age < 18 or not all([
                name, gender, blood_group,
                phone, city, address
            ]):
                raise ValueError

        except ValueError:
            flash("Please enter valid donor details.")
            return redirect(f"/edit-donor/{donor_id}")

        update_donor(
            donor_id, name, age, gender,
            blood_group, phone, city, address
        )

        flash("Donor details updated successfully!")
        return redirect("/admin")

    return render_template("edit_donor.html", donor=donor)


# Delete Donor
@app.route("/delete-donor/<int:donor_id>", methods=["POST"])
def remove_donor(donor_id):

    if not session.get("admin_logged_in"):
        return redirect("/admin-login")

    delete_donor(donor_id)

    flash("Donor deleted successfully!")
    return redirect("/admin")

# Admin Logout
@app.route("/admin-logout")
def admin_logout():

    session.pop("admin_logged_in", None)
    return redirect("/admin-login")

# Start Flask Server
if __name__ == "__main__":
    app.run(debug=True)