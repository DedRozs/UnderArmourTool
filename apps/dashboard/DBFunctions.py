#!/usr/bin/python
import pandas as pd
import pymysql
from django.conf import settings


def query_prod(query: str) -> pd.DataFrame:
    """Execute raw SQL on the external DB and get results as DataFrame."""
    with pymysql.connect(
        host=settings.EXTERNAL_DB_HOSTNAME,
        user=settings.EXTERNAL_DB_USERNAME,
        passwd=settings.EXTERNAL_DB_PASSWORD,
        db=settings.EXTERNAL_DB_NAME,
    ) as connection:
        cur = connection.cursor()
        cur.execute(query)
        data_frame = pd.DataFrame(cur.fetchall())

    return data_frame


# Simple routine to run a query on a database and print the results:

# query="""SELECT
#     et.eventID,
#     et.teamID,
#     et.rosterSize,
#     et.teamCode,
#     t.name,
#     ld.name,
#     s.name,
#     ll.name,
#     u.id,
#     u.firstName,
#     u.lastName,
#     lut.name
# FROM
#     sportsthreaddev.EventTeams et
# LEFT JOIN sportsthreaddev.Teams t ON
#     et.teamID = t.ID
# LEFT JOIN sportsthreaddev.Sport s ON
#     t.sportID = s.ID
# LEFT JOIN sportsthreaddev.LookupLevels ll ON
#     t.levelID = ll.ID
# LEFT JOIN sportsthreaddev.LookupDivisions ld ON
#     t.divisionID = ld.ID
# LEFT JOIN sportsthreaddev.EventTeamRoster etr ON
#     et.teamID = etr.teamId
# LEFT JOIN sportsthreaddev.`User` u ON
#     etr.userId = u.id
# LEFT JOIN sportsthreaddev.LookupUserType lut ON
#     u.userTypeID = lut.ID
# WHERE et.eventID =5941 and u.userTypeID =2"""

# print(query_prod(query))
