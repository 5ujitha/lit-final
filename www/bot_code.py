import os
import telebot
# import text2emotion as te
# hi
import random
import numpy
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton , ReplyKeyboardMarkup, Update

# import telegram
# from telegram.ext import InlineQueryHandler, CallbackQueryHandler

my_secret = '1931100716:AAGg2A0Zx2fvq5q1DBF9mvYmXCQAqCR2zzc'
bot = telebot.TeleBot(my_secret)

#use for formatting: parse_mode = 'html'


@bot.message_handler(commands=['start'])
def greet(message): 
  # bot.send_photo(message.chat.id, 'https://www.freeiconspng.com/img/28501', 'Hello there! How are you feeling today? I hope you are well \U0001F604')
  bot.send_message(message.chat.id, 'Welcome to Legal Buddies! I am your <b>one-stop legal companion</b> for people that are looking for legal avenues and where to get help! How may I help you today?\n\n<u><b>Here are a list of things I can assist with:</b></u> \n/legalaid: Find details of legal aid schemes available \n/lawyers: Find details of lawyers available \n', parse_mode = 'html')


#LEGAL AID SCHEMES
#Foreigner/Singaporean
def gen_markup():
    markup = InlineKeyboardMarkup() 
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Foreigner", callback_data="foreigner"), InlineKeyboardButton("Singaporean", callback_data="singaporean"), InlineKeyboardButton("Organisation", callback_data="organisation"))
    return markup

def legal_aid(message):
  if type(message) is str:
    if message == '/legalaid':
      return True

def lawyers(message):
  if type(message) is str:
    if message == '/lawyers':
      return True

@bot.message_handler(func=lambda msg: legal_aid(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "Are you a foreigner, Singaporean, or are you representing an organisation (e.g. NGOs)?", reply_markup=gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "foreigner":
        bot.send_message(call.message.chat.id,"<b>| QUICK LINKS |</b>\n\U0001F538 <b>Humanitarian Organisation for Migration Economics (HOME)</b> - workplace abuse: https://www.home.org.sg/contact \n\n\U0001F539 <b>Transient Workers Count Too (TWC2)</b> - workplace injury, abuse, or late salary payments: https://twc2.org.sg/\n\n\U0001F538 <b>Justice Without Borders (JWB)</b> - workplace abuse or violation:  https://forjusticewithoutborders.org/get-help/ \n\n\U0001F539<b>Foreign Domestic Worker Association for Social Support and Training (FAST)</b> - mediation services: https://www.fast.org.sg/care/", parse_mode = 'html', disable_web_page_preview=True)
    elif call.data == 'organisation':
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard = True)
        markup.add('Description [PLH]', 'Apply Now [PLH]')
        bot.send_message(call.message.chat.id,'Currently in Singapore, only ProjectLawHelp is available to aid NGOs', reply_markup=markup)
    elif call.data == "singaporean":
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard = True)
        markup.add('Civil', 'Criminal')
        bot.send_message(call.message.chat.id,'What field of law does your case fall under?', reply_markup=markup)

#Singaporean - type of case
def type_case_civil(message):
  if type(message) is str:
    if message == 'Civil':
      return True

def type_case_crim(message):
  if type(message) is str:
    if message == 'Criminal':
      return True

@bot.message_handler(func=lambda msg: type_case_crim(msg.text))
def message_handler(message):
   markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard = True)
   markup.add('Description [CLAS]', 'Apply Now [CLAS]')
   bot.send_message(message.chat.id,'How would you like to find out more about the Criminal Legal Aid Scheme?', reply_markup=markup)

#Criminal- ClAS
def type_case_clas_description(message):
  if type(message) is str:
    if message == 'Description [CLAS]':
      return True

def type_case_clas_apply(message):
  if type(message) is str:
    if message == 'Apply Now [CLAS]':
      return True
      
