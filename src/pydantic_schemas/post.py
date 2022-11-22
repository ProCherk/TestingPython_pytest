from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int  # = Field(le=1000)
    name: str
    email: str
    gender: str
    status: str
    # name: str = Field(alias="_ name")  # if parameter name starts with underline

# the same as Field
    @validator("id")
    def check_id_requirement(cls, n):  # id need to be more than 1000
        if n > 1000:
            raise ValueError("id is not required")
        else:
            return n


'''
[{'id': 2698, 'name': 'Dayamayee Guha DVM', 'email': 'dayamayee_guha_dvm@aufderhar.name', 'gender': 'female', 'status': 
'active'}, 
{'id': 2691, 'name': 'Atreyi Jha', 'email': 'atreyi_jha@hegmann.io', 'gender': 'male', 'status': 'inactive'}, 
{'id': 2690, 'name': 'Urmila Asan', 'email': 'urmila_asan@hermann-nader.org', 'gender': 'male', 'status': 'active'}, 
{'id': 2689, 'name': 'Sushil Naik', 'email': 'sushil_naik@kunde-daugherty.info', 'gender': 'male', 'status': 'active'}, 
{'id': 2687, 'name': 'Gov. Akshayakeerti Prajapat', 'email': 'akshayakeerti_prajapat_gov@beatty.co', 'gender': 'female',
 'status': 'active'}, 
{'id': 2686, 'name': 'Karunanidhi Varman II', 'email': 'varman_karunanidhi_ii@hilpert.io', 'gender': 'female', 'status':
 'active'}, 
{'id': 2685, 'name': 'Raj Joshi', 'email': 'joshi_raj@schumm.name', 'gender': 'female', 'status': 'inactive'}, 
{'id': 2684, 'name': 'Sumitra Nair', 'email': 'sumitra_nair@ferry.io', 'gender': 'female', 'status': 'inactive'}, 
{'id': 2683, 'name': 'Vrund Saini', 'email': 'saini_vrund@prohaska-klein.net', 'gender': 'male', 'status': 'active'}, 
{'id': 2682, 'name': 'Dhaanyalakshmi Naik', 'email': 'dhaanyalakshmi_naik@jacobson-macejkovic.co', 'gender': 'female', 
'status': 'active'}]}
'''
