from flask import render_template
from . import public_bp
from ...models.InternalResourcesModel import InternalResourcesModel
from ...models.ClassRecordingsModel import ClassRecordingsModel
from ...models.ClassTagsModel import ClassTagsModel
from ...models.TagsModel import TagsModel
from ...models.ExternalResourcesModel import ExternalResourcesModel


@public_bp.route("/resources")
def resources():
    class_recording_info = dict()

    class_recordings = ClassRecordingsModel.get_all_records()
    all_tags = [ClassTagsModel.find_by_class_id(id) for id in [recording[0] for recording in class_recordings]]

    for recording in class_recordings:
        class_recording_info[recording[0]] = {
            "title": recording[1],
            "description": recording[2],
            "file_path": recording[3],
            "date_recorded": recording[4],
            "duration": recording[5],
            "tags": []
        }
        for tag in all_tags:
            class_recording_info[recording[0]]["tags"].append(TagsModel.find_by_id(tag[1])[1])

    internal_resources = InternalResourcesModel.get_all_records()
    external_resources = ExternalResourcesModel.get_all_records()

    return render_template(
        "public/resources.html",
        internal_resources=internal_resources,
        class_recordings=class_recording_info,
        external_resources=external_resources
    )