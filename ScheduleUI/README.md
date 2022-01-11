# ScheduleUI #
### libs:
* psycopg2
* traceback
* sys
* PyQt5

### Methods of the "MainWindow" class: ###
*	_connect_to_db - connect to database "timetable_db"
*	_create_sсhedule_tab - create tab for selected day of week
*	_create_day_table - create table
*	_update_day_table - add rows from db and other update table 
*	_change_day_from_table - change rows in table
*	_delete_day_table - delete row in table and db