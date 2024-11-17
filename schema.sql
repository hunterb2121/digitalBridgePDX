CREATE TYPE form_status ENUM('pending', 'in review', 'contacted', 'completed', 'unknown', 'N/A');
CREATE TYPE experience ENUM('0-1', '1-5', '5-10', '10+', 'unknown', 'N/A');
CREATE TYPE support_type ENUM('in-person', 'in-home', 'over the phone', 'unknown', 'N/A');
CREATE TYPE aid_needs ENUM('computer', 'cell phone', 'tablet', 'bills', 'other', 'unknown', 'N/A');
CREATE TYPE income ENUM('less than 30,001', '30,001-58,020', '58,021-94,000', '94,001-153,000', 'greater than 153,000', 'unknown', 'N/A');
CREATE TYPE donating ENUM('computer', 'cell phone', 'tablet', 'other device', 'money', 'unknown', 'N/A');
CREATE TYPE donation_status ENUM('pending', 'received', 'distributed', 'unknown', 'N/A');
CREATE TYPE device_condition ENUM('new', 'like new', 'good', 'needs repair', 'unknown', 'N/A');
CREATE TYPE device_status ENUM('in use', 'in storage', 'out for repair', 'unknown', 'N/A');

/* Tables for the Different Forms */
CREATE TABLE volunteer_registration (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    phone_number VARCHAR NOT NULL,
    it_experience BOOLEAN NOT NULL,
    other_experience BOOLEAN NOT NULL,
    years_experience experience NOT NULL,
    additional_information TEXT,
    status form_status NOT NULL DEFAULT 'pending',
    submitted_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX volunteer_registration_name_idx ON volunteer_registration (name);
CREATE INDEX volunteer_registration_email_idx ON volunteer_registration (email);
CREATE INDEX volunteer_registration_status_idx ON volunteer_registration (status);
CREATE INDEX volunteer_registration_submitted_date_idx ON volunteer_registration (submitted_date);

CREATE TABLE volunteer_interests (
    volunteer_id BIGINT NOT NULL REFERENCES volunteer_registration (id) ON DELETE CASCADE,
    interest_id BIGINT NOT NULL REFERENCES volunteer_roles (id) ON DELETE CASCADE,
    PRIMARY KEY (volunteer_id, interest_id)
);

CREATE TABLE volunteer_roles (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL UNIQUE,
    description VARCHAR NOT NULL
);

CREATE INDEX volunteer_roles_title_idx ON volunteer_roles (title);

CREATE TABLE partner_registration (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    business_name VARCHAR NOT NULL,
    contact_name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    phone_number VARCHAR NOT NULL,
    message TEXT,
    status form_status NOT NULL DEFAULT 'pending',
    submitted_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX partner_registration_business_name_idx ON partner_registration (business_name);
CREATE INDEX partner_registration_contact_name_idx ON partner_registration (contact_name);
CREATE INDEX partner_registration_email_idx ON partner_registration (email);
CREATE INDEX partner_registration_status_idx ON partner_registration (status);
CREATE INDEX partner_registration_submitted_date_idx ON partner_registration (submitted_date);

CREATE TABLE general_form (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    phone_number VARCHAR NOT NULL,
    message TEXT,
    status form_status NOT NULL DEFAULT 'pending',
    submitted_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX general_form_name_idx ON general_form (name);
CREATE INDEX general_form_email_idx ON general_form (email);
CREATE INDEX general_form_status_idx ON general_form (status);
CREATE INDEX general_form_submitted_date_idx ON general_form (submitted_date);

CREATE TABLE get_support_form (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    phone_number VARCHAR,
    type_of_support support_type NOT NULL,
    problem_description TEXT NOT NULL,
    status form_status NOT NULL DEFAULT 'pending',
    submitted_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX get_support_form_name_idx ON get_support_form (name);
CREATE INDEX get_support_form_email_idx ON get_support_form (email);
CREATE INDEX get_support_form_status_idx ON get_support_form (status);
CREATE INDEX get_support_form_submitted_date_idx ON get_support_form (submitted_date);

CREATE TABLE get_support_times (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    support_form_id BIGINT NOT NULL REFERENCES get_support_form (id) ON DELETE CASCADE,
    morning BOOLEAN NOT NULL,
    afternoon BOOLEAN NOT NULL,
    evening BOOLEAN NOT NULL
);

CREATE TABLE new_class_request_form (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    phone_number VARCHAR NOT NULL,
    class_idea TEXT NOT NULL,
    status form_status NOT NULL DEFAULT 'pending',
    submitted_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX new_class_request_form_name_idx ON new_class_request_form (name);
CREATE INDEX new_class_request_form_email_idx ON new_class_request_form (email);
CREATE INDEX new_class_request_form_status_idx ON new_class_request_form (status);
CREATE INDEX new_class_request_form_submitted_date_idx ON new_class_request_form (submitted_date);

CREATE TABLE need_aid_form (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    phone_number VARCHAR,
    whats_needed aid_needs NOT NULL,
    yearly_income income NOT NULL,
    additional_information TEXT NOT NULL,
    status form_status NOT NULL DEFAULT 'pending',
    submitted_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX need_aid_form_name_idx ON need_aid_form (name);
CREATE INDEX need_aid_form_email_idx ON need_aid_form (email);
CREATE INDEX need_aid_form_status_idx ON need_aid_form (status);
CREATE INDEX need_aid_form_submitted_date_idx ON need_aid_form (submitted_date);

CREATE TABLE donating_form (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    phone_number VARCHAR,
    what_donating donating NOT NULL,
    additional_information TEXT,
    status form_status NOT NULL DEFAULT 'pending',
    submitted_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX donating_form_name_idx ON donating_form (name);
CREATE INDEX donating_form_email_idx ON donating_form (email);
CREATE INDEX donating_form_status_idx ON donating_form (status);
CREATE INDEX donating_form_submitted_date_idx ON donating_form (submitted_date);

/* Tables for resources */
CREATE TABLE class_recordings (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL UNIQUE,
    description VARCHAR NOT NULL,
    file_path VARCHAR NOT NULL,
    date_recorded DATE NOT NULL DEFAULT CURRENT_DATE,
    tags VARCHAR [],
    duration INTERVAL NOT NULL
);

CREATE INDEX class_recordings_title_idx ON class_recordings (title);
CREATE INDEX class_recording_date_recorded_idx ON class_recordings (date_recorded);

CREATE TABLE external_resources (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL UNIQUE,
    description VARCHAR NOT NULL,
    url VARCHAR NOT NULL,
    category VARCHAR NOT NULL
);

CREATE INDEX external_resources_title_idx ON external_resources (title);

CREATE TABLE internal_resources (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL UNIQUE,
    description VARCHAR NOT NULL,
    file_path VARCHAR NOT NULL,
    category VARCHAR NOT NULL,
    date_created DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX internal_resources_title_idx ON internal_resources (title);

/* Tables for internal information */
CREATE TABLE classes (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    location VARCHAR NOT NULL
);

CREATE INDEX classes_title_idx ON classes (title);
CREATE INDEX classes_date_idx ON classes (date);
CREATE INDEX classes_location_idx ON classes (location);

CREATE TABLE volunteers (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    availability VARCHAR NOT NULL,
    availability_notes TEXT,
    skills VARCHAR [],
    volunteer_since DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX volunteers_name_idx ON volunteers (name);
CREATE INDEX volunteers_email_idx ON volunteers (email);

CREATE TABLE volunteers_jobs (
    volunteers_id BIGINT NOT NULL REFERENCES volunteers (id) ON DELETE CASCADE,
    role_id BIGINT NOT NULL REFERENCES volunteer_roles (id) ON DELETE CASCADE,
    PRIMARY KEY (volunteers_id, role_id)
);

CREATE TABLE volunteer_assignments (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    volunteer_id BIGINT NOT NULL REFERENCES volunteers (id) ON DELETE CASCADE,
    task_type VARCHAR NOT NULL,
    description TEXT,
    assignment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    completion_date DATE
);

CREATE INDEX volunteer_assignments_task_type_idx ON volunteer_assignments (task_type);

CREATE TABLE donations (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    what_donated donating NOT NULL,
    quantity INTEGER NOT NULL,
    specific_donation_info VARCHAR NOT NULL,
    donor_name VARCHAR NOT NULL,
    donor_email VARCHAR NOT NULL,
    donor_phone_number VARCHAR,
    status donation_status NOT NULL DEFAULT 'pending',
    notes TEXT,
    donated_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX donations_what_donated_idx ON donations (what_donated);
CREATE INDEX donations_donor_name_idx ON donations (donor_name);
CREATE INDEX donations_donor_email_idx ON donations (donor_email);
CREATE INDEX donations_status_idx ON donations (status);
CREATE INDEX donations_donated_date_idx ON donations (donated_date);

CREATE TABLE received_aid (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    phone_number VARCHAR,
    what_received donating NOT NULL,
    date_aid_received DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX received_aid_name_idx ON received_aid (name);
CREATE INDEX received_aid_email_idx ON received_aid (email);
CREATE INDEX received_aid_what_received_idx ON received_aid (what_received);
CREATE INDEX received_aid_date_aid_received_idx ON received_aid (date_aid_received);

CREATE TABLE partners (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    business_name VARCHAR NOT NULL,
    contact_person VARCHAR NOT NULL,
    contact_email VARCHAR NOT NULL,
    contact_phone VARCHAR NOT NULL,
    notes TEXT
);

CREATE INDEX partners_business_name_idx ON partners (business_name);
CREATE INDEX partners_contact_person_idx ON partners (contact_person);
CREATE INDEX partners_email_idx ON partners (contact_email);
CREATE INDEX partners_phone_idx ON partners (contact_phone);

CREATE TABLE internal_inventory (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    device_type VARCHAR NOT NULL,
    device_manf VARCHAR NOT NULL,
    device_model VARCHAR NOT NULL,
    serial_number VARCHAR NOT NULL UNIQUE,
    condition device_condition NOT NULL,
    date_acquired DATE NOT NULL DEFAULT CURRENT_DATE,
    acquisition_source VARCHAR NOT NULL,
    notes TEXT NOT NULL,
    value NUMERIC(7,2) NOT NULL,
    current_location VARCHAR NOT NULL,
    purpose VARCHAR NOT NULL,
    assigned_to BIGINT REFERENCES volunteers (id),
    last_assigned DATE,
    status device_status NOT NULL
);

CREATE INDEX internal_inventory_device_type_idx ON internal_inventory (device_type);
CREATE INDEX internal_inventory_serial_number ON internal_inventory (serial_number);
CREATE INDEX internal_inventory_date_acquired_idx ON internal_inventory (date_acquired);
CREATE INDEX internal_inventory_acquisition_source_idx ON internal_inventory (acquisition_source);
CREATE INDEX internal_inventory_value_idx ON internal_inventory (value);
CREATE INDEX internal_inventory_current_location_idx ON internal_inventory (current_location);
CREATE INDEX internal_inventory_purpose_idx ON internal_inventory (purpose);
CREATE INDEX internal_inventory_assigned_to_idx ON internal_inventory (assigned_to);
CREATE INDEX internal_inventory_status_idx ON internal_inventory (status);

CREATE TABLE donation_inventory (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    device_type VARCHAR NOT NULL,
    device_manf VARCHAR NOT NULL,
    device_model VARCHAR NOT NULL,
    serial_number VARCHAR NOT NULL UNIQUE,
    condition device_condition NOT NULL,
    date_acquired DATE NOT NULL DEFAULT CURRENT_DATE,
    acquisition_source VARCHAR NOT NULL,
    notes TEXT NOT NULL,
    value NUMERIC(7,2) NOT NULL,
    current_location VARCHAR NOT NULL,
    recipient BIGINT REFERENCES received_aid (id),
    donation_information BIGINT REFERENCES donations (id),
    when_donated DATE,
    repair_needed BOOLEAN NOT NULL,
    repair_cost_estimate NUMERIC(7,2) DEFAULT 0.00
);

CREATE INDEX donation_inventory_device_type_idx ON donation_inventory (device_type);
CREATE INDEX donation_inventory_serial_number ON donation_inventory (serial_number);
CREATE INDEX donation_inventory_date_acquired_idx ON donation_inventory (date_acquired);
CREATE INDEX donation_inventory_acquisition_source_idx ON donation_inventory (acquisition_source);
CREATE INDEX donation_inventory_value_idx ON donation_inventory (value);
CREATE INDEX donation_inventory_current_location_idx ON donation_inventory (current_location);
CREATE INDEX donation_inventory_recipient_idx ON donation_inventory (recipient);
CREATE INDEX donation_inventory_donation_information_idx ON donation_inventory (donation_information);
CREATE INDEX donation_inventory_when_donated_idx ON donation_inventory (when_donated);
CREATE INDEX donation_inventory_repair_needed_idx ON donation_inventory (repair_needed);

CREATE TABLE audit_logs (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    table_name VARCHAR NOT NULL,
    record_id BIGINT NOT NULL,
    action_type VARCHAR NOT NULL,
    performed_by VARCHAR NOT NULL,
    change_details JSONB NOT NULL,
    change_timestamp TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX audit_logs_table_name_idx ON audit_logs (table_name);
CREATE INDEX audit_logs_record_id_idx ON audit_logs (record_id);
CREATE INDEX audit_logs_action_type_idx ON audit_logs (action_type);
CREATE INDEX audit_logs_performed_by_idx ON audit_logs (performed_by);
CREATE INDEX audit_logs_change_timestamp_idx ON audit_logs (change_timestamp);