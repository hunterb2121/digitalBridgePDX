-- Create volunteer opportunities/jobs
INSERT INTO volunteer_jobs (title, description)
VALUES ('Tech Support', 'Provide free technical assistance to community members, including troubleshooting, repairs, setup, and advice for various devices and software.');
INSERT INTO volunteer_jobs (title, description)
VALUES ('Teaching', 'Lead or assist with classes covering a range of topics, from basic device usage to more advanced skills like coding or IT support.');
INSERT INTO volunteer_jobs (title, description)
VALUES ('Community Outreach', 'Build connections with local organizations, promote the network\'s services, and raise awareness to attract participants and volunteers.');
INSERT INTO volunteer_jobs (title, description)
VALUES ('Inventory and Resource Management', 'Organize and catalog donated devices and supplies, and track distributed resources to ensure effective use of donations.');
INSERT INTO volunteer_jobs (title, description)
VALUES ('Communications and Social Media', 'Manage social media platforms, write newsletters, and create promotional materials to engage with the community and share updates.');
INSERT INTO volunteer_jobs (title, description)
VALUES ('Translation and Accessibility Services', 'Translate materials into multiple languages and ensure that resources and events are accessible to people with disabilities.');
INSERT INTO volunteer_jobs (title, description)
VALUES ('Event Planning and Logistics', 'Coordinate in-person classes, tech support drop-ins, and other events, ensuring all logistical needs - space, equipment, and volunteers - are met.');
INSERT INTO volunteer_jobs (title, description)
VALUES ('Web Development and Content Management', 'Maintain and update the network\'s website, upload class schedules and recordings, and manage a potential blog or other digital tools.');
INSERT INTO volunteer_jobs (title, description)
VALUES ('Fundraising and Grant Writing', 'Help secure funding by writing grant proposals, organizing fundraisers, or reaching out to local businesses and sponsors.');
INSERT INTO volunteer_jobs (title, description)
VALUES ('Device Refurbishment and Repair', 'Assess and repair donated devices, ensuring they are functional and ready to be distributed to community members in need.');
INSERT INTO volunteer_jobs (title, description)
VALUES ('Purchasing and Procurement', 'Manage sourcing and purchasing of tech supplies, tools, and other resources needed for classes, tech support, and community donations.');

-- Create classes
INSERT INTO classes (title, description)
VALUES ('Device Basics', 'Learn the basics of computers, tablets, and smartphones. And, learn about the most recent Operating Systems (Windows, MacOS, Linux, iOS, and Android), file management, and device settings.');
INSERT INTO classes (title, description)
VALUES ('Office Tools', 'Practical training on LibreOffice and Microsoft Office, covering Writer, Calc, Impress, Word, Excel, and PowerPoint.');
INSERT INTO classes (title, description)
VALUES ('Internet Basics', 'Understand web browsing, search techniques, safe internet practices, and managing online accounts.');
INSERT INTO classes (title, description)
VALUES ('Cybersecurity Essentials', 'Learn the basics of keeping devices and data secure, including password management, identifying phishing attempts, and safe online practices.');
INSERT INTO classes (title, description)
VALUES ('Digital Accessibility', 'Overview of assistive technology, accessibility settings in devices, and understanding inclusive digital design.');
INSERT INTO classes (title, description)
VALUES ('PC Hardware Basics', 'Introduction to computer hardware components, basic troubleshooting, and an overview of setting up a computer.');
INSERT INTO classes (title, description)
VALUES ('Data Privacy and Digital Rights', 'Overview of data privacy concepts, rights to personal data, and tips on protecting digital privacy.');
INSERT INTO classes (title, description)
VALUES ('Networking Basics', 'Introduction to networking fundamentals, IP addresses, routers, switches, and simple network setups.');
INSERT INTO classes (title, description)
VALUES ('Programming and Coding', 'Beginner-level courses introducing programming concepts with Python and web development with HTML and CSS.');
INSERT INTO classes (title, description)
VALUES ('Career Exploration in Tech', 'Classes introducing career paths in IT, including IT support, systems administration, networking, data analysis, cybersecurity, UX/UI design, cloud computing, software development and more. Each session provides an overview of the role, basic skills needed, and introductory activities.');

-- Adding some free resources
INSERT INTO external_resources (title, description, url, category)
VALUES ('Professor Messer', 'Professor Messer makes amazing free video trainings for the core CompTIZ certifications - the A+, the Network+, and the Security+.', 'https://www.professormesser.com/', 'Learn IT');
INSERT INTO external_resources (title, description, url, category)
VALUES ('CS50x - Introduction to Computer Science', 'CS50x is an amazing, free entry-level course from Harvard taught by David Malan. It goes over the basics of computer science and programming covering topics including abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development.', 'https://www.edx.org/learn/computer-science/harvard-university-cs50-s-introduction-to-computer-science', 'Computer Science');
INSERT INTO external_resources (title, description, url, category)
VALUES ('freeCodeCamp', 'freeCodeCamp is a wonderful place to learn how to program. They offer hands-on, step-by-step courses that teach you web development from the basics with HTML and CSS to more advanced topics with JavaScript, Python, databases, and more. Starting on December 25th, 2024, freeCodeCamp is releasing a new certification that teaches you almost everything you would need to know for web development and software development.', 'https://www.freecodecamp.org/learn', 'Programming');