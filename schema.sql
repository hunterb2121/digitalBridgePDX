-- ENUMS for standardizing data
CREATE TYPE form_status ENUM('pending', 'in review', 'contacted', 'completed', 'unknown', 'N/A');
CREATE TYPE experience ENUM('0-1', '1-5', '5-10', '10+', 'unknown', 'N/A');
CREATE TYPE support_type ENUM('in-person', 'in-home', 'over the phone', 'unknown', 'N/A');
CREATE TYPE aid_needs ENUM('computer', 'cell phone', 'tablet', 'bills', 'other', 'unknown', 'N/A');
CREATE TYPE income ENUM('less than 30,001', '30,001-58,020', '58,021-94,000', '94,001-153,000', 'greater than 153,000', 'unknown', 'N/A');
CREATE TYPE donating ENUM('computer', 'cell phone', 'tablet', 'other device', 'money', 'unknown', 'N/A');
CREATE TYPE donation_status ENUM('pending', 'received', 'distributed', 'unknown', 'N/A');
CREATE TYPE device_condition ENUM('new', 'like new', 'good', 'needs repair', 'unknown', 'N/A');
CREATE TYPE device_status ENUM('in use', 'in storage', 'out for repair', 'unknown', 'N/A');

-- Volunteer Registration Form
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

-- Apply chosen volunteer jobs that were marked in the volunteer registration form
CREATE TABLE volunteer_interests (
    volunteer_id BIGINT NOT NULL REFERENCES volunteer_registration (id) ON DELETE CASCADE,
    interest_id BIGINT NOT NULL REFERENCES volunteer_jobs (id) ON DELETE CASCADE,
    PRIMARY KEY (volunteer_id, interest_id)
);

-- All the volunteer jobs available that are posted on the website
CREATE TABLE volunteer_jobs (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL UNIQUE,
    description VARCHAR NOT NULL
);

CREATE INDEX volunteer_jobs_title_idx ON volunteer_jobs (title);

-- Partner Registration Form
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

-- General Contact Form
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

-- Get Tech Support Form
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

-- Times available for tech support and marking which were chosen on the Get Tech Support Form
CREATE TABLE get_support_times (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    support_form_id BIGINT NOT NULL REFERENCES get_support_form (id) ON DELETE CASCADE,
    morning BOOLEAN NOT NULL,
    afternoon BOOLEAN NOT NULL,
    evening BOOLEAN NOT NULL
);

-- New Class Idea Request Form
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

-- Financial / Device Aid Registration Form
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

-- Donation Form
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

-- Recordings of Classes
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

-- External Resources
CREATE TABLE external_resources (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL UNIQUE,
    description VARCHAR NOT NULL,
    url VARCHAR NOT NULL,
    category VARCHAR NOT NULL
);

CREATE INDEX external_resources_title_idx ON external_resources (title);

