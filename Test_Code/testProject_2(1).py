from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Test_Data import project_2
import pytest
import time 

class Test_Project_3:
    url = "https://opensource-demo.orangehrmlive.com" 

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Edge()
        yield
        self.driver.close() 
    @pytest.fixture    
    def test_login(self, booting_function):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=project_2.Project_Selectors_2.input_box_username).send_keys(project_2.Project_Data_2.username)
        self.driver.find_element(by=By.NAME, value=project_2.Project_Selectors_2.input_box_password).send_keys(project_2.Project_Data_2.password)
        self.driver.find_element(by=By.XPATH, value=project_2.Project_Selectors_2.login_xpath).click()
        
    def test_employee_creation(self,booting_function,test_login):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.pim_xpath_1).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.pim_add_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.create_login_details_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.first_name_xpath).send_keys(project_2.Project_Data_3.first_name)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.middle_name_xpath).send_keys(project_2.Project_Data_3.middle_name)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.last_name_xpath).send_keys(project_2.Project_Data_3.last_name)
        time.sleep(1)
        element = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.employee_id_xpath)
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(1)
        element.send_keys(project_2.Project_Data_3.emp_id)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.username_xpath).send_keys(project_2.Project_Data_3.user_name_field_1)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.password_xpath).send_keys(project_2.Project_Data_3.password_field)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.confirm_password_xpath).send_keys(project_2.Project_Data_3.password_field)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.enabled_button).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.save_button).click()
        time.sleep(3)
        #print("New Employee under PIM is created successfully..!!")"""
        
    
        
    #updating employee contact details
    def test_TC_PIM_06(self,booting_function,test_login): 
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.pim_xpath_1).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.employee_list_empid_xpath).send_keys(project_2.Project_Data_3.emp_id)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value='/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.employee_list_vya_edit_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_contact_details_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.street1_xpath).send_keys(project_2.Project_Data_3.street_1)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.street2_xpath).send_keys(project_2.Project_Data_3.street_2)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.city_xpath).send_keys(project_2.Project_Data_3.city)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.state_xpath).send_keys(project_2.Project_Data_3.State)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.zip_code_xpath).send_keys(project_2.Project_Data_3.zip_code)
        time.sleep(1)
        elements = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.country_xpath)
        elements.click()
        for i in range(99):
            elements.send_keys(Keys.ARROW_DOWN)
        elements.send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.home_number_xpath).send_keys(project_2.Project_Data_3.Home_no)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.mobile_number_xpath).send_keys(project_2.Project_Data_3.mobile_no)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.work_number_xpath).send_keys(project_2.Project_Data_3.work_no)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.work_email_xpath).send_keys(project_2.Project_Data_3.work_email)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.other_email_xpath).send_keys(project_2.Project_Data_3.other_email)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.save_1_xpath).click()
        time.sleep(5)
        print("Contact Details is created successfully")
        time.sleep(6)
        self.driver.refresh()
        time.sleep(4)
        d1=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.street1_xpath).is_displayed()
        print("street 1 is presented")
        d2=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.street2_xpath).is_displayed()
        print("street 2 is presented")
        d3=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.city_xpath).is_displayed()
        print("city is presented")
        d4=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.state_xpath).is_displayed()
        print("state is presented")
        d5=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.zip_code_xpath).is_displayed()
        print("zip code is presented")
        country=self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]').text
        print("country is presented")
        d6=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.home_number_xpath).is_displayed()
        print("home number is presented")
        d7=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.mobile_number_xpath).is_displayed()
        print("mobile number is presented")
        d8=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.work_number_xpath).is_displayed()
        print("work number is presented")
        d9=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.work_email_xpath).is_displayed()
        print("work email is presented")
        d10=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.other_email_xpath).is_displayed()
        print("other email is presented")
        
    #emergency contact details
    def test_TC_PIM_07(self,booting_function,test_login): 
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.pim_xpath_1).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.employee_list_empid_xpath).send_keys(project_2.Project_Data_3.emp_id)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.employee_list_search_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.employee_list_vya_edit_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_emer_contacts_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.emergency_contact_add_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.emergency_name_xpath).send_keys(project_2.Project_Data_4.emergency_name)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.emergency_relationship_xpath).send_keys(project_2.Project_Data_4.emergency_relationship)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.emergency_home_tele_xpath).send_keys(project_2.Project_Data_4.home_telephone)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.emergency_mobileno_xpath).send_keys(project_2.Project_Data_4.emergency_mobile)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.emergency_worktele_xpath).send_keys(project_2.Project_Data_4.work_telephone)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_6.emergency_contact_save_xpath).click()
        print("Emergency contact details has created")
        time.sleep(4)
        data_1 = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div').text
        if data_1=='jay':
            print("Name is present under emergency contact details")
        data_2 = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div').text
        if data_2=='Father':
            print("Father Name is present under emergency contact details")
        data_3 = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div').text
        if data_3=='9575434545':
            print("Home telephone no is present under emergency contact details")
        data_4 = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div').text
        if data_4=='7894563425':
            print(" mobile no is present under emergency contact details")
        data_5 = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div').text
        if data_5=='6537428778':
            print("work telephone no is present under emergency contact details")
        print("ALL FILLED DETAILS ARE PRESENT UNDER EMERGENCY CONTACT DETAILS")