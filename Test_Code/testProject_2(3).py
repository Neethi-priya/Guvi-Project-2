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
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.username_xpath).send_keys(project_2.Project_Data_3.user_name_field_3)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.password_xpath).send_keys(project_2.Project_Data_3.password_field)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.confirm_password_xpath).send_keys(project_2.Project_Data_3.password_field)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.enabled_button).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.save_button).click()
        time.sleep(3)
        print("New Employee under PIM is created successfully..!!")
        
    def test_TC_PIM_09(self,booting_function,test_login): 
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
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_job_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.job_joined_date_xpath).send_keys(project_2.Project_Data_4.job_joined_date)
        time.sleep(1)
        title=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.job_Title_xpath)
        title.click()
        for i in range(17):
            title.send_keys(Keys.ARROW_DOWN)
        title.send_keys(Keys.ENTER)
        time.sleep(1)
        category=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.job_category_xpath)
        category.click()
        for i in range(6):
            category.send_keys(Keys.ARROW_DOWN)
        category.send_keys(Keys.ENTER)
        time.sleep(1)
        sub_unit=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.job_subunit_xpath)
        sub_unit.click()
        for i in range(4):
            sub_unit.send_keys(Keys.ARROW_DOWN)
        sub_unit.send_keys(Keys.ENTER)
        time.sleep(1)
        location=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.job_location_xpath)
        location.click()
        for i in range(1):
            location.send_keys(Keys.ARROW_DOWN)
        location.send_keys(Keys.ENTER)
        time.sleep(1)
        status=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.job_employement_status)
        status.click()
        for i in range(2):
           status.send_keys(Keys.ARROW_DOWN)
        status.send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.job_include_toggle_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.contract_start_date_xpath).send_keys(project_2.Project_Data_4.contract_start_date)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.contract_end_date_xpath).send_keys(project_2.Project_Data_4.contract_end_date)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.job_save_button_xpath).click()
        time.sleep(2)
        print("Updated Employee Job Details..!")
        time.sleep(3)
        #self.driver.refresh()
        data_1 =self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.job_joined_date_xpath).is_displayed()
        if data_1 :
            print("Joined date is filled")
        data_2 =self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]').text 
        if data_2=='QA Engineer':
            print("Job title is filled")
        data_3 =self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]').text
        if data_3=='Professionals':
            print("Job category is filled")
        data_4 =self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[1]').text
        if data_4=='Quality Assurance':
            print("Job sub unit is filled")
        data_5 =self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[1]').text
        if data_5 == 'Full-Time Contract':
            print("Employment status is filled") 
        data_6 =self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.contract_start_date_xpath).is_displayed()
        if data_6:
            print("contract start date is filled")
        data_7 =self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.contract_end_date_xpath).is_displayed()
        if data_7 :
            print("contract end date is filled")
        data_8 = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.job_include_toggle_xpath).is_enabled()
        if data_8:
            print("Include toggle is enabled")
        print("ALL FILLED DETAILS ARE PRESENT UNDER JOB DETAILS")
        
     
    #termination and check job activation
    def test_TC_PIM_10(self,booting_function,test_login):
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
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_job_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.terminate_employement).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.termination_date_xpath).send_keys(project_2.Project_Data_4.termination_date)
        time.sleep(1)
        ter = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div/div[1]')
        ter.click()
        for i in range(5):
            ter.send_keys(Keys.ARROW_DOWN)
            ter.send_keys(Keys.ENTER)
        ter.click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.termination_save_button_xpath).click()
        time.sleep(5)
        print("TERMINATION DATE AND REASON ARE CREATED")
        time.sleep(6)
        data=self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/p').text
        if data == 'Terminated on: 2022-10-11':
            print("Termination date is validated")
        time.sleep(1)
        data_1=self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button')
        if data_1:
            print("Active Employement is Visible")
        else:
            print("Its not visible")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button').click()
        time.sleep(7)
        t1 =self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button').text
        if t1 == 'Terminate Employment':
            print("TC_PIM_10  : EMPLOYEE JOB is Activated")
        else:
            print("no")
            
    
        
        
    
        
        
        
        
        
        
        