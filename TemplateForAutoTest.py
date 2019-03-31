import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class CreateTemplate (unittest.TestCase):

    def setUp(self):
        self.drv = webdriver.Chrome("chromedriver.exe")

    def test_createAutoTest(self):

        def openFail(name, how):
            return open(name, how)

        def closeFail(opf):
            return opf.close()

        testCaseNumber = "DBAP-T11"
        self.drv.get("https://sbtatlas.sigma.sbrf.ru/jira/secure/Tests.jspa#/testCase/"+testCaseNumber)
        assert 'Welcome to Jira' in self.drv.page_source
        elmLogin = self.drv.find_element_by_name('os_username')
        elmLogin.send_keys('out-gimon-av')
        elmPassword = self.drv.find_element_by_name('os_password')
        elmPassword.send_keys('')
        elmPassword.send_keys(Keys.RETURN)
        self.drv.get("https://sbtatlas.sigma.sbrf.ru/jira/secure/Tests.jspa#/testCase/"+testCaseNumber)
        time.sleep(7)
        assertNamber = self.drv.find_element_by_xpath('//*[@id="content"]/div/div/div/floating-header/div/header/div/div[2]/div/ol/li[3]/a').text
        assert testCaseNumber in assertNamber
        nameFail ='C:\\Users\\WE\\Desktop\\case\\'+testCaseNumber+'.txt'
        failTest = openFail(nameFail,'w')
        failTest.write('import org.junit.Before;\n')
        failTest.write('import org.junit.Rule;\n')
        failTest.write('import org.junit.Test;\n')
        failTest.write('import org.junit.runner.RunWith;\n\n')
        failTest.write('import ru.tinkoff.allure.android.FailshotRule;\n')
        failTest.write('import ru.tinkoff.allure.annotations.DisplayName;\n')
        failTest.write('import ru.tinkoff.allure.annotations.Issue;\n')
        failTest.write('import uitesting.core.runner.SbolRetryRunner;\n\n')
        failTest.write('import static ru.tinkoff.allure.android.StepKt.step;\n')
        failTest.write('import static ru.tinkoff.allure.android.StepKt.stepWithScreen;\n\n')
        failTest.write('/**\n')
        nameTest = self.drv.find_element_by_xpath('//*[@id="content"]/div/div/div/floating-header/div/header/div/div[2]/h1').text
        failTest.write(' * '+nameTest+'\n')
        failTest.write(' * <a href="https://sbtatlas.sigma.sbrf.ru/jira/secure/Tests.jspa#/testCase/'+testCaseNumber+'">'+testCaseNumber+'</a>\n')
        precondition = self.drv.find_element_by_xpath('//*[@id="rte-precondition"]/div/div/span[1]')
        failTest.write(' *')
        for element in precondition.text:
            failTest.write(element)
            if (element == '\n'):
                failTest.write('\n *')
        self.drv.find_element_by_xpath('//*[@id="content"]/div/div/div/floating-header/div/ng-transclude/header-content/aui-navigation/nav/div/div/ul/li[2]/a/span').click()
        time.sleep(5)
        failTest.write('\n * <p>\n')
        try:
            for i in range (1,100):
                self.drv.find_element_by_xpath('//*[@id="content"]/div/div/div/div[1]/div/form[2]/ng-include/div/div[3]/div/test-case-script-step['+str(i)+']/div/div[2]/span[1]')
                step = self.drv.find_element_by_xpath('//*[@id="rte-step-description-'+str(i)+'"]/div/div/span[1]')
                failTest.write(' *'+str(i)+'. '+step.text+'\n * </p><p>\n')
                testData = self.drv.find_element_by_xpath('//*[@id="rte-step-test-data-'+str(i)+'"]/div/div/span[2]')
                if (len(testData.text)>0):
                    failTest.write(' * test data: '+testData.text+'\n * </p><p>\n')
                result = self.drv.find_element_by_xpath('//*[@id="rte-step-expected-result-'+str(i)+'"]/div/div/span[1]')
                failTest.write(' * -> '+result.text+'\n * </p><p>\n')
                sumStep = i
        except NoSuchElementException:
            failTest.write(' * @author Gimon Anton\n */\n\n')
            failTest.write('@DisplayName(" ")\n')
            failTest.write('@RunWith(SbolRetryRunner.class)\n')
            failTest.write('public class '+testCaseNumber+' extends PostLoginTest {\n\n')
            failTest.write('    @Rule\n    public FailshotRule failshotRule = new FailshotRule();\n\n')
            failTest.write('    @Before\n    public void initPages() {\n        step("initPages",()->{\n\n        });\n')
            failTest.write('    }\n\n')
            failTest.write('    @Test\n')
            failTest.write('    @Issue("'+testCaseNumber+'")\n')
            failTest.write('    @DisplayName("'+testCaseNumber+' - '+nameTest+'")\n')
            failTest.write('    public void test() {\n\n')
            for j in range(1,(sumStep+1)):
                step = self.drv.find_element_by_xpath('//*[@id="rte-step-description-' + str(j) + '"]/div/div/span[1]')
                failTest.write('        stepWithScreen("' + str(j) + '. ' + step.text + '", () -> {\n\n        });\n\n')
            failTest.write('    }\n}')
            closeFail(failTest)


    def tearDown(self):
        self.drv.close()

if __name__ == '__main__':
    unittest.main()