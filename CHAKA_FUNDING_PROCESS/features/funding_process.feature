Feature: Chaka platform, user should be able to fund account

    As a new user, I should be able to loggin successfully, I should
    be able to fund my account successfully
    Scenario: User should be able to fund account and amount 
    funded should reflect in the user account balance

        Given I am on chaka website
        And I can login
        And I can click on fund portfolio
        And I can click on fund your local wallet
        And I can enter amount in Naira
        And I click continue
        And I can click Instant Bank Funding
        And I can copy GTB account number
        And I can click on back
        And I can click on Regular Bank Transfer
        And I can click on back
         And I can click on paystack
        And I can input amount within account range
        Then I click on fund
        When I input card number
        When I input card expiry
        When I input cvv on card 
        And I click on pay