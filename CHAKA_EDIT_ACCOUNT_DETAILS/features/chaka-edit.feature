Feature: Chaka platform, user should be able to edit account details

    As a new user, I should be able to edit my account details successfully
    Scenario: User should be able to edits acount details,
    so that al information and will be feasible during transaction time

        Given I am on chaka website
        And I can login
        And I can click on account
        And I can select settings from dropdown opton
        When I can upload passport .jpg
        When I upload address field .jpg
        Then I can enter my full name
        And I can click on Submit