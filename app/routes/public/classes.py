from datetime import datetime, timedelta
from flask import render_template, request, flash, redirect, url_for
from . import public_bp
from ...forms.public.new_class_request_form import NewClassRequestForm
from ...models.NewClassRequestFormModel import NewClassRequestFormModel
from ...models.ClassesModel import ClassesModel
from ...models.ClassRecordingsModel import ClassRecordingsModel
from ...models.ClassTagsModel import ClassTagsModel
from ...models.TagsModel import TagsModel


@public_bp.route("/classes", methods=["GET", "POST"])
def classes():
    new_class_request_form = NewClassRequestForm()

    our_classes = ClassesModel.get_all_records() or None

    six_months_ago = datetime.now() - timedelta(days=6 * 30)

    query_recent_recordings = "SELECT * FROM class_recordings WHERE date_recorded >= %s ORDER BY date_recorded DESC;"

    class_recording_info = dict()

    recent_recordings = ClassRecordingsModel.get_all(query_recent_recordings, (six_months_ago,)) or None

    if recent_recordings:
        class_ids = [recording[0] for recording in recent_recordings]
        all_tags = ClassTagsModel.find_by_class_id(class_ids)

        for recording in recent_recordings:
            class_recording_info[recording[0]] = {
                "title": recording[1],
                "description": recording[2],
                "file_path": recording[3],
                "date_recorded": recording[4],
                "duration": recording[5],
                "tags": []
            }
            for tag in all_tags:
                class_recording_info[recording[0]]["tags"].append(TagsModel.find_by_id(tag[1]).name)

    if request.method == "POST":
        if new_class_request_form.validate_on_submit():
            NewClassRequestFormModel.insert(
                [
                    "name",
                    "email",
                    "phone_number",
                    "class_idea"
                ],
                (
                    new_class_request_form.name.data,
                    new_class_request_form.email.data,
                    new_class_request_form.phone_number.data,
                    new_class_request_form.class_idea.data
                )
            )
            flash("Form submitted successfully!", "success")
            return redirect(url_for("public.classes"))
        else:
            flash("There was a problem submitting your form. Please check your form input and try again.", "danger")

    return render_template(
        "public/classes.html", 
        class_list = our_classes,
        recent_recordings=recent_recordings,
        class_recordings=dict(sorted(class_recording_info)),
        request_form=new_class_request_form
    )