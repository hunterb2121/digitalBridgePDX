document.querySelectorAll(".register-button").forEach(button => {
    button.addEventListener("click", event => {
        const scheduleId = event.target.dataset.scheduleId;
        const eventId = event.target.dataset.eventId;
        const registrationForm = document.querySelector(`#register_class_form_${eventId}`);
        registrationForm.querySelector("input[name='schedule_id']").value = scheduleId;
    });
});