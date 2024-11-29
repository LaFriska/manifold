# Manifold

## NOTE THAT THIS APP IS STILL UNDER DEVELOPMENT

"Manifold" is an open source, multifaceted Discord bot designed to streamline various academic tasks, primarily focusing on managing degrees at the Australian National University (ANU). This comprehensive system offers features such as degree planning, course searching, and data management. Written in Java for Discord bot functionalities and Python for data manipulation tasks, "Manifold" utilizes SQL for efficient database management, course data processing, and data wrangling. With its diverse capabilities and integration with Discord, "Manifold" serves as a powerful tool for students and administrators alike, enhancing the academic experience at ANU.

## Development

In order to replicate this system on your local computer, please follow the following steps.

1. Clone the git repo on your local machine. You may do so using the IDE you are using, or by using `git clone`.
2. Ensure you have a python virtual environment module under `./course_processor/`.
3. Ensure you have a PostgreSQL server installed on  your computer. Visit [this](https://www.bing.com/search?q=postgre+sql+download&cvid=1448d5a296574bb89c28925baa318289&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDIzOTlqMGo5qAIEsAIB&FORM=ANAB01&PC=NMTS) for more information.
4. Create a file named `config.properties` at root director of this project, with the following template
    
```md
#Bot
token = YOUR_TOKEN
prefix = !

# Database configurations
db_server = localhost
db_database = postgres
db_port = 5432
db_username = postgres
db_password = YOUR_PASSWORD
```
Make sure to change any key-value pairs to match your database server or desired prefix for Discord bot.
