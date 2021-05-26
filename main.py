import os
import sendgrid
from flask import Flask
from flask_restful import Api, Resource, reqparse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


app = Flask(__name__)
api = Api(app)

email_put_args = reqparse.RequestParser()
email_put_args.add_argument("to", type=str, help="Recipient Email Required", required=True)
email_put_args.add_argument("subject", type=str, help="Subject Line Required", required=True)
email_put_args.add_argument("content", type=str, help="Content Required", required=True)

def email(self, args):
    message = Mail(from_email = "turingmesh@gmail.com",
                   to_emails = args['to'],
                   subject = args['subject'],
                   plain_text_content = args['content'])
    try:
        send_message = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = send_message.send(message)

    except Exception as e:
        print(e.message)


class EmailService(Resource):
    def put(self):
        args = email_put_args.parse_args()
        email(self, args)
        return {"data": "Email has been sent successfully"}


api.add_resource(EmailService, "/api/v1/email")

if __name__ == "__main__":
    app.run(debug=True)