#!/usr/bin/env bash
-- a script that creates the table unique_id
CREATE USER IF NOT EXISTS unique_id (
	`id` INT DEFAULT 1,
	`name` VARCHAR(256)
);
