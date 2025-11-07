CREATE TABLE os_types (
  type_id integer PRIMARY KEY,
  type_name varchar(50) NOT NULL
);

CREATE TABLE architectures (
  architecture_id integer PRIMARY KEY,
  architecture_name varchar(50) NOT NULL
);

CREATE TABLE publishers (
  publisher_id integer PRIMARY KEY,
  publisher_name varchar(100) NOT NULL
);

CREATE TABLE operating_systems (
  os_id integer PRIMARY KEY,
  os_name varchar(100) NOT NULL,
  release_year integer NOT NULL,
  version varchar(50),
  install_size_gb numeric,
  architecture_id integer NOT NULL,
  type_id integer NOT NULL,
  publisher_id integer NOT NULL,
  support_end date,
  FOREIGN KEY (architecture_id) REFERENCES architectures(architecture_id),
  FOREIGN KEY (type_id) REFERENCES os_types(type_id),
  FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
);

