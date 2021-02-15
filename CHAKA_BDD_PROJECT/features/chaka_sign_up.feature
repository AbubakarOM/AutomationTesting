Feature: Chaka signup, sign-in and password-reset process

    As a new user, I must be able to signup successfully, 
    I must be able to sign-in successfully and reset my password

    Scenario: User should be able to signup, sign-in and reset password 
    on chaka page

        Given I am on chaka website
        And I can click on signup
        And I can enter email address
        And I can enter password
        And I can enter confirm password
        And I can click on signup botton 
        And I can click on Login on chaka website
        And I can enter my email address
        And I can enter my password
        And I can click on Login Button