CREATE TABLE `user` (
    `username` VARCHAR(20) NULL DEFAULT NULL,
    `password` VARCHAR(500) NULL DEFAULT NULL,
    `name` VARCHAR(20) NULL DEFAULT NULL,
    `isAccountNonExpired` TINYINT(1) NULL DEFAULT NULL,
    `isAccountNonLocked` TINYINT(1) NULL DEFAULT NULL,
    `isCredentialsNonExpired` TINYINT(1) NULL DEFAULT NULL,
    `isEnabled` TINYINT(1) NULL DEFAULT NULL
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;