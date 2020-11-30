from app import application
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm
import boto3

# dynamodb
db = boto3.resource('dynamodb', region_name='ap-south-1')
table = db.Table('signuptable')

# sns
notification = boto3.client('sns', region_name='ap-south-1')
topic_arn = "arn:aws:sns:ap-south-1:821574977720:flask-aws-sns"


@application.route('/')
@application.route('/home')
def home_page():
    return render_template('home.html')


@application.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        table.put_item(
            Item={
                'name': form.name.data, 'email': form.email.data,
                'mobile': form.mobile.data, 'country': form.country.data,
                'newsletter': form.newsletter.data
            }
        )
        # print(form.name.data, form.email.data, form.mobile.data, form.country.data, form.newsletter.data)
        msg = f"Congratulations !!! {form.name.data} is now a Premium Member !"
        flash(msg)
        # email to owner
        email_message = f'\nname: {form.name.data}' \
                        f'\nmobile: {form.mobile.data}' \
                        f'\nemail: {form.email.data}' \
                        f'\ncountry: {form.country.data}'
        notification.publish(Message=email_message, TopicArn=topic_arn, Subject="You've got a subscriber")
        return redirect(url_for('home_page'))
    return render_template('signup.html', form=form)