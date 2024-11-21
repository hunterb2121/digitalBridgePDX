from flask import render_template, request, flash, redirect, url_for
from . import public_bp
from ...forms.public.need_aid_form import NeedAidForm
from ...forms.public.donate_form import DonateForm
from ...models.NeedAidFormModel import NeedAidFormModel
from ...models.DonatingFormModel import DonatingFormModel


@public_bp.route("/aid-fund-and-donations", methods=["GET", "POST"])
def aid_fund_donations():
    need_aid = NeedAidForm()
    donate = DonateForm()

    if request.method == "POST":
        if need_aid.validate_on_submit() and need_aid.form_type.data == "need_aid":
            NeedAidFormModel.insert(
                [
                    "name", 
                    "email", 
                    "phone_number", 
                    "whats_needed", 
                    "yearly_income", 
                    "additional_information"
                ], 
                (
                    need_aid.name.data, 
                    need_aid.email.data, 
                    need_aid.phone_number.data, 
                    need_aid.aid_type.data, 
                    need_aid.income.data, 
                    need_aid.message.data
                )
            )
            flash("Form submitted successfully!", "success")
            return redirect(url_for("public.aid_fund_donations"))
        
        elif donate.validate_on_submit() and donate.form_type.data == "donate":
            DonatingFormModel.insert(
                [
                    "name",
                    "email",
                    "phone_number",
                    "what_donating",
                    "additional_information"
                ],
                (
                    donate.name.data,
                    donate.email.data,
                    donate.phone_number.data,
                    donate.donate_type.data,
                    donate.message.data
                )
            )
        else:
            flash("There was a problem submitting your form. Please check your form input and try again.", "danger")
        
    return render_template(
        "public/aid_fund_donations.html",
        need_aid_form=need_aid,
        donate_form=donate
    )