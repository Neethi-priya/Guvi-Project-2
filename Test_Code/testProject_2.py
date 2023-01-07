from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Test_Data import project_2
import pytest
import time 

class Test_Project_2:
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
        
    def test_TC_PIM_01(self,booting_function,test_login):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(2)
        element=self.driver.find_element(by=By.XPATH, value=project_2.Project_Selectors_2.search_box)
        element.send_keys(project_2.Project_Data_2.Admin_text) 
        ele_one = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.admin_xpath)
        time.sleep(2)
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(2)
        element.send_keys(project_2.Project_Data_2.Admin_text_1)
        ele_two = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.admin_xpath)
        if ele_one.is_displayed():
            print("Admin menu name is Displayed(lowercase)")
        if ele_two.is_displayed():
            print("Admin menu name is Displayed(uppercase)")
            
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(3)
        element.send_keys(project_2.Project_Data_2.pim_text)
        ele_one = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.pim_xpath)
        time.sleep(2)
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(2)
        element.send_keys(project_2.Project_Data_2.pim_text_1)
        ele_two = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.pim_xpath)
        time.sleep(2)
        if ele_one.is_displayed():
            print("PIM menu name is Displayed(lowercase)")
        if ele_two.is_displayed():
            print("PIM menu name is Displayed(uppercase)")
        
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(3)
        element.send_keys(project_2.Project_Data_2.leave_text)
        ele_one = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.leave_xpath)
        time.sleep(2)
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(2)
        element.send_keys(project_2.Project_Data_2.leave_text_1)
        ele_two = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.leave_xpath)
        time.sleep(2)
        if ele_one.is_displayed():
            print("Leave menu name is Displayed(lowercase)")
        if ele_two.is_displayed():
            print("Leave menu name is Displayed(uppercase)")
       
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(3)
        element.send_keys(project_2.Project_Data_2.time_text)
        ele_one = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.time_xpath)
        time.sleep(2)
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(2)
        element.send_keys(project_2.Project_Data_2.time_text_1)
        ele_two = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.time_xpath)
        time.sleep(2)
        if ele_one.is_displayed():
            print("Time menu name is Displayed(lowercase)")
        if ele_two.is_displayed():
            print("Time menu name is Displayed(uppercase)")
            
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(3)
        element.send_keys(project_2.Project_Data_2.recruitment_text)
        ele_one = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.recruitment_xpath)
        time.sleep(2)
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(2)
        element.send_keys(project_2.Project_Data_2.recruitment_text_1)
        ele_two = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.recruitment_xpath)
        time.sleep(2)
        if ele_one.is_displayed():
            print("Recruitment menu name is Displayed(lowercase)")
        if ele_two.is_displayed():
            print("Recruitment menu name is Displayed(uppercase)") 
            
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(3)
        element.send_keys(project_2.Project_Data_2.my_info_text)
        ele_one = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.my_info_xpath)
        time.sleep(2)
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(2)
        element.send_keys(project_2.Project_Data_2.my_info_text_1)
        ele_two = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.my_info_xpath)
        time.sleep(2)
        if ele_one.is_displayed():
            print("My Info menu name is Displayed(lowercase)")
        if ele_two.is_displayed():
            print("My Info menu name is Displayed(uppercase)") 
            
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(2)
        element.send_keys(project_2.Project_Data_2.performance_text)
        ele_one = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.performance_xpath)
        time.sleep(2)
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(2)
        element.send_keys(project_2.Project_Data_2.performance_text_1)
        ele_two = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.performance_xpath)
        time.sleep(2)
        if ele_one.is_displayed():
            print("Performance menu name is Displayed(lowercase)")
        if ele_two.is_displayed():
            print("Performance menu name is Displayed(uppercase)") 
            
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(4)
        element.send_keys(project_2.Project_Data_2.dashboard_text)
        ele_one = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.dashboard_xpath)
        time.sleep(4)
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(2)
        element.send_keys(project_2.Project_Data_2.dashboard_text_1)
        ele_two = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.dashboard_xpath)
        time.sleep(4)
        if ele_one.is_displayed():
            print("Dashboard menu name is Displayed(lowercase)")
        if ele_two.is_displayed():
            print("Dashboard menu name is Displayed(uppercase)")
            
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(3)
        element.send_keys(project_2.Project_Data_2.maintenance_text)
        ele_one = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.maintenance_xpath)
        time.sleep(2)
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(2)
        element.send_keys(project_2.Project_Data_2.maintenance_text_1)
        ele_two = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.maintenance_xpath)
        time.sleep(2)
        if ele_one.is_displayed():
            print("Maintenance menu name is Displayed(lowercase)")
        if ele_two.is_displayed():
            print("Maintenance menu name is Displayed(uppercase)") 
            
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(3)
        element.send_keys(project_2.Project_Data_2.directory_text)
        ele_one = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.directory_xpath)
        time.sleep(2)
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(2)
        element.send_keys(project_2.Project_Data_2.directory_text_1)
        ele_two = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.directory_xpath)
        time.sleep(2)
        if ele_one.is_displayed():
            print("Directory menu name is Displayed(lowercase)")
        if ele_two.is_displayed():
            print("Directory menu name is Displayed(uppercase)")     
            
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(3)
        element.send_keys(project_2.Project_Data_2.buzz_text)
        ele_one = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.buzz_xpath)
        time.sleep(2)
        element.click()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        time.sleep(2)
        element.send_keys(project_2.Project_Data_2.buzz_text_1)
        ele_two = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.buzz_xpath)
        time.sleep(2)
        if ele_one.is_displayed():
            print("Buzz menu name is Displayed(lowercase)")
        if ele_two.is_displayed():
            print("Buzz menu name is Displayed(uppercase)")
        
        
          
    def test_TC_PIM_02(self,booting_function,test_login):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_2.admin_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.user_management_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.user_management_users_xpath).click()
        time.sleep(2)
        ele=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.user_role_select_xpath) 
        ele.click()
        for i in range(1):
            ele.send_keys(Keys.ARROW_DOWN)
            ele.click()
        admin=self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]').text
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.reset_button).click()
        time.sleep(1)
       
        for i in range(1,2):
            ele.send_keys(Keys.ARROW_DOWN)
            ele.click()
        ess= self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]').text
        time.sleep(1)
        
        ele_1=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.admin_status_select_path)
        ele_1.click()
        time.sleep(2)
        for i in range(1):
            ele_1.send_keys(Keys.ARROW_DOWN)
            ele_1.click()
        enabled=self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]').text
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.reset_button).click()
        time.sleep(1)
        
        for i in range(1,2):
            ele_1.send_keys(Keys.ARROW_DOWN)
            ele_1.click()
        disabled=self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]').text
        time.sleep(1)
        if admin == 'Admin':
            print('Admin field present under user role')
        if ess=='ESS':
            print("ESS field present under user role ")
        if enabled == 'Enabled':
            print("Enabled field present under status")
        if disabled == 'Disabled':
            print("Disabled field present under status")
        
            
    #creation of user details in pim        
    def test_TC_PIM_03(self,booting_function,test_login):
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
        print("New Employee under PIM is created successfully..!!")
    
    #validating_tabs under user in pim module    
    def test_TC_PIM_04(self,booting_function,test_login):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_3.pim_xpath_1).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_employee_list_edit_xpath).click()
        time.sleep(1)
        ele_1 = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_personal_details_xpath).is_displayed()
        if ele_1:
            print("Personal details tab is present")
        ele_2 = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_contact_details_xpath).is_displayed()
        if ele_2:
            print("Contact details tab is present")
        ele_3 = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_emer_contacts_xpath).is_displayed()
        if ele_3:
            print("Emergency contacts tab is present")
        ele_4 = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_dependants_xpath).is_displayed()
        if ele_4:
            print("Dependents tab is present")
        ele_5 = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_immigration_xpath).is_displayed()
        if ele_5:
            print("Immigrations tab is present")
        ele_6 = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_job_xpath).is_displayed()
        if ele_6:
            print("Job tab is present")
        ele_7= self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_salary_xpath).is_displayed()
        if ele_7:
            print("Salary tab is present")
        ele_8 = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_tax_xpath).is_displayed()
        if ele_8:
            print("Tax excemptions tab is present")
        ele_9 = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_reportto_xpath).is_displayed()
        if ele_9:
            print("Report to tab is present")
        ele_10 = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_qualifications_xpath).is_displayed()
        if ele_10:
            print("Qualifications tab is present")
        ele_11 = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_memberships_xpath).is_displayed()
        if ele_11:
            print("Memberships tab is present")
            
   #update personal_details_pim
    def test_TC_PIM_05(self,booting_function,test_login):  
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
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_4.pim_personal_details_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.nickname_xpath).send_keys(project_2.Project_Data_3.nick_name)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.otherID_xpath).send_keys(project_2.Project_Data_3.other_id)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.licenceNO_xpath).send_keys(project_2.Project_Data_3.license_no)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.license_expirydate_xpath).send_keys(project_2.Project_Data_3.license_expiry_date)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.SSN_xpath).send_keys(project_2.Project_Data_3.SSN_no)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.SIN_xpath).send_keys(project_2.Project_Data_3.SIN_no)
        time.sleep(1)
        element=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.nationality_dropdown_xpath)
        element.click()
        for i in range(22):
            element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)
        time.sleep(3)
        element_1 = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.marital_status_dropdown_xpath)
        element_1.click()
        for i in range(1):
            element_1.send_keys(Keys.ARROW_DOWN)
        element_1.send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.dob_xpath).send_keys(project_2.Project_Data_3.dob)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.gender_female_button_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.military_xpath).send_keys(project_2.Project_Data_3.military_service)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.employee_list_save_xpath).click()
        time.sleep(1)
        element_3=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.blood_type_xpath)
        element_3.click()
        for i in range(3):
            element_3.send_keys(Keys.ARROW_DOWN)
        element_3.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.employee_list_bloodtype_save_xpath).click()
        print("Personal Details Filled Successfully")
        #self.driver.refresh()
        time.sleep(10)
        other = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.otherID_xpath).is_displayed()
        print("other Id is presented")
        dri_lic_no = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.licenceNO_xpath).is_displayed()
        print("driver licence no is presented")
        lic_exp_date= self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.license_expirydate_xpath).text
        if lic_exp_date=='2024-12-12':
            print("licene expiry date is presented")
        ssn_no = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.SSN_xpath).is_displayed()
        print("SSN number is presented")
        sin_no= self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.SIN_xpath).is_displayed()
        print("SIN number is presented")
        dob= self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.dob_xpath).text
        if dob=='1996-01-17':
            print("dob is presented")
        nationality=self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]').text        
        if nationality=='Beninese':
            print("nationality is presented")
        martial =self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]').text
        if martial=='Single':
            print("marital status is selected")
        military = self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.military_xpath).is_displayed()
        print("military service is presented")
        blood = self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]').text
        if blood=='B+':
            print("Blood type is presented")
        gender=self.driver.find_element(by=By.XPATH,value=project_2.Project_Selectors_5.gender_female_button_xpath).is_enabled()
        print("female button is enabled")
    
        

    
    