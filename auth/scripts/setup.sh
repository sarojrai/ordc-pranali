# Dumps Models for fixtures
python manage.py dumpdata notification.ClientCommunication --indent 4 >apps/notification/fixtures/initial_client_communication.json 
# Loads fixtures into Models
python manage.py loaddata apps/notification/fixtures/initial_commu_mode.json