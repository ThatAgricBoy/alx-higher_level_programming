#!/usr/bin/env bash
-- a script that creates the table unique_id
CREATE TABLE IF NOT EXISTS unique_id (
	`id` INT DEFAULT UNIQUE 1,
	`name` VARCHAR(256)
);
