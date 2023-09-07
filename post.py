import threading

import cv2
import numpy as np
import random
import pyautogui
import time

international_dollar_elements = [
    "Introduction: Learn about the International Dollar, a peer-to-peer electronic cash system with limited supply and 0% inflation.",
    "Scalability: The International Dollar solves scalability issues plaguing other cryptocurrencies, offering faster transactions.",
    "Proof-of-Ip: Discover the innovative algorithm ensuring secure and efficient transactions with the International Dollar.",
    "Calculations: Explore the math behind the International Dollar's security against network dominance attempts.",
    "GUI Design: The International Dollar's sleek GUI offers a user-friendly experience for all users.",
    "Printable Bills: Secure your transactions with printable bills that protect against digital threats.",
    "Security Measures: Learn how the International Dollar safeguards its network against potential attacks.",
    "Crypto Revolution: Join the revolution and be part of the future of digital finance with the International Dollar.",
    "Financial Freedom: Experience financial freedom with the International Dollar's decentralized approach.",
    "Efficient Business: Discover how businesses can operate more efficiently with the International Dollar.",
    "Global Transactions: The International Dollar simplifies cross-border transactions for seamless global commerce.",
    "Instant Transactions: Say goodbye to long confirmation times with instant transactions on the International Dollar network.",
    "Anonymity: Enjoy the highest levels of security and anonymity with the International Dollar.",
    "Mainstream Adoption: Explore the challenges that have hindered the mainstream adoption of cryptocurrencies.",
    "Transaction Fees: The International Dollar eliminates transaction fees, making it cost-effective for all users.",
    "Volatility: Address the issue of cryptocurrency volatility with the stable International Dollar.",
    "Merchant Acceptance: Learn why widespread merchant acceptance is crucial for cryptocurrency adoption.",
    "Node Network: Understand how the International Dollar's node network ensures network security.",
    "IP Addresses: Dive into the importance of IP addresses in the International Dollar's Proof-of-Ip algorithm.",
    "Network Integrity: Learn how a large number of truthful nodes protect the International Dollar's integrity.",
    "Network Attacks: Explore potential network attacks and the measures in place to counteract them.",
    "User Participation: See how user participation is key to the International Dollar's success.",
    "Mobile App Expansion: Discover plans to expand the node network through a user-friendly mobile app.",
    "Security Measures: Explore the security measures in place to prevent IP spoofing and maintain data integrity.",
    "Founder Node: Understand the role of the founder node and its gradual reduction in voting power.",
    "Network Safeguard: Learn why just 1000 honest nodes are sufficient to safeguard against unfair network dominance.",
    "CIDR Notation: Get familiar with CIDR notation used to represent IP address blocks.",
    "Class A, B, and C Blocks: Explore the different classes of IP address blocks and their significance.",
    "Accepted IPs: See the range of accepted IPs and their importance in network security.",
    "US Department of Defense: Understand why even organizations like the US Department of Defense can't dominate the International Dollar network.",
    "Billionaire Attack: Dive into the hypothetical scenario of a billionaire attempting to gain network dominance.",
    "Inflation Effects: Explore how inflation would impact the billionaire's efforts to control the network.",
    "Growing User Base: See how the growing user and node base can outpace network dominance attempts.",
    "Transaction Block: Understand the structure of a transaction block on the International Dollar network.",
    "Sender's Public Key: Learn about the sender's public key and its role in transactions.",
    "Receiver's Address: Explore the receiver's address and its significance in the transaction process.",
    "Digital Signature: Understand how digital signatures ensure the authenticity of transactions.",
    "Message Propagation: See how transaction messages propagate through the International Dollar node network.",
    "Node Verification: Learn how each node verifies transaction data to maintain network integrity.",
    "Transaction Iterations: Explore the concept of transaction iterations in International Dollar transactions.",
    "Transaction Serial Number: Understand the importance of serial numbers in transaction blocks.",
    "Secure Transactions: Discover how the International Dollar ensures secure and efficient transactions.",
    "User Interface: Explore the modern and user-friendly GUI design of the International Dollar system.",
    "Paper Wallets: Learn about printable bills that serve as secure paper wallets for real-life transactions.",
    "Private Key Protection: Understand how the International Dollar's paper wallets protect against digital threats.",
    "Printable Bill Design: Explore the design of printable bills and their role in the International Dollar ecosystem.",
    "Conclusion: Summarize the key benefits of the International Dollar system and its potential impact on digital finance.",
    "Join the Revolution: Get involved and be part of the International Dollar revolution today!",
    "Cryptocurrency Evolution: Witness the evolution of digital currencies with the International Dollar.",
    "Secure Your Future: Secure your financial future with the International Dollar's innovative approach.",
    "Global Finance: Explore the International Dollar's role in shaping the future of global finance.",
    "Innovation in Finance: Learn how the International Dollar brings innovation to the world of finance.",
    "Cryptocurrency Challenges: Understand the challenges that cryptocurrencies face on the road to mainstream adoption.",
    "Overcome Barriers: See how the International Dollar overcomes barriers to entry for average users.",
    "Crypto Investment: Discover why cryptocurrencies have captured the imagination of investors worldwide.",
    "Technological Promise: Explore the technological promise of cryptocurrencies and their potential impact on society.",
    "Blockchain vs. POI: Understand why the International Dollar replaced blockchain with Proof-of-Ip for enhanced efficiency.",
    "Energy Consumption: Learn how the International Dollar eliminates unnecessary energy consumption in its network.",
    "Financial Control: See how the International Dollar empowers individuals to have greater control over their financial transactions.",
    "Seamless Transactions: Experience a future where cross-border transactions become seamless and cost-effective.",
    "Digital Currency Evolution: Witness the International Dollar as a significant step forward in the evolution of digital currencies.",
    "Limitations of Cryptocurrencies: Explore the limitations that have hindered the adoption of traditional cryptocurrencies.",
    "Cryptocurrency Enthusiasm: Understand why cryptocurrencies have driven significant interest and investment over the past decade.",
    "Mainstream Adoption Challenges: Dive into the key reasons behind the failure of mainstream cryptocurrency adoption.",
    "Digital Finance Future: Discover how the International Dollar has the potential to shape the future of global finance.",
    "Financial Innovation: Witness the International Dollar as an innovative solution to the challenges of traditional finance.",
    "Decentralization: Explore the decentralized nature of the International Dollar and its promise of financial freedom.",
    "Crypto Enthusiasts: Join the ranks of cryptocurrency enthusiasts and explore the world of digital finance with the International Dollar.",
    "Efficient Transactions: Say goodbye to transaction processing bottlenecks with the International Dollar's efficient system.",
    "Low Transaction Fees: Enjoy the benefits of free transactions with the International Dollar's cost-effective approach.",
    "Blockchain Revolution: Understand why the International Dollar's replacement of blockchain with POI is a game-changer.",
    "Energy-Efficient Cryptocurrency: Witness how the International Dollar reduces energy consumption in its network.",
    "Secure Anonymity: Experience the highest levels of security and anonymity with the International Dollar's system.",
    "Cryptocurrency Promise: Learn about the early promise of cryptocurrencies and their potential for financial freedom.",
    "Widespread Adoption: Explore the importance of widespread merchant acceptance for cryptocurrency adoption.",
    "Comprehensive Solution: Discover how the International Dollar provides a comprehensive solution to cryptocurrency challenges.",
    "Financial Transactions: Unlock greater control over your financial transactions with the International Dollar's system.",
    "Cross-Border Commerce: Seamlessly conduct cross-border transactions with the International Dollar's cost-effective approach.",
    "Digital Finance Impact: Explore the potential impact of the International Dollar on the world of digital finance.",
    "Blockchain Challenges: Understand the scalability and technical challenges that traditional cryptocurrencies like Bitcoin face.",
    "Transaction Processing: Witness the International Dollar's high-speed transaction processing for efficient peer-to-peer transactions.",
    "Blockchain Fees: Say goodbye to high transaction fees during peak periods with the International Dollar's system.",
    "Wallet Management: Overcome the technical complexities of wallet management and security with the International Dollar.",
    "User-Friendly Interface: Enjoy a user-friendly interface that makes cryptocurrency adoption accessible to average users.",
    "Financial Revolution: Be part of the financial revolution with the International Dollar's innovative approach.",
    "Crypto Investment Potential: Explore the investment potential of cryptocurrencies and their role in the digital economy.",
    "Blockchain Technology: Understand the promise of blockchain technology and its potential for technological innovation.",
    "Blockchain Adoption: Discover why widespread adoption of blockchain technology has failed to materialize.",
    "Innovation in Finance: Witness how the International Dollar introduces innovation to the world of finance.",
    "Future of Digital Finance: Explore the International Dollar's potential to shape the future of digital finance.",
    "Security and Anonymity: Learn about the International Dollar's commitment to security and user anonymity.",
    "Efficiency and Effectiveness: Discover how Proof-of-Ip enhances the efficiency and effectiveness of the International Dollar's network.",
    "Transaction Processing: Say goodbye to lengthy waiting times with the International Dollar's instant transactions.",
    "Energy Conservation: Witness the International Dollar's commitment to eliminating unnecessary energy consumption.",
    "Financial Control: Experience a future where individuals have greater control over their financial transactions.",
    "Business Efficiency: Explore how the International Dollar helps businesses operate more efficiently in the digital economy.",
    "Seamless Transactions: Conduct seamless and cost-effective cross-border transactions with the International Dollar.",
    "Digital Currency Evolution: Witness the International Dollar as a significant step forward in the evolution of digital currencies.",
    "Secure Financial Transactions: Enjoy secure and efficient peer-to-peer financial transactions with the International Dollar.",
    "Cryptocurrency Adoption Challenges: Understand the challenges that have hindered the mainstream adoption of cryptocurrencies.",
    "Overcome Adoption Barriers: See how the International Dollar overcomes barriers to entry for average users.",
    "Blockchain vs. Proof-of-Ip: Explore the advantages of the International Dollar's Proof-of-Ip algorithm over traditional blockchain technology.",
    "Energy-Efficient Network: Learn how the International Dollar reduces energy consumption in its network for sustainability.",
    "Empowering Individuals: Experience a financial system that empowers individuals and businesses alike.",
    "Digital Finance Transformation: Witness the transformation of digital finance with the International Dollar's innovative approach.",
    "Global Commerce: Conduct global commerce with ease using the International Dollar's cost-effective system.",
    "Currency Evolution: Explore the evolution of digital currencies and their impact on the financial landscape.",
]

