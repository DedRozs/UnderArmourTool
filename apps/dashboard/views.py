from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from apps.authentication.models import *
from . import DBFunctions as DBF
import json
import pandas as pd
from django.template import loader
from django.http import HttpResponse
from datetime import datetime
from io import StringIO

# Create your views here.
def update_partners():
    query = f"""SELECT
        p.ID,
        p.name
    FROM
        Partners p;
    """
    partner_df = DBF.query_prod(query)
    partner_dict= partner_df.to_dict('records')
    partner_instances = [
        Partner(
                id = record[0],
                name = record[1],
            ) for record in partner_dict]

    Partner.objects.bulk_create(partner_instances, update_conflicts=True, update_fields=['name'], unique_fields=['id'])
    print(len(partner_instances)) 

@login_required(login_url="/login/")
def event_claim_export(request):

    now = datetime.now()
    profile = request.user.userprofile
    partnerID = list(profile.partner.values_list('id', flat=True))
    partner_ids_str = str(partnerID).replace("[","").replace("]","")
    
    query = f"""SELECT
            e.name AS "Event Name",
            ld.name AS "Division",
            ec.userId AS "User ID",
            u.firstName AS "First Name",
            u.lastName AS "Last Name",
            u.birthday AS "DOB",
            u.gender AS "Gender",
            qc.checkedInAt AS "Checked-In",
            u.email AS "Athlete Email",
            u.phone AS "Athlete Phone",
            t.name AS "Team Name",
            etr.jerseyNumber AS "Jersey Number",
            qc.url AS "QR Badge Link",
            ec.status AS "Event Claim Status",
            concat(u2.firstName, " ", u2.lastName) AS "Parent Name",
            u2.email AS "Parent Email",
            u2.phone AS "Parent Phone",
            erp.totalAmount/100 AS "Purchase Price",
            erp.createdAt AS "Purchase Date",
            ec.claimedAt  AS "Claimed At Date",
            av.isVerified AS "Age verification status",
            p.inquiryId, 
            lq.title AS "League Question",
            la.answer AS "League Answer" ,
            lad.document AS "League Answer Document",
            lq.id
        FROM
            sportsthreadprod.EventClaims ec
        LEFT JOIN sportsthreadprod.LookupDivisions ld ON
            ec.divisionId = ld.ID
        LEFT JOIN sportsthreadprod.Events e ON
            ec.eventId = e.id
        LEFT JOIN sportsthreadprod.`User` u ON
            ec.userId = u.ID
        LEFT JOIN sportsthreadprod.`User` u2 ON
            u.parentID = u2.ID
        LEFT JOIN sportsthreadprod.QrCodes qc ON
            ec.eventId  = qc.eventId
            AND ec.userId  = qc.userId
        LEFT JOIN sportsthreadprod.EventTeamRoster etr ON
            ec.eventId = etr.eventId and ec.userId =etr.userId  and ec.teamId =etr.teamId 
        LEFT JOIN sportsthreadprod.Teams t ON
            ec.teamId  = t.ID
        LEFT JOIN sportsthreadprod.EventRegistrationPayments erp ON
            ec.paymentId = erp.id
        LEFT JOIN sportsthreadprod.AgeVerification av ON
            ec.userId = av.userId 
        LEFT JOIN sportsthreadprod.LeagueQuestions lq ON
            ec.eventId = lq.eventId 
        LEFT JOIN sportsthreadprod.LeagueAnswers la ON
            lq.id  = la.questionId and ec.userId = la.userId 
        LEFT JOIN sportsthreadprod.LeagueAnswerDocuments lad ON
            la.id  =lad.answerId
        LEFT JOIN sportsthreadprod.PersonaRequests p ON
            av.personaRequestId = p.id
        WHERE
            e.partnerid in ({partner_ids_str}) and (e.endDate like "%{now.year}%" or e.endDate like "%{int(now.year+1)}%"  )
        ORDER BY u.id, lq.index;"""
    data = DBF.query_prod(query)
    report_dict = {}
    if len(data.columns) >=1:
        for index, row in data.iterrows():
            if row[9] == "":
                row[9] = None
            if row[8] == "":
                row[8] = None
            if row[12] == "":
                row[12] = None
            if str(row[17]) == "" or row[17] == None:
                row[17] = None
            else:
                row[17] = int(row[17])
            if str(row[20]).lower() == "nan" or row[20] == None:
                row[20] = None
            else:
                row[20] = int(row[20])
            if str(row[21]).lower() == "nan" or row[21] == None:
                row[21] = None
            else:
                row[21] = str(row[21])
            
            if str(row[23]).lower() == "nan":
                row[23]= None
            
            if str(row[24]).lower() == "nan":
                row[24]= None
            
            if str(row[11]).lower() == "nan":
                row[11]= None

            user = {
                "Event_Name":row[0],
                "Division":row[1],
                "User_ID":row[2],
                "First_Name":row[3],
                "Last_Name":row[4],
                "DOB":str(row[5]),
                "Gender":row[6],
                "Athlete_Email":row[8],
                "Athlete_Phone":row[9],
                "Team_Name":row[10],
                "Jersey_Number":row[11],
                "Event_Claim_Status":row[13],
                "Parent_Name":row[14],
                "Parent_Email":row[15],
                "Parent_Phone":row[16],
                "Claimed_At_Date":str(row[19]),
                }
            

            
            try:
                if row[22] != None:
                    report_dict[user["User_ID"]][row[22]] = row[23]
                elif row[23] !=None:
                    report_dict[user["User_ID"]][row[22]] = row[24]
                else:
                    report_dict[user["User_ID"]][row[22]] = row[23]
            except:
                report_dict[user["User_ID"]] = user


        ReportJson = json.dumps(report_dict, indent=4)
        ReportDF = pd.read_json(StringIO(ReportJson), orient='index')
        ReportDF = ReportDF.drop(ReportDF.columns[-1],axis=1)
        ReportDF = ReportDF.set_index('User_ID')

    else:
        ReportDF = None

    try:
        if len(ReportDF.columns) >=1:
            has_data = True
    except:
        has_data = False



    context = {
        'segment': 'eventclaimexport',
        "PartnerID":partnerID,
        "Data":ReportDF,
        "has_data":has_data,
            } 
    html_template = loader.get_template('dashboard/eventclaimexport.html')
    return HttpResponse(html_template.render(context, request))