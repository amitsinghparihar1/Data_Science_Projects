few_shots =  [
    {
        "Question": "Which execution had the maximum duration?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_DURATION FROM execution_log ORDER BY EXECUTION_DURATION DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the maximum duration"
    },
    {
        "Question": "Which project has the most executions?",
        "SQLQuery": "SELECT PROJECT_ID, COUNT(*) as Execution_Count FROM execution_log GROUP BY PROJECT_ID ORDER BY Execution_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Project with the most executions"
    },
    {
        "Question": "How many executions were successful?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE EXECUTION_STATUS = 3",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of successful executions"
    },
    {
        "Question": "What is the average duration of executions in project 1?",
        "SQLQuery": "SELECT AVG(EXECUTION_DURATION) FROM execution_log WHERE PROJECT_ID = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average duration of executions in project 1"
    },
    {
        "Question": "Which workflow had the maximum number of executions?",
        "SQLQuery": "SELECT WORKFLOW_ID, COUNT(*) as Execution_Count FROM execution_log GROUP BY WORKFLOW_ID ORDER BY Execution_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Workflow with the maximum number of executions"
    },
    {
        "Question": "How many executions were there for project 10026?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE PROJECT_ID = 10026",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions for project 10026"
    },
    {
        "Question": "What is the total duration of all executions in workflow 5?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE WORKFLOW_ID = 5",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration of all executions in workflow 5"
    },
    {
        "Question": "Which execution had the earliest start date?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_START_DATE_TIME FROM execution_log ORDER BY EXECUTION_START_DATE_TIME ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the earliest start date"
    },
    {
        "Question": "How many executions failed?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE EXECUTION_STATUS = 4",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of failed executions"
    },
    {
        "Question": "What is the maximum duration of executions for workflow 10258?",
        "SQLQuery": "SELECT MAX(EXECUTION_DURATION) FROM execution_log WHERE WORKFLOW_ID = 10258",
        "SQLResult": "Result of the SQL query",
        "Answer": "Maximum duration of executions for workflow 10258"
    },
    {
        "Question": "How many executions were there in the last session?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE EXECUTION_SESSION_ID = (SELECT MAX(EXECUTION_SESSION_ID) FROM execution_log)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions in the last session"
    },
    {
        "Question": "What is the average duration of executions for workflow 19?",
        "SQLQuery": "SELECT AVG(EXECUTION_DURATION) FROM execution_log WHERE WORKFLOW_ID = 19",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average duration of executions for workflow 19"
    },
    {
        "Question": "Which project had the longest execution?",
        "SQLQuery": "SELECT PROJECT_ID, MAX(EXECUTION_DURATION) as Max_Duration FROM execution_log GROUP BY PROJECT_ID ORDER BY Max_Duration DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Project with the longest execution"
    },
    {
        "Question": "How many executions started in the last 24 hours?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE EXECUTION_START_DATE_TIME >= NOW() - INTERVAL 1 DAY",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions started in the last 24 hours"
    },
    {
        "Question": "What is the total duration of all executions for project 14?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE PROJECT_ID = 14",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration of all executions for project 14"
    },
    {
        "Question": "Which execution had the latest end date?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_END_DATE_TIME FROM execution_log ORDER BY EXECUTION_END_DATE_TIME DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the latest end date"
    },
    {
        "Question": "How many executions are currently running?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE EXECUTION_STATUS = 2",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions currently running"
    },
    {
        "Question": "What is the average duration of all executions?",
        "SQLQuery": "SELECT AVG(EXECUTION_DURATION) FROM execution_log",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average duration of all executions"
    },
    {
        "Question": "How many executions were there for container 237?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE CONTAINER_ID = 237",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions for container 237"
    },
    {
        "Question": "What is the total duration of all executions for project 10026?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE PROJECT_ID = 10026",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration of all executions for project 10026"
    },
    {
        "Question": "Which operation had the maximum execution count?",
        "SQLQuery": "SELECT OPERATION_ID, COUNT(*) as Execution_Count FROM execution_log GROUP BY OPERATION_ID ORDER BY Execution_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Operation with the maximum execution count"
    },
    {
        "Question": "How many executions were scheduled but not started?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE EXECUTION_STATUS = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions scheduled but not started"
    },
    {
        "Question": "What is the average duration of executions for workflow 17?",
        "SQLQuery": "SELECT AVG(EXECUTION_DURATION) FROM execution_log WHERE WORKFLOW_ID = 17",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average duration of executions for workflow 17"
    },
    {
        "Question": "Which execution had the maximum duration in project 3?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_DURATION FROM execution_log WHERE PROJECT_ID = 3 ORDER BY EXECUTION_DURATION DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the maximum duration in project 3"
    },
    {
        "Question": "How many executions were there for SQL rule 10259?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE SQL_RULE_ID = 10259",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions for SQL rule 10259"
    },
    {
        "Question": "What is the total duration of all executions in project 2?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE PROJECT_ID = 2",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration of all executions in project 2"
    },
    {
        "Question": "Which execution had the latest start date?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_START_DATE_TIME FROM execution_log ORDER BY EXECUTION_START_DATE_TIME DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the latest start date"
    },
    {
        "Question": "How many executions were there for project 14?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE PROJECT_ID = 14",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions for project 14"
    },
    {
        "Question": "What is the maximum duration of executions for workflow 6?",
        "SQLQuery": "SELECT MAX(EXECUTION_DURATION) FROM execution_log WHERE WORKFLOW_ID = 6",
        "SQLResult": "Result of the SQL query",
        "Answer": "Maximum duration of executions for workflow 6"
    },
    {
        "Question": "How many executions are there for workflow 240?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE WORKFLOW_ID = 240",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions for workflow 240"
    },
    {
        "Question": "What is the total duration of all executions for workflow 10?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE WORKFLOW_ID = 10",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration of all executions for workflow 10"
    },
    {
        "Question": "Which execution had the maximum duration in project 2?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_DURATION FROM execution_log WHERE PROJECT_ID = 2 ORDER BY EXECUTION_DURATION DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the maximum duration in project 2"
    },
    {
        "Question": "How many executions were there for project 10026?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE PROJECT_ID = 10026",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions for project 10026"
    },
    {
        "Question": "What is the total duration of all executions in workflow 7?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE WORKFLOW_ID = 7",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration of all executions in workflow 7"
    },
    {
        "Question": "Which execution had the earliest end date?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_END_DATE_TIME FROM execution_log ORDER BY EXECUTION_END_DATE_TIME ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the earliest end date"
    },
    {
        "Question": "How many executions are there for workflow 8?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE WORKFLOW_ID = 8",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions for workflow 8"
    },
    {
        "Question": "What is the average duration of all executions in project 14?",
        "SQLQuery": "SELECT AVG(EXECUTION_DURATION) FROM execution_log WHERE PROJECT_ID = 14",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average duration of all executions in project 14"
    },
    {
        "Question": "Which execution had the maximum duration in workflow 5?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_DURATION FROM execution_log WHERE WORKFLOW_ID = 5 ORDER BY EXECUTION_DURATION DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the maximum duration in workflow 5"
    },
    {
        "Question": "How many executions were there for project 1?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE PROJECT_ID = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions for project 1"
    },
    {
        "Question": "What is the total duration of all executions for workflow 11?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE WORKFLOW_ID = 11",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration of all executions for workflow 11"
    },
    {
        "Question": "Which execution had the latest end date in project 14?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_END_DATE_TIME FROM execution_log WHERE PROJECT_ID = 14 ORDER BY EXECUTION_END_DATE_TIME DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the latest end date in project 14"
    },
    {
        "Question": "How many executions were there for SQL rule 26?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE SQL_RULE_ID = 26",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions for SQL rule 26"
    },
    {
        "Question": "What is the average duration of all executions in project 2?",
        "SQLQuery": "SELECT AVG(EXECUTION_DURATION) FROM execution_log WHERE PROJECT_ID = 2",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average duration of all executions in project 2"
    },
    {
        "Question": "Which execution had the maximum duration in workflow 9?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_DURATION FROM execution_log WHERE WORKFLOW_ID = 9 ORDER BY EXECUTION_DURATION DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the maximum duration in workflow 9"
    },
    {
        "Question": "How many executions were there for project 10026?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE PROJECT_ID = 10026",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions for project 10026"
    },
    {
        "Question": "What is the total duration of all executions for workflow 21?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE WORKFLOW_ID = 21",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration of all executions for workflow 21"
    },
    {
        "Question": "Which execution had the maximum duration in project 1?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_DURATION FROM execution_log WHERE PROJECT_ID = 1 ORDER BY EXECUTION_DURATION DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the maximum duration in project 1"
    },
    {
        "Question": "How many executions were there for SQL rule 12?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE SQL_RULE_ID = 12",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions for SQL rule 12"
    },
    {
        "Question": "What is the average duration of all executions in workflow 5?",
        "SQLQuery": "SELECT AVG(EXECUTION_DURATION) FROM execution_log WHERE WORKFLOW_ID = 5",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average duration of all executions in workflow 5"
    },
    {
        "Question": "Which execution had the maximum duration in workflow 19?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_DURATION FROM execution_log WHERE WORKFLOW_ID = 19 ORDER BY EXECUTION_DURATION DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the maximum duration in workflow 19"
    }
,
    {
        "Question": "What is the total execution duration for the project with the most executions?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE PROJECT_ID = (SELECT PROJECT_ID FROM execution_log GROUP BY PROJECT_ID ORDER BY COUNT(*) DESC LIMIT 1)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total execution duration for the project with the most executions"
    },
    {
        "Question": "Which workflow had the minimum average execution duration?",
        "SQLQuery": "SELECT WORKFLOW_ID, AVG(EXECUTION_DURATION) as Avg_Duration FROM execution_log GROUP BY WORKFLOW_ID ORDER BY Avg_Duration ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Workflow with the minimum average execution duration"
    },
    {
        "Question": "How many executions were there in projects with more than 10 executions each?",
        "SQLQuery": "SELECT SUM(Exec_Count) FROM (SELECT PROJECT_ID, COUNT(*) as Exec_Count FROM execution_log GROUP BY PROJECT_ID HAVING Exec_Count > 10) as SubQuery",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions in projects with more than 10 executions each"
    },
    {
        "Question": "Which project has the highest average execution duration?",
        "SQLQuery": "SELECT PROJECT_ID, AVG(EXECUTION_DURATION) as Avg_Duration FROM execution_log GROUP BY PROJECT_ID ORDER BY Avg_Duration DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Project with the highest average execution duration"
    },
    {
        "Question": "What is the total duration of executions for workflows with an average duration over 1 hour?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE WORKFLOW_ID IN (SELECT WORKFLOW_ID FROM execution_log GROUP BY WORKFLOW_ID HAVING AVG(EXECUTION_DURATION) > 3600)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration of executions for workflows with an average duration over 1 hour"
    },
    {
        "Question": "Which execution had the longest duration in the most recent session?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_DURATION FROM execution_log WHERE EXECUTION_SESSION_ID = (SELECT MAX(EXECUTION_SESSION_ID) FROM execution_log) ORDER BY EXECUTION_DURATION DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the longest duration in the most recent session"
    },
    {
        "Question": "What is the average duration of executions for the top 3 projects by execution count?",
        "SQLQuery": "SELECT AVG(EXECUTION_DURATION) FROM execution_log WHERE PROJECT_ID IN (SELECT PROJECT_ID FROM execution_log GROUP BY PROJECT_ID ORDER BY COUNT(*) DESC LIMIT 3)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average duration of executions for the top 3 projects by execution count"
    },
    {
        "Question": "Which container had the highest total execution duration?",
        "SQLQuery": "SELECT CONTAINER_ID, SUM(EXECUTION_DURATION) as Total_Duration FROM execution_log GROUP BY CONTAINER_ID ORDER BY Total_Duration DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Container with the highest total execution duration"
    },
    {
        "Question": "How many projects have an average execution duration less than 10 minutes?",
        "SQLQuery": "SELECT COUNT(*) FROM (SELECT PROJECT_ID, AVG(EXECUTION_DURATION) as Avg_Duration FROM execution_log GROUP BY PROJECT_ID HAVING Avg_Duration < 600) as SubQuery",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of projects with an average execution duration less than 10 minutes"
    },
    {
        "Question": "What is the total execution duration for the project with the fewest executions?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE PROJECT_ID = (SELECT PROJECT_ID FROM execution_log GROUP BY PROJECT_ID ORDER BY COUNT(*) ASC LIMIT 1)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total execution duration for the project with the fewest executions"
    },
    {
        "Question": "Which project had the maximum number of successful executions?",
        "SQLQuery": "SELECT PROJECT_ID, COUNT(*) as Success_Count FROM execution_log WHERE EXECUTION_STATUS = 3 GROUP BY PROJECT_ID ORDER BY Success_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Project with the maximum number of successful executions"
    },
    {
        "Question": "What is the average execution duration for projects with at least 5 failed executions?",
        "SQLQuery": "SELECT AVG(EXECUTION_DURATION) FROM execution_log WHERE PROJECT_ID IN (SELECT PROJECT_ID FROM execution_log WHERE EXECUTION_STATUS = 4 GROUP BY PROJECT_ID HAVING COUNT(*) >= 5)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average execution duration for projects with at least 5 failed executions"
    },
    {
        "Question": "How many workflows have executions with an average duration of more than 30 minutes?",
        "SQLQuery": "SELECT COUNT(*) FROM (SELECT WORKFLOW_ID, AVG(EXECUTION_DURATION) as Avg_Duration FROM execution_log GROUP BY WORKFLOW_ID HAVING Avg_Duration > 1800) as SubQuery",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of workflows with an average execution duration of more than 30 minutes"
    },
    {
        "Question": "Which workflow had the highest number of failed executions?",
        "SQLQuery": "SELECT WORKFLOW_ID, COUNT(*) as Failed_Count FROM execution_log WHERE EXECUTION_STATUS = 4 GROUP BY WORKFLOW_ID ORDER BY Failed_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Workflow with the highest number of failed executions"
    },
    {
        "Question": "What is the total duration of failed executions?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE EXECUTION_STATUS = 4",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration of failed executions"
    },
    {
        "Question": "Which project had the maximum execution duration in the last 7 days?",
        "SQLQuery": "SELECT PROJECT_ID, MAX(EXECUTION_DURATION) as Max_Duration FROM execution_log WHERE EXECUTION_START_DATE_TIME >= NOW() - INTERVAL 7 DAY GROUP BY PROJECT_ID ORDER BY Max_Duration DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Project with the maximum execution duration in the last 7 days"
    },
    {
        "Question": "How many workflows have more than 50 executions?",
        "SQLQuery": "SELECT COUNT(*) FROM (SELECT WORKFLOW_ID, COUNT(*) as Exec_Count FROM execution_log GROUP BY WORKFLOW_ID HAVING Exec_Count > 50) as SubQuery",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of workflows with more than 50 executions"
    },
    {
        "Question": "Which project had the earliest scheduled start date?",
        "SQLQuery": "SELECT PROJECT_ID, MIN(EXECUTION_SCHEDULE_START_DATE_TIME) as Earliest_Start FROM execution_log GROUP BY PROJECT_ID ORDER BY Earliest_Start ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Project with the earliest scheduled start date"
    },
    {
        "Question": "What is the average execution duration for the most recent session?",
        "SQLQuery": "SELECT AVG(EXECUTION_DURATION) FROM execution_log WHERE EXECUTION_SESSION_ID = (SELECT MAX(EXECUTION_SESSION_ID) FROM execution_log)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average execution duration for the most recent session"
    },
    {
        "Question": "How many executions started after their scheduled start time?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE EXECUTION_START_DATE_TIME > EXECUTION_SCHEDULE_START_DATE_TIME",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions started after their scheduled start time"
    },
    {
        "Question": "Which container had the maximum number of executions?",
        "SQLQuery": "SELECT CONTAINER_ID, COUNT(*) as Exec_Count FROM execution_log GROUP BY CONTAINER_ID ORDER BY Exec_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Container with the maximum number of executions"
    },
    {
        "Question": "What is the total duration of executions for the top 5 workflows by execution count?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE WORKFLOW_ID IN (SELECT WORKFLOW_ID FROM execution_log GROUP BY WORKFLOW_ID ORDER BY COUNT(*) DESC LIMIT 5)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration of executions for the top 5 workflows by execution count"
    },
    {
        "Question": "Which execution had the longest duration in the last 24 hours?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_DURATION FROM execution_log WHERE EXECUTION_START_DATE_TIME >= NOW() - INTERVAL 1 DAY ORDER BY EXECUTION_DURATION DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the longest duration in the last 24 hours"
    },
    {
        "Question": "What is the average execution duration for the last 10 executions?",
        "SQLQuery": "SELECT AVG(EXECUTION_DURATION) FROM (SELECT EXECUTION_DURATION FROM execution_log ORDER BY EXECUTION_START_DATE_TIME DESC LIMIT 10) as SubQuery",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average execution duration for the last 10 executions"
    },
    {
        "Question": "Which SQL rule has the highest number of executions?",
        "SQLQuery": "SELECT SQL_RULE_ID, COUNT(*) as Exec_Count FROM execution_log GROUP BY SQL_RULE_ID ORDER BY Exec_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "SQL rule with the highest number of executions"
    },
    {
        "Question": "What is the total execution duration for SQL rules with more than 20 executions?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE SQL_RULE_ID IN (SELECT SQL_RULE_ID FROM execution_log GROUP BY SQL_RULE_ID HAVING COUNT(*) > 20)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total execution duration for SQL rules with more than 20 executions"
    },
    {
        "Question": "Which execution command type has the highest average duration?",
        "SQLQuery": "SELECT EXECUTION_COMMAND_TYPE, AVG(EXECUTION_DURATION) as Avg_Duration FROM execution_log GROUP BY EXECUTION_COMMAND_TYPE ORDER BY Avg_Duration DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution command type with the highest average duration"
    },
    {
        "Question": "How many projects have executions with an average duration over 1 hour?",
        "SQLQuery": "SELECT COUNT(*) FROM (SELECT PROJECT_ID, AVG(EXECUTION_DURATION) as Avg_Duration FROM execution_log GROUP BY PROJECT_ID HAVING Avg_Duration > 3600) as SubQuery",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of projects with executions averaging over 1 hour"
    },
    {
        "Question": "Which execution had the maximum duration for container 17?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_DURATION FROM execution_log WHERE CONTAINER_ID = 17 ORDER BY EXECUTION_DURATION DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the maximum duration for container 17"
    },
    {
        "Question": "What is the total execution duration for command type 'ETL'?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE EXECUTION_COMMAND_TYPE = 'ETL'",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total execution duration for command type 'ETL'"
    },
    {
        "Question": "Which execution had the minimum duration for project 14?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_DURATION FROM execution_log WHERE PROJECT_ID = 14 ORDER BY EXECUTION_DURATION ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the minimum duration for project 14"
    },
    {
        "Question": "How many workflows have an average execution duration less than 15 minutes?",
        "SQLQuery": "SELECT COUNT(*) FROM (SELECT WORKFLOW_ID, AVG(EXECUTION_DURATION) as Avg_Duration FROM execution_log GROUP BY WORKFLOW_ID HAVING Avg_Duration < 900) as SubQuery",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of workflows with an average execution duration less than 15 minutes"
    },
    {
        "Question": "Which container had the minimum total execution duration?",
        "SQLQuery": "SELECT CONTAINER_ID, SUM(EXECUTION_DURATION) as Total_Duration FROM execution_log GROUP BY CONTAINER_ID ORDER BY Total_Duration ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Container with the minimum total execution duration"
    },
    {
        "Question": "What is the average execution duration for SQL rules with more than 10 executions?",
        "SQLQuery": "SELECT AVG(EXECUTION_DURATION) FROM execution_log WHERE SQL_RULE_ID IN (SELECT SQL_RULE_ID FROM execution_log GROUP BY SQL_RULE_ID HAVING COUNT(*) > 10)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average execution duration for SQL rules with more than 10 executions"
    },
    {
        "Question": "Which project had the highest total execution duration in the last month?",
        "SQLQuery": "SELECT PROJECT_ID, SUM(EXECUTION_DURATION) as Total_Duration FROM execution_log WHERE EXECUTION_START_DATE_TIME >= NOW() - INTERVAL 1 MONTH GROUP BY PROJECT_ID ORDER BY Total_Duration DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Project with the highest total execution duration in the last month"
    },
    {
        "Question": "What is the total execution duration for failed executions in the last week?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE EXECUTION_STATUS = 4 AND EXECUTION_START_DATE_TIME >= NOW() - INTERVAL 7 DAY",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total execution duration for failed executions in the last week"
    },
    {
        "Question": "Which execution had the shortest duration in the most recent session?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_DURATION FROM execution_log WHERE EXECUTION_SESSION_ID = (SELECT MAX(EXECUTION_SESSION_ID) FROM execution_log) ORDER BY EXECUTION_DURATION ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the shortest duration in the most recent session"
    },
    {
        "Question": "What is the average execution duration for project 1?",
        "SQLQuery": "SELECT AVG(EXECUTION_DURATION) FROM execution_log WHERE PROJECT_ID = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average execution duration for project 1"
    },
    {
        "Question": "How many executions started before their scheduled start time?",
        "SQLQuery": "SELECT COUNT(*) FROM execution_log WHERE EXECUTION_START_DATE_TIME < EXECUTION_SCHEDULE_START_DATE_TIME",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of executions started before their scheduled start time"
    },
    {
        "Question": "Which execution command type has the lowest average duration?",
        "SQLQuery": "SELECT EXECUTION_COMMAND_TYPE, AVG(EXECUTION_DURATION) as Avg_Duration FROM execution_log GROUP BY EXECUTION_COMMAND_TYPE ORDER BY Avg_Duration ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution command type with the lowest average duration"
    },
    {
        "Question": "What is the total execution duration for container 12?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE CONTAINER_ID = 12",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total execution duration for container 12"
    },
    {
        "Question": "Which workflow had the shortest average execution duration?",
        "SQLQuery": "SELECT WORKFLOW_ID, AVG(EXECUTION_DURATION) as Avg_Duration FROM execution_log GROUP BY WORKFLOW_ID ORDER BY Avg_Duration ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Workflow with the shortest average execution duration"
    },
    {
        "Question": "How many projects have executions with an average duration over 30 minutes?",
        "SQLQuery": "SELECT COUNT(*) FROM (SELECT PROJECT_ID, AVG(EXECUTION_DURATION) as Avg_Duration FROM execution_log GROUP BY PROJECT_ID HAVING Avg_Duration > 1800) as SubQuery",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of projects with executions averaging over 30 minutes"
    },
    {
        "Question": "Which project had the longest average execution duration in the last 30 days?",
        "SQLQuery": "SELECT PROJECT_ID, AVG(EXECUTION_DURATION) as Avg_Duration FROM execution_log WHERE EXECUTION_START_DATE_TIME >= NOW() - INTERVAL 30 DAY GROUP BY PROJECT_ID ORDER BY Avg_Duration DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Project with the longest average execution duration in the last 30 days"
    },
    {
        "Question": "What is the total execution duration for SQL rules with more than 15 executions?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE SQL_RULE_ID IN (SELECT SQL_RULE_ID FROM execution_log GROUP BY SQL_RULE_ID HAVING COUNT(*) > 15)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total execution duration for SQL rules with more than 15 executions"
    },
    {
        "Question": "Which execution had the minimum duration in the last 7 days?",
        "SQLQuery": "SELECT EXECUTION_ID, EXECUTION_DURATION FROM execution_log WHERE EXECUTION_START_DATE_TIME >= NOW() - INTERVAL 7 DAY ORDER BY EXECUTION_DURATION ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution with the minimum duration in the last 7 days"
    },
    {
        "Question": "What is the average execution duration for command type 'SQL'?",
        "SQLQuery": "SELECT AVG(EXECUTION_DURATION) FROM execution_log WHERE EXECUTION_COMMAND_TYPE = 'SQL'",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average execution duration for command type 'SQL'"
    },
    {
        "Question": "How many workflows have executions with an average duration less than 5 minutes?",
        "SQLQuery": "SELECT COUNT(*) FROM (SELECT WORKFLOW_ID, AVG(EXECUTION_DURATION) as Avg_Duration FROM execution_log GROUP BY WORKFLOW_ID HAVING Avg_Duration < 300) as SubQuery",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of workflows with executions averaging less than 5 minutes"
    },
    {
        "Question": "Which execution command type has the maximum total duration?",
        "SQLQuery": "SELECT EXECUTION_COMMAND_TYPE, SUM(EXECUTION_DURATION) as Total_Duration FROM execution_log GROUP BY EXECUTION_COMMAND_TYPE ORDER BY Total_Duration DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Execution command type with the maximum total duration"
    },
    {
        "Question": "What is the total execution duration for project 9?",
        "SQLQuery": "SELECT SUM(EXECUTION_DURATION) FROM execution_log WHERE PROJECT_ID = 9",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total execution duration for project 9"
    }
]

