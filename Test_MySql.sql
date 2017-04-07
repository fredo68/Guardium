-- =================================
-- Policies
-- =================================
DROP TABLE POLICIES;

CREATE TABLE POLICIES

(
POLICY_NAME     CHAR (128) 	-- Can be either a FQDN or an IP
);

ALTER TABLE POLICIES   ADD POLICY_ID INT AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE POLICIES   ADD CONSTRAINT UNIQUE (POLICY_NAME);
INSERT INTO POLICIES   SET POLICY_NAME = 'POLICY 1';
INSERT INTO POLICIES   SET POLICY_NAME = 'POLICY 2';
