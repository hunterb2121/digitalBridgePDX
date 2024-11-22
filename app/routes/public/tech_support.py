from flask import render_template, request, flash, redirect, url_for
from . import public_bp
from ...forms.public.tech_support_form import TechSupportForm
from ...models.GetSupportFormModel import GetSupportFormModel
from ...models.GetSupportTimesModel import GetSupportTimesModel


@public_bp.route("/tech-support", methods=["GET", "POST"])
def tech_support():
    support_form = TechSupportForm()

    if request.method == "POST":
        if support_form.validate_on_submit():
            times = support_form.preferred_times.data
            support_id = GetSupportFormModel.insert_return_id(
                [
                    "name",
                    "email",
                    "phone_number",
                    "type_of_support",
                    "problem_description"
                ],
                (
                    support_form.name.data,
                    support_form.email.data,
                    support_form.phone_number.data,
                    support_form.support_location.data,
                    support_form.message.data
                )
            )
            GetSupportTimesModel.insert(
                [
                    "support_form_id",
                    "morning",
                    "afternoon",
                    "evening"
                ],
                (
                    support_id,
                    True if "morning" in times else False,
                    True if "afternoon" in times else False,
                    True if "evening" in times else False
                )
            )
            flash("Form submitted successfully!", "success")
            return redirect(url_for("public.tech_support"))
        else:
            flash("There was a problem submitting your form. Please check your form input and try again.", "danger")
    return render_template(
        "public/tech_support.html",
        support_form=support_form
    )