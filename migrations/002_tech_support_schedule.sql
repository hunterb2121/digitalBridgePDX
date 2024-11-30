-- Table to hold in person tech support schedules
CREATE TABLE IF NOT EXISTS tech_support_schedule (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    event_id BIGINT NOT NULL REFERENCES events (id) ON DELETE CASCADE,
    end_time TIME NOT NULL
);

ALTER TABLE class_schedule ADD end_time TIME NOT NULL;