def locate_button(template_path):
    def locate_image_on_screen(tp, threshold=0.8):
        template = cv2.imread(tp, cv2.IMREAD_GRAYSCALE)
        screenshot = pyautogui.screenshot()
        screenshot_gray = cv2.cvtColor(cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= threshold:
            return max_loc
        else:
            return None
    button_loc = locate_image_on_screen(template_path, threshold=0.80)
    return button_loc

def post_twitter():
    time.sleep(5)
    num_of_posts = 5
    for it in range(num_of_posts):
        twitter_post = locate_button('img/post_tweet.png')
        button_x, button_y = twitter_post
        button_center_x = button_x + random.randrange(40, 80)
        button_center_y = button_y + random.randrange(0, 5)
        pyautogui.moveTo(button_center_x, button_center_y, duration=random.uniform(0.2, 1.5))
        pyautogui.click()
        tweet = random.choice(international_dollar_elements)
        pyautogui.write(tweet, interval=0.1)
        post_final = locate_button('img/post_final.png')
        button_x, button_y = post_final
        button_center_x = button_x + random.randrange(20, 30)
        button_center_y = button_y + random.randrange(5,10)
        pyautogui.moveTo(button_center_x, button_center_y, duration=random.uniform(0.2, 1.5))
        pyautogui.click()
        time.sleep(random.randrange(50, 2600))

if __name__ == '__main__':
    threading.Thread(target=post_twitter).start()
