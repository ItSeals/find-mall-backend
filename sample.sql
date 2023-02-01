-- Adminer 4.8.1 MySQL 8.0.32 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1,	'Can add log entry',	1,	'add_logentry'),
(2,	'Can change log entry',	1,	'change_logentry'),
(3,	'Can delete log entry',	1,	'delete_logentry'),
(4,	'Can view log entry',	1,	'view_logentry'),
(5,	'Can add permission',	2,	'add_permission'),
(6,	'Can change permission',	2,	'change_permission'),
(7,	'Can delete permission',	2,	'delete_permission'),
(8,	'Can view permission',	2,	'view_permission'),
(9,	'Can add group',	3,	'add_group'),
(10,	'Can change group',	3,	'change_group'),
(11,	'Can delete group',	3,	'delete_group'),
(12,	'Can view group',	3,	'view_group'),
(13,	'Can add user',	4,	'add_user'),
(14,	'Can change user',	4,	'change_user'),
(15,	'Can delete user',	4,	'delete_user'),
(16,	'Can view user',	4,	'view_user'),
(17,	'Can add content type',	5,	'add_contenttype'),
(18,	'Can change content type',	5,	'change_contenttype'),
(19,	'Can delete content type',	5,	'delete_contenttype'),
(20,	'Can view content type',	5,	'view_contenttype'),
(21,	'Can add session',	6,	'add_session'),
(22,	'Can change session',	6,	'change_session'),
(23,	'Can delete session',	6,	'delete_session'),
(24,	'Can view session',	6,	'view_session'),
(25,	'Can add categories',	7,	'add_categories'),
(26,	'Can change categories',	7,	'change_categories'),
(27,	'Can delete categories',	7,	'delete_categories'),
(28,	'Can view categories',	7,	'view_categories'),
(29,	'Can add mall',	8,	'add_mall'),
(30,	'Can change mall',	8,	'change_mall'),
(31,	'Can delete mall',	8,	'delete_mall'),
(32,	'Can view mall',	8,	'view_mall'),
(33,	'Can add item',	9,	'add_item'),
(34,	'Can change item',	9,	'change_item'),
(35,	'Can delete item',	9,	'delete_item'),
(36,	'Can view item',	9,	'view_item'),
(37,	'Can add tag',	10,	'add_tag'),
(38,	'Can change tag',	10,	'change_tag'),
(39,	'Can delete tag',	10,	'delete_tag'),
(40,	'Can view tag',	10,	'view_tag');

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1,	'admin',	'logentry'),
(3,	'auth',	'group'),
(2,	'auth',	'permission'),
(4,	'auth',	'user'),
(5,	'contenttypes',	'contenttype'),
(7,	'find_mall_api',	'categories'),
(9,	'find_mall_api',	'item'),
(8,	'find_mall_api',	'mall'),
(10,	'find_mall_api',	'tag'),
(6,	'sessions',	'session');

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1,	'contenttypes',	'0001_initial',	'2023-01-29 17:49:38.863738'),
(2,	'auth',	'0001_initial',	'2023-01-29 17:49:39.825443'),
(3,	'admin',	'0001_initial',	'2023-01-29 17:49:40.026009'),
(4,	'admin',	'0002_logentry_remove_auto_add',	'2023-01-29 17:49:40.040328'),
(5,	'admin',	'0003_logentry_add_action_flag_choices',	'2023-01-29 17:49:40.055772'),
(6,	'contenttypes',	'0002_remove_content_type_name',	'2023-01-29 17:49:40.170986'),
(7,	'auth',	'0002_alter_permission_name_max_length',	'2023-01-29 17:49:40.256349'),
(8,	'auth',	'0003_alter_user_email_max_length',	'2023-01-29 17:49:40.291329'),
(9,	'auth',	'0004_alter_user_username_opts',	'2023-01-29 17:49:40.304306'),
(10,	'auth',	'0005_alter_user_last_login_null',	'2023-01-29 17:49:40.383860'),
(11,	'auth',	'0006_require_contenttypes_0002',	'2023-01-29 17:49:40.390157'),
(12,	'auth',	'0007_alter_validators_add_error_messages',	'2023-01-29 17:49:40.404999'),
(13,	'auth',	'0008_alter_user_username_max_length',	'2023-01-29 17:49:40.500158'),
(14,	'auth',	'0009_alter_user_last_name_max_length',	'2023-01-29 17:49:40.593399'),
(15,	'auth',	'0010_alter_group_name_max_length',	'2023-01-29 17:49:40.628902'),
(16,	'auth',	'0011_update_proxy_permissions',	'2023-01-29 17:49:40.643647'),
(17,	'auth',	'0012_alter_user_first_name_max_length',	'2023-01-29 17:49:40.737111'),
(18,	'find_mall_api',	'0001_initial',	'2023-01-29 17:49:40.908287'),
(19,	'find_mall_api',	'0002_remove_categories_created_at_and_more',	'2023-01-29 17:49:41.023162'),
(20,	'find_mall_api',	'0003_item_malls',	'2023-01-29 17:49:41.240186'),
(21,	'find_mall_api',	'0004_tag_item_tags',	'2023-01-29 17:49:41.480904'),
(22,	'find_mall_api',	'0005_alter_item_category',	'2023-01-29 17:49:41.493108'),
(23,	'find_mall_api',	'0006_alter_item_category',	'2023-01-29 17:49:41.503499'),
(24,	'find_mall_api',	'0007_item_item_image',	'2023-01-29 17:49:41.546916'),
(25,	'sessions',	'0001_initial',	'2023-01-29 17:49:41.611494');

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `find_mall_api_categories`;
CREATE TABLE `find_mall_api_categories` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `find_mall_api_categories` (`id`, `title`) VALUES
(1,	'категорія');

