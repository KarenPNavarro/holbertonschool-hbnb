-- Initial data for HBnB

-- Administrator user
-- Replace the id and password hash with the values from your task page
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'Admin',
    'HBnB',
    'admin@hbnb.io',
    '$2b$12$WUVJJ34lZWn4dZAYCsfajOH82BSweSSaKvSdXgbWfEunKgav/Qzm.',
    TRUE
);

-- Amenities (ids should be unique UUIDs)
INSERT INTO amenities (id, name) VALUES
    ('a1111111-1111-1111-1111-111111111111', 'WiFi'),
    ('a2222222-2222-2222-2222-222222222222', 'Swimming Pool'),
    ('a3333333-3333-3333-3333-333333333333', 'Air Conditioning');
