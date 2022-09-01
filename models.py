from pydantic import BaseModel 

class Person(BaseModel): 
    age: int
    bmi: float
    total_test_beck: int