from flask import render_template, request, flash, redirect, url_for
from . import public_bp
from ...forms.public.volunteer_registration_form import VolunteerRegistrationForm
from ...forms.public.partner_registration_form import PartnerRegistrationForm
from ...models.VolunteerRegistrationModel import VolunteerRegistrationModel
from ...models.VolunteerInterestsModel import VolunteerInterestsModel
from ...models.VolunteerJobsModel import VolunteerJobsModel
from ...models.PartnerRegistrationModel import PartnerRegistrationModel


@public_bp.route("/get-involved", methods=["GET", "POST"])
def get_involved():
    volunteer_form = VolunteerRegistrationForm()
    partner_form = PartnerRegistrationForm()

    our_jobs = VolunteerJobsModel.get_all_records()
    job_title_to_id = {job[1].title(): job[0] for job in our_jobs}

    if request.method == "POST":
        if volunteer_form.validate_on_submit() and volunteer_form.form_type.data == "volunteer":
            jobs_interested = volunteer_form.volunteer_job.data
            selected_job_ids = [job_title_to_id[job_title.title()] for job_title in jobs_interested if job_title in job_title_to_id]

            volunteer_id = VolunteerRegistrationModel.insert(
                [
                    "name",
                    "email",
                    "phone_number",
                    "it_experience",
                    "other_experience",
                    "years_experience",
                    "additional_information"
                ],
                (
                    volunteer_form.name.data,
                    volunteer_form.email.data,
                    volunteer_form.phone_number.data,
                    volunteer_form.experience_in_it.data,
                    volunteer_form.other_experience.data,
                    volunteer_form.experience_amount.data,
                    volunteer_form.message.data
                )
            )
            for id in selected_job_ids:
                VolunteerInterestsModel.insert(
                    [
                        "volunteer_id",
                        "interest_id"
                    ],
                    (
                        volunteer_id,
                        id
                    )
                )
            flash("Form submitted successfully!", "success")
            return redirect(url_for("public.get_involved"))
        elif partner_form.validate_on_submit() and partner_form.form_type.data == "partner":
            PartnerRegistrationModel.insert(
                [
                    "business_name",
                    "contact_name",
                    "email",
                    "phone_number",
                    "message"
                ],
                (
                    partner_form.business_name.data,
                    partner_form.contact_name.data,
                    partner_form.email.data,
                    partner_form.phone_number.data,
                    partner_form.message.data
                )
            )
            flash("Form submitted successfully!", "success")
            return redirect(url_for("public.get_involved"))
        else:
            flash("There was a problem submitting your form. Please check your form input and try again.", "danger")

    return render_template(
        "public/get_involved.html", 
        our_jobs=our_jobs, 
        volunteer_form=volunteer_form, 
        partner_form=partner_form
    )