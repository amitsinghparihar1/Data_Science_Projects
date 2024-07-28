few_shots =  [
    {
        "Question": "Which job had the maximum failed count in the last session?",
        "SQLQuery": "SELECT Job, Failed_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Failed_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum failed count in the last session"
    },
    {
        "Question": "How many jobs had a success count greater than 10 in the most recent session?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Last_Session = 1 AND Success_Count > 10",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a success count greater than 10 in the most recent session"
    },
    {
        "Question": "What is the total count of all jobs in the current session?",
        "SQLQuery": "SELECT SUM(Total_Count) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total count of all jobs in the current session"
    },
    {
        "Question": "Which job has the longest duration in minutes?",
        "SQLQuery": "SELECT Job, Duration_Minutes FROM execution_summarry ORDER BY Duration_Minutes DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the longest duration in minutes"
    },
    {
        "Question": "How many jobs are currently running?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Running_Count > 0",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs currently running"
    },
    {
        "Question": "Which job had the minimum success count in the last session?",
        "SQLQuery": "SELECT Job, Success_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Success_Count ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum success count in the last session"
    },
    {
        "Question": "What is the average duration in seconds for jobs in the last session?",
        "SQLQuery": "SELECT AVG(Duration_Seconds) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average duration in seconds for jobs in the last session"
    },
    {
        "Question": "How many jobs have failed in total?",
        "SQLQuery": "SELECT SUM(Failed_Count) FROM execution_summarry",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total number of jobs that have failed"
    },
    {
        "Question": "Which job has the maximum running count in the current session?",
        "SQLQuery": "SELECT Job, Running_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Running_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum running count in the current session"
    },
    {
        "Question": "What is the total duration in minutes for all jobs in the last session?",
        "SQLQuery": "SELECT SUM(Duration_Minutes) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration in minutes for all jobs in the last session"
    },
    {
        "Question": "Which job had the maximum waiting count in the last session?",
        "SQLQuery": "SELECT Job, Waiting_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Waiting_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum waiting count in the last session"
    },
    {
        "Question": "How many jobs have a total count greater than 50?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Total_Count > 50",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a total count greater than 50"
    },
    {
        "Question": "What is the average success count for jobs in the current session?",
        "SQLQuery": "SELECT AVG(Success_Count) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average success count for jobs in the current session"
    },
    {
        "Question": "Which job had the minimum running count in the last session?",
        "SQLQuery": "SELECT Job, Running_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Running_Count ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum running count in the last session"
    },
    {
        "Question": "What is the maximum duration in seconds for any job?",
        "SQLQuery": "SELECT MAX(Duration_Seconds) FROM execution_summarry",
        "SQLResult": "Result of the SQL query",
        "Answer": "Maximum duration in seconds for any job"
    },
    {
        "Question": "Which job has the highest total count?",
        "SQLQuery": "SELECT Job, Total_Count FROM execution_summarry ORDER BY Total_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the highest total count"
    },
    {
        "Question": "How many jobs had a failed count greater than 5 in the last session?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Last_Session = 1 AND Failed_Count > 5",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a failed count greater than 5 in the last session"
    },
    {
        "Question": "What is the sum of the success count for all jobs?",
        "SQLQuery": "SELECT SUM(Success_Count) FROM execution_summarry",
        "SQLResult": "Result of the SQL query",
        "Answer": "Sum of the success count for all jobs"
    },
    {
        "Question": "Which job had the minimum waiting count in the last session?",
        "SQLQuery": "SELECT Job, Waiting_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Waiting_Count ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum waiting count in the last session"
    },
    {
        "Question": "What is the total count of jobs with a duration of more than 60 minutes?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Duration_Minutes > 60",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total count of jobs with a duration of more than 60 minutes"
    },
    {
        "Question": "Which job had the maximum duration in seconds in the last session?",
        "SQLQuery": "SELECT Job, Duration_Seconds FROM execution_summarry WHERE Last_Session = 1 ORDER BY Duration_Seconds DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum duration in seconds in the last session"
    },
    {
        "Question": "How many jobs have a waiting count less than 3?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Waiting_Count < 3",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a waiting count less than 3"
    },
    {
        "Question": "What is the average total count for jobs in the last session?",
        "SQLQuery": "SELECT AVG(Total_Count) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average total count for jobs in the last session"
    },
    {
        "Question": "Which job had the minimum failed count in the last session?",
        "SQLQuery": "SELECT Job, Failed_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Failed_Count ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum failed count in the last session"
    },
    {
        "Question": "What is the sum of the duration in minutes for all jobs?",
        "SQLQuery": "SELECT SUM(Duration_Minutes) FROM execution_summarry",
        "SQLResult": "Result of the SQL query",
        "Answer": "Sum of the duration in minutes for all jobs"
    },
    {
        "Question": "How many jobs have a running count of exactly 1?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Running_Count = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a running count of exactly 1"
    },
    {
        "Question": "Which job had the maximum success count in the last session?",
        "SQLQuery": "SELECT Job, Success_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Success_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum success count in the last session"
    },
    {
        "Question": "What is the total duration in seconds for all jobs in the current session?",
        "SQLQuery": "SELECT SUM(Duration_Seconds) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration in seconds for all jobs in the current session"
    },
    {
        "Question": "Which job had the minimum duration in minutes in the last session?",
        "SQLQuery": "SELECT Job, Duration_Minutes FROM execution_summarry WHERE Last_Session = 1 ORDER BY Duration_Minutes ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum duration in minutes in the last session"
    },
    {
        "Question": "What is the average waiting count for jobs in the current session?",
        "SQLQuery": "SELECT AVG(Waiting_Count) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average waiting count for jobs in the current session"
    },
    {
        "Question": "Which job had the maximum total count in the last session?",
        "SQLQuery": "SELECT Job, Total_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Total_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum total count in the last session"
    },
    {
        "Question": "What is the sum of the failed count for all jobs?",
        "SQLQuery": "SELECT SUM(Failed_Count) FROM execution_summarry",
        "SQLResult": "Result of the SQL query",
        "Answer": "Sum of the failed count for all jobs"
    },
    {
        "Question": "How many jobs have a duration of less than 30 minutes?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Duration_Minutes < 30",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a duration of less than 30 minutes"
    },
    {
        "Question": "Which job had the minimum duration in seconds in the last session?",
        "SQLQuery": "SELECT Job, Duration_Seconds FROM execution_summarry WHERE Last_Session = 1 ORDER BY Duration_Seconds ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum duration in seconds in the last session"
    },
    {
        "Question": "What is the average running count for jobs in the last session?",
        "SQLQuery": "SELECT AVG(Running_Count) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average running count for jobs in the last session"
    },
    {
        "Question": "Which job had the maximum failed count in the last session?",
        "SQLQuery": "SELECT Job, Failed_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Failed_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum failed count in the last session"
    },
    {
        "Question": "What is the total duration in minutes for all jobs in the current session?",
        "SQLQuery": "SELECT SUM(Duration_Minutes) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration in minutes for all jobs in the current session"
    },
    {
        "Question": "Which job had the minimum success count in the last session?",
        "SQLQuery": "SELECT Job, Success_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Success_Count ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum success count in the last session"
    },
    {
        "Question": "What is the average duration in seconds for jobs in the current session?",
        "SQLQuery": "SELECT AVG(Duration_Seconds) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average duration in seconds for jobs in the current session"
    },
    {
        "Question": "How many jobs had a running count greater than 2 in the last session?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Last_Session = 1 AND Running_Count > 2",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a running count greater than 2 in the last session"
    },
    {
        "Question": "What is the sum of the success count for jobs in the current session?",
        "SQLQuery": "SELECT SUM(Success_Count) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Sum of the success count for jobs in the current session"
    },
    {
        "Question": "Which job had the maximum waiting count in the last session?",
        "SQLQuery": "SELECT Job, Waiting_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Waiting_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum waiting count in the last session"
    },
    {
        "Question": "How many jobs have a total count less than 20?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Total_Count < 20",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a total count less than 20"
    },
    {
        "Question": "What is the average success count for jobs in the last session?",
        "SQLQuery": "SELECT AVG(Success_Count) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average success count for jobs in the last session"
    },
    {
        "Question": "Which job had the minimum running count in the last session?",
        "SQLQuery": "SELECT Job, Running_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Running_Count ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum running count in the last session"
    },
    {
        "Question": "What is the maximum duration in minutes for any job?",
        "SQLQuery": "SELECT MAX(Duration_Minutes) FROM execution_summarry",
        "SQLResult": "Result of the SQL query",
        "Answer": "Maximum duration in minutes for any job"
    },
    {
        "Question": "Which job has the highest total count in the last session?",
        "SQLQuery": "SELECT Job, Total_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Total_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the highest total count in the last session"
    },
    {
        "Question": "How many jobs had a failed count less than 3 in the last session?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Last_Session = 1 AND Failed_Count < 3",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a failed count less than 3 in the last session"
    },
    {
        "Question": "What is the sum of the duration in seconds for all jobs?",
        "SQLQuery": "SELECT SUM(Duration_Seconds) FROM execution_summarry",
        "SQLResult": "Result of the SQL query",
        "Answer": "Sum of the duration in seconds for all jobs"
    },
    {
        "Question": "How many jobs have a waiting count of exactly 2?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Waiting_Count = 2",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a waiting count of exactly 2"
    },
    {
        "Question": "What is the maximum success count among all jobs?",
        "SQLQuery": "SELECT MAX(Success_Count) FROM execution_summarry",
        "SQLResult": "Result of the SQL query",
        "Answer": "Maximum success count among all jobs"
    },
    {
        "Question": "How many jobs have a failed count of exactly 0?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Failed_Count = 0",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a failed count of exactly 0"
    },
    {
        "Question": "What is the average duration in minutes for jobs that have failed at least once?",
        "SQLQuery": "SELECT AVG(Duration_Minutes) FROM execution_summarry WHERE Failed_Count > 0",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average duration in minutes for jobs that have failed at least once"
    },
    {
        "Question": "Which job has the highest waiting count among jobs with more than 100 total counts?",
        "SQLQuery": "SELECT Job, Waiting_Count FROM execution_summarry WHERE Total_Count > 100 ORDER BY Waiting_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the highest waiting count among jobs with more than 100 total counts"
    },
    {
        "Question": "What is the total success count for all jobs in the current session?",
        "SQLQuery": "SELECT SUM(Success_Count) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total success count for all jobs in the current session"
    },
    {
        "Question": "How many jobs have a total count of more than 200 in the last session?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Last_Session = 1 AND Total_Count > 200",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a total count of more than 200 in the last session"
    },
    {
        "Question": "What is the average failed count for jobs that have a running count greater than 5?",
        "SQLQuery": "SELECT AVG(Failed_Count) FROM execution_summarry WHERE Running_Count > 5",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average failed count for jobs that have a running count greater than 5"
    },
    {
        "Question": "Which job has the longest duration in seconds among jobs that have succeeded at least once?",
        "SQLQuery": "SELECT Job, Duration_Seconds FROM execution_summarry WHERE Success_Count > 0 ORDER BY Duration_Seconds DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the longest duration in seconds among jobs that have succeeded at least once"
    },
    {
        "Question": "What is the total waiting count for all jobs in the last session?",
        "SQLQuery": "SELECT SUM(Waiting_Count) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total waiting count for all jobs in the last session"
    },
    {
        "Question": "How many jobs have a success count of exactly 0?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Success_Count = 0",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a success count of exactly 0"
    },
    {
        "Question": "What is the average total count for jobs that have a waiting count less than 5?",
        "SQLQuery": "SELECT AVG(Total_Count) FROM execution_summarry WHERE Waiting_Count < 5",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average total count for jobs that have a waiting count less than 5"
    },
    {
        "Question": "Which job has the minimum success count among jobs with more than 10 running counts?",
        "SQLQuery": "SELECT Job, Success_Count FROM execution_summarry WHERE Running_Count > 10 ORDER BY Success_Count ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum success count among jobs with more than 10 running counts"
    },
    {
        "Question": "What is the total failed count for all jobs in the last session?",
        "SQLQuery": "SELECT SUM(Failed_Count) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total failed count for all jobs in the last session"
    },
    {
        "Question": "How many jobs have a duration in seconds greater than the average duration?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Duration_Seconds > (SELECT AVG(Duration_Seconds) FROM execution_summarry)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a duration in seconds greater than the average duration"
    },
    {
        "Question": "Which job has the maximum running count in the last session?",
        "SQLQuery": "SELECT Job, Running_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Running_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum running count in the last session"
    },
    {
        "Question": "What is the average success count for jobs with a total count greater than 50?",
        "SQLQuery": "SELECT AVG(Success_Count) FROM execution_summarry WHERE Total_Count > 50",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average success count for jobs with a total count greater than 50"
    },
    {
        "Question": "Which job had the minimum waiting count in the last session?",
        "SQLQuery": "SELECT Job, Waiting_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Waiting_Count ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum waiting count in the last session"
    },
    {
        "Question": "What is the total count of jobs that have a success count greater than the average success count?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Success_Count > (SELECT AVG(Success_Count) FROM execution_summarry)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total count of jobs that have a success count greater than the average success count"
    },
    {
        "Question": "Which job has the maximum duration in minutes among jobs with a failed count less than 5?",
        "SQLQuery": "SELECT Job, Duration_Minutes FROM execution_summarry WHERE Failed_Count < 5 ORDER BY Duration_Minutes DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum duration in minutes among jobs with a failed count less than 5"
    },
    {
        "Question": "What is the average waiting count for jobs in the last session?",
        "SQLQuery": "SELECT AVG(Waiting_Count) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average waiting count for jobs in the last session"
    },
    {
        "Question": "How many jobs have a running count of more than 0?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Running_Count > 0",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a running count of more than 0"
    },
    {
        "Question": "Which job has the longest duration in seconds among jobs with more than 50 total counts?",
        "SQLQuery": "SELECT Job, Duration_Seconds FROM execution_summarry WHERE Total_Count > 50 ORDER BY Duration_Seconds DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the longest duration in seconds among jobs with more than 50 total counts"
    },
    {
        "Question": "What is the total success count for all jobs with a waiting count greater than 2?",
        "SQLQuery": "SELECT SUM(Success_Count) FROM execution_summarry WHERE Waiting_Count > 2",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total success count for all jobs with a waiting count greater than 2"
    },
    {
        "Question": "How many jobs have a failed count less than the average failed count?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Failed_Count < (SELECT AVG(Failed_Count) FROM execution_summarry)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a failed count less than the average failed count"
    },
    {
        "Question": "Which job has the minimum running count among jobs with a success count greater than 10?",
        "SQLQuery": "SELECT Job, Running_Count FROM execution_summarry WHERE Success_Count > 10 ORDER BY Running_Count ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum running count among jobs with a success count greater than 10"
    },
    {
        "Question": "What is the average total count for jobs in the last session?",
        "SQLQuery": "SELECT AVG(Total_Count) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average total count for jobs in the last session"
    },
    {
        "Question": "How many jobs have a duration in minutes less than the average duration?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Duration_Minutes < (SELECT AVG(Duration_Minutes) FROM execution_summarry)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a duration in minutes less than the average duration"
    },
    {
        "Question": "Which job has the maximum success count among jobs with a total count less than 50?",
        "SQLQuery": "SELECT Job, Success_Count FROM execution_summarry WHERE Total_Count < 50 ORDER BY Success_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum success count among jobs with a total count less than 50"
    },
    {
        "Question": "What is the sum of the running count for all jobs?",
        "SQLQuery": "SELECT SUM(Running_Count) FROM execution_summarry",
        "SQLResult": "Result of the SQL query",
        "Answer": "Sum of the running count for all jobs"
    },
    {
        "Question": "Which job had the shortest duration in seconds?",
        "SQLQuery": "SELECT Job, Duration_Seconds FROM execution_summarry ORDER BY Duration_Seconds ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the shortest duration in seconds"
    },
    {
        "Question": "What is the total number of jobs that ran in the last session?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total number of jobs that ran in the last session"
    },
    {
        "Question": "Which job had the highest total count overall?",
        "SQLQuery": "SELECT Job, Total_Count FROM execution_summarry ORDER BY Total_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the highest total count overall"
    },
    {
        "Question": "What is the average duration in seconds for all jobs?",
        "SQLQuery": "SELECT AVG(Duration_Seconds) FROM execution_summarry",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average duration in seconds for all jobs"
    },
    {
        "Question": "How many jobs have a success count greater than or equal to 50?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Success_Count >= 50",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a success count greater than or equal to 50"
    },
    {
        "Question": "Which job has the minimum running count in the last session?",
        "SQLQuery": "SELECT Job, Running_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Running_Count ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum running count in the last session"
    },
    {
        "Question": "What is the total failed count for all jobs that have a success count greater than 20?",
        "SQLQuery": "SELECT SUM(Failed_Count) FROM execution_summarry WHERE Success_Count > 20",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total failed count for all jobs that have a success count greater than 20"
    },
    {
        "Question": "Which job had the maximum waiting count in the last session?",
        "SQLQuery": "SELECT Job, Waiting_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Waiting_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum waiting count in the last session"
    },
    {
        "Question": "What is the average success count for jobs that have a duration in minutes greater than 30?",
        "SQLQuery": "SELECT AVG(Success_Count) FROM execution_summarry WHERE Duration_Minutes > 30",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average success count for jobs that have a duration in minutes greater than 30"
    },
    {
        "Question": "How many jobs have a total count less than 100?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Total_Count < 100",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a total count less than 100"
    },
    {
        "Question": "Which job had the maximum failed count in the last session?",
        "SQLQuery": "SELECT Job, Failed_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Failed_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum failed count in the last session"
    },
    {
        "Question": "What is the total success count for all jobs with a failed count less than 5?",
        "SQLQuery": "SELECT SUM(Success_Count) FROM execution_summarry WHERE Failed_Count < 5",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total success count for all jobs with a failed count less than 5"
    },
    {
        "Question": "Which job had the longest duration in minutes among jobs that ran in the last session?",
        "SQLQuery": "SELECT Job, Duration_Minutes FROM execution_summarry WHERE Last_Session = 1 ORDER BY Duration_Minutes DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the longest duration in minutes among jobs that ran in the last session"
    },
    {
        "Question": "What is the average waiting count for all jobs with a success count greater than 10?",
        "SQLQuery": "SELECT AVG(Waiting_Count) FROM execution_summarry WHERE Success_Count > 10",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average waiting count for all jobs with a success count greater than 10"
    },
    {
        "Question": "How many jobs have a duration in seconds less than the average duration?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Duration_Seconds < (SELECT AVG(Duration_Seconds) FROM execution_summarry)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a duration in seconds less than the average duration"
    },
    {
        "Question": "Which job has the minimum total count among jobs that ran in the last session?",
        "SQLQuery": "SELECT Job, Total_Count FROM execution_summarry WHERE Last_Session = 1 ORDER BY Total_Count ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum total count among jobs that ran in the last session"
    },
    {
        "Question": "What is the total running count for all jobs with a failed count greater than 5?",
        "SQLQuery": "SELECT SUM(Running_Count) FROM execution_summarry WHERE Failed_Count > 5",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total running count for all jobs with a failed count greater than 5"
    },
    {
        "Question": "Which job had the maximum success count among jobs that have a duration in minutes less than 20?",
        "SQLQuery": "SELECT Job, Success_Count FROM execution_summarry WHERE Duration_Minutes < 20 ORDER BY Success_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum success count among jobs that have a duration in minutes less than 20"
    },
    {
        "Question": "What is the average total count for jobs with a waiting count greater than 3?",
        "SQLQuery": "SELECT AVG(Total_Count) FROM execution_summarry WHERE Waiting_Count > 3",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average total count for jobs with a waiting count greater than 3"
    },
    {
        "Question": "How many jobs have a success count less than the average success count?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Success_Count < (SELECT AVG(Success_Count) FROM execution_summarry)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a success count less than the average success count"
    },
    {
        "Question": "Which job had the maximum failed count overall?",
        "SQLQuery": "SELECT Job, Failed_Count FROM execution_summarry ORDER BY Failed_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum failed count overall"
    },
    {
        "Question": "What is the total duration in minutes for all jobs that ran in the last session?",
        "SQLQuery": "SELECT SUM(Duration_Minutes) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total duration in minutes for all jobs that ran in the last session"
    },
    {
        "Question": "How many jobs have a waiting count greater than or equal to 2?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Waiting_Count >= 2",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a waiting count greater than or equal to 2"
    },
    {
        "Question": "Which job had the shortest duration in minutes in the last session?",
        "SQLQuery": "SELECT Job, Duration_Minutes FROM execution_summarry WHERE Last_Session = 1 ORDER BY Duration_Minutes ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the shortest duration in minutes in the last session"
    },
    {
        "Question": "What is the average failed count for jobs with a total count greater than 100?",
        "SQLQuery": "SELECT AVG(Failed_Count) FROM execution_summarry WHERE Total_Count > 100",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average failed count for jobs with a total count greater than 100"
    },
    {
        "Question": "How many jobs have a duration in seconds greater than the average duration?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Duration_Seconds > (SELECT AVG(Duration_Seconds) FROM execution_summarry)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a duration in seconds greater than the average duration"
    },
    {
        "Question": "Which job had the minimum duration in minutes?",
        "SQLQuery": "SELECT Job, Duration_Minutes FROM execution_summarry ORDER BY Duration_Minutes ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum duration in minutes"
    },
    {
        "Question": "What is the average success count for jobs with a running count less than 5?",
        "SQLQuery": "SELECT AVG(Success_Count) FROM execution_summarry WHERE Running_Count < 5",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average success count for jobs with a running count less than 5"
    },
    {
        "Question": "How many jobs have a total count greater than 500?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Total_Count > 500",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a total count greater than 500"
    },
    {
        "Question": "Which job had the maximum success count among jobs with a failed count less than 2?",
        "SQLQuery": "SELECT Job, Success_Count FROM execution_summarry WHERE Failed_Count < 2 ORDER BY Success_Count DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum success count among jobs with a failed count less than 2"
    },
    {
        "Question": "What is the total running count for all jobs that ran in the last session?",
        "SQLQuery": "SELECT SUM(Running_Count) FROM execution_summarry WHERE Last_Session = 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total running count for all jobs that ran in the last session"
    },
    {
        "Question": "Which job had the minimum total count overall?",
        "SQLQuery": "SELECT Job, Total_Count FROM execution_summarry ORDER BY Total_Count ASC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the minimum total count overall"
    },
    {
        "Question": "What is the average waiting count for jobs with a success count greater than 15?",
        "SQLQuery": "SELECT AVG(Waiting_Count) FROM execution_summarry WHERE Success_Count > 15",
        "SQLResult": "Result of the SQL query",
        "Answer": "Average waiting count for jobs with a success count greater than 15"
    },
    {
        "Question": "How many jobs have a duration in seconds less than 30 and a success count greater than 10?",
        "SQLQuery": "SELECT COUNT(Job) FROM execution_summarry WHERE Duration_Seconds < 30 AND Success_Count > 10",
        "SQLResult": "Result of the SQL query",
        "Answer": "Number of jobs with a duration in seconds less than 30 and a success count greater than 10"
    },
    {
        "Question": "Which job had the maximum duration in minutes among jobs with a failed count less than 1?",
        "SQLQuery": "SELECT Job, Duration_Minutes FROM execution_summarry WHERE Failed_Count < 1 ORDER BY Duration_Minutes DESC LIMIT 1",
        "SQLResult": "Result of the SQL query",
        "Answer": "Job with the maximum duration in minutes among jobs with a failed count less than 1"
    },
    {
        "Question": "What is the total success count for all jobs with a waiting count greater than 8?",
        "SQLQuery": "SELECT SUM(Success_Count) FROM execution_summarry WHERE Waiting_Count > 8",
        "SQLResult": "Result of the SQL query",
        "Answer": "Total success count for all jobs with a waiting count greater than 8"
    }
]