-- Internal Resources
CREATE TABLE internal_resources (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL UNIQUE,
    description VARCHAR NOT NULL,
    file_path VARCHAR NOT NULL,
    category VARCHAR NOT NULL,
    date_created DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX internal_resources_title_idx ON internal_resources (title);

-- Translations for resources (blog posts, internal resources, classes, etc) and whether they are done or not
CREATE TABLE translations (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    content_type VARCHAR NOT NULL,
    content_id BIGINT NOT NULL,
    language VARCHAR NOT NULL,
    fully_translated BOOLEAN NOT NULL DEFAULT FALSE,
    translated_date DATE 
);

CREATE INDEX translations_content_type_idx ON translations (content_type);
CREATE INDEX translations_language_idx ON translations (language);
CREATE INDEX translations_fully_translated_idx ON translations (fully_translated);
CREATE INDEX translations_translated_date_idx ON translations (translated_date);

-- Marking resources and things that need to be more accessible for people with disabilities and progress towards that
CREATE TABLE accessibility_requests (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    resource_id BIGINT NOT NULL,
    request_type VARCHAR NOT NULL,
    description TEXT,
    request_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX accessibility_requests_resource_id_idx ON accessibility_requests (resource_id);
CREATE INDEX accessibility_requests_request_type_idx ON accessibility_requests (request_type);
CREATE INDEX accessibility_requests_request_date_idx ON accessibility_requests (request_date);

-- Hold information for all events
CREATE TABLE events (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    location VARCHAR NOT NULL
);

-- Hold information for the different classes
CREATE TABLE classes (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL,
    description TEXT NOT NULL
);

CREATE INDEX classes_title_idx ON classes (title);
CREATE INDEX classes_date_idx ON classes (date);
CREATE INDEX classes_location_idx ON classes (location);

-- Hold information for the volunteers
CREATE TABLE volunteers (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    phone_number VARCHAR UNIQUE,
    password_hash VARCHAR NOT NULL,
    availability VARCHAR NOT NULL,
    availability_notes TEXT,
    skills VARCHAR [],
    volunteer_since DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX volunteers_name_idx ON volunteers (name);
CREATE INDEX volunteers_email_idx ON volunteers (email);

-- Hold information for what jobs that volunteers assigned and able to do
CREATE TABLE volunteers_assigned_jobs (
    volunteer_id BIGINT NOT NULL REFERENCES volunteers (id) ON DELETE CASCADE,
    job_id BIGINT NOT NULL REFERENCES volunteer_jobs (id) ON DELETE CASCADE,
    assigned_date DATE NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (volunteer_id, job_id)
);

-- Hold the different RBAC roles for the website
CREATE TABLE site_roles (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL UNIQUE,
    description TEXT
);

CREATE INDEX site_roles_title_idx ON site_roles (title);

-- Assign different roles to the different volunteers
CREATE TABLE user_roles (
    volunteers_id BIGINT NOT NULL REFERENCES volunteers (id) ON DELETE CASCADE,
    role_id BIGINT NOT NULL REFERENCES site_roles (id) ON DELETE CASCADE,
    assigned_date DATE NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (volunteers_id, role_id)
);

-- Hold the different assignments and tasks that are in the works
CREATE TABLE assignments (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    task_type VARCHAR NOT NULL,
    description TEXT,
    assignment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    completion_date DATE
);

CREATE INDEX volunteer_assignments_task_type_idx ON volunteer_assignments (task_type);

-- Assign the different volunteers to the different assignments/tasks
CREATE TABLE volunteers_assignments (
    volunteer_id BIGINT NOT NULL REFERENCES volunteers (id),
    assignment_id BIGINT NOT NULL REFERENCES assignments (id),
    assigned_date DATE NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (volunteer_id, assignement_id)
);

CREATE INDEX volunteers_assignments_volunteer_id_idx ON volunteers_assignments (volunteer_id);
CREATE INDEX volunteers_assignments_assignment_id_idx ON volunteers_assignments (assignment_id);

-- Assign the different volunteers to different events
CREATE TABLE event_volunteers (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    event_id BIGINT NOT NULL REFERENCES events (id) ON DELETE CASCADE,
    volunteer_id BIGINT NOT NULL REFERENCES volunteers (id) ON DELETE CASCADE,
    role VARCHAR NOT NULL,
    assignment_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX event_volunteers_event_id_idx ON event_volunteers (event_id);
CREATE INDEX event_volunteers_volunteer_id_idx ON event_volunteers (volunteer_id);
CREATE INDEX event_volunteers_role_idx ON event_volunteers (role);

-- Hold the different categories for tech support (e.g., software, network, hardware, etc.)
CREATE TABLE tech_support_categories (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR NOT NULL UNIQUE,
    description TEXT
);

CREATE INDEX tech_support_categories_name_idx ON tech_support_categories (name);

-- Hold information for the different tech support tickets that have been created based off of requests from the Get Support Form, email, and phone
CREATE TABLE tech_support_tickets (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    requester_name VARCHAR NOT NULL,
    requester_email VARCHAR NOT NULL,
    requester_phone VARCHAR,
    type_of_support support_type NOT NULL,
    problem_description TEXT NOT NULL,
    category_id BIGINT REFERENCES tech_support_categories (id),
    status form_status NOT NULL DEFAULT 'pending',
    assigned_to BIGINT REFERENCES volunteers (id),
    submitted_date DATE NOT NULL DEFAULT CURRENT_DATE,
    resolved_date DATE
);

CREATE INDEX tech_support_tickets_requester_name_idx ON tech_support_tickets (requester_name);
CREATE INDEX tech_support_tickets_requester_email_idx ON tech_support_tickets (requester_email);
CREATE INDEX tech_support_tickets_type_of_support_idx ON tech_support_tickets (type_of_support);
CREATE INDEX tech_support_tickets_category_id_idx ON tech_support_tickets (category_id);
CREATE INDEX tech_support_tickets_status_idx ON tech_support_tickets (status);
CREATE INDEX tech_support_tickets_assigned_to_idx ON tech_support_tickets (assigned_to);
CREATE INDEX tech_support_tickets_submitted_date_idx ON tech_support_tickets (submitted_date);

-- Hold notes for the different tech support tickets to keep track of what has happened on the tech support tickets
CREATE INDEX tech_support_notes (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    request_id BIGINT NOT NULL REFERENCES tech_support_tickets (id) ON DELETE CASCADE,
    note_author BIGINT NOT NULL REFERENCES volunteers (id),
    note_text TEXT NOT NULL,
    note_date TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX tech_support_notes_request_id_idx ON tech_support_notes (request_id);
CREATE INDEX tech_support_notes_note_author_idx ON tech_support_notes (note_author);

-- Hold the different internal resources (guides, common issues, common fixes, where to get additional help, etc.) to help with tech support issues
CREATE TABLE tech_support_resources (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL UNIQUE,
    description TEXT NOT NULL,
    file_path VARCHAR NOT NULL,
    category_id BIGINT REFERENCES support_categories (id),
    created_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX tech_support_resources_title_idx ON tech_support_resources (title);
CREATE INDEX tech_support_resources_file_path_idx ON tech_support_resources (file_path);
CREATE INDEX tech_support_resources_category_id_idx ON tech_support_resources (category_id);

-- Hold information for different donations
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

-- Hold information for people that have received aid
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

-- Hold information on different businesses we partner with
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

-- Hold information for grants that we are working on
CREATE TABLE grants (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL,
    description TEXT NOT NULL,
    submitted_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status VARCHAR NOT NULL,
    amount_requested NUMERIC(10, 2) NOT NULL,
    amount_awarded NUMERIC(10, 2)
);

CREATE INDEX grants_title_idx ON grants (title);
CREATE INDEX grants_submitted_date_idx ON grants (submitted_date);
CREATE INDEX grants_status_idx ON grants (status);

-- Hold information for the different fundraising activities we are holding
CREATE TABLE fundraising_activities (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL,
    description TEXT NOT NULL,
    goal_amount NUMERIC(10, 2) NOT NULL,
    funds_raised NUMERIC(10, 2) NOT NULL DEFAULT 0.00,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE INDEX fundraising_activities_title_idx ON fundraising_activities (title);
CREATE INDEX fundraising_activities_goal_amount_idx ON fundraising_activities (goal_amount);
CREATE INDEX fundraising_activities_funds_raised_idx ON fundraising_activities (funds_raised);
CREATE INDEX fundraising_activities_start_date_idx ON fundraising_activities (start_date);
CREATE INDEX fundraising_activities_end_date_idx ON fundraising_activities (end_date);

-- Hold the content for different social media posts
CREATE TABLE social_media_posts (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    platform VARCHAR NOT NULL,
    post_content TEXT NOT NULL,
    post_date DATE NOT NULL DEFAULT CURRENT_DATE,
    metrics JSONB
);

CREATE INDEX social_media_posts_platform_idx ON social_media_posts (platform);
CREATE INDEX social_media_posts_post_date_idx ON social_media_posts (post_date);

-- Hold images and videos that go with the different social media posts
CREATE TABLE social_media_posts_media (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    post_id BIGINT NOT NULL REFERENCES social_media_posts (id) ON DELETE CASCADE,
    post_media_url VARCHAR NOT NULL
);

-- Hold information on all the devices that we currently have in our inventory
CREATE TABLE devices (
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
    repair_needed BOOLEAN NOT NULL,
    repair_cost_estimate NUMERIC(7,2) DEFAULT 0.00,
    repair_history BIGINT REFERENCES repair_logs (id)
);

CREATE INDEX devices_device_type_idx ON devices (device_type);
CREATE INDEX devices_device_manf_idx ON devices (device_manf);
CREATE INDEX devices_device_model_idx ON devices (device_model);
CREATE INDEX devices_serial_number_idx ON devices (serial_number);
CREATE INDEX devices_condition_idx ON devices (condition);
CREATE INDEX devices_date_acquired_idx ON devices (date_acquired);
CREATE INDEX devices_acquisition_source_idx ON devices (acquisition_source);
CREATE INDEX devices_value_idx ON devices (value);
CREATE INDEX devices_current_location_idx ON devices (current_location);
CREATE INDEX devices_repair_needed_idx ON devices (repair_needed);

-- Hold information for repairs that we are working on or have done for the different devices that we have received
CREATE TABLE repair_logs (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    device_id BIGINT NOT NULL REFERENCES devices (id) ON DELETE CASCADE,
    technician_id BIGINT NOT NULL REFERENCES volunteers (id),
    repair_date DATE NOT NULL DEFAULT CURRENT_DATE,
    description TEXT NOT NULL,
    cost NUMERIC(7,2),
    status device_status NOT NULL
);

CREATE INDEX repair_logs_device_id_idx ON repair_logs (device_id);
CREATE INDEX repair_logs_technician_id_idx ON repair_logs (technician_id);
CREATE INDEX repair_logs_repair_date_idx ON repair_logs (repair_date);
CREATE INDEX repair_logs_cost_idx ON repair_logs (cost);
CREATE INDEX repair_logs_status_idx ON repair_logs (status);

-- Hold specific information for devices that are for internal use (tech support, classes, etc.)
CREATE TABLE internal_inventory (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    device_id BIGINT NOT NULL REFERENCES devices (id) ON DELETE CASCADE,
    purpose VARCHAR NOT NULL,
    assigned_to BIGINT REFERENCES volunteers (id),
    last_assigned DATE,
    status device_status NOT NULL
);

CREATE INDEX internal_inventory_device_id_idx ON internal_inventory (device_id);
CREATE INDEX internal_inventory_purpose_idx ON internal_inventory (purpose);
CREATE INDEX internal_inventory_assigned_to_idx ON internal_inventory (assigned_to);
CREATE INDEX internal_inventory_last_assigned_idx ON internal_inventory (last_assigned);
CREATE INDEX internal_inventory_status_idx ON internal_inventory (status);

-- Hold specific information for devices that are being donated
CREATE TABLE donation_inventory (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    device_id BIGINT NOT NULL REFERENCES devices (id) ON DELETE CASCADE,
    recipient BIGINT REFERENCES received_aid (id),
    donation_information BIGINT REFERENCES donations (id),
    when_donated DATE NOT NULL
);

CREATE INDEX donation_inventory_device_id_idx ON donation_inventory (device_id);
CREATE INDEX donation_inventory_recipient_idx ON donation_inventory (recipient);
CREATE INDEX donation_inventory_donation_information_idx ON donation_inventory (donation_information);
CREATE INDEX donation_inventory_when_donated_idx ON donation_inventory (when_donated);

-- Hold logs for auditing things that have been done on the website for transparency, accountability, and tracking 
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

-- Hold different tags for things like blog posts, newsletters, classes, etc.
CREATE TABLE tags (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR NOT NULL UNIQUE
);

CREATE INDEX tags_name_idx ON tags (name);

-- Associate tags with specific blog posts
CREATE TABLE post_tags (
    post_id BIGINT NOT NULL REFERENCES blog_posts (id) ON DELETE CASCADE,
    tag_id BIGINT NOT NULL REFERENCES tags (id) ON DELETE CASCADE,
    PRIMARY KEY (post_id, tag_id)
);

-- Associate tags with specific newsletters
CREATE TABLE newsletter_tags (
    newsletter_id BIGINT NOT NULL REFERENCES newsletters (id) ON DELETE CASCADE,
    tag_id BIGINT NOT NULL REFERENCES tags (id) ON DELETE CASCADE,
    PRIMARY KEY (newsletter_id, tag_id)
);

-- Associate tags with specific class recordings
CREATE TABLE class_tags (
    class_id BIGINT NOT NULL REFERENCES class_recordings (id) ON DELETE CASCADE,
    tag_id BIGINT NOT NULL REFERENCES tags (id) ON DELETE CASCADE,
    PRIMARY KEY (class_id, tag_id)
);

-- Hold information for blog posts, including the file path (still working out how to best do blog posts)
CREATE TABLE blog_posts (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL,
    author_id BIGINT NOT NULL REFERENCES volunteers (id) ON DELETE SET NULL,
    file_path VARCHAR NOT NULL,
    published_date TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_published BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE INDEX blog_posts_title_idx ON blog_posts (title);
CREATE INDEX blog_posts_author_id_idx ON blog_posts (author_id);
CREATE INDEX blog_posts_published_date ON blog_posts (published_date);

-- Hold information for newsletters
CREATE TABLE newsletters (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR NOT NULL,
    issue_number INTEGER UNIQUE NOT NULL,
    file_path VARCHAR NOT NULL,
    published_date TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX newsletters_title_idx ON newsletters (title);
CREATE INDEX newsletters_issue_number_idx ON newsletters (issue_number);
CREATE INDEX newsletters_published_date_idx ON newsletters (published_date);