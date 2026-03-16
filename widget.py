# # Text Widget in Streamlit
import streamlit as st
import datetime
from altair import value

# from altair import value
# from numpy.ma.core import max_val
# from streamlit import number_input
#
# st.markdown("# Markdown display")
# st.markdown("## Markdown display")
# st.markdown("### Markdown display")
#
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.text("This is a text")
# st.caption("This is a caption")
st.write("##*************************************************************************************##")

#   *************Dropdown widget************
st.header("All about dropdown")

Grade = ["Grade 7","Grade 8","Grade 9","Grade 19","Grade 11","Grade 12"]

selected_grade = st.selectbox(label="Grade",
                              options=Grade,placeholder="Select grade here",
                              index=None,

                              help="select your grade ")

# print(selected_grade)

# Multiselect widget

sections = [ "Grade7_Sec1",  "Grade7_Sec2", "Grade8_Sec1", "Grade8_Sec2",
                     "Grade9_Sec1", "Grade10_Sec1", "Grade11_Sec1", "Grade11_Sec2",
                     "Grade12_Sec1"]
selected_sections = st.multiselect(label="Select section/s",
                                   options=sections,help="selecte your section/s ",
                                   max_selections=3,
                                   placeholder= "select sections"

                                   )

# print("selected_sections")

# basic slider
basic_slider = st.slider(label="basic label",
                         min_value=1,
                         max_value=100,
                         value=50) # value - default value
# st.write("selected number: {}".format(basic_slider))
st.write(f"selected value: {basic_slider}")

# float slider
float_slider = st.slider(label="float slider",
                         min_value=1.0,
                         max_value=100.00,
                         value=50.00) # value - default value
# st.write("selected number: {}".format(basic_slider))
st.write(f"selected value: {float_slider}")

# range slider
range_slider = st.slider(label="select range",
                         min_value=1,
                         max_value=100,
                         value=(30,50)) # value - default value
# st.write("selected range: {}".format(range_slider))
st.write(f"selected range: {range_slider}")

# date slider upto today

date_slider_today = st.slider(label="select a date",
                        min_value = datetime.date(2025, 8, 17),
                        # max_value = datetime.date(2026, 2, 26),
                        max_value=datetime.date.today(),   # ← max is today
                        value = datetime.date(2026, 1, 1),
                        format = "MM/DD/YY",
                        )

st.write(f"selected date: {date_slider_today}")

# date slider - import datetime

date_slider = st.slider(label="select a date",
                        min_value = datetime.date(2025, 8, 17),
                        max_value = datetime.date(2026, 2, 26),
                        # max_value=datetime.date.today(),   # ← max is today
                        value = datetime.date(2026, 1, 1),
                        format = "MM/DD/YY",
                        )

st.write(f"selected date: {date_slider}")

st.write("##*************************************************************************************##")
# Number input
number_input = st.number_input(label="Enter a number",
                               min_value=0,
                               max_value=100,
                               value=50,
                               step=1,
                               help="use widget to input a number.")

st.write("##*************************************************************************************##")
# Side bar number input
sidebar_number_input = st.sidebar.number_input(label="Enter a number",
                               min_value=0,
                               max_value=100,
                               value=50,
                               step=1,
                               help="use widget to input a number.")
st.write(f"Selected number:  {sidebar_number_input}")

st.write("##*************************************************************************************##")

# add a form in the main area
st.header("Forms in streamlit")
Staff_Name = ['    ','Fiona Ochieng', 'Ahmed Qaalib', 'Saciid Bile', 'Guleid Ali',
       'Ebenezer Okike', 'Abdikhaliq Mohamoud Awil', 'Josephine Adoyo',
       'Suubiye Abdilahi', 'Tomoki Sasaki', 'Abdiaziz Sulub',
       'Ubah Hamuud Muhumed', 'Khalid Ismail', 'Abdilahi Cumar',
       'Nancy Wambura', 'Mary Fisher', 'Silver Enyoru', 'Zelalem Fikadu',
       'Ridge Daka', 'Matthew Baucco', 'Benjamin DeCoste', 'Fahma Abdi',
       'Elvis Alavi', 'Allison Ballweg', 'Istahil Hassan']
form  = st.form(key="form1",
                clear_on_submit=False,
                enter_to_submit=True,
                border=True)
selected_staff_name = form.selectbox(label="Staff Name",
               options=Staff_Name,
               placeholder=None
               )
submit = form.form_submit_button(label="Submit details")

if submit:
    print(f"Submit button value {submit}")
    print(selected_staff_name)

# form in sidebar
second_form = st.sidebar.form(key="sidebar_form")
age = second_form.number_input(label="Age",
                                         min_value=20,
                                         max_value=60)
submit_second_form = second_form.form_submit_button()

if submit_second_form:
    st.markdown("second form was submited")
    print(age)

# Tabs
st.header("Tabs")
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.subheader("I am in tab 1")

with tab2:
    st.subheader("I am in tab 2")

with tab3:
    st.subheader("I am in tab 3")


# Learnabout columns
st.header("Columns")

col1, col2, col3 = st.columns(3, gap="small", vertical_alignment="top")

with col1:
    st.subheader("Column 1")
    st.image("abr_net.jpg")

with col2:
    st.subheader("Column 2")
    st.image("abr_net.jpg")

with col3:
    st.subheader("Column 3")
    st.image("abr_net.jpg")

col4, col5, col6 = st.columns([1,2,3], gap="small", vertical_alignment="top")

col4.subheader("Column 4")
col5.subheader("Column 5")
col6.subheader("Column 6")

col7, col8 = st.columns([1,4], gap="small", vertical_alignment="top")


col7.subheader("Column 7")
col7.image("abr_net.jpg")

col8.subheader("Column 8")
col8.image("abr_net.jpg")

st.write("................................................................................... ")
# Sidebar
st.header("Sidebar")

st.sidebar.subheader("Sidebar")
st.sidebar.selectbox(label="Gender", options=["M","F"])