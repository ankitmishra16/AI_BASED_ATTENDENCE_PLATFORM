import argparse
from flask import Flask,request,jsonify
import json
import requests

@app.route('/institue/add_attendence', methods=['GET', 'POST'])
def schedule_service():
    content = request.json
    """
    content
	{
		"institue_id":1213,
		"course":cs123,
		"present":[roll_no_1,roll_no_2,...]
	}

    """
    return {"Response":"OK/ERROR"}


@app.route('/institue/get_attendence', methods=['GET', 'POST'])
def schedule_service():
    content = request.json
    """
	input content
	{

		"institue_id":1213,
		"query":{
					"courses":["cs123","cs247"] OR ["ALL"]
					"students":["roll_no_1",["roll_no_2"]] OR ["ALL"]
					"start_date":"12-03-2020"
					"end_date":"22-04-2020"
					"condition":{
							"greater_than":"80"   FOR INDIVIDUAL COURSES
							"less_than":"50"	
						}
					CONDITION CAN BE NONE IF CONDITION IS NOT NONE THEN EITHER greater_than OR less_than will be present
			}
	}
	
    """
    """
    output if no condition
    {
		"course_id_1":{
			"date_1":["roll_no_1","roll_no_2"],
			"date_2":["roll_no_1","roll_no_3"],
			.
			.
			.
		},
		"course_id_2":{
			"date_1":["roll_no_1","roll_no_2"],
			"date_2":["roll_no_1","roll_no_3"],
			.
			.
			.
		}
    }


        OUTPUT if condition
    {
		"course_id_1":["roll_no_1","roll_no_2"]
		"course_id_2":["roll_no_1","roll_no_5"]
	}
    
    """
    return OUTPUT


@app.route('/corporate/add_attendence', methods=['GET', 'POST'])
def schedule_service():
    content = request.json
    """
    content
	{
		"corporate_id":1213,
		"type":"IN/OUT",
		"ids":[emp_no_1,emp_no_2,...] 

	}

    """
    return {"Response":"OK/ERROR"}


@app.route('/corporate/get_attendence', methods=['GET', 'POST'])
def schedule_service():
    content = request.json
    """
    input content
	{
		"corporate_id":1213,
		"ids":[emp_no_1,emp_no_2] OR ["ALL"]
		"query":{
			"start_date":"12-03-2020"
			"end_date":"22-04-2020"
			"effective_time":"YES" or None
			"condition":{
				"greater_than":"80"   FOR INDIVIDUAL COURSES
				"less_than":"50"	
			}
		}
	}

    """

    """
    OUTPUT
    case 1: if effective time is None
    			subcase 1: if condition is None:
    					OUTPUT = {
									"date_1":[emp_no_1,emp_no_2],
									"date_2":[emp_no_1,emp_no_2],
									.
									.

    						}
    			subcase 2: if condition is Not None
    					OUTPUT = {
								ids:[emp_1,emp_2]   these are the emps whose attendence between start and end date is according to condition
    						}
    case 2: if effective time is not None
			in this case condition will always be present
    			
    					OUTPUT = {
								ids:[emp_1,emp_2]   these are the emps whose average effective time between start and end date  is according to condition
    						}
    """
    return OUTPUT


if __name__ == "__main__": 
	ap = argparse.ArgumentParser()
	ap.add_argument("-p","--port",required=True)
	args = vars(ap.parse_args())       
	app.run(debug=True,port=int(args["port"])) 