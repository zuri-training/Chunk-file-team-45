from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):

    name = forms.CharField(max_length=120, label='Name',required=True)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(widget=forms.Textarea, label='Message', required=True)

    def get_info(self):
        """
        Method that returns formatted information
        :return: msg
        """
        # Cleaned data
        clean_data = super().clean()

        name = clean_data.get('name').strip()
        from_email = clean_data.get('email')

        msg = f'{name}, with email {from_email} says\n'
        msg += clean_data.get('message')

        return msg

    def send(self):

	    msg = self.get_info()

	    try:
	    	send_mail(
	    		subject='Hello, I need help.',
	    		message=msg,
	    		from_email='admin@mail.com',
				recipient_list=['user@mail.com']
			)
	    	return True
	    except:
	    	return None 