@bot.message_handler(func=lambda msg: type_case_clas_description(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "The Criminal Legal Aid Scheme (CLAS) provides pro-bono legal assistance to persons who are facing charges in court for non-death penalty criminal offences and who are unable to afford a lawyer. This means that a volunteer lawyer will be handling your case. \n\nYou may need to pay CLAS a co-payment amount before you can be assigned a volunteer lawyer. You will be advised how much, if any, you need to pay to CLAS when you are informed of the outcome of the application. The payment is calculated based on your income and assets.")


@bot.message_handler(func=lambda msg: type_case_clas_apply(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, 'You have to be formally charged in court and your charge must be covered by CLAS. You also have to undergo a Means Test and Merits Test.\n\n<b><u>Means Test</u></b>\nYou will be asked about your income, savings, property, and other assets. To qualify under the Means Test, your disposable income and assets should not be more than $10,000 each, over the last twelve months. For further clarifications of what disposable income and assets consist of, click <a href="https://www.lawsocprobono.org/Pages/Criminal-Legal-Aid-Scheme.aspx#qualify">here</a>.\n\nThe parents of single minor applicants under the age of 21 will also be assessed for means, and the same Means Test criteria apply.\nCLAS reserves the right to request for additional documents and/or to conduct additional interviews to ensure that a holistic assessment of Means is being done.\n\n<u><b>Merits Test</b></u>\nAn interviewing lawyer will ask questions regarding your case. Under the Merits Test, CLAS will decide whether giving you a lawyer will help your case. The Merits Test assesses whether you have reasonable grounds for defending your case in Court. The Merits Tester will ask you about the facts of your case and your intended defence, (if any). If there is no merit, CLAS may not approve your application.\n\n<b>Apply here:</b> <a href="https://tinyurl.com/y94fvvs7">Application Form</a>',parse_mode = 'html', disable_webpage_preview = True)




#CIVIL


def civil(message):
  if type(message) is str:
    if message == 'Civil':
      return True

@bot.message_handler(func=lambda msg: civil(msg.text))
def message_handler(message):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard = True)
    markup.add('Legal Aid Bureau', 'Primary Justice Project')

    bot.send_message(message.chat.id, "There are currently two schemes available for civil cases. Click the scheme you are interested to find more about.", reply_markup=markup)

def lab(message):
  if type(message) is str:
    if message == 'Legal Aid Bureau':
      return True

def pjp(message):
  if type(message) is str:
    if message == 'Primary Justice Project':
      return True

@bot.message_handler(func=lambda msg: lab(msg.text))
def message_handler(message):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard = True)
    markup.add('Description [LAB]', 'Apply Now [LAB]')
    bot.send_message(message.chat.id,'How would you like to find out more about Legal Aid Bureau?', reply_markup=markup)
    
@bot.message_handler(func=lambda msg: pjp(msg.text))
def message_handler(message):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard = True)
    markup.add('Description [PJP]', 'Apply Now [PJP]')
    bot.send_message(message.chat.id,'How would you like to find out more about Primary Justice Project?', reply_markup=markup)

# LAB
def lab_description(message):
  if type(message) is str:
    if message == 'Description [LAB]':
      return True

def lab_application(message):
  if type(message) is str:
    if message == 'Apply Now [LAB]':
      return True