DROP TABLE IF EXISTS `find_mall_api_item`;
CREATE TABLE `find_mall_api_item` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `category_id` bigint NOT NULL,
  `item_image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `find_mall_api_item_category_id_09820f49_fk_find_mall` (`category_id`),
  CONSTRAINT `find_mall_api_item_category_id_09820f49_fk_find_mall` FOREIGN KEY (`category_id`) REFERENCES `find_mall_api_categories` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `find_mall_api_item_malls`;
CREATE TABLE `find_mall_api_item_malls` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `item_id` bigint NOT NULL,
  `mall_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `find_mall_api_item_malls_item_id_mall_id_390fecab_uniq` (`item_id`,`mall_id`),
  KEY `find_mall_api_item_m_mall_id_f0496879_fk_find_mall` (`mall_id`),
  CONSTRAINT `find_mall_api_item_m_item_id_71aa3b9d_fk_find_mall` FOREIGN KEY (`item_id`) REFERENCES `find_mall_api_item` (`id`),
  CONSTRAINT `find_mall_api_item_m_mall_id_f0496879_fk_find_mall` FOREIGN KEY (`mall_id`) REFERENCES `find_mall_api_mall` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `find_mall_api_item_tags`;
CREATE TABLE `find_mall_api_item_tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `item_id` bigint NOT NULL,
  `tag_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `find_mall_api_item_tags_item_id_tag_id_71552272_uniq` (`item_id`,`tag_id`),
  KEY `find_mall_api_item_tags_tag_id_c5dca39f_fk_find_mall_api_tag_id` (`tag_id`),
  CONSTRAINT `find_mall_api_item_t_item_id_fa2e4095_fk_find_mall` FOREIGN KEY (`item_id`) REFERENCES `find_mall_api_item` (`id`),
  CONSTRAINT `find_mall_api_item_tags_tag_id_c5dca39f_fk_find_mall_api_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `find_mall_api_tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `find_mall_api_mall`;
CREATE TABLE `find_mall_api_mall` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `find_mall_api_mall` (`id`, `title`, `location`) VALUES
(1,	'Forum',	'Bohdan-Lutsyk Street'),
(11,	'Skrynya',	'Horodotska, 16');

DROP TABLE IF EXISTS `find_mall_api_tag`;
CREATE TABLE `find_mall_api_tag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `find_mall_api_tag` (`id`, `title`) VALUES
(1,	'ТЕГ');

-- 2023-01-30 16:44:51
