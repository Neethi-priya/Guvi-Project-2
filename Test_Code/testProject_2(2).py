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
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.username_xpath).send_keys(project_2.Project_Data_3.user_name_field)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.password_xpath).send_keys(project_2.Project_Data_3.password_field)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.confirm_password_xpath).send_keys(project_2.Project_Data_3.password_field)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.enabled_button).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.save_button).click()
        time.sleep(3)
        #print("New Employee under PIM is created successfully..!!")
        
    
    
            
    def test_TC_PIM_08(self,booting_function,test_login): 
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.pim_xpath_1).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.employee_list_empid_xpath).send_keys(project_2.Project_Data_3.emp_id)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.employee_list_vya_edit_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_dependants_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.dependents_add_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.dependents_name_xpath).send_keys(project_2.Project_Data_4.dependent_name)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.dependents_dob_xpath).send_keys(project_2.Project_Data_4.dependent_dob)
        time.sleep(1)
        data= self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.dependents_relationship_xpath)
        data.click()
        for i in range(2):
            data.send_keys(Keys.ARROW_DOWN)
        data.send_keys(Keys.ENTER)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.dependents_specify_xpath).send_keys('cousin')
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_7.dependents_save_xpath).click()
        time.sleep(7)
        print("Dependents Details has added successfully")
        data_1 =self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div').text
        if data_1 == 'np':
            print("name is present under dependent details")
        data_2 =self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div').text 
        if data_2=='cousin':
            print("Relationship detail is present under dependent details")
        data_3 =self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div').text 
        if data_3=='1996-07-25':
            print("DOB detail is present under dependent details")
        print("ALL DETAILS ARE FOUND")
        
    #employee salary details
    def test_TC_PIM_12(self,booting_function,test_login): 
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
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_salary_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.salary_assigned_components_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.salary_component_xpath).send_keys(project_2.Project_Data_4.salary_component)
        time.sleep(1)
        grade = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.salary_payGrade_xpath)
        grade.click()
        for i in range(1):
            grade.send_keys(Keys.ARROW_DOWN)
        grade.send_keys(Keys.ENTER)
        time.sleep(1)
        freq = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.salary_payFrequency_xpath)
        freq.click()
        for i in range(2):
            freq.send_keys(Keys.ARROW_DOWN)
        freq.send_keys(Keys.ENTER)
        time.sleep(1)
        currency = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.salary_currency_xpath)
        currency.click()
        for i in range(62):
            currency.send_keys(Keys.ARROW_DOWN)
        currency.send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.salary_addsalary_amount_xpath).send_keys(project_2.Project_Data_4.add_salary_component_amount)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.salary_comments_xpath).send_keys(project_2.Project_Data_4.comments)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.salary_include_DDD_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.salary_accno_xpath).send_keys(project_2.Project_Data_4.account_number)
        time.sleep(1)
        acc=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.salary_acctype_xpath)
        acc.click()
        for i in range(2):
            acc.send_keys(Keys.ARROW_DOWN)
        acc.send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.salary_routingno_xpath).send_keys(project_2.Project_Data_4.routing_number)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.salary_amount_xpath).send_keys(project_2.Project_Data_4.DDD_amount)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.salary_save_button_xpath).click()
        time.sleep(2)
        print("Salary Details Updated..!")
        time.sleep(6)
        #self.driver.refresh()
        data_1 = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div').text
        if data_1 == 'Basic Salary':
            print("salary component is filled")
        data_2 = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div').text
        if data_2 == '60000':
            print("amount is filled")
        data_3 = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div').text
        if data_3 == 'Indian Rupee':
            print("currency is filled")
        data_4 = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div').text
        if data_4 == 'Hourly':
            print("Pay frequency is filled")
        data_6 =self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div').text
        if data_6 =='20000':
            print("DDD amount is filled")
        print("ALL FILLED DETAILS ARE PRESENT UNDER SALARY DETAILS")
    
    #tax exemptions details  
    def test_TC_PIM_13(self,booting_function,test_login): 
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
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_tax_xpath).click()
        time.sleep(1)
        status = self.driver.find_element(by=By.XPATH,value='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]')
        status.click()
        for i in range(1):
            status.send_keys(Keys.ARROW_DOWN)
            status.send_keys(Keys.ENTER)
        status.click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.Exemptions_xpath).send_keys(project_2.Project_Data_4.federal_exemptions)
        time.sleep(1)
        state = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.state_tax_xpath)
        state.click()
        for i in range(11):
            state.send_keys(Keys.ARROW_DOWN)
        state.send_keys(Keys.ENTER)
        time.sleep(1)
        status_1 = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.status_Incometax_xpath)
        status_1.click()
        for i in range(1):
            status_1.send_keys(Keys.ARROW_DOWN)
            status_1.send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.state_exemption_xpath).send_keys(project_2.Project_Data_4.state_income_exemptions)
        time.sleep(1)
        unemp = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.unemployement_stae_xpath)
        unemp.click()
        for i in range(12):
            unemp.send_keys(Keys.ARROW_DOWN)
        unemp.send_keys(Keys.ENTER)
        time.sleep(1)
        work = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.workstate_xpath)
        work.click()
        for i in range(16):
            work.send_keys(Keys.ARROW_DOWN)
            work.send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_8.tax_save_xpath).click()
        time.sleep(5)
        print("Tax Exemption page is updated")
        time.sleep(5)
        #self.driver.refresh()
        data_1 = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]').text
        if data_1 == 'Single':
            print("status is filled")
        data_2 =self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input').text 
        if data_2 == '10':
            print("excepmtion is filled")
        data_3 = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/div[1]').text
        if data_3=='Armed Forces Pacific':
            print("State is filled")
        data_4 =self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]').text
        if data_4 == 'Single':
            print("income tax status is filled")
        data_5 =self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input').text 
        if data_5 == '30':
            print("excepmtion is filled")
        data_6 = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]').text
        if data_6 == 'California':
            print("unemployment state is filled")
        data_7 = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[1]').text
        if data_7 == 'Alaska':
            print("work state is filled")
        print("ALL DETAILS ARE PRESENT")