@bot.message_handler(func=lambda msg: lab_description(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "<b><u>Legal Advice</u></b>\nLAB lawyers can give you oral advice on questions relating to Singapore law and suggest practical steps you may take in your case. \n\n<b><u>Legal Assistance (Drafting of Simple Legal Documents)</u></b>\nLAB can help you draft the following: \n1. Will (a legal document by which a person expresses his wishes as to how his property will be distributed upon his death and the persons who will manage the distribution of such property) \n2.Deed of Separation (a legal document signed by a married couple stating their mutual decision to live separately, before deciding on a divorce).\n\n<b><u>Legal Aid</u></b>\nLAB lawyers or a lawyer assigned by LAB can represent you in many kinds of civil proceedings, as set out in the Legal Aid and Advice Act. These include proceedings before the Court of Appeal, the High Court, District Courts, Magistrates’ Courts, the Family Courts, the Syariah Court and the Syariah Court Appeal Board, and the Commissioner of Labour under the Work Injury Compensation Act.\n\n<i>LAB does not handle criminal proceedings, some civil proceedings (defamation cases, proceedings from Small Claims tribunals, proceedings in the Family Justice Courts)</i>", parse_mode = 'html')

@bot.message_handler(func=lambda msg: lab_application(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "<b>Apply here:</b> https://eservices.mlaw.gov.sg/labesvc/\n(a) For Legal Advice and Assistance matters, you must pass the Means Test.\n(b) For Legal Aid, you must pass both the Means and Merits Test. \n\n<b><u>Means Test</u></b>\n1. The average Per Capita Gross Monthly Household Income (PCHI) must be $950 or lower for the last 12 months prior to the application\n2. The Annual Value of applicant’s place of residence owned by the applicant must be $13,000 or lower\n3. The applicant’s savings and non-CPF investments must be $10,000 or lower, if he is younger than 60 years old. Applicants aged 60 and above are allowed to have savings and non-CPF investments of $40,000 or lower.\n4. The applicant must not own any other property besides his/her place of residence.\n\n<u><b>Merits Test</b></u>\nWhether there are reasonable grounds for filing a case will be determined by the Legal aid Bureau. ", parse_mode = 'html')

#PJP
def pjp_description(message):
  if type(message) is str:
    if message == 'Description [PJP]':
      return True

def pjp_application(message):
  if type(message) is str:
    if message == 'Apply Now [PJP]':
      return True

@bot.message_handler(func=lambda msg: pjp_description(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "<b>Primary Justice Project is able to cover:</b>\n1. Civil claims below $60,000\n2. Divorce matters with most ancillary matters close to settlement\n3. Representation on behalf of an unrepresented accused person during the Criminal Case Management System (CCMS) or the Criminal Case Resolution (CCR) process. This will include at least one round of written or oral representations to the prosecutors \n4. Harassment cases \n5. Neighbour disputes.\n\n<b>Costs under this project: Fixed fee of $1800 for 6h.</b>",parse_mode = 'html')

@bot.message_handler(func=lambda msg: pjp_application(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "No appointment is required, do bring along a copy of your ID for registration of the session and any other documents relevant to your legal issue to 1 Havelock Square B1-6/7/8, State Courts Towers, Singapore 059724. \n\n<b>Tel:</b> +65 6557 4100\n<b>Email:</b> help@cjc.org.sg", parse_mode = 'html')


#ProjectLawHelp
def type_case_description(message):
  if type(message) is str:
    if message == 'Description [PLH]':
      return True

def type_case_application(message):
  if type(message) is str:
    if message == 'Apply Now [PLH]':
      return True

@bot.message_handler(func=lambda msg: type_case_description(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "We match community organisations which qualify for assistance with law firms willing to provide free non-litigation commercial legal services. Examples of such legal services include: \n1. <b>Corporate Law </b> (e.g. advice on contracts with suppliers, indemnity agreements for corporate sponsors, drafting pledges for donors)\n2. <b>Employment Law</b> (e.g. drafting or reviewing employment contracts)\n3. <b>Intellectual Property Law</b> (e.g. advice on copyright, data protection, website use)\n 4. <b>Property Law </b> (e.g. lease terms)\n5. Other legal matters <b>not</b> involving court litigation advice or representation. \n\nSuccessful applicants will work directly with the law firm assigned. All legal matters of the community organisation are handled in professional confidence by he volunteer law practice.",parse_mode = 'html')


@bot.message_handler(func=lambda msg: type_case_application(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "https://form.jotform.me/91284013638456")


#Find no of lawyers available

@bot.message_handler(func=lambda msg:lawyers(msg.text))
def message_handler(message):
   my_number= str(numpy.random.randint(0,100))
   bot.send_message(message.chat.id,"Number of available lawyers: " + my_number)


bot.polling()