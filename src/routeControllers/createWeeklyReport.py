from flask import Blueprint, jsonify, render_template, request
from src.appConfig import getConfig
from src.services.weeklyReportCreationHandler import WeeklyReportCreationHandler
import datetime as dt

# get application config
appConfig = getConfig()

createWeeklyReportPage = Blueprint('createWeeklyReport', __name__,
                                   template_folder='templates')


@createWeeklyReportPage.route('/', methods=['GET', 'POST'])
def createWeeklyReport():
    # in case of post request, create weekly report and return json response
    if request.method == 'POST':
        reqData = request.get_json()
        reportCreator = WeeklyReportCreationHandler(
            appConfig['weeklyRepCreationServiceUrl'])
        startDate = dt.datetime.strptime(reqData['startDate'], '%Y-%m-%d')
        endDate = dt.datetime.strptime(reqData['endDate'], '%Y-%m-%d')
        resp = reportCreator.createWeeklyReport(startDate, endDate)
        return jsonify(resp), resp['status']
    # in case of get request just return the html template
    return render_template('createWeeklyReport.html.j2')
