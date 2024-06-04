from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def randomize_answer(options):
    return random.choice(options)
def click_element(driver, xpath, retries=5):
    for _ in range(retries):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            if element.is_displayed() and element.is_enabled():
                driver.execute_script("arguments[0].click();", element)
                return True
        except Exception as e:
            print(f"Retrying click on element: {xpath}. Error: {e}")
            time.sleep(1)
    return False
def fill_survey():
    for i in range(39):
        try:
            # Specify the path to your msedgedriver executable
            edge_driver_path = r'C:\Users\bakal\OneDrive\Pulpit\Egde\msedgedriver.exe'

            # Initialize Edge WebDriver with incognito mode
            edge_service = EdgeService(executable_path=edge_driver_path)
            options = EdgeOptions()
            options.add_argument("--inprivate")
            options.add_argument("--start-maximized")
            driver = webdriver.Edge(service=edge_service, options=options)
            # Open Survey URL
            survey_url = 'https://www.survio.com/survey/d/R5I4R7F6Q9O8L2R4Z'
            driver.get(survey_url)
            driver.maximize_window()  # Ensure the window is maximized
            time.sleep(2)  # wait for page to load

            # Start the survey
            if not click_element(driver, '//*[text()="Rozpocznij ankietę teraz"]'):
                print(f"Iteration {i + 1}: Failed to start survey")
                continue
            time.sleep(2)

            # Answer the first question: Jakiej jesteś płci?
            question_1_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79045598.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79045598.0.3.0.$singleChoice1"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_1_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_1_options)).click()
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79045618"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the second question: W jakim przedziale wiekowym jesteś?
            question_2_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79045618.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79045618.0.3.0.$singleChoice1"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79045618.0.3.0.$singleChoice2"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79045618.0.3.0.$singleChoice3"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79045618.0.3.0.$singleChoice4"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_2_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_2_options)).click()
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046224"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the third question: Jakie jest twoje aktualne wykształcenie?
            question_3_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046224.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046224.0.3.0.$singleChoice1"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046224.0.3.0.$singleChoice2"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046224.0.3.0.$singleChoice3"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_3_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_3_options)).click()
            print(f"Iteration {i+1}: Answered question 3")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046253"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the fourth question: Czym się aktualnie zajmujesz?
            question_4_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046253.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046253.0.3.0.$singleChoice1"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046253.0.3.0.$singleChoice2"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046253.0.3.0.$singleChoice3"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046253.0.3.0.$singleChoice4"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046253.0.3.0.$singleChoice5"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_4_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_4_options)).click()
            print(f"Iteration {i+1}: Answered question 4")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046276"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the fifth question: Jakie jest twoje miejsce zamieszkania?
            question_5_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046276.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046276.0.3.0.$singleChoice1"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046276.0.3.0.$singleChoice2"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_5_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_5_options)).click()
            print(f"Iteration {i+1}: Answered question 5")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046287"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the sixth question: Czy czujesz się bezpieczna/y w swoim miejscu zamieszkania?
            question_6_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046287.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046287.0.3.0.$singleChoice1"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046287.0.3.0.$singleChoice2"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046287.0.3.0.$singleChoice3"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046287.0.3.0.$singleChoice4"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_6_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_6_options)).click()
            print(f"Iteration {i+1}: Answered question 6")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046290"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the seventh question: Czy aktualnie czujesz się bardziej bezpieczny niż dwa lata temu?
            question_7_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046290.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046290.0.3.0.$singleChoice1"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046290.0.3.0.$singleChoice2"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046290.0.3.0.$singleChoice3"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046290.0.3.0.$singleChoice4"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_7_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_7_options)).click()
            print(f"Iteration {i+1}: Answered question 7")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046293"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the eighth question: Czy kiedykolwiek interesowałaś/es się sprawami kryminalistycznymi?
            question_8_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046293.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046293.0.3.0.$singleChoice1"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_8_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_8_options)).click()
            print(f"Iteration {i+1}: Answered question 8")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046311"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the ninth question: Jak według ciebie można zostać technikiem kryminalistyki?
            question_9_answers = [
                "Technikiem kryminalistyki można zostać poprzez ukończenie odpowiednich studiów i zdobycie doświadczenia. Praca polega na zbieraniu i analizie dowodów. Technik powinien być spostrzegawczy, dokładny i mieć zdolności analityczne.",
                "Aby zostać technikiem kryminalistyki, należy ukończyć studia związane z kryminalistyką lub pokrewnymi dziedzinami oraz zdobyć odpowiednie certyfikaty.",
                "Technik kryminalistyki powinien posiadać odpowiednie wykształcenie oraz doświadczenie praktyczne. Powinien być skrupulatny, precyzyjny i posiadać umiejętność pracy pod presją.",
                "Trzeba ukończyć studia kryminalistyczne i odbyć praktyki w laboratoriach kryminalistycznych.",
                "Wykształcenie wyższe w dziedzinie kryminalistyki i praktyka w policji lub laboratorium są niezbędne.",
                "Technik kryminalistyki powinien mieć silne zdolności analityczne i ukończone studia z kryminalistyki.",
                "Należy ukończyć studia kierunkowe i zdobyć certyfikaty oraz doświadczenie w terenie.",
                "Studia kryminalistyczne i praktyka w laboratoriach kryminalistycznych to klucz do sukcesu.",
                "Praca technika kryminalistyki wymaga dokładności, spostrzegawczości i analitycznego myślenia.",
                "Technik kryminalistyki musi ukończyć odpowiednie studia i zdobyć doświadczenie praktyczne.",
                "Zdolności analityczne i odpowiednie wykształcenie są kluczowe dla technika kryminalistyki.",
                "Studia kryminalistyczne i praktyki w laboratoriach kryminalistycznych to podstawowe wymagania.",
                "Technik kryminalistyki musi być dokładny, cierpliwy i posiadać zdolności analityczne.",
                "Aby zostać technikiem kryminalistyki, należy ukończyć studia wyższe z kryminalistyki i zdobyć praktykę zawodową.",
                "Kryminologia, analiza dowodów i ścisła współpraca z policją to podstawa pracy technika kryminalistyki.",
                "Technik kryminalistyki musi być dobrze wykształcony i mieć doświadczenie praktyczne w analizie dowodów.",
                "Studia kryminalistyczne i staż w laboratorium są kluczowe dla technika kryminalistyki.",
                "Technik kryminalistyki powinien ukończyć studia z kryminalistyki i odbyć praktykę zawodową.",
                "Technik kryminalistyki musi mieć odpowiednie wykształcenie i umiejętność analizy dowodów.",
                "Technik kryminalistyki musi ukończyć studia wyższe i zdobyć praktykę w laboratorium kryminalistycznym."
            ]
            driver.find_element(By.XPATH, '//*[@id="text79046311"]').send_keys(randomize_answer(question_9_answers))
            print(f"Iteration {i+1}: Answered question 9")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046318"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the tenth question: Czy według ciebie, na stanowisku technika kryminalistyki, występują czynniki szkodliwe?
            question_10_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046318.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046318.0.3.0.$singleChoice1"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_10_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_10_options)).click()
            print(f"Iteration {i+1}: Answered question 10")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046320"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the eleventh question: Jezeli w powyższym pytaniu zaznaczyłaś/eś pierwsza możliwą odpowiedz, czy jesteś wstanie wymienić szkodliwe czynności z którymi spotyka się technik śledczy?
            question_11_answers = [
                "Tak, technik śledczy może być narażony na kontakt z substancjami chemicznymi, materiałami biologicznymi oraz pracować w niebezpiecznych miejscach.",
                "Technik śledczy często spotyka się z czynnikami szkodliwymi takimi jak chemikalia, materiały biologiczne i inne niebezpieczne substancje.",
                "Technik śledczy narażony jest na wiele szkodliwych czynników, w tym kontakt z niebezpiecznymi substancjami i materiałami.",
                "Technik śledczy pracuje w warunkach, które mogą być szkodliwe, w tym kontakt z chemikaliami i materiałami biologicznymi.",
                "Technik śledczy może być narażony na szkodliwe chemikalia, materiały biologiczne i inne niebezpieczne substancje.",
                "Technik śledczy musi często pracować z niebezpiecznymi substancjami chemicznymi i biologicznymi.",
                "Technik śledczy może mieć kontakt z chemikaliami, materiałami biologicznymi i innymi niebezpiecznymi substancjami.",
                "Tak, praca technika śledczego wiąże się z ryzykiem narażenia na szkodliwe substancje chemiczne i biologiczne.",
                "Technik śledczy pracuje z chemikaliami i materiałami biologicznymi, co może być szkodliwe dla zdrowia.",
                "Technik śledczy narażony jest na kontakt z niebezpiecznymi substancjami chemicznymi i biologicznymi.",
                "Praca technika śledczego często wiąże się z ryzykiem kontaktu z szkodliwymi chemikaliami i materiałami biologicznymi.",
                "Technik śledczy może być narażony na różne szkodliwe czynniki, w tym chemikalia i materiały biologiczne.",
                "Tak, technik śledczy spotyka się z wieloma szkodliwymi czynnikami, w tym substancjami chemicznymi i biologicznymi.",
                "Technik śledczy musi pracować z chemikaliami i materiałami biologicznymi, co może być szkodliwe dla zdrowia.",
                "Technik śledczy może być narażony na kontakt z niebezpiecznymi substancjami chemicznymi i biologicznymi.",
                "Technik śledczy często ma do czynienia z chemikaliami i materiałami biologicznymi, które mogą być szkodliwe.",
                "Praca technika śledczego wiąże się z ryzykiem narażenia na szkodliwe chemikalia i materiały biologiczne.",
                "Technik śledczy narażony jest na kontakt z niebezpiecznymi substancjami chemicznymi i biologicznymi.",
                "Technik śledczy pracuje z chemikaliami i materiałami biologicznymi, co może być szkodliwe dla zdrowia.",
                "Tak, technik śledczy spotyka się z wieloma szkodliwymi czynnikami, w tym substancjami chemicznymi i biologicznymi."
            ]
            driver.find_element(By.XPATH, '//*[@id="text79046320"]').send_keys(randomize_answer(question_11_answers))
            print(f"Iteration {i+1}: Answered question 11")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046353"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the twelfth question: Jak myślisz, jaka jest najważniejsze narzędzie bez którego technik nie może ruszyć się na oględziny miejsca zdarzenia?
            question_12_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046353.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046353.0.3.0.$singleChoice1"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046353.0.3.0.$singleChoice2"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046353.0.3.0.$singleChoice3"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046353.0.3.0.$singleChoice4"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046353.0.3.0.$singleChoice5"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046353.0.3.0.$singleChoice6"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046353.0.3.0.$singleChoice7"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_12_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_12_options)).click()
            print(f"Iteration {i+1}: Answered question 12")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046365"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the thirteenth question: Jak myślisz ile trwają oględziny miejsca zdarzenia?
            question_13_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046365.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046365.0.3.0.$singleChoice1"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046365.0.3.0.$singleChoice2"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_13_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_13_options)).click()
            print(f"Iteration {i+1}: Answered question 13")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046371"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the fourteenth question: Czy myślałeś kiedyś o pracy jako technik śledczy?
            question_14_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046371.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046371.0.3.0.$singleChoice1"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_14_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_14_options)).click()
            print(f"Iteration {i+1}: Answered question 14")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046379"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the fifteenth question: Jak sądzisz ile procent spraw jest rozwiązywanych starannie i finalnie sprawca zostaje złapany?
            question_15_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046379.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046379.0.3.0.$singleChoice1"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046379.0.3.0.$singleChoice2"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046379.0.3.0.$singleChoice3"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046379.0.3.0.$singleChoice4"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_15_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_15_options)).click()
            print(f"Iteration {i+1}: Answered question 15")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046403"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the sixteenth question: Myslisz że organizacje śledcze mają istotne znaczenie w aspekcie efektywnego reagowania na różnorodne zagrożenia?
            question_16_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046403.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046403.0.3.0.$singleChoice1"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046403.0.3.0.$singleChoice2"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_16_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_16_options)).click()
            print(f"Iteration {i+1}: Answered question 16")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046421"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the seventeenth question: Jak myślisz, jakie są najczęstsze przyczyny zabójstw?
            question_17_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046421.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046421.0.3.0.$singleChoice1"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046421.0.3.0.$singleChoice2"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046421.0.3.0.$singleChoice3"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046421.0.3.0.$singleChoice4"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_17_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_17_options)).click()
            print(f"Iteration {i+1}: Answered question 17")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046442"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the eighteenth question: Czy przy oglądaniu aktualnych seriali dokumentalnych w telewizji, myślisz ze odzwierciedlają one realna prace służb?
            question_18_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046442.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046442.0.3.0.$singleChoice1"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046442.0.3.0.$singleChoice2"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046442.0.3.0.$singleChoice3"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046442.0.3.0.$singleChoice4"]'
            ]
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, question_18_options[0]))
            )
            driver.find_element(By.XPATH, randomize_answer(question_18_options)).click()
            print(f"Iteration {i+1}: Answered question 18")
            next_question = driver.find_element(By.XPATH, '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046463"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_question)
            time.sleep(1)

            # Answer the nineteenth question: Uważasz, że jakość świadczonych usług przez służby jest wystarczająca?
            question_19_options = [
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046463.0.3.0.$singleChoice0"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046463.0.3.0.$singleChoice1"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046463.0.3.0.$singleChoice2"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046463.0.3.0.$singleChoice3"]',
                '//*[@data-reactid=".0.0:$pages.$Frame0.0.1.0.0.1.$question79046463.0.3.0.$singleChoice4"]'
            ]
            if not click_element(driver, randomize_answer(question_19_options)):
                print(f"Iteration {i + 1}: Failed to answer question 19")
                continue
            print(f"Iteration {i + 1}: Answered question 19")

            # Submit the survey using JavaScript
            submit_button_xpath = '//*[text()="Wyślij"]'
            if not click_element(driver, submit_button_xpath):
                print(f"Iteration {i + 1}: Failed to submit the survey")
                continue
            print(f"Iteration {i + 1}: Submitted the survey")

            # Check for submission confirmation
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[contains(text(), "Dziękujemy za wypełnienie ankiety")]'))
                )
                print(f"Iteration {i + 1}: Survey submission confirmed")
            except Exception as e:
                print(f"Iteration {i + 1}: Survey submission confirmation failed: {e}")
                continue

            # Open a new incognito window
            new_driver = webdriver.Edge(service=edge_service, options=options)
            new_driver.get(survey_url)
            print(f"Iteration {i + 1}: Opened new incognito window")

            # Start the survey in the new window
            if not click_element(new_driver, '//*[text()="Rozpocznij ankietę teraz"]'):
                print(f"Iteration {i + 1}: Failed to start new survey in new incognito window")
                continue
            print(f"Iteration {i + 1}: Started new survey in new incognito window")

            # Close the current driver and switch to the new driver
            driver.quit()
            driver = new_driver

            # Wait before starting the next iteration
            time.sleep(2)

        except Exception as e:
            print(f"An error occurred during iteration {i + 1}: {str(e)}")

# Run the survey filling process
fill_survey()