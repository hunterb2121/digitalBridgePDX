from flask import render_template, request, flash, redirect, url_for
from . import public_bp
from ...forms.public.general_contact_form import GeneralContactForm
from ...models.GeneralFormModel import GeneralFormModel


@public_bp.route("/contact", methods=["GET", "POST"])
def contact():
    general_form = GeneralContactForm()

    if request.method == "POST":
        if general_form.validate_on_submit():
            GeneralFormModel.insert(
                [
                    "name",
                    "email",
                    "phone_number",
                    "message"
                ],
                (
                    general_form.name.data,
                    general_form.email.data,
                    general_form.phone_number.data,
                    general_form.message.data
                )
            )
            flash("Form submitted successfully!", "success")
            return redirect(url_for("public.contact"))
        else:
            flash("There was a problem submitting your form. Please check your form inpurt and try again.", "danger")

    return render_template(
        "public/contact.html",
        general_form=general_form
    )