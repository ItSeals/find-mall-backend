CREATE TABLE `malls` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `title` varchar(255),
  `description` text,
  `status` int,
  `created_at` datetime,
  `updated_at` datetime
);

CREATE TABLE `categories` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `title` varchar(255),
  `description` text,
  `status` int,
  `created_at` datetime,
  `updated_at` datetime
);

CREATE TABLE `shops` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `title` varchar(255),
  `description` text,
  `status` int,
  `mall_id` int,
  `category_id` int,
  `created_at` datetime,
  `updated_at` datetime
);

CREATE TABLE `admins` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `email` varchar(255),
  `password` varchar(255)
);

ALTER TABLE `shops` ADD FOREIGN KEY (`mall_id`) REFERENCES `malls` (`id`);

ALTER TABLE `shops` ADD FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`);
