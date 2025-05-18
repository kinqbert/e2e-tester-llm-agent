from browser_use import Agent, Browser

from pydantic import BaseModel

class Prompt(BaseModel):
    content: str
    scenario_name: str


REGISTER_PROMPT = Prompt(
    content="""
1. Open http://localhost:3000/register
2. Fill in name: "Test User"
3. Fill in email: "user123@example.com"
4. Fill in password: "Qwerty123!"
5. Fill in password confirmation: "Qwerty123!"
6. Click the "Register" button
7. Wait until the page shows "Dashboard" or redirects
""",
    scenario_name="register_user"
)

TRANSACTION_PROMPT = Prompt(
    content="""
1. Open http://localhost:3000/login
2. Log in with:
   - Email: testuserlmao@email.com
   - Password: testuserlmao
3. Wait for redirect to dashboard or visible transaction list
4. Click "Add transaction"
5. In the form:
   - Category: test
   - Description: Test Transaction 123
   - Amount: 123.45
6. Click "Save"
7. Wait until the new transaction appears in the table
""",
    scenario_name="add_transaction"
